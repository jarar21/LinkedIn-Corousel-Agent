
# CrewAI LinkedIn Post Generator

This project uses CrewAI to generate LinkedIn posts on a given topic.

## Setup and Installation

1. **Navigate to the project directory:**
   ```bash
   cd crewai_linkedin_post
   ```

2. **Create a virtual environment:**
   # LinkedIn Carousel Studio — Portfolio

   A compact creative tool that turns short slide JSON into high-quality LinkedIn carousel PDFs. Built as a designer-friendly prototype and portfolio piece showcasing automated slide generation, theme-driven rendering, and PDF output optimized for social sharing.

   **Highlights**
   - Purpose: Generate multi-page PDFs where each page is a single LinkedIn carousel card.
   - Visual output: 1080×1350 px pages (portrait) composed with custom themes, dynamic graphics, and typographic scaling.
   - Themes: Multiple pre-designed looks (Neon, Swiss, Obsidian, Deep Ocean, Golden Luxe, Minimal Grey) defined in [theme_config.py](theme_config.py#L1).
   - Output folder: Generated PDFs are placed in `static/results` and follow the pattern `Carousel_{id}_{style_key}.pdf`.

   **What this project demonstrates**
   - Programmatic layout and typography decisions that avoid overflow and keep content legible.
   - Theme-first design system where color, spacing, and small graphics are driven by a single config object.
   - Integration pattern: lightweight agent-driven content generation feeding a deterministic renderer (`crew_logic.py`).

   **Sample artifacts**
   - Multi-theme PDFs (one file per theme) suitable for direct upload to LinkedIn as a document/carousel.
   - Example filenames and thumbnails are stored under `static/results` when the generator is run.

   **Where to look in the code**
   - `crew_logic.py` — orchestration, slide JSON parsing, and `CarouselGenerator` renderer.
   - `theme_config.py` — theme definitions and tunable graphic parameters.

   If you'd like, I can add a minimal showcase page or a simple gallery route to preview generated PDFs; say the word and I'll scaffold a small viewer in `app.py`.

   ---
   If you want, I can also:
   - Add a small Flask route to serve the generated PDFs.
   - Add a CLI entry for custom topics and output folder.

   Tell me which of those you'd like next.
