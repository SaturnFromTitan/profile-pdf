import pathlib
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, StringConstraints

from . import MEDIA_DIR

YearMonth = Annotated[str, StringConstraints(pattern=r"^20\d{2}/(0[1-9]|1[0-2])$")]


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
    start: YearMonth
    end: YearMonth | None = None
    location: str | None
    description: str
    bullet_points: list[str] = []
    technologies: dict[str, list[str]]


class Education(BaseModel):
    """Education"""

    field_of_study: str
    institution: str
    degree: str
    start: YearMonth
    end: YearMonth | None = None
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
                Technology(name="Event-Driven Software Architectures", years=4),
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
            start="2025/03",
            end="2025/07",
            location="Remote",
            description="Helped Vonovia to extend its internal elevator IoT platform to support external clients.",
            bullet_points=[
                "Proactive role in architecture and feature design",
                "Directly collaborated with users and non-technical stakeholders",
                "Developed features in a vast micro-service landscape",
                "Upgraded tooling and drastically improved test coverage",
            ],
            technologies={
                "Python": [
                    "Alembic",
                    "Asyncio",
                    "Boto3",
                    "FactoryBoy",
                    "FastAPI",
                    "Httpx",
                    "Mypy",
                    "Pika",
                    "Pydantic",
                    "Pytest",
                    "Ruff",
                    "SQLAlchemy",
                    "Threading",
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
                    "Grafana",
                    "Helm",
                    "Just",
                    "K9s",
                    "MariaDB",
                    "OpenAPI",
                    "PostgreSQL",
                    "Pre-Commit",
                    "Prometheus",
                    "RabbitMQ",
                ],
            },
        ),
        WorkExperience(
            title="Senior Full-Stack Developer",
            contract_type=ContractType.FREELANCE,
            company="Tomorrow Education Group",
            start="2025/05",
            end="2025/05",
            location="Remote",
            description="Built a custom browser extension to automate tedious, critical workflows within a SaaS CMS.",
            bullet_points=[
                "Discussed the business problem directly with non-technical stakeholders to gather requiremnts",
                "Decided for a manifest v3 Chrome extension after comparing it to various alternative solutions",
                "Private distribution to the Chrome Web Store",
                "After 2 weeks, we launched smoothly",
                "The tool significantly improved the efficiency of the marketing team",
            ],
            technologies={
                "TypeScript": [
                    "ESLint",
                    "Jest",
                    "Prettier",
                ],
                "Others": [
                    "Chrome Web Store",
                    "GitHub Actions",
                    "Just",
                    "Manifest V3",
                    "Pre-Commit",
                ],
            },
        ),
        WorkExperience(
            title="Senior Backend Developer",
            contract_type=ContractType.FREELANCE,
            company="Bayer AG",
            start="2023/01",
            end="2025/02",
            location="Remote",
            description='Bayer\'s Crop Protection Innovation Lab builds AI-driven IoT products for farmers (<a href="https://magicscout.app/de-DE/magictrap">magicscout.app</a>).',
            bullet_points=[
                "Integration of custom-built AI models to deliver real-time insights to customers",
                "Backend for mobile apps and tens of thousands of IoT devices and DJI drones",
                "Cost-effective, serverless, event-driven ingestion of GBs of image data on AWS",
                "Proactive role in architecture and feature design",
                "Proactive cross-team communication",
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
                    "MongoDB",
                    "OAuth 2.0",
                    "OpenAPI",
                    "Pre-Commit",
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
            title="Solution Architect",
            contract_type=ContractType.CONSULTANT,
            company="Selly Biz",
            start="2023/05",
            end="2023/05",
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
            start="2022/08",
            end="2022/10",
            location="Berlin",
            description='Kickstarted a platform for German companies to hire international kitchen staff (<a href="https://www.chef-bao.com/">chef-bao.com</a>).',
            bullet_points=[
                "Built a custom web application for job listings and CV submissions",
                "In-house experts reviewed CVs and matched candidates to open positions",
                "As the sole developer, I was responsible for FE, BE, infrastructure, deployments and observability",
                "Optimized applicant-facing pages for mobile",
                "After 2 months, we launched smoothly to an international user base",
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
                    "DrawIO",
                    "GitHub Actions",
                    "Heroku",
                    "HTML",
                    "JavaScript",
                    "Localstack",
                    "OAuth 2.0",
                    "PostgreSQL",
                    "Pre-Commit",
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
            start="2021/07",
            end="2022/06",
            location="Berlin",
            description='Collaborating with Europe\'s leading producer (<a href="https://en.wikipedia.org/wiki/Lonza_Group">Lonza</a>), we built a start-up to sell innovative food supplements.',
            bullet_points=[
                "Scaled to 6-figure annual revenue while automating nearly all operative tasks",
                "Built a full-stack webshop on Django Oscar",
                "Integrated payments via PayPal and Stripe",
                "Reporting with Apache Airflow and Metabase",
                "Custom reports to analyse marketing ROAS and customer lifetime value",
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
                    "Bootstrap CSS",
                    "Dependabot",
                    "Docker",
                    "DrawIO",
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
                    "Pre-Commit",
                    "Redis",
                    "Selenium",
                    "Sentry",
                    "Stripe",
                ],
            },
        ),
        # WorkExperience(
        #     title="External Advisor",
        #     contract_type=ContractType.CONSULTANT,
        #     company="HelloFresh",
        #     start="2020/03",
        #     end="2020/03",
        #     location="Remote",
        #     description="External audit of HelloFresh's Marketing Business Intelligence.",
        #     technologies={
        #         "Others": ["Facebook Ads", "Google Ads", "Google Analytics"],
        #     },
        # ),
        WorkExperience(
            title="Open Source Contributor",
            contract_type=None,
            company="Pandas",
            start="2019/10",
            end="2020/04",
            location="Remote",
            description="Contributed regularly to pandas to learn its internals and to give back to the community.",
            technologies={
                "Python": ["Pandas", "Pytest"],
            },
        ),
        WorkExperience(
            title="Lead Backend Developer",
            contract_type=ContractType.CONSULTANT,
            company="Zalando Marketing Services",
            start="2018/12",
            end="2021/07",
            location="Berlin",
            description="Zalando was unhappy with their Salesforce integration, so we set out to build a greenfield CRM application to manage sales processes end to end.",
            bullet_points=[
                "Onboarded first users after 2 months; deprecated Salesforce after 4 months",
                "Managed campaigns worth >€100M after 1 year",
                "Led the backend team and authored most backend code",
                "Close collaboration with CTO, PO, other teams, and users",
                "Drove architecture and feature discussions",
                "Proactive ideation of new features and identification of current bottleneck",
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
                    "DrawIO",
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
                    "Pre-Commit",
                    "Prometheus",
                    "React",
                    "Sentry",
                    "TypeScript",
                ],
                "Work Method": ["Initially Kanban, later Scrum"],
            },
        ),
        # WorkExperience(
        #     title="Backend Developer",
        #     contract_type=ContractType.CONSULTANT,
        #     company="BlaBlaCar",
        #     start="2019/05",
        #     end="2019/07",
        #     location=None,
        #     description="Build an internal application to automate Google Ads campaign managemnet.",
        #     technologies={
        #         "Python": [
        #             "Flask",
        #             "Mypy",
        #             "Pytest",
        #             "Requests",
        #         ],
        #         "Others": [
        #             "BitBucket", "Bootstrap CSS", "Google Cloud (GCP)", "HTML", "WebSockets",
        #         ],
        #     },
        # ),
        WorkExperience(
            title="Backend Developer",
            contract_type=ContractType.CONSULTANT,
            company="Zalando Marketing Services",
            start="2018/02",
            end="2018/12",
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
                    "DrawIO",
                    "GitHub",
                    "OAuth 2.0",
                    "Presto",
                ],
                "Work Method": ["Kanban"],
            },
        ),
        # WorkExperience(
        #     title="Data Engineer",
        #     contract_type=ContractType.CONSULTANT,
        #     company="Clearly",
        #     start="2017/09",
        #     end="2018/02",
        #     location="Vancouver, BC (Canada)",
        #     description="In-house expert for web tracking, marketing and BI tools.",
        #     technologies={
        #         "Python": ["Pandas", "Pytest"],
        #         "Others": [
        #             "Adobe Analytics", "Dash", "GitHub", "Facebook Ads", "Google Ads", "Google Analytics", "Google Tag Manager", "R", "Shiny",
        #         ],
        #     },
        # ),
        # WorkExperience(
        #     title="Performance Marketing Automation Engineer",
        #     contract_type=ContractType.FREELANCE,
        #     company="Omio (formerly GoEuro)",
        #     start="2017/02",
        #     end="2017/06",
        #     location="Berlin",
        #     description="Custom Python scripts to automate Google Ads campaign management.",
        #     technologies={
        #         "Python": ["Pandas", "Pytest"],
        #         "Others": [
        #             "AWS Redshift", "GitHub", "Google Ads", "Google Tag Manager", "Google Analytics",
        #         ],
        #     },
        # ),
        WorkExperience(
            title="Performance Marketing Automation Engineer",
            contract_type=ContractType.EMPLOYED,
            company="Auto1 AG",
            start="2016/02",
            end="2017/02",
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
            start="2013/02",
            end="2015/02",
            location="Leipzig",
            description="In-house expert for web tracking and reporting tools.",
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
            start="2010/10",
            end="2016/02",
            specialisation="Mathematical optimisation of business problems",
            thesis="Design and implementation of a swarm intelligence algorithm to solve scheduling problems (flow shop)",
        ),
    ]
