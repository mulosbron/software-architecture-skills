# Claude Automation Skillset (Skills, Tools, Scripts & SOPs)

Every actionable workflow from the 1-hour **Claude Full Course: Build & Automate Anything** training, packaged together: **13 ready-to-use `SKILL.md` files**, **interactive HTML mini-apps**, **Excel/CSV trackers** and **Python/Bash automation scripts**.

> In this repository the 13 skills were distributed across packs: `scraping-skills` (ai-news-researcher, browser-agent-operator), `seo-skills` (seo-blog-writer, youtube-title-generator), `writing-skills` (x-twitter-viral-engine, limited-time-promo-generator, livestream-mega-guide, business-advisor-debate, thirty-day-constraint-solver), `ui-ux-visual-lighting-skills` (landing-page-builder), `gamification-skills` (mini-app-gamifier) and `software-architecture-skills` (claude-code-github-launcher, mcp-connector-setup). Each skill carries its own scripts and tools.

---

## Folder Layout

```text
claude_automation_skillset/
├── README.md                                  # This main guide
├── projects/
│   └── claude_projects_setup_guide.md         # Setup and SOP guide for 5 core Claude Projects
├── skills/                                    # 13 SKILL.md files compatible with Claude / Gemini / agentic IDEs
│   ├── ai-news-researcher/SKILL.md
│   ├── browser-agent-operator/SKILL.md
│   ├── business-advisor-debate/SKILL.md
│   ├── claude-code-github-launcher/SKILL.md
│   ├── landing-page-builder/SKILL.md
│   ├── limited-time-promo-generator/SKILL.md
│   ├── livestream-mega-guide/SKILL.md
│   ├── mcp-connector-setup/SKILL.md
│   ├── mini-app-gamifier/SKILL.md
│   ├── seo-blog-writer/SKILL.md
│   ├── thirty-day-constraint-solver/SKILL.md
│   ├── x-twitter-viral-engine/SKILL.md
│   └── youtube-title-generator/SKILL.md
├── tools/                                     # Tools that run directly in the browser & trackers
│   ├── gamified-pomodoro-app.html             # Gamified Pomodoro with XP, levels, streaks and sound effects
│   ├── ai-seo-content-studio.html             # SEO content & prompt studio + live Markdown preview
│   ├── landing-page-template.html             # Conversion-focused template compatible with Netlify / WordPress / GHL
│   └── trackers/
│       ├── x_viral_hooks_tracker.xlsx         # X (Twitter) Top 10% / Bottom 90% performance tracker
│       ├── x_viral_hooks_tracker.csv          # CSV template ready for script processing
│       ├── 30_day_input_output_tracker.xlsx   # 30-day input/output + KPI gap Excel tracker
│       └── 30_day_input_output_tracker.csv    # CSV version
└── scripts/                                   # Runnable Python 3 & Bash automation scripts
    ├── hook_feedback_loop.py                  # Analyzes Top 10% / Bottom 90% from the X tracker and generates a prompt
    ├── youtube_title_analyzer.py              # Generates a SKILL.md automatically from YouTube title data
    ├── transcript_to_prompts.py               # Produces an SEO/X/livestream prompt pack from a video transcript
    ├── format_for_paste.py                    # One-sentence-per-line SEO formatting and keyword check
    ├── generate_30day_tracker.py              # Generates a custom 30-day .xlsx tracker for any goal
    ├── github_claude_launcher.sh              # Bash script that clones a GitHub repo and launches it with Claude Code
    └── claude_api_runner.py                   # Runs any SKILL.md file from the CLI via the Anthropic API
```

---

## Quick Start

### 1. Importing Skills (`skills/`)
- **Claude Desktop / Web:** upload the `SKILL.md` you want via `Settings -> Capabilities -> Skills -> Import Skill`.
- **Claude Code / IDE:** copy the relevant `SKILL.md` files into the project's `.claude/skills/` directory.

### 2. Using the Interactive Tools (`tools/`)
- Double-click the `.html` files to open them directly in your browser (no internet or installation needed; data is stored with `localStorage`).
- Open `tools/trackers/*.xlsx` directly in **Google Sheets** or **Microsoft Excel** (all `SUM`, percentage and `Gap` formulas are ready).

### 3. Running the Scripts (`scripts/`)
All Python scripts run on Python 3.8+:

```bash
# 1. Generate the X (Twitter) Top 10% / Bottom 90% feedback loop
python3 scripts/hook_feedback_loop.py tools/trackers/x_viral_hooks_tracker.csv -o updated_x_instructions.md

# 2. Generate a SKILL.md automatically from YouTube title analysis
python3 scripts/youtube_title_analyzer.py sample_titles.csv -o youtube_titles_custom_SKILL.md

# 3. Turn a video transcript into a multi-platform prompt pack
python3 scripts/transcript_to_prompts.py transcript.txt --keyword "Claude Automation" --cta "https://example.com"

# 4. Convert text to SEO format (each sentence on a new line) and validate the keyword
python3 scripts/format_for_paste.py article.md --keyword "Claude Automation"

# 5. Create a 30-day input/output Excel tracker for your own goal
python3 scripts/generate_30day_tracker.py --goal "Hire SEO Sales Reps" --inputs "Upwork Post,LinkedIn DM,Community Post" --outputs "Applications,Calls Booked,Offers Made" -o my_30day_plan.xlsx

# 6. Clone a GitHub repo and bring it up with Claude Code
bash scripts/github_claude_launcher.sh https://github.com/user/repo
```
