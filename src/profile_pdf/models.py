import pathlib
from enum import StrEnum

from pydantic import BaseModel

from . import MEDIA_DIR


class LanguageProficiency(StrEnum):
    """Language proficiency"""

    NATIVE_SPEAKER = "Native speaker"
    BUSINESS_FLUENT = "Business fluent"


class Language(BaseModel):
    """Language proficiency information"""

    language: str
    proficiency: LanguageProficiency


class Links(BaseModel):
    """Social media profiles"""

    medium: str
    github: str


class Technology(BaseModel):
    """Technology"""

    name: str
    years: int


class CoreSkill(BaseModel):
    """Skills and experience"""

    subject: str
    technologies: list[Technology]


class Certification(BaseModel):
    """Professional certification"""

    name: str
    code: str


class Profile(BaseModel):
    """Complete profile information"""

    # Images
    profile_image_path: pathlib.Path = MEDIA_DIR / "photo.jpeg"
    icon_paths: list[pathlib.Path] = [
        MEDIA_DIR / "logo-python.png",
        MEDIA_DIR / "logo-aws.png",
    ]

    # Personal information
    name: str = "Martin Winkel"
    location: str = "Berlin (Prenzlauer Berg)"
    languages: list[Language] = [
        Language(language="German", proficiency=LanguageProficiency.NATIVE_SPEAKER),
        Language(language="English", proficiency=LanguageProficiency.BUSINESS_FLUENT),
    ]

    # Contact information
    phone: str = "(hidden)"
    email: str = "martin@pythonation.de"
    linkedin: str = "@martin-winkel"

    # Links to other platforms
    links: Links = Links(
        medium="@SaturnFromTitan",
        github="@SaturnFromTitan",
    )

    # Professional summary
    summary: list[str] = [
        "<strong>Lead Software Engineer</strong> and <strong>Certified AWS Solutions Architect</strong> with over 10 years of experience. Combining deep technical expertise, a strong product mindset, and excellent communication skills.",
        "In 2017, I co-founded and led a software development consultancy focusing on digital transformation. I built and supervised applications of various sizes and business domains for clients ranging from start-ups to DAX companies.",
        "Since 2023, I have been working as a freelance developer and advisor again.",
    ]

    # Skills
    core_skills: list[CoreSkill] = [
        CoreSkill(
            subject="Code",
            technologies=[
                Technology(name="Python", years=10),
                Technology(
                    name="Python Web Frameworks (FastAPI, Django, Flask)", years=7
                ),
                Technology(name="Pydantic", years=5),
                Technology(name="Pandas", years=5),
                Technology(name="TypeScript", years=2),
                Technology(name="HTML, CSS (Bootstrap, Tailwind)", years=3),
                Technology(
                    name="Test-Driven Development (unit, integration, end to end, load testing, etc.)",
                    years=9,
                ),
            ],
        ),
        CoreSkill(
            subject="DevOps",
            technologies=[
                Technology(name="Amazon Web Services (AWS)", years=6),
                Technology(name="AWS Serverless", years=2),
                Technology(name="CI/CD", years=7),
                Technology(name="Docker", years=7),
                Technology(name="Infrastructure as Code (IaC)", years=5),
                Technology(name="Kubernetes", years=1),
            ],
        ),
        CoreSkill(
            subject="Others",
            technologies=[
                Technology(
                    name="SQL Databases (PostgreSQL, MariaDB, MSSQL, etc.)", years=6
                ),
                Technology(
                    name="NoSQL Databases (MongoDB, DocumentDB, DynamoDB)", years=3
                ),
                Technology(name="Microservices", years=6),
                Technology(name="REST APIs (incl. OpenAPI/Swagger)", years=6),
                Technology(name="GraphQL APIs", years=2),
                Technology(name="Serverless Architectures", years=2),
                Technology(name="Event-driven Software Architectures", years=4),
            ],
        ),
    ]

    # Certifications
    certifications: list[Certification] = [
        Certification(name="AWS Solutions Architect - Associate", code="SAA-C03"),
        Certification(name="AWS Certified Developer - Associate", code="DVA-C02"),
    ]
