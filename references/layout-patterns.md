# Layout Patterns

Use this reference to choose or explain layout patterns. Use the default preset layout first, and ask the user only when the layout choice would materially change the output.

## Layout menu

1. `academic-method-framework`
   - Best for papers, defenses, and academic reports that need a formal technical route rather than a decorative process chain.
   - Uses research-objective, data/sample, method, training/implementation, and validation/output sections on a clean matrix canvas.

2. `proposal-matrix-route`
   - Best for thesis proposals, grant reports, and research plans.
   - Uses explicit sections such as research objective, research content, key technologies, experimental validation, and expected outputs.

3. `software-system-route`
   - Best for software or system projects.
   - Uses system layers such as user input, data layer, service layer, rendering/output layer, and quality/release layer.

4. `campaign-strategy-map`
   - Legacy/experimental option for advertising and campaign planning when the user explicitly selects a business route.
   - Separates audience, insight, message, channels, measurement, and optimization.

5. `horizontal-stages`
   - Best for project summaries, defenses, and reports.
   - Reads left to right: objective, input, method, implementation, validation, output.

6. `vertical-research-route`
   - Best for thesis, proposal, and research-topic route diagrams.
   - Reads top to bottom and supports branch groups under each research phase.

7. `three-column`
   - Best for Chinese-style research reports and project proposals.
   - Columns: goals, technical content, expected results.

8. `ai-pipeline`
   - Best for AI, ML, computer vision, NLP, or data projects.
   - Typical route: data acquisition, preprocessing, model, training/inference, evaluation, deployment.

9. `engineering-architecture`
   - Best for software and systems engineering.
   - Typical route: requirements, architecture, modules/services, integration, tests, deployment.

10. `timeline-swimlane`
   - Best for product or implementation roadmaps.
   - Uses time periods as columns and lanes such as frontend, backend, data, model, ops, validation.

11. `layered-architecture`
   - Best for platform and service systems.
   - Uses layers such as user/input, application, domain/model, data, infrastructure, output.

12. `closed-loop-optimization`
   - Best for research or engineering workflows with feedback.
   - Shows design, implementation, evaluation, feedback, optimization, and re-validation.

13. `evidence-centered`
   - Best when traceability matters.
   - Places route nodes around evidence groups: source files, scripts, datasets, metrics, outputs.

14. `hub-and-spoke-core-method`
   - Best when one core model, method, service, or creative idea coordinates several inputs and outputs.
   - Strength: highlights novelty or central strategy.
   - Risk: can over-center one block and hide sequential order.

15. `baseline-vs-ours-split`
   - Best when novelty is comparative.
   - Strength: quickly shows what changes relative to a baseline or old workflow.
   - Risk: can oversimplify the source if differences are subtle.

16. `case-walkthrough-strip`
   - Best when one example, sample, user, or customer moves through the method.
   - Strength: intuitive and strong for qualitative evidence.
   - Risk: insufficient as a full method specification unless paired with a framework overview.

17. `campaign-funnel`
   - Legacy/experimental option for teams mapping audience, awareness, engagement, conversion, retention, and measurement.
   - Strength: familiar business communication path.
   - Risk: can hide production dependencies.

18. `creative-production-pipeline`
   - Legacy/experimental option for mapping brief, insight, concept, assets, media, launch, and optimization.
   - Strength: separates creative work from channel execution.
   - Risk: needs clear approval/revision loops.

19. `proposal-phase-axis`
   - Legacy option for long vertical research-topic roadmaps when the user explicitly requests a left phase axis.
   - Reads top to bottom with a left phase axis, dashed stage regions, and grouped task nodes.
   - Risk: easily becomes a decorative stacked flowchart and should not be used as the default Gallery/README example.

20. `wide-collaboration-map`
   - Best for project reports, platform construction, industry-academia collaboration, and policy/resource coordination.
   - Reads as side axes plus a central collaboration system.
   - Strength: exposes actors, dependencies, work packages, and support systems better than a simple pipeline.
   - Risk: can look busy if every stakeholder becomes a node.

## Design rules

- Keep the main route to 4 to 7 stages.
- Keep each stage to 2 to 6 nodes.
- Keep labels short; put details in evidence tables, notes, or HTML panels.
- Use grouped regions for stages.
- For proposal-style academic routes, prefer matrix sections or framework sections first. Use a left phase axis only when the user explicitly chooses a long vertical route.
- For polished PPT landscape routes, use a wide canvas, central modules, side labels, and restrained connector arrows rather than a single cramped line.
- Use semantic edge labels.
- Put variables, metrics, parameters, and pass-through artifacts on edges or ports before promoting them to nodes.
- Separate the audit/semantic graph from the visible render graph.
- Add a 3 to 7 step `reader_path` for academic, engineering, workflow, and legacy campaign diagrams.
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

Legacy campaign route references commonly use:
- target audience and insight;
- creative idea and message route;
- media/channel route;
- content production route;
- launch and measurement route;
- optimization feedback loop.
