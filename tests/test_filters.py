import pytest

from profile_pdf.generate import _format_duration
from profile_pdf.models import Education, WorkExperience


@pytest.mark.parametrize(
    ("start", "end", "expected"),
    [
        ("2020/01", "2023/12", "2020/01 - 2023/12"),
        ("2020/01", None, "Since 2020/01"),
        ("2020/01", "", "Since 2020/01"),
    ],
)
@pytest.mark.parametrize("cls", [WorkExperience, Education])
def test_format_duration(start, end, expected, cls):
    obj = cls.model_construct(start=start, end=end)
    assert _format_duration(obj) == expected
