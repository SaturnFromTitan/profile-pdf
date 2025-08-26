import logging
import pathlib
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from weasyprint import CSS, HTML
from weasyprint.text.fonts import FontConfiguration

from .models import Profile

logger = logging.getLogger(__name__)

PACKAGE_DIR = pathlib.Path(__file__).parent
TEMPLATES_DIR = PACKAGE_DIR / "templates"
STYLES_DIR = PACKAGE_DIR / "styles"
REPO_ROOT = PACKAGE_DIR.parent.parent
OUTPUT_DIR = REPO_ROOT / "output"


def main() -> None:
    # File paths
    css_file = STYLES_DIR / "tailwind.css"
    output_file = OUTPUT_DIR / "profile.pdf"
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Create profile instance
    profile = Profile()

    # Generate HTML content from profile model
    html_content = _generate_html_from_profile(profile)

    # Generate PDF
    success = _generate_pdf(html_content, css_file, output_file)

    if success:
        sys.exit(0)
    else:
        sys.exit(1)


def _generate_html_from_profile(profile: Profile) -> str:
    """Generate HTML content from profile model using Jinja2 template"""
    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR), autoescape=True)
    template = env.get_template("profile.html")

    # Render template with profile data
    return template.render(profile=profile)


def _generate_pdf(
    html_content: str,
    css_file: str | Path,
    output_file: str | Path,
) -> bool:
    """Generate PDF from HTML content and CSS file"""
    try:
        # Read CSS file
        with open(css_file, encoding="utf-8") as f:
            css_content = f.read()

        # Configure fonts
        font_config = FontConfiguration()

        # Create HTML object
        html_doc = HTML(string=html_content, base_url=Path.cwd())

        # Create CSS object
        css_doc = CSS(string=css_content, font_config=font_config)

        # Generate PDF
        html_doc.write_pdf(output_file, stylesheets=[css_doc], font_config=font_config)

        return True
    except Exception:
        logger.exception("Failed to generate PDF")
        return False
