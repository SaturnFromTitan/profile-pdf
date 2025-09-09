import datetime
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


class ContractType(StrEnum):
    """Language proficiency"""

    FREELANCE = "freelancer"
    CONSULTANT = "consultant"
    EMPLOYED = "employed"


class WorkExperience(BaseModel):
    """Work Experience"""

    title: str
    contract_type: ContractType | None
    company: str
    start: datetime.date
    end: datetime.date | None = None
    location: str | None
    description: str
    bullet_points: list[str]
    technologies: dict[str, list[str]]


class Education(BaseModel):
    """Education"""

    field_of_study: str
    institution: str
    degree: str
    start: datetime.date
    end: datetime.date | None = None
    specialisation: str
    thesis: str


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
    phone: str = "(upon request)"
    email: str = "martin@pythonation.de"
    linkedin: str = "@martin-winkel"

    # Links to other platforms
    links: Links = Links(
        medium="SaturnFromTitan",
        github="SaturnFromTitan",
    )

    # Professional summary
    summary: list[str] = [
        '<span class="highlighted">Lead Software Engineer</span> and <span class="highlighted">Certified AWS Solutions Architect</span> with over 10 years of experience. Combining deep technical expertise, a strong product mindset, and excellent communication skills.',
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
                Technology(name="JavaScript & TypeScript", years=3),
                Technology(name="HTML, CSS", years=5),
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
                Technology(name="Kubernetes", years=2),
            ],
        ),
        CoreSkill(
            subject="Others",
            technologies=[
                Technology(name="SQL Databases", years=6),
                Technology(name="NoSQL Databases", years=3),
                Technology(name="Microservices", years=6),
                Technology(name="REST APIs (incl. OpenAPI/Swagger)", years=6),
                Technology(name="GraphQL APIs", years=2),
                Technology(name="Event-Based Software Architectures", years=4),
                Technology(name="Test-Driven Development", years=9),
            ],
        ),
    ]

    # Certifications
    certifications: list[Certification] = [
        Certification(name="AWS Solutions Architect - Associate", code="SAA-C03"),
        Certification(name="AWS Certified Developer - Associate", code="DVA-C02"),
    ]

    # Work Experience
    work_experience: list[WorkExperience] = [
        WorkExperience(
            title="Senior Backend Developer",
            contract_type=ContractType.FREELANCE,
            company="Vonovia SE",
            start=datetime.date(2025, 3, 1),
            end=datetime.date(2025, 7, 31),
            location="Remote",
            description="TBA",
            bullet_points=[],
            technologies={
                "Python": [
                    "Alembic",
                    "Asyncio",
                    "Boto3",
                    "FactoryBoy",
                    "FastAPI",
                    "Httpx",
                    "Mypy",
                    "Pydantic",
                    "Pytest",
                    "Ruff",
                    "SQLAlchemy",
                    "Uv",
                    "Uvicorn",
                ],
                "Azure": ["ACR", "AKS"],
                "Others": [
                    "Azure DevOps",
                    "Azure DevOps Pipelines",
                    "Bash",
                    "ConceptBoard",
                    "Docker",
                    "Helm",
                    "Just",
                    "K9s",
                    "MariaDB",
                    "OpenAPI",
                    "PostgreSQL",
                ],
            },
        ),
        WorkExperience(
            title="Senior Backend Developer",
            contract_type=ContractType.FREELANCE,
            company="Bayer AG",
            start=datetime.date(2023, 1, 1),
            end=datetime.date(2025, 2, 28),
            location="Remote",
            description='Bayer\'s Crop Protection Innovation Lab builds AI-driven products for farmers (<a href="https://magicscout.app/de-DE/magictrap">magicscout.app</a>).',
            bullet_points=[
                "Backend for mobile apps and tens of thousands of IoT devices",
                "Cost-effective, serverless, event-driven ingestion of GBs of image data on AWS",
                "Integration of in-house AI models to deliver insights to customers in seconds",
                "Proactive role in architecture and feature design",
                "Cross-team communication",
                "Reference expert for Python",
            ],
            technologies={
                "Python": [
                    "AWS Lambda Powertools",
                    "Asyncio",
                    "Boto3",
                    "FastAPI",
                    "Httpx",
                    "Locust",
                    "Motor",
                    "Mypy",
                    "Poetry",
                    "PyMongo",
                    "Pydantic",
                    "Pytest",
                    "Ruff",
                    "Strawberry",
                ],
                "AWS": [
                    "API Gateway",
                    "Athena",
                    "Backup",
                    "CloudFront",
                    "CloudWatch",
                    "CloudTrail",
                    "Cognito",
                    "Cost Explorer",
                    "DevOps Guru",
                    "DocumentDB",
                    "DynamoDB",
                    "EventBridge",
                    "Grafana",
                    "IAM",
                    "Incident Manager",
                    "Lambda",
                    "KMS",
                    "Route53",
                    "S3",
                    "SES",
                    "SNS",
                    "SQS",
                    "Systems Manager (SSM)",
                    "Transit Gateway",
                    "VPC",
                    "WAF",
                    "XRay",
                ],
                "Others": [
                    "Artifactory",
                    "Azure DevOps",
                    "Bash",
                    "Dependabot",
                    "Docker",
                    "DrawIO",
                    "FigJam",
                    "GitHub Actions",
                    "GitLab CI",
                    "Go",
                    "ImageMagick",
                    "JavaScript",
                    "OAuth 2.0",
                    "OpenAPI",
                    "Sentry",
                    "SonarQube",
                    "Terraform",
                    "TFSec",
                    "Trivy",
                    "TypeScript",
                ],
                "Work Method": ["Scrum"],
            },
        ),
        WorkExperience(
            title="Solution Architect & Advisor",
            contract_type=ContractType.CONSULTANT,
            company="Selly Biz",
            start=datetime.date(2023, 5, 1),
            end=datetime.date(2023, 5, 31),
            location="Berlin",
            description="Designed a scalable data ingestion application using Apache Airflow on AWS.",
            bullet_points=[
                "Designed the system with the CEO & CTO",
                "Provided in-depth Apache Airflow knowledge",
            ],
            technologies={
                "Python": ["Airflow", "Dagster", "Prefect"],
                "AWS": ["S3", "Managed Airflow"],
            },
        ),
        WorkExperience(
            title="Lead Full Stack Developer",
            contract_type=ContractType.CONSULTANT,
            company="Selly Biz",
            start=datetime.date(2022, 8, 1),
            end=datetime.date(2022, 10, 31),
            location="Berlin",
            description='Kickstarted a platform for German companies to hire international kitchen staff (<a href="https://www.chef-bao.com/">chef-bao.com</a>).',
            bullet_points=[
                "Built a custom app for job listings and CV submissions",
                "In-house experts reviewed CVs and matched candidates",
                "Optimized applicant-facing pages for mobile",
                "Launched smoothly to an international user base after 2 months",
            ],
            technologies={
                "Python": [
                    "Boto3",
                    "Celery",
                    "Django",
                    "FactoryBoy",
                    "Gunicorn",
                    "Mypy",
                    "Poetry",
                    "Pytest",
                    "Weasyprint",
                ],
                "AWS": ["Route53", "S3", "SES"],
                "Others": [
                    "Dependabot",
                    "Docker",
                    "Draw.io",
                    "GitHub Actions",
                    "Heroku",
                    "HTML",
                    "JavaScript",
                    "Localstack",
                    "OAuth 2.0",
                    "PostgreSQL",
                    "Redis",
                    "Selenium",
                    "Sentry",
                    "Tailwind CSS",
                ],
            },
        ),
        WorkExperience(
            title="Lead Full Stack Developer & Co-Founder",
            contract_type=ContractType.EMPLOYED,
            company="Lemon Tree",
            start=datetime.date(2021, 7, 1),
            end=datetime.date(2022, 6, 30),
            location="Berlin",
            description='Collaborating with Europe\'s leading producer (<a href="https://en.wikipedia.org/wiki/Lonza_Group">Lonza</a>), we built a start-up to sell innovative food supplements.',
            bullet_points=[
                "Scaled to 6-figure annual revenue with heavy automation",
                "Built full-stack webshop on Django Oscar",
                "Payments via PayPal and Stripe",
                "Reporting with Apache Airflow and Metabase",
                "Custom reports on marketing spend vs revenue",
                "Designed a custom bidding algorithm for Amazon Ads",
            ],
            technologies={
                "Python": [
                    "Airflow",
                    "Alembic",
                    "Boto3",
                    "Celery",
                    "Django",
                    "FactoryBoy",
                    "Gunicorn",
                    "Mypy",
                    "Oscar",
                    "Pandas",
                    "Poetry",
                    "Polars",
                    "Pytest",
                    "Ruff",
                    "SQLAlchemy",
                ],
                "AWS": ["IAM", "S3", "SES"],
                "Others": [
                    "Amazon Order API",
                    "Amazon Ads",
                    "Bootstrap",
                    "Dependabot",
                    "Docker",
                    "Draw.io",
                    "Facebook Ads",
                    "GitHub Actions",
                    "Google Ads",
                    "Heroku",
                    "HTML",
                    "JavaScript",
                    "Localstack",
                    "Metabase",
                    "OAuth 2.0",
                    "PayPal",
                    "PostgreSQL",
                    "Redis",
                    "Selenium",
                    "Sentry",
                    "Stripe",
                ],
            },
        ),
        WorkExperience(
            title="Open Source Contributor",
            contract_type=None,
            company="Pandas",
            start=datetime.date(2019, 10, 1),
            end=datetime.date(2020, 4, 30),
            location="Remote",
            description="Contributed regularly to pandas to learn its internals and to give back to the community.",
            bullet_points=[
                "Frequent contributions to pandas",
                "Focused on deepening understanding of library internals",
            ],
            technologies={
                "Python": ["Pandas", "Pytest"],
            },
        ),
        WorkExperience(
            title="Lead Backend Developer",
            contract_type=ContractType.CONSULTANT,
            company="Zalando Marketing Services",
            start=datetime.date(2018, 12, 1),
            end=datetime.date(2021, 7, 31),
            location="Berlin",
            description="Zalando was unhappy with their Salesforce integration, so we set out to build a greenfield CRM application to manage sales processes end to end.",
            bullet_points=[
                "Onboarded first users after 2 months; deprecated Salesforce after 4 months",
                "Managed campaigns worth >€100M after 1 year",
                "Led the backend team and authored most backend code",
                "Close collaboration with CTO, PO, other teams, and users",
                "Proactive ideation and bottleneck identification",
                "Drove architecture and feature discussions",
                "Mentored junior developers",
            ],
            technologies={
                "Python": [
                    "Airflow",
                    "Boto3",
                    "Celery",
                    "Django Rest Framework (DRF)",
                    "FactoryBoy",
                    "Gunicorn",
                    "Mypy",
                    "Poetry",
                    "Pytest",
                    "Requests",
                    "Weasyprint",
                ],
                "AWS": [
                    "ALB",
                    "EC2",
                    "IAM",
                    "Lambda",
                    "RDS",
                    "Route53",
                    "S3",
                    "SQS",
                    "SES",
                    "Systems Manager (SSM)",
                ],
                "Others": [
                    "Docker",
                    "Draw.io",
                    "GitHub",
                    "Grafana",
                    "HTML",
                    "Kubectl",
                    "Kubernetes",
                    "Localstack",
                    "Nakadi (Kafka)",
                    "Nginx",
                    "OAuth 2.0",
                    "OpenAPI/Swagger",
                    "PostgreSQL",
                    "Prometheus",
                    "React",
                    "Sentry",
                    "TypeScript",
                ],
                "Work Method": ["Initially Kanban, later Scrum"],
            },
        ),
        WorkExperience(
            title="Backend Developer",
            contract_type=ContractType.CONSULTANT,
            company="Zalando Marketing Services",
            start=datetime.date(2018, 2, 1),
            end=datetime.date(2018, 12, 31),
            location="Berlin",
            description="Automate critical sales processes to enable growth.",
            bullet_points=[
                "Flask microservices to create sales reports and slide decks",
                "Close collaboration with CTO, BI, and Sales",
            ],
            technologies={
                "Python": [
                    "Flask",
                    "Openpyxl",
                    "Pandas",
                    "Poetry",
                    "Pytest",
                    "python-pptx",
                    "SQLAlchemy",
                ],
                "AWS": ["ALB", "EC2", "IAM", "S3"],
                "Others": [
                    "BigQuery",
                    "Docker",
                    "Draw.io",
                    "GitHub",
                    "OAuth 2.0",
                    "Presto",
                ],
                "Work Method": ["Kanban"],
            },
        ),
        WorkExperience(
            title="Performance Marketing Automation Engineer",
            contract_type=ContractType.EMPLOYED,
            company="Auto1 AG",
            start=datetime.date(2016, 2, 1),
            end=datetime.date(2017, 2, 28),
            location="Berlin",
            description="Dramatically improved efficiency and decision-making with custom tools for online marketing platforms.",
            bullet_points=[
                "Designed and implemented a Google Ads bidding algorithm",
                "Built scripts/tools to automate online marketing campaign management",
            ],
            technologies={
                "Python": ["Pandas", "Pytest"],
                "Others": [
                    "BitBucket",
                    "DigitalOcean",
                    "Facebook Ads",
                    "Google Ads",
                    "Jenkins",
                ],
                "Work Method": ["Scrum"],
            },
        ),
        WorkExperience(
            title="Web Analyst (Part-Time)",
            contract_type=ContractType.EMPLOYED,
            company="Spreadshirt AG",
            start=datetime.date(2013, 2, 1),
            end=datetime.date(2015, 2, 28),
            location="Leipzig",
            description="In-house expert for web tracking and reporting tools.",
            bullet_points=[],
            technologies={
                "Others": ["Adobe Analytics", "Excel", "Google Analytics", "Jira"],
            },
        ),
    ]

    # Education
    education: list[Education] = [
        Education(
            field_of_study="Economical Mathematics",
            institution="Leipzig University",
            degree="Diplom (equal to Master of Science)",
            start=datetime.date(2010, 10, 1),
            end=datetime.date(2016, 2, 1),
            specialisation="Mathematical optimisation of business problems",
            thesis="Design and implementation of a swarm intelligence algorithm to solve scheduling problems (flow shop)",
        ),
    ]
