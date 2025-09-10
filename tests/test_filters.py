import pytest

from profile_pdf.generate import _format_duration
from profile_pdf.models import Education, WorkExperience


@pytest.mark.parametrize(
    ("start", "end", "expected"),
    [
        ("2020/01", "2023/12", "2020/01 - 2023/12"),
        ("2020/01", None, "Since 2020/01"),
    ],
)
def test_format_duration(start, end, expected):
    obj = WorkExperience(
        start=start,
        end=end,
        title="unused",
        contract_type=None,
        company="unused",
        location="unused",
        description="unused",
        technologies={},
    )
    assert _format_duration(obj) == expected

    obj2 = Education(
        start=start,
        end=end,
        field_of_study="unused",
        institution="unused",
        degree="unused",
        specialisation="unused",
        thesis="unused",
    )
    assert _format_duration(obj2) == expected
