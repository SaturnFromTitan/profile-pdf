import pathlib

PACKAGE_DIR = pathlib.Path(__file__).parent
REPO_ROOT = PACKAGE_DIR.parent.parent

# inputs
TEMPLATES_DIR = PACKAGE_DIR / "templates"
STYLES_DIR = PACKAGE_DIR / "styles"
MEDIA_DIR = PACKAGE_DIR / "media"

# outputs
OUTPUT_DIR = REPO_ROOT / "output"
