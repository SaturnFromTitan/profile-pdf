import datetime
import zoneinfo

from pypdf import PdfReader

from profile_pdf.generate import _main


def test_generate():
    buffer = _main()

    # number of pages
    pdf_reader = PdfReader(buffer)
    assert len(pdf_reader.pages) == 4

    # assert content
    # cover page
    first_page_text = pdf_reader.pages[0].extract_text().lower()
    assert "martin winkel" in first_page_text
    assert "personal information" in first_page_text
    assert "contact" in first_page_text
    assert "links" in first_page_text
    assert "core technologies" in first_page_text
    assert "certifications" in first_page_text
    # profile image + 2 icons in the top right
    assert len(pdf_reader.pages[0].images) == 3

    # second page
    second_page_text = pdf_reader.pages[1].extract_text().lower()
    assert "work experience" in second_page_text

    # last page
    last_page_text = pdf_reader.pages[-1].extract_text().lower()
    assert "education" in last_page_text
    assert "mathematics" in last_page_text
    today = datetime.datetime.now(tz=zoneinfo.ZoneInfo("Europe/Berlin")).date()
    assert f"last updated: {today.isoformat()}" in last_page_text
