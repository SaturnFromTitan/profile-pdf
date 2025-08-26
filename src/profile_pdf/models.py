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
    proficiency: str


class Contact(BaseModel):
    """Contact information"""

    phone: str
    email: str
    linkedin: str


class Links(BaseModel):
    """Social media profiles"""

    medium: str
    github: str


class PersonalInfo(BaseModel):
    """Personal information section"""

    name: str
    address: str
    languages: list[Language]


class TechnologySkill(BaseModel):
    """Technology"""

    name: str
    years: int


class CoreSkill(BaseModel):
    """Skills and experience"""

    subject: str
    technologies: list[TechnologySkill]


class Certification(BaseModel):
    """Professional certification"""

    name: str
    code: str


class Profile(BaseModel):
    """Complete profile information"""

    # Images
    profile_image_path: pathlib.Path = MEDIA_DIR / "photo.jpeg"
    icon_paths: list[pathlib.Path] = [
        MEDIA_DIR / "logo-aws.png",
        MEDIA_DIR / "logo-python.png",
    ]

    # Personal information
    name: str = "Martin Winkel"
    location: str = "Berlin (Prenzlauer Berg)"
    languages: list[Language] = [
        Language(language="German", proficiency=LanguageProficiency.NATIVE_SPEAKER),
        Language(language="English", proficiency=LanguageProficiency.BUSINESS_FLUENT),
    ]

    # Contact information
    contact: Contact = Contact(
        phone="upon request",
        email="martin@pythonation.de",
        linkedin="@martin-winkel",
    )

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
                TechnologySkill(name="Python", years=10),
                TechnologySkill(
                    name="Python Web Frameworks (FastAPI, Django, Flask)", years=7
                ),
                TechnologySkill(name="Pydantic", years=5),
                TechnologySkill(name="Pandas", years=5),
                TechnologySkill(name="TypeScript", years=2),
                TechnologySkill(name="HTML, CSS (Bootstrap, Tailwind)", years=3),
                TechnologySkill(
                    name="Test-Driven Development (unit, integration, end to end, load testing, etc.)",
                    years=9,
                ),
            ],
        ),
        CoreSkill(
            subject="DevOps",
            technologies=[
                TechnologySkill(name="Amazon Web Services (AWS)", years=6),
                TechnologySkill(name="AWS Serverless", years=2),
                TechnologySkill(name="CI/CD", years=7),
                TechnologySkill(name="Docker", years=7),
                TechnologySkill(name="Infrastructure as Code (IaC)", years=5),
                TechnologySkill(name="Kubernetes", years=1),
            ],
        ),
        CoreSkill(
            subject="Others",
            technologies=[
                TechnologySkill(
                    name="SQL Databases (PostgreSQL, MariaDB, MSSQL, etc.)", years=6
                ),
                TechnologySkill(
                    name="NoSQL Databases (MongoDB, DocumentDB, DynamoDB)", years=3
                ),
                TechnologySkill(name="Microservices", years=6),
                TechnologySkill(name="REST APIs (incl. OpenAPI/Swagger)", years=6),
                TechnologySkill(name="GraphQL APIs", years=2),
                TechnologySkill(name="Serverless Architectures", years=2),
                TechnologySkill(name="Event-driven Software Architectures", years=4),
            ],
        ),
    ]

    # Certifications
    certifications: list[Certification] = [
        Certification(name="AWS Solutions Architect - Associate", code="SAA-C03"),
        Certification(name="AWS Certified Developer - Associate", code="DVA-C02"),
    ]
