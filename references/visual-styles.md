# Visual Styles

Use this reference when asking the user to choose a visual style. Ask explicitly. Do not infer style from "paper", "defense", "presentation", or similar words.

## Style menu

1. `academic-blue`
   - White background, blue headers, light blue stage fills.
   - Useful for theses, reports, and general academic diagrams.

2. `blue-green-research`
   - Blue and teal accents with neutral gray text.
   - Useful for science and engineering topics.

3. `monochrome-paper`
   - Black, white, and gray only.
   - Useful for print-safe papers and journals.

4. `defense-color`
   - Stronger multi-color stage palette.
   - Useful for slides and oral presentations.

5. `minimal-gray`
   - Low-saturation gray, white, and one accent.
   - Useful for technical documentation.

6. `nature-editorial`
   - White background, restrained color blocks, high whitespace, crisp labels.
   - Useful for polished academic presentation, without imitating a specific publication template.

7. `accessible-high-contrast`
   - High contrast, colorblind-safe palette, thick connectors.
   - Useful when readability matters more than decoration.

8. `dark-technical`
   - Dark background with bright but restrained accents.
   - Useful for engineering demos and technical talks.

9. `soft-pastel`
   - Soft category colors, low contrast boxes, clear connector lines.
   - Useful for workshop and planning views.

10. `schematic-precision`
   - Exact module boundaries, typed arrows, controlled labels, and clean line-art.
   - Useful for paper method and architecture figures where interfaces matter.

11. `editorial-clarity`
   - Sparse modules, strong hierarchy, low text density, and caption-supported definitions.
   - Useful for intro figures and fast first-glance comprehension.

12. `mechanism-snapshot`
   - Central mechanism, zoom callout, cause-effect arrows, and compact internal motifs.
   - Useful for explaining why a method works.

13. `evidence-infographic`
   - Method route plus small evidence cards, metric badges, or ablation anchors.
   - Useful when a route must connect to results without inventing numbers.

14. `premium-scientific`
   - Restrained color, vector-safe landmarks, high whitespace, and polished academic composition.
   - Useful for publication-style paper figures and high-quality defense slides.

15. `advertising-clean-campaign`
   - Clean brand-neutral campaign map with audience, insight, creative, media, launch, and KPI accents.
   - Useful for advertising strategy and campaign-production route diagrams.

## Style rules

- Use color to encode stage category, not decoration.
- Keep connector lines darker than node fills.
- Avoid dense gradients and decorative backgrounds.
- Use enough whitespace to keep every label readable.
- Use one main font family per output.
- For PPTX and SVG, keep labels as editable text.
- For monochrome output, vary borders, fill intensity, or line styles instead of relying on color.
- For academic figures, visible style must serve the reader question and selected figure subtype.
- For advertising diagrams, visual style may be more presentation-oriented, but audience, channel, and measurement logic must stay explicit.
- Do not transfer paper-specific facts, claims, metrics, labels, or symbols from visual references into a new diagram.

## Palette defaults

Render scripts provide default palettes for all style IDs. The user may later ask to change colors; update `theme` in `tech-route.json` and re-render.
