# Route Schema

Use this schema for `tech-route.json`. The file is the single source of truth for every rendered format.

## Minimal example

```json
{
  "title": "Project Technical Route",
  "subtitle": "Generated from repository evidence",
  "layout": "horizontal-stages",
  "style": "academic-blue",
  "audience": "academic",
  "figure_subtype": "academic_method_framework",
  "reader_question": "What is the proposed method and how do the stages connect?",
  "reader_path": ["Objective", "Input", "Method", "Validation", "Output"],
  "stages": [
    {
      "id": "objective",
      "title": "Objective",
      "nodes": [
        {
          "id": "objective_1",
          "label": "Define project goal",
          "detail": "Summarize the core problem and expected result.",
          "tag": "objective",
          "evidence": [
            {"kind": "file", "path": "README.md", "note": "Project overview"}
          ]
        }
      ]
    }
  ],
  "edges": [
    {"from": "objective_1", "to": "input_1", "label": "guides"}
  ],
  "metadata": {
    "source_scope": ".",
    "generated_by": "tech-route-maker"
  }
}
```

## Required top-level fields

- `title`: visible diagram title.
- `stages`: ordered list of route stages.

## Recommended top-level fields

- `subtitle`: optional visible subtitle.
- `layout`: selected layout ID.
- `style`: selected visual style ID.
- `edges`: semantic links between node IDs.
- `metadata`: source scope, date, author, assumptions, and selected output formats.
- `audience`: `academic`, `advertising`, `engineering`, or another user group.
- `figure_subtype`: selected figure purpose/subtype.
- `reader_question`: the main question the diagram answers.
- `reader_path`: 3 to 7 first-glance anchor steps.
- `visible_text_contract`: separates node labels, edge labels, internal micro-labels, and legend/caption labels.
- `density_budget`: node count, repeated element compression, and first-glance risk.
- `caption_support_plan`: what the figure body carries versus what caption/legend/supporting text carries.

## Stage fields

- `id`: stable stage identifier.
- `title`: visible stage label.
- `summary`: optional detail for HTML or Markdown.
- `nodes`: ordered node list.

## Node fields

- `id`: stable node identifier.
- `label`: visible node label.
- `detail`: node explanation.
- `tag`: category such as `objective`, `input`, `method`, `implementation`, `validation`, `output`, `risk`, `inference`.
- `evidence`: list of evidence objects.

## Evidence fields

- `kind`: `file`, `function`, `class`, `config`, `document`, `dataset`, `metric`, `output`, or `inference`.
- `path`: source path when available.
- `symbol`: function/class/config key when available.
- `note`: short explanation.

If a node is inferred from weak evidence, include:

```json
{"kind": "inference", "note": "Inferred from project structure; verify with owner."}
```

## Edge fields

- `from`: source node ID.
- `to`: target node ID.
- `label`: semantic transition.
- `kind`: optional edge category such as `flow`, `feedback`, `dependency`, `evidence`.

## Normalization rules

The scripts normalize missing IDs, derive sequential edges when no edges are provided, and preserve user labels. Do not rely on normalization for final handoff; write stable IDs when possible.

## Academic and advertising additions

For paper, thesis, proposal, and research-project diagrams, include `figure_subtype`, `reader_question`, `reader_path`, and a short `caption_support_plan`.

For advertising diagrams, include audience/segment, creative or campaign stage labels, channel/media stages, measurement nodes, and any approval or optimization loops.

Use `visible_text_contract` to prevent file paths, schema keys, audit IDs, and long explanations from appearing inside visible boxes.
