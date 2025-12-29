
# CrewAI LinkedIn Post Generator

This project uses CrewAI to generate LinkedIn posts on a given topic.

## Setup and Installation

1. **Navigate to the project directory:**
   ```bash
   cd crewai_linkedin_post
   ```

2. **Create a virtual environment:**
   On Windows:
   ```bash
   python -m venv venv
   ```
   On macOS/Linux:
   ```bash
   # CrewAI LinkedIn Carousel Generator

   This repository generates LinkedIn carousel PDFs from short slide JSON using CrewAI agents and a local image renderer.

   **Key files**
   - [crew_logic.py](crew_logic.py#L1): Main crew workflow and `CarouselGenerator` implementation.
   - [theme_config.py](theme_config.py#L1): Theme definitions (colors, layout, graphics) used by the renderer.
   - [app.py](app.py#L1): (Optional) Flask or web entrypoint (if present) to serve results.

   ## Quick setup

   1. Create and activate a Python virtual environment (recommended):

   On Windows:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   On macOS / Linux:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   3. Environment variables
   - Create a `.env` file in the project root or set environment variables directly.
   - Required: `SERPER_API_KEY` (used by the `SerperDevTool` search integration). Example `.env`:
   ```
   SERPER_API_KEY=your_serper_api_key_here
   ```

   The code uses `python-dotenv` to load `.env` automatically in `crew_logic.py`.

   ## Run the PDF generator

   To run the basic test that generates carousel PDFs, run:

   ```bash
   python crew_logic.py
   ```

   This calls `run_pdf_crew("AI Agents for Marketing")` (see the `if __name__ == "__main__"` block) and produces one PDF per theme.

   Output location and filenames
   - PDFs are written to the `static/results` folder by default.
   - Filenames follow the pattern: `Carousel_{uniqueid}_{style_key}.pdf`, e.g. `Carousel_1234_neon_tech.pdf`.

   ## How the generator works (brief)
   - `run_pdf_crew(topic)` runs two CrewAI agents: a researcher and an architect.
   - The architect returns a JSON array of 5 slides (title + content) used by `CarouselGenerator`.
   - `CarouselGenerator.create_pdf(...)` renders each slide into 1080×1350 images and saves a multi-page PDF.
   - Themes are defined in `theme_config.py` under the `THEMES` dictionary — add or tweak styles there.

   ## Uploading the generated PDF as a LinkedIn carousel

   1. Go to LinkedIn and start a new post.
   2. Click the document / attach file option (icon looks like a document).
   3. Select the generated PDF from `static/results` (the file can contain multiple pages — each page becomes a carousel slide).
   4. Give the document a title and click `Done`, then publish.

   Best-practice tips for LinkedIn carousel PDFs
   - Recommended slide size: 1080 × 1350 px (portrait) — this is what the renderer uses by default.
   - Keep text large and readable: title ≈ 48–95pt, body ≈ 36–48pt depending on content.
   - Use clear page breaks; each PDF page is one carousel card.

   ## Customization
   - Edit or add themes in [theme_config.py](theme_config.py#L1). Each theme controls colors, fonts, layout, and graphics.
   - Change output directory in `CarouselGenerator.__init__` or pass a different `output_folder` when constructing it.

   ## Next steps / automation ideas
   - Add a simple route in [app.py](app.py#L1) to list and serve generated PDFs for download.
   - Add an upload helper that uses LinkedIn APIs (requires app credentials) to programmatically create posts with PDFs.

   ## Troubleshooting
   - If PDFs are not created, confirm `SERPER_API_KEY` is set and that `crew_logic.py` ran without JSON parse errors.
   - Check `static/results` for output and console logs for errors.

   ---
   If you want, I can also:
   - Add a small Flask route to serve the generated PDFs.
   - Add a CLI entry for custom topics and output folder.

   Tell me which of those you'd like next.
