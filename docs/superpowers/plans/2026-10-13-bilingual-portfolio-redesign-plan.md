# Bilingual Portfolio Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the legacy Mobirise homepage with a responsive Portuguese/English portfolio that presents Carlos França's mobile engineering profile, featured Méliuz and Kahsh work, and current professional history.

**Architecture:** Keep the site static and GitHub Pages-compatible. The root `index.html` will contain semantic sections and translation hooks; `assets/js/site.js` will own the translation dictionary, language persistence, mobile navigation, and active-section behavior; `assets/css/site.css` will own the complete visual system and breakpoints. Existing legacy project folders remain untouched.

**Tech Stack:** Semantic HTML5, vanilla CSS, vanilla JavaScript, local image/PDF assets, Python validation script, browser-based visual verification.

**Spec:** `docs/superpowers/specs/2026-10-13-bilingual-portfolio-redesign-design.md`

## Global Constraints

- The published URL and GitHub Pages deployment on `gh-pages` must remain unchanged.
- The site must stay static with no backend, database, CMS, new analytics, or submission form.
- Portuguese is the initial language; English is selected through a visible `PT` / `EN` toggle and persisted in `localStorage`.
- Méliuz and Kahsh must use local project images with descriptive `alt` text; fragile LinkedIn hotlinks are not allowed.
- Hitss, EY, Méliuz, and Accenture must appear in the bilingual timeline.
- Legacy project folders must not be deleted or renamed.
- Desktop and tablet favor one-line hero text; mobile may wrap the hero name, subtitle, and tagline.
- Keyboard focus, visible contrast, semantic headings, and `prefers-reduced-motion` support are required.

## Review Focus

- Missing translation key: the validator and browser toggle must expose any `data-i18n` key without a PT/EN value (Task 2).
- Missing project asset or broken local path: asset validation must fail before the page is considered publishable (Task 1).
- Mobile navigation and wrapped hero text: the visual pass must verify the menu, section anchors, and multi-line hero at mobile width (Task 5).
- Language persistence after reload: the browser pass must confirm the selected language survives a reload (Task 3).
- Accessibility regressions: the HTML/CSS review must verify heading order, image `alt`, keyboard focus, contrast, and reduced-motion behavior (Tasks 2 and 5).

---

### Task 1: Add validation and stage user-owned assets

**Files:**
- Create: `scripts/validate_portfolio.py`
- Create: `assets/images/projects/meliuz/` (local project images)
- Create: `assets/images/projects/kahsh/` (local project images)
- Create: `assets/docs/cv-carlos-franca-junior.pdf`
- Test: `scripts/validate_portfolio.py`

**Interfaces:**
- Consumes: the approved spec, the current CV PDF, and the project images visible in the user's LinkedIn profile.
- Produces: a deterministic validator command and stable local asset paths consumed by the HTML cards.

- [ ] **Step 1: Write the failing validator**

  Implement a Python script that reads `index.html`, `assets/js/site.js`, and the asset directories, then asserts the required section IDs, both language dictionaries, current social links, four timeline companies, local Méliuz/Kahsh images, and the local CV path. It must fail clearly when a required file or translation key is absent.

- [ ] **Step 2: Run the validator before implementation**

  Run: `python3 scripts/validate_portfolio.py`

  Expected: FAIL because the new files, sections, and translation model do not exist yet.

- [ ] **Step 3: Stage image and CV assets**

  Copy the user-provided CV into `assets/docs/cv-carlos-franca-junior.pdf`. Save the best available local images for Méliuz and Kahsh under their project directories. Use stable lowercase filenames and do not modify the original legacy image files. If LinkedIn does not expose downloadable originals, stop this step and request the original image files from the user instead of using fragile external URLs.

- [ ] **Step 4: Re-run asset-only checks**

  Run: `python3 scripts/validate_portfolio.py`

  Expected: still FAIL on missing page structure, but report that staged asset paths are present.

