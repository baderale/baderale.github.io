# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Personal portfolio site for **https://baderale.github.io/** — a GitHub Pages user site served from the `main` branch root. The deliverable is a single self-contained `index.html` with all CSS inlined; there is no build step, no JS framework, and no bundler. Pushing to `main` triggers a Pages rebuild automatically.

## Local development

The repo ships a tiny livereload server so changes to HTML/CSS/JS hot-reload in the browser:

```bash
uv run python serve.py
```

Serves `index.html` at http://127.0.0.1:5500/ and watches `*.html`, `*.css`, `*.js` recursively. Python 3.12+ via `uv` (see `pyproject.toml`, `uv.lock`).

There are no tests, lints, or build commands — this is a static one-page site.

## Architecture

`index.html` is monolithic by design. Editing conventions:

- **CSS lives in a single `<style>` block in `<head>`.** Color/spacing tokens are defined as custom properties under `:root` near the top — reuse them rather than introducing hex values inline. Sections inside the stylesheet are demarcated with `/* ========== SECTION ========== */` banners that mirror the markup section names (HERO, SKILLS, TIMELINE, etc.). Match an existing banner when adding new styles instead of appending to the bottom.
- **Page sections are delimited by HTML comments** of the same form. Each `<section>` carries an `id` used by the sticky top nav: `#about` (hero), `#skills`, `#stack`, `#projects`, `#experience`, `#contact`. The hero uses `id="about"` even though it's not literally an "about" section — the skills section's `section-label` reads `about.md`, but the nav `about` link points at the top of the page (the hero) by convention.
- **Skill cards** (`.cell`) use a `data-num` attribute that renders the index in the top-right corner via CSS `::before { content: attr(data-num) }`. When adding/removing/reordering cards, keep `data-num` values monotonic (`01`, `02`, …) so the visual numbering stays correct.
- **Design** is modeled on getartcraft.com, light theme only: warm off-white `--bg`, Archivo (wide, heavy) display, Instrument Serif italic accents (`.serif`), Geist Mono uppercase labels (`.mono`), framed sections with `NN / Title` panel heads, a tag ticker, and a fixed scroll ruler + section index (JS at bottom of `index.html`).
- **The portrait is local** at `assets/bader.jpg` (360×478 preview; swap in a higher-res export if available). `assets/avatar.png` is the old pixel-art avatar, now unused. Use relative paths for any new assets so they resolve identically on the dev server and on `baderale.github.io`. GitHub Pages serves on Linux (case-sensitive); stick to lowercase filenames.
- **Sticky nav offset:** the top nav is `position: sticky; top: 0`. `section[id]` has `scroll-margin-top` so anchors clear it.

## Deployment notes

- Remote `origin` points at the public `baderale.github.io` user-site repo on GitHub. Default branch is `main`.
- After `git push origin main`, check Pages build status with `gh api repos/baderale/baderale.github.io/pages/builds/latest` — `status` transitions `building` → `built` in roughly 30–60s. Hard-refresh the live URL to bust the GitHub CDN cache if you see a stale page.
- `.claude/` is gitignored — don't commit local agent state. Same for `.venv/`, `__pycache__/`, build artifacts (see `.gitignore`).
