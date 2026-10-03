#!/usr/bin/env python3
"""Validate the CTL Black Cultural Knowledge Graph seed files.

Checks entities.json and relationships.json against schema.json:
  - required fields, types, and enum values
  - unique, well-formed entity IDs (765 in the 2026-10-03 promotion)
  - no dangling relationship endpoints
  - no duplicate (from, to, type) edges
Exit 0 = valid (warnings allowed), exit 1 = errors found.
"""
import json
import re
import sys

import os
BASE = os.path.dirname(os.path.abspath(__file__))
errors, warnings = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def main():
    try:
        schema = json.load(open(f'{BASE}/schema.json'))
    except Exception as e:
        err(f'schema.json does not parse: {e}')
        return report()
    try:
        entities = json.load(open(f'{BASE}/entities.json'))
    except Exception as e:
        err(f'entities.json does not parse: {e}')
        return report()
    try:
        relationships = json.load(open(f'{BASE}/relationships.json'))
    except Exception as e:
        err(f'relationships.json does not parse: {e}')
        return report()

    if not isinstance(entities, list):
        err('entities.json must be a JSON array')
        return report()
    if not isinstance(relationships, list):
        err('relationships.json must be a JSON array')
        return report()

    entity_types = schema.get('entity_types', {})
    rel_types = {t['name']: t for t in schema.get('relationship_types', [])}
    project_ids = set(schema.get('project_ids', []))
    ver_levels = set(schema.get('verification_levels', []))
    ent_required = schema.get('entity_required_fields', [])
    rel_required = schema.get('relationship_required_fields', [])

    if len(entities) != 765:
        err(f'entities.json must contain exactly 765 entities (2026-10-03 promotion), found {len(entities)}')

    seen_ids = set()
    id2type = {}
    for i, e in enumerate(entities):
        tag = f'entities[{i}]'
        if not isinstance(e, dict):
            err(f'{tag} is not an object'); continue
        for f in ent_required:
            if f not in e:
                err(f'{tag} missing required field "{f}"')
        eid = e.get('id', '')
        if not isinstance(eid, str) or not re.fullmatch(r'CTL-E-\d{4}', eid):
            err(f'{tag} has invalid id: {eid!r}')
        elif eid in seen_ids:
            err(f'duplicate entity id: {eid}')
        else:
            seen_ids.add(eid)
        etype = e.get('type')
        if etype not in entity_types:
            err(f'{tag} ({eid}) has invalid type: {etype!r}')
        else:
            id2type[eid] = etype
            subtypes = entity_types[etype].get('subtypes', [])
            if e.get('subtype') and subtypes and e['subtype'] not in subtypes:
                err(f'{tag} ({eid}) has invalid subtype {e["subtype"]!r} for type {etype}')
        for f in ('name', 'description', 'era'):
            if f in e and (not isinstance(e[f], str) or not e[f].strip()):
                err(f'{tag} ({eid}) field "{f}" must be a non-empty string')
        if 'aliases' in e and (not isinstance(e['aliases'], list)
                               or any(not isinstance(a, str) for a in e['aliases'])):
            err(f'{tag} ({eid}) "aliases" must be a list of strings')
        pids = e.get('project_ids')
        if not isinstance(pids, list) or not pids or any(p not in project_ids for p in pids):
            err(f'{tag} ({eid}) has invalid project_ids: {pids!r}')
        if e.get('verification') not in ver_levels:
            err(f'{tag} ({eid}) has invalid verification: {e.get("verification")!r}')
        srcs = e.get('sources')
        if not isinstance(srcs, list) or not srcs:
            err(f'{tag} ({eid}) must have a non-empty sources array')
        else:
            for s in srcs:
                if (not isinstance(s, dict) or not s.get('citation')
                        or not isinstance(s.get('primary'), bool)):
                    err(f'{tag} ({eid}) has malformed source: {s!r}')

    # every required project should appear at least once
    covered = {p for e in entities if isinstance(e, dict) for p in e.get('project_ids', [])}
    for p in project_ids:
        if p not in covered:
            warn(f'no entity references project {p}')

    seen_edges = set()
    for i, r in enumerate(relationships):
        tag = f'relationships[{i}]'
        if not isinstance(r, dict):
            err(f'{tag} is not an object'); continue
        for f in rel_required:
            if f not in r:
                err(f'{tag} missing required field "{f}"')
        frm, to, typ = r.get('from'), r.get('to'), r.get('type')
        if frm not in seen_ids:
            err(f'{tag} dangling "from" endpoint: {frm!r}')
        if to not in seen_ids:
            err(f'{tag} dangling "to" endpoint: {to!r}')
        if typ not in rel_types:
            err(f'{tag} has invalid type: {typ!r}')
        elif frm in id2type and to in id2type:
            rt = rel_types[typ]
            if id2type[frm] not in rt['from_types'] or id2type[to] not in rt['to_types']:
                err(f'{tag} type {typ} incompatible with endpoint types '
                    f'{id2type[frm]} -> {id2type[to]}')
        key = (frm, to, typ)
        if key in seen_edges:
            err(f'{tag} duplicate edge: {frm} -> {to} [{typ}]')
        seen_edges.add(key)
        if r.get('verification') not in ver_levels:
            err(f'{tag} has invalid verification: {r.get("verification")!r}')
        for f in ('evidence', 'source'):
            if f in r and (not isinstance(r[f], str) or not r[f].strip()):
                err(f'{tag} field "{f}" must be a non-empty string')

    n = len(relationships)
    if n < 300:
        warn(f'only {n} edges; target is 300-500 for the seed')
    elif n > 600:
        warn(f'{n} edges exceeds the 300-500 seed target; review for bloat')

    return report()


def report():
    for w in warnings:
        print(f'WARNING: {w}')
    for e in errors:
        print(f'ERROR: {e}')
    print(f'\n{len(errors)} error(s), {len(warnings)} warning(s)')
    if not errors:
        print('VALIDATION PASSED')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
