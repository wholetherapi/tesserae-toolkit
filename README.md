# Tesserae

Tesserae audits provenance for tiled raster products.  It walks the tile graph, checks
declared lineage against content hashes and emits a machine-readable audit report.

## Components

- `src/tesserae/tiles.py` - tile graph construction and hash verification
- `src/tesserae/audit.py` - lineage checks and report emission
- `data/sample_manifest.json` - small manifest for integration tests
- `experiments/pilot_notes.md` - results from the pilot deployment

## Command line

```bash
tesserae audit --manifest data/sample_manifest.json --out report.json
```

Licensed under the Apache 2.0 license.
