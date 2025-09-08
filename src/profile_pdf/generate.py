import logging
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from weasyprint import CSS, HTML
from weasyprint.text.fonts import FontConfiguration

from . import OUTPUT_DIR, STYLES_DIR, TEMPLATES_DIR
from .models import Profile

logger = logging.getLogger(__name__)


def main() -> None:
    # File paths
    output_file = OUTPUT_DIR / "profile.pdf"
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Create profile instance
    profile = Profile()

    # Generate HTML content from profile model
    html_content = _render_html_template(profile)

    # Generate PDF
    success = _generate_pdf(html_content, output_file)

    if success:
        sys.exit(0)
    else:
        sys.exit(1)


def _render_html_template(profile: Profile) -> str:
    """Generate HTML content from profile model using Jinja2 template"""
    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR), autoescape=True)
    template = env.get_template("profile.html")

    # Render template with profile data
    return template.render(profile=profile)


def _generate_pdf(
    html_content: str,
    output_file: Path,
) -> bool:
    """Generate PDF from HTML content and CSS file"""
    try:
        font_config = FontConfiguration()

        # Create HTML object
        html_doc = HTML(string=html_content, base_url=Path.cwd())

        # Generate PDF
        html_doc.write_pdf(
            output_file,
            stylesheets=[
                CSS(filename=str(STYLES_DIR / "custom.css"), font_config=font_config),
            ],
            font_config=font_config,
        )

        return True
    except Exception:
        logger.exception("Failed to generate PDF")
        return False
