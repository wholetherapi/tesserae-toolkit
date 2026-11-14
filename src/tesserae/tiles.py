"""Tile graph construction and content hashing."""

import hashlib
from dataclasses import dataclass, field


@dataclass
class Tile:
    tile_id: str
    parent: str = None
    declared_hash: str = None
    children: list = field(default_factory=list)


def build_graph(manifest):
    tiles = {}
    for row in manifest["tiles"]:
        tiles[row["tile_id"]] = Tile(
            tile_id=row["tile_id"],
            parent=row.get("parent"),
            declared_hash=row.get("hash"),
        )
    for tile in tiles.values():
        if tile.parent and tile.parent in tiles:
            tiles[tile.parent].children.append(tile.tile_id)
    return tiles


def content_hash(payload):
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()
