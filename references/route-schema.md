# Route Schema Reference

Use this schema for `tech-route.json`. The file is the single source of truth for every rendered format.

Current schema version: `0.2.0`.

## Top-level fields

| Field | Required | Notes |
|---|---|---|
| `route_version` | yes | Current version is `0.2.0`. |
| `title` | yes | Visible diagram title. |
| `subtitle` | no | Optional visible subtitle. |
| `selected_preset` | yes | `academic-method`, `thesis-proposal`, `engineering-system`, `workflow-pipeline`, or `custom`. |
| `layout` | recommended | Renderer layout ID. |
| `style` | recommended | Renderer visual style ID. |
| `metadata` | recommended | Source files, selected outputs, language and audience. |
| `stages` | yes | Ordered stage list. |
| `edges` | recommended | Semantic links between node IDs. |
| `assumptions` | recommended | Explains inferred content. |
| `unresolved_questions` | recommended | Questions requiring user or source-owner review. |
| `quality_report` | generated | Filled by validator/render tooling. |
| `citations` | optional | External citation records when needed. |
| `renderer_overrides` | optional | Format-specific render hints. |

## Metadata fields

- `created_by`: normally `tech-route-maker`.
- `selected_output_formats`: actual rendered outputs.
- `source_type`: `paper`, `proposal`, `engineering`, `workflow`, `legacy-campaign`, or `custom`.
- `source_files`: list of source files with `path`, `kind`, and `description`.
- `source_hashes`: optional file hashes for audit trails.
- `language`: route language.
- `audience`: `research`, `engineering`, `technical`, or another target audience.

## Node fields

- `id`: stable node identifier.
- `label`: visible node label.
- `detail`: longer explanation for HTML/Markdown.
- `tag`: category such as `objective`, `input`, `method`, `implementation`, `validation`, `output`, `risk`, or `feedback`.
- `node_type`: optional semantic type.
- `confidence`: `high`, `medium`, or `low`.
- `is_inferred`: boolean. Use `true` only when the node is not directly stated in the source.
- `evidence`: source-grounding list.

## Evidence fields

- `kind`: `source`, `file`, `function`, `class`, `config`, `document`, `dataset`, `metric`, `output`, or `inference`.
- `source_id`: optional source record ID.
- `path`: source path when available.
- `locator`: section, page, paragraph, function, table, figure, or row locator.
- `quote_or_note`: short evidence note. Keep it concise.
- `symbol`: function/class/config key when available.

## Edge fields

- `id`: stable edge identifier.
- `from`: source node ID.
- `to`: target node ID.
- `label`: semantic transition.
- `kind`: `flow`, `feedback`, `dependency`, `validation`, or `evidence`.
- `confidence`: `high`, `medium`, or `low`.
- `evidence`: optional edge-level support.

## Validation rules

- `route_version` must exist.
- `selected_preset` must be valid.
- Stages should usually be 4 to 7.
- Each stage should usually contain 2 to 6 nodes.
- Every visible node must have evidence or be explicitly inferred.
- Inferred nodes should be linked from an assumption by `node_ids`.
- Edge endpoints must point to existing nodes.
- Confidence values must be `high`, `medium`, or `low`.