- [ ] **Step 5: Commit the asset and validator foundation**

  ```bash
  git add scripts/validate_portfolio.py assets/images/projects assets/docs/cv-carlos-franca-junior.pdf
  git commit -m "chore: stage portfolio assets and validation"
  ```

### Task 2: Build the semantic bilingual page structure

**Files:**
- Modify: `index.html`
- Modify: `scripts/validate_portfolio.py`

**Interfaces:**
- Consumes: local asset paths from Task 1 and the translation key contract used by Task 3.
- Produces: one semantic page with `data-i18n` hooks, stable section IDs, accessible links, project cards, timeline items, and mobile navigation markup.

- [ ] **Step 1: Extend the failing validator**

  Add assertions for the section IDs `hero`, `about`, `skills`, `projects`, `experience`, `history`, and `contact`; the `PT` / `EN` controls; `data-i18n` attributes; four experience companies; Méliuz/Kahsh cards; local image references with non-empty `alt`; and the download link.

- [ ] **Step 2: Run the structural checks to confirm RED**

  Run: `python3 scripts/validate_portfolio.py`

  Expected: FAIL on the legacy Mobirise structure and missing translation hooks.

- [ ] **Step 3: Replace the root Mobirise markup with semantic HTML**

  Build the page sections in the exact order from the spec. Keep all primary copy in Portuguese in the markup, attach `data-i18n` keys to mutable text, use buttons for language/menu controls, use headings in order, and include local image `alt` text. Preserve links to the current LinkedIn, GitHub, Instagram, Facebook, email, project destinations, and CV.

- [ ] **Step 4: Run structural validation**

  Run: `python3 scripts/validate_portfolio.py`

  Expected: PASS for section structure and local asset references; translation-content assertions may remain RED until Task 3.

- [ ] **Step 5: Commit the semantic page**

  ```bash
  git add index.html scripts/validate_portfolio.py
  git commit -m "feat: add bilingual portfolio page structure"
  ```

### Task 3: Implement the bilingual content model and interactions

**Files:**
- Create: `assets/js/site.js`
- Modify: `index.html`
- Modify: `scripts/validate_portfolio.py`

**Interfaces:**
- Produces `translations: Record<"pt" | "en", Record<string, string>>`.
- Produces `getPreferredLanguage(): "pt" | "en"`.
- Produces `setLanguage(language: "pt" | "en"): void`.
- Produces `applyTranslations(language: "pt" | "en"): void`.
- Produces `initSite(): void` called once on `DOMContentLoaded`.

- [ ] **Step 1: Extend the failing validator**

  Assert that `site.js` defines both `pt` and `en` dictionaries, every HTML `data-i18n` key exists in both dictionaries, the language toggle references both allowed values, and `localStorage` is used under a site-specific key.

- [ ] **Step 2: Run the JavaScript contract checks to confirm RED**

  Run: `python3 scripts/validate_portfolio.py`

  Expected: FAIL because `assets/js/site.js` does not exist.

- [ ] **Step 3: Implement the translation dictionary**

  Add complete Portuguese and English values for navigation, hero, about, stack, projects, timeline, historical portfolio, contact, buttons, image alternatives, and accessibility labels. Keep project and experience content concise and faithful to the CV/LinkedIn source.

- [ ] **Step 4: Implement `getPreferredLanguage`, `setLanguage`, and `applyTranslations`**

  Read only `pt` or `en` from `localStorage`; default to `pt`; update all `[data-i18n]` nodes and translated attributes; update the toggle's selected state and document language; then persist the selection.

- [ ] **Step 5: Implement `initSite` interactions**

  Wire the mobile menu, smooth anchor navigation, active-section indicator using `IntersectionObserver` when available, and a safe fallback when it is not. Respect reduced motion by avoiding forced smooth scrolling when `prefers-reduced-motion: reduce` matches.

- [ ] **Step 6: Run the content and JavaScript contract checks**

  Run: `python3 scripts/validate_portfolio.py`

  Expected: PASS, including equal PT/EN translation-key coverage.

