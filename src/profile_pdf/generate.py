import datetime
import io
import logging
import zoneinfo
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from weasyprint import CSS, HTML
from weasyprint.text.fonts import FontConfiguration

from . import OUTPUT_DIR, STYLES_DIR, TEMPLATES_DIR
from .models import Profile

logger = logging.getLogger(__name__)


def main() -> None:
    buffer = _main()

    # persist to disk
    output_file = OUTPUT_DIR / "profile.pdf"
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_bytes(buffer.getvalue())


def _main() -> io.BytesIO:
    target = io.BytesIO()

    # Instantiate metadata
    profile = Profile()

    # render HTML content from profile model
    html_content = _render_html_template(profile)

    # render PDF
    _render_pdf(target, html_content)
    return target


def _render_html_template(profile: Profile) -> str:
    """Generate HTML content from profile model using Jinja2 template"""
    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR), autoescape=True)
    template = env.get_template("profile.html")

    # Render template with profile data
    today = datetime.datetime.now(tz=zoneinfo.ZoneInfo("Europe/Berlin")).date()
    return template.render(profile=profile, today=today)


def _render_pdf(target: io.BytesIO, html_content: str) -> bytes:
    """Generate PDF from HTML content and CSS file"""
    font_config = FontConfiguration()
    stylesheets = [
        CSS(filename=str(STYLES_DIR / "custom.css"), font_config=font_config),
    ]
    html_doc = HTML(string=html_content, base_url=Path.cwd())
    return html_doc.write_pdf(target, stylesheets=stylesheets, font_config=font_config)
