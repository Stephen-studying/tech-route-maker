# Before / After Quality Comparison

This comparison documents the v0.2.x Chinese academic style upgrade. The baseline was captured from the repository outputs before this change. The current outputs were regenerated after adding Chinese academic layouts, styles, demo routes, and renderer updates.

## Summary

The core research and engineering examples improved. The main gains are:

- Chinese academic presets now use dedicated `cn-*` layouts and styles instead of generic academic, proposal, or dark engineering themes.
- Chinese proposal and grant examples now render as portrait route diagrams in SVG and PPTX.
- PPTX outputs remain editable native shapes and connectors; no screenshot or raster main diagram is used.
- SVG structural checks report no text out-of-bounds flags and no same-center text overlap flags in the checked examples.
- A new grant/project-application example was added.

## Metric Notes

The alignment score is a repository QA heuristic, not a scientific aesthetic score. It rewards:

- dedicated Chinese academic layout/style usage;
- no text out-of-bounds flags;
- no same-center text overlap flags;
- editable PPTX shapes with zero embedded picture elements;
- Chinese route metadata where applicable;
- Chinese academic preset IDs.

## Core Example Comparison

| Example | Before layout / style | After layout / style | Before score | After score | Key improvement |
|---|---|---|---:|---:|---|
| `academic-paper-demo` | `academic-method-framework` / `academic-blue` | `cn-research-method-matrix` / `cn-blue-green-proposal` | 47 | 100 | Changed from generic academic matrix to Chinese paper-method matrix. |
| `thesis-proposal-demo` | `proposal-matrix-route` / `presentation-clean` | `cn-proposal-poster-route` / `cn-polished-pastel-academic` | 47 | 100 | Changed to portrait proposal poster route with phase axis and pastel academic styling. |
| `engineering-energy-system-demo` | `engineering-architecture-route` / `dark-technical` | `cn-wide-project-map` / `cn-blue-green-proposal` | 47 | 100 | Changed from dark engineering theme to white Chinese project-report map. |
| `agent-workflow-demo` | `horizontal-stages` / `minimal-gray` | `horizontal-stages` / `minimal-gray` | 35 | 35 | Intentionally unchanged because it is a tool workflow example, not a Chinese academic route. |

## Output Checks

| Example | SVG size after | SVG text overlap flags | SVG out-of-bounds flags | PPTX portrait after | PPTX pictures after |
|---|---:|---:|---:|---|---:|
| `academic-paper-demo` | `1380x1030` | 0 | 0 | No | 0 |
| `thesis-proposal-demo` | `1060x1272` | 0 | 0 | Yes | 0 |
| `chinese-grant-application-demo` | `1060x1272` | 0 | 0 | Yes | 0 |
| `engineering-energy-system-demo` | `1500x890` | 0 | 0 | No | 0 |

## Conclusion

The update improves the research-facing examples and renderer behavior. The repository now supports route diagrams closer to common Chinese academic proposal, grant, and project-report aesthetics while preserving editable PPTX, SVG, Draw.io, HTML, Markdown, Mermaid, Excalidraw, and JSON outputs.

Generated figures are still editable drafts. Users should revise terminology, evidence, spacing, colors, and final layout before submitting them in papers, defenses, grants, or engineering reports.

