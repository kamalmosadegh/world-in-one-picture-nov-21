// The World in One Picture — 21 November 2026 (Node 22, standard library only).
//
// The poster is drawn by draw_poster.py and shipped as poster.png beside
// this file. This program's only job is to place that exact file in the
// output directory, byte for byte.
//
// The copy is deterministic: repeated runs write identical bytes — nothing
// is generated here, nothing depends on the clock, nothing touches the
// network.
//
// Locally, OUTPUT_DIR stands in for /output, so a check run is:
//   mkdir -p out && OUTPUT_DIR=out node main.ts

import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const poster = readFileSync(join(here, "poster.png"));

// The output file keeps the name poster.png.
const outDir = process.env.OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
writeFileSync(join(outDir, "poster.png"), poster);
console.log(`wrote ${join(outDir, "poster.png")}`);
