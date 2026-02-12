import datetime
import io
import logging
import zoneinfo
from pathlib import Path

import dotenv
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from weasyprint import CSS, HTML
from weasyprint.text.fonts import FontConfiguration

from . import OUTPUT_DIR, REPO_ROOT, STYLES_DIR, TEMPLATES_DIR
from .models import DEFAULT_PHONE_NUMBER, Education, Profile, WorkExperience

DEFAULT_FILE_NAME = "profile.pdf"

logger = logging.getLogger(__name__)


def main() -> None:
    # Optional configurations for customised local execution
    env_file = REPO_ROOT / ".env"
    config = dotenv.dotenv_values(env_file)
    file_name = config.get("FILE_NAME") or DEFAULT_FILE_NAME
    phone_number = config.get("PHONE_NUMBER") or DEFAULT_PHONE_NUMBER

    # render PDF
    buffer = _main(phone_number)

    # persist to disk
    output_file = OUTPUT_DIR / file_name
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_bytes(buffer.getvalue())


def _main(phone_number: str = DEFAULT_PHONE_NUMBER) -> io.BytesIO:
    target = io.BytesIO()

    # Instantiate metadata
    profile = Profile(phone=phone_number)

    # render HTML content from profile model
    html_content = _render_html_template(profile)

    # render PDF
    _render_pdf(target, html_content)
    return target


def _render_html_template(profile: Profile) -> str:
    """Generate HTML content from profile model using Jinja2 template"""
    # Set up Jinja2 environment
    env = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=True,
        undefined=StrictUndefined,
    )
    env.filters["format_duration"] = _format_duration

    template = env.get_template("profile.html")

    # Render template with profile data
    today = datetime.datetime.now(tz=zoneinfo.ZoneInfo("Europe/Berlin")).date()
    return template.render(profile=profile, today=today)


def _format_duration(obj: WorkExperience | Education) -> str:
    """Format duration string from an object with start and end attributes"""
    if obj.end:
        return f"{obj.start} - {obj.end}"
    return f"Since {obj.start}"


def _render_pdf(target: io.BytesIO, html_content: str) -> bytes:
    """Generate PDF from HTML content and CSS file"""
    font_config = FontConfiguration()
    stylesheets = [
        CSS(filename=str(STYLES_DIR / "base.css"), font_config=font_config),
        CSS(filename=str(STYLES_DIR / "cover_page.css")),
        CSS(filename=str(STYLES_DIR / "experiences.css")),
    ]
    html_doc = HTML(string=html_content, base_url=Path.cwd())
    return html_doc.write_pdf(target, stylesheets=stylesheets, font_config=font_config)
