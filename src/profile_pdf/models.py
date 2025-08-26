from pydantic import BaseModel, Field


class Language(BaseModel):
    """Language proficiency information"""

    language: str
    proficiency: str


class Contact(BaseModel):
    """Contact information"""

    phone: str
    email: str
    linkedin: str


class SocialMedia(BaseModel):
    """Social media profiles"""

    medium_blog: str
    github: str


class PersonalInfo(BaseModel):
    """Personal information section"""

    name: str
    address: str
    languages: list[Language]


class Skills(BaseModel):
    """Skills and experience"""

    code: list[str] = Field(description="Programming and development skills")
    devops: list[str] = Field(description="DevOps and infrastructure skills")
    others: list[str] = Field(description="Other technical skills")


class Certification(BaseModel):
    """Professional certification"""

    name: str
    code: str | None = None


class Profile(BaseModel):
    """Complete profile information"""

    # Basic info
    name: str = "Martin Winkel"
    title: str = "Lead Software Engineer & Certified AWS Solutions Architect"
    subtitle: str = (
        "Over 10 years of experience • Product mindset • Strong communication"
    )

    # Personal information
    address: str = "Berlin (Friedrichshain)"
    languages: list[Language] = [
        Language(language="German", proficiency="Native speaker"),
        Language(language="English", proficiency="Business fluent"),
    ]

    # Contact information
    contact: Contact = Contact(
        phone="+49 160 97064381",
        email="martin@pythonation.de",
        linkedin="@martin-winkel",
    )

    # Social media
    social: SocialMedia = SocialMedia(
        medium_blog="@SaturnFromTitan", github="@SaturnFromTitan"
    )

    # Professional summary
    summary: list[str] = [
        "With over 10 years of experience, combining deep technical expertise, a strong product mindset, and excellent communication skills.",
        "In 2017, I co-founded and led a software development consultancy focusing on digital transformation. I built and supervised applications of various sizes and business domains for clients ranging from start-ups to DAX companies.",
        "Since 2023, I have been working as a freelance developer and advisor again.",
    ]

    # Skills
    skills: Skills = Skills(
        code=[
            "Python: 10 years",
            "Python Web Frameworks (FastAPI, Django, Flask): 7 years",
            "Pydantic: 5 years",
            "Pandas: 5 years",
            "HTML, CSS (Bootstrap, Tailwind): 3 years",
            "Test-driven Development: 7 years",
        ],
        devops=[
            "Amazon Web Services (AWS): 6 years",
            "AWS Serverless: 2 years",
            "CI/CD: 7 years",
            "Docker: 7 years",
            "Infrastructure as Code: 5 years",
            "Kubernetes: 1 year",
        ],
        others=[
            "SQL Databases (PostgreSQL): 6 years",
            "NoSQL Databases (MongoDB, DocumentDB, DynamoDB): 3 years",
            "Microservices: 6 years",
            "REST APIs (incl. OpenAPI/Swagger): 6 years",
            "GraphQL APIs: 2 years",
            "Event-driven Software Architectures: 3 years",
        ],
    )

    # Certifications
    certifications: list[Certification] = [
        Certification(name="AWS Solutions Architect - Associate", code="SAA-C03"),
        Certification(name="AWS Certified Developer - Associate", code="DVA-C02"),
    ]

    # Profile image path
    profile_image: str = "/mnt/data/profile_martin_winkel.jpg"