- [ ] **Step 7: Commit the bilingual behavior**

  ```bash
  git add index.html assets/js/site.js scripts/validate_portfolio.py
  git commit -m "feat: add Portuguese and English portfolio content"
  ```

### Task 4: Implement the dark editor-inspired visual system

**Files:**
- Create: `assets/css/site.css`
- Modify: `index.html`
- Modify: `scripts/validate_portfolio.py`

**Interfaces:**
- Consumes: semantic class names and IDs from Task 2 plus interaction hooks from Task 3.
- Produces: responsive desktop/tablet/mobile presentation, grid background, side rail, cards, timeline, focus states, reduced-motion media rule, and image-safe layouts.

- [ ] **Step 1: Extend the validator with visual-contract checks**

  Assert that `index.html` loads `assets/css/site.css`, the stylesheet defines the dark theme variables, the mobile breakpoint, focus-visible styles, `prefers-reduced-motion`, and non-overflowing project media rules.

- [ ] **Step 2: Run the visual-contract checks to confirm RED**

  Run: `python3 scripts/validate_portfolio.py`

  Expected: FAIL because the new stylesheet is absent.

- [ ] **Step 3: Implement the base visual system**

  Add CSS variables, reset styles, grid background, typography, accent color, side rail, hero, section labels, buttons, project cards, tags, timeline, contact, and footer. Keep the implementation dependency-free and use the existing local font assets only where they load reliably.

- [ ] **Step 4: Implement responsive and accessibility behavior**

  Collapse the rail into a mobile menu, use one-column sections on narrow screens, allow hero text and project descriptions to wrap, constrain images with `object-fit` and `max-width`, provide `:focus-visible` styles, and disable nonessential motion under `prefers-reduced-motion`.

- [ ] **Step 5: Run the validator and `git diff --check`**

  Run: `python3 scripts/validate_portfolio.py && git diff --check`

  Expected: PASS with no whitespace errors.

- [ ] **Step 6: Commit the visual system**

  ```bash
  git add index.html assets/css/site.css scripts/validate_portfolio.py
  git commit -m "feat: add editor-inspired portfolio styling"
  ```

### Task 5: Verify locally and publish

**Files:**
- Modify: `scripts/validate_portfolio.py` only if verification reveals a missing deterministic check.

**Interfaces:**
- Consumes: completed page, assets, translation behavior, and visual system from Tasks 1–4.
- Produces: verified local preview and a published `gh-pages` commit.

- [ ] **Step 1: Run the complete deterministic checks**

  Run: `python3 scripts/validate_portfolio.py && git diff --check && git status --short`

  Expected: validator passes, diff check is clean, and only intended redesign files are present.

- [ ] **Step 2: Preview the site locally**

  Run a local static server from the repository root and inspect the page at desktop, tablet, and mobile viewport sizes. Confirm hero wrapping on mobile, side-rail/menu behavior, project image cropping, PT/EN switching, selected language after reload, keyboard focus, and all contact/project links.

- [ ] **Step 3: Perform a final content review**

  Compare visible copy against the approved CV/LinkedIn facts. Confirm no stale Mobirise hero, outdated social link, Twitter/YouTube link, or incorrect company/date remains in the new root page.

- [ ] **Step 4: Commit any final verification-only fixes**

  ```bash
  git add .
  git commit -m "chore: verify bilingual portfolio release"
  ```

- [ ] **Step 5: Publish to GitHub Pages**

  ```bash
  git push origin HEAD:gh-pages
  gh api repos/francasense/francajr/pages/builds/latest --jq '{status,commit,updated_at}'
  ```

  Expected: the Pages build reports `built` and the commit matches the pushed commit.

- [ ] **Step 6: Verify the public page**

  Load `https://francasense.github.io/francajr/?v=<commit>` and confirm the new title, hero, bilingual controls, featured project cards, local assets, and current contact links are served publicly.
