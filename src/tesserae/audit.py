"""Lineage verification and report emission."""

import json
import click

from .tiles import build_graph


def audit_manifest(manifest):
    graph = build_graph(manifest)
    findings = []
    for tile in graph.values():
        if tile.declared_hash is None:
            findings.append({"tile": tile.tile_id, "issue": "missing_hash"})
        elif tile.parent is None and len(tile.children) == 0:
            findings.append({"tile": tile.tile_id, "issue": "orphan_tile"})
    return {"tiles": len(graph), "findings": findings}


@click.command()
@click.option("--manifest", required=True)
@click.option("--out", default="report.json")
def cli(manifest, out):
    with open(manifest, encoding="utf-8") as handle:
        report = audit_manifest(json.load(handle))
    with open(out, "w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2)
    click.echo(f"wrote {out}")
