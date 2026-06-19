# Thesis Proposal Technical Route

Data-driven PV module degradation assessment demo

```mermaid
flowchart TB
  title["Thesis Proposal Technical Route"]
  subgraph question["Research Question"]
    question_define["Define degradation risk"]
  end
  subgraph evidence["Source Evidence"]
    evidence_collect["Collect field evidence"]
    evidence_align["Clean and align data"]
  end
  subgraph features["Feature Route"]
    features_construct["Construct indicators"]
    features_select["Select feature groups"]
  end
  subgraph modeling["Modeling"]
    model_fit["Fit interpretable model"]
    model_uncertainty["Label uncertainty"]
  end
  subgraph validation["Validation"]
    validation_cases["Validate on fault cases"]
    validation_review["Review feature ablation"]
  end
  subgraph output["Thesis Output"]
    output_priority["Output inspection priority"]
  end
  question_define -->|requires evidence| evidence_collect
  evidence_collect -->|prepares| evidence_align
  evidence_align -->|feeds| features_construct
  features_construct -->|filters| features_select
  features_select -->|trains| model_fit
  model_fit -->|qualifies| model_uncertainty
  model_uncertainty -->|tests| validation_cases
  validation_cases -->|checks| validation_review
  validation_review -->|supports| output_priority
```

## Route Evidence

| Stage | Node | Evidence |
|---|---|---|
| Research Question | Define degradation risk | document - examples/thesis-proposal-demo/source/project-brief.md - Research question |
| Source Evidence | Collect field evidence | document - examples/thesis-proposal-demo/source/project-brief.md - Inputs |
| Source Evidence | Clean and align data | document - examples/thesis-proposal-demo/source/project-brief.md - Preparation |
| Feature Route | Construct indicators | document - examples/thesis-proposal-demo/source/project-brief.md - Feature construction |
| Feature Route | Select feature groups | document - examples/thesis-proposal-demo/source/project-brief.md - Feature selection |
| Modeling | Fit interpretable model | document - examples/thesis-proposal-demo/source/project-brief.md - Interpretable model and risk scoring |
| Modeling | Label uncertainty | document - examples/thesis-proposal-demo/source/project-brief.md - Uncertainty labeling |
| Validation | Validate on fault cases | document - examples/thesis-proposal-demo/source/project-brief.md - Historical fault cases and cross-site comparison |
| Validation | Review feature ablation | document - examples/thesis-proposal-demo/source/project-brief.md - Ablation and expert review |
| Thesis Output | Output inspection priority | document - examples/thesis-proposal-demo/source/project-brief.md - Output |
