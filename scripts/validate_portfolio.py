from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
SCRIPT = ROOT / "assets/js/site.js"
CSS = ROOT / "assets/css/site.css"
CV = ROOT / "assets/docs/cv-carlos-franca-junior.pdf"

html = INDEX.read_text(encoding="utf-8") if INDEX.exists() else ""
js = SCRIPT.read_text(encoding="utf-8") if SCRIPT.exists() else ""
css = CSS.read_text(encoding="utf-8") if CSS.exists() else ""
errors = []


def require(condition, message):
    if not condition:
        errors.append(message)


if "--assets-only" in sys.argv:
    require(CV.exists(), "local CV PDF is missing")
    for project in ("meliuz", "kahsh"):
        project_dir = ROOT / "assets/images/projects" / project
        images = [path for path in project_dir.glob("*") if path.is_file()]
        require(images, f"no local images found for {project}")

    if errors:
        print("portfolio asset validation failed:")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    print("portfolio asset validation passed")
    sys.exit(0)


require(INDEX.exists(), "index.html is missing")
require(CV.exists(), "local CV PDF is missing")
require(SCRIPT.exists(), "assets/js/site.js is missing")
require(CSS.exists(), "assets/css/site.css is missing")

for project in ("meliuz", "kahsh"):
    project_dir = ROOT / "assets/images/projects" / project
    images = [path for path in project_dir.glob("*") if path.is_file()]
    require(images, f"no local images found for {project}")

for section_id in ("hero", "about", "skills", "projects", "experience", "history", "contact"):
    require(f'id="{section_id}"' in html, f"missing section: {section_id}")

require('data-language="pt"' in html and 'data-language="en"' in html, "missing PT/EN language controls")
require("data-i18n=" in html, "missing data-i18n translation hooks")
require("francasense@gmail.com" in html, "missing current email")
require("linkedin.com/in/francajunior" in html, "missing current LinkedIn URL")
require("github.com/francasense" in html, "missing current GitHub URL")
require("instagram.com" not in html, "Instagram link should be removed")
require("facebook.com" not in html, "Facebook link should be removed")
require("assets/docs/cv-carlos-franca-junior.pdf" in html, "missing CV download link")
require("Méliuz" in html, "missing Méliuz project card")
require("Kahsh" in html, "missing Kahsh project card")
for company in ("Hitss", "Ernst", "Méliuz", "Accenture"):
    require(company in html, f"missing timeline company: {company}")
for updated_fact in (
    "INMET",
    "07/2025",
    "11/2022",
    "06/2025",
    "Context API",
    "Zustand",
    "Testing Library",
    "Google Colab",
    "Pós-Graduação em Jogos Digitais",
):
    require(updated_fact in html, f"missing updated CV fact: {updated_fact}")

for image_path in (
    "assets/images/projects/meliuz/menu-principal.jpg",
    "assets/images/projects/meliuz/login.jpg",
    "assets/images/projects/meliuz/recarga.jpg",
    "assets/images/projects/kahsh/cadastro.jpg",
    "assets/images/projects/kahsh/relatorios.jpg",
    "assets/images/projects/kahsh/transacoes.jpg",
):
    require(image_path in html, f"missing local project image reference: {image_path}")

for image_tag in re.findall(r"<img\b[^>]*>", html, flags=re.IGNORECASE):
    require(bool(re.search(r'\balt="[^"].*?"', image_tag, flags=re.IGNORECASE)), "project image is missing non-empty alt text")

require("translations" in js and 'pt:' in js and 'en:' in js, "missing PT/EN translation dictionaries")
require("localStorage" in js, "missing language persistence")
require("site.css" in html, "index.html does not load site.css")
require("--color-bg" in css and "--color-accent" in css, "missing dark theme variables")
require("@media" in css and "max-width" in css, "missing responsive breakpoint")
require(":focus-visible" in css, "missing keyboard focus style")
require("prefers-reduced-motion" in css, "missing reduced-motion support")
require("object-fit" in css and "max-width: 100%" in css, "missing constrained project media rules")

data_keys = set(re.findall(r'data-i18n="([^"]+)"', html))
data_keys.update(re.findall(r'data-i18n-alt="([^"]+)"', html))
data_keys.update(re.findall(r'data-i18n-aria-label="([^"]+)"', html))
for key in sorted(data_keys):
    require(key in js, f"translation key is not present in site.js: {key}")
    require(js.count(f'"{key}"') >= 2, f"translation key is not present in both PT/EN dictionaries: {key}")

if errors:
    print("portfolio validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("portfolio validation passed")
