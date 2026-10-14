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
require("instagram.com/carlos.fjr" in html, "missing current Instagram URL")
for company in ("Hitss", "Ernst", "Méliuz", "Accenture"):
    require(company in html, f"missing timeline company: {company}")

require("translations" in js and 'pt:' in js and 'en:' in js, "missing PT/EN translation dictionaries")
require("localStorage" in js, "missing language persistence")
require("site.css" in html, "index.html does not load site.css")
require(":focus-visible" in css, "missing keyboard focus style")
require("prefers-reduced-motion" in css, "missing reduced-motion support")

data_keys = set(re.findall(r'data-i18n="([^"]+)"', html))
for key in sorted(data_keys):
    require(key in js, f"translation key is not present in site.js: {key}")

if errors:
    print("portfolio validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("portfolio validation passed")
