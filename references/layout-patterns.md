# Layout Patterns

Use this reference to offer layout choices. Ask the user to choose one layout. Do not infer the layout from the request.

## Layout menu

1. `horizontal-stages`
   - Best for project summaries, defenses, and reports.
   - Reads left to right: objective, input, method, implementation, validation, output.

2. `vertical-research-route`
   - Best for thesis, proposal, and research-topic route diagrams.
   - Reads top to bottom and supports branch groups under each research phase.

3. `three-column`
   - Best for Chinese-style research reports and project proposals.
   - Columns: goals, technical content, expected results.

4. `ai-pipeline`
   - Best for AI, ML, computer vision, NLP, or data projects.
   - Typical route: data acquisition, preprocessing, model, training/inference, evaluation, deployment.

5. `engineering-architecture`
   - Best for software and systems engineering.
   - Typical route: requirements, architecture, modules/services, integration, tests, deployment.

6. `timeline-swimlane`
   - Best for product or implementation roadmaps.
   - Uses time periods as columns and lanes such as frontend, backend, data, model, ops, validation.

7. `layered-architecture`
   - Best for platform and service systems.
   - Uses layers such as user/input, application, domain/model, data, infrastructure, output.

8. `closed-loop-optimization`
   - Best for research or engineering workflows with feedback.
   - Shows design, implementation, evaluation, feedback, optimization, and re-validation.

9. `evidence-centered`
   - Best when traceability matters.
   - Places route nodes around evidence groups: source files, scripts, datasets, metrics, outputs.

10. `hub-and-spoke-core-method`
   - Best when one core model, method, service, or creative idea coordinates several inputs and outputs.
   - Strength: highlights novelty or central strategy.
   - Risk: can over-center one block and hide sequential order.

11. `baseline-vs-ours-split`
   - Best when novelty is comparative.
   - Strength: quickly shows what changes relative to a baseline or old workflow.
   - Risk: can oversimplify the source if differences are subtle.

12. `case-walkthrough-strip`
   - Best when one example, sample, user, or customer moves through the method.
   - Strength: intuitive and strong for qualitative evidence.
   - Risk: insufficient as a full method specification unless paired with a framework overview.

13. `campaign-funnel`
   - Best for advertising teams mapping audience, awareness, engagement, conversion, retention, and measurement.
   - Strength: familiar business communication path.
   - Risk: can hide production dependencies.

14. `creative-production-pipeline`
   - Best for advertising teams mapping brief, insight, concept, assets, media, launch, and optimization.
   - Strength: separates creative work from channel execution.
   - Risk: needs clear approval/revision loops.

## Design rules

- Keep the main route to 4 to 7 stages.
- Keep each stage to 2 to 6 nodes.
- Keep labels short; put details in evidence tables, notes, or HTML panels.
- Use grouped regions for stages.
- Use semantic edge labels.
- Put variables, metrics, parameters, and pass-through artifacts on edges or ports before promoting them to nodes.
- Separate the audit/semantic graph from the visible render graph.
- Add a 3 to 7 step `reader_path` for academic and advertising-facing diagrams.
- Use feedback arrows only when the project has real iteration or optimization evidence.
- If the source is uncertain, mark the node evidence as `inference` instead of presenting it as confirmed.

## Source patterns

Academic and technical-route references commonly use:
- Research goal and hypothesis.
- Literature or theoretical framework.
- Method and technical route.
- Key tasks and steps.
- Time plan and milestones.
- Analysis, design, implementation, optimization, validation.

Roadmap references commonly use:
- Vision or why.
- Themes or major workstreams.
- Milestones and dependencies.
- Audience-specific detail.
- Periodic review and adjustment.

Paper-framework figure references also commonly use:
- reader question and paper slot;
- method framework, architecture, pipeline, mechanism, case walkthrough, evidence-linked, and failure-aware subtypes;
- caption/legend/body division of labor;
- visual text contracts;
- edge-label-first variables and artifact labels;
- density and repetition-compression budgets.

Advertising route references commonly use:
- target audience and insight;
- creative idea and message route;
- media/channel route;
- content production route;
- launch and measurement route;
- optimization feedback loop.
