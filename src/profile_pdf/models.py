import pathlib
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, StringConstraints

from . import MEDIA_DIR

DEFAULT_PHONE_NUMBER = "(upon request)"

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
    logo: pathlib.Path
    contract_type: ContractType | None
    company: str
    start: YearMonth
    end: YearMonth | None = None
    location: str = "Remote"
    description: str
    bullet_points: list[str] = []
    technologies: dict[str, list[str]]


class Education(BaseModel):
    """Education"""

    logo: pathlib.Path
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
    phone: str = DEFAULT_PHONE_NUMBER
    email: str = "martin@pythonation.de"
    linkedin: str = "@martin-winkel"

    # Links to other platforms
    links: Links = Links(
        medium="SaturnFromTitan",
        github="SaturnFromTitan",
    )

    # Professional summary
    summary: list[str] = [
        '<span class="highlighted">Lead Python Backend Developer</span> and <span class="highlighted">Certified AWS Solutions Architect</span> with over 10 years of experience. Combining deep technical expertise, a strong product mindset, and excellent communication skills.',
        "I am a very proactive engineer who values code quality, modern tooling, and always follows the latest best practises and standards. I usually come in as the Python reference expert and modernize the applications by improve the tooling, the testability, coverage metrics, coding & deployment standards and the observability setup. By that I ensure decreased failure rates and increased developer productivity and happiness.",
    ]

    # Skills
    core_skills: list[CoreSkill] = [
        CoreSkill(
            subject="Code",
            technologies=[
                Technology(name="Python", years=11),
                Technology(
                    name="Python Web Frameworks (FastAPI, Django, Flask)", years=8
                ),
                Technology(name="Pydantic (API Validation & Contracts)", years=6),
                Technology(name="Pandas", years=5),
                Technology(name="JavaScript & TypeScript", years=4),
                Technology(name="HTML, CSS", years=6),
            ],
        ),
        CoreSkill(
            subject="DevOps",
            technologies=[
                Technology(name="Amazon Web Services (AWS)", years=6),
                Technology(name="AWS Serverless", years=2),
                Technology(name="Infrastructure as Code (IaC)", years=5),
                Technology(name="CI/CD", years=8),
                Technology(name="Docker", years=8),
                Technology(name="Kubernetes", years=2),
            ],
        ),
        CoreSkill(
            subject="Others",
            technologies=[
                Technology(name="Test-Driven Development", years=10),
                Technology(name="Microservices", years=6),
                Technology(name="REST APIs (incl. OpenAPI/Swagger)", years=6),
                Technology(name="GraphQL APIs", years=2),
                Technology(name="Event-Driven Software Architectures", years=4),
                Technology(name="SQL Databases", years=7),
                Technology(name="NoSQL Databases", years=3),
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
        # WorkExperience(
        #     title="Full-Stack App Developer",
        #     logo=MEDIA_DIR / "comp-logo-pull-up-club.jpeg",
        #     contract_type=None,
        #     company="Personal",
        #     start="2025/11",
        #     end="2025/12",
        #     description="Built a production-ready iOS workout app.",
        #     bullet_points=[
        #         "Offline-first architecture with optional bidirectional cloud sync",
        #         "iOS widget extension and Live Activities for home screen and Dynamic Island",
        #         "CI/CD pipeline with Fastlane and GitHub Actions for automated TestFlight deployments",
        #         "Apple Sign-In integration for authentication and cloud sync",
        #         "Remote config and forced-update functionality",
        #         'Published to the <a href="https://apps.apple.com/app/pull-up-club/id6754757771">Apple App Store</a>',
        #         'Open-sourced the entire codebase on <a href="https://github.com/SaturnFromTitan/pull-up-club">GitHub</a> with comprehensive documentation',
        #     ],
        #     technologies={
        #         "Dart": [
        #             "Drift",
        #             "Flutter",
        #             "Provider",
        #         ],
        #         "Swift": [
        #             "ActivityKit",
        #             "WidgetKit",
        #         ],
        #         "Backend": [
        #             "PostgreSQL",
        #             "PostgREST",
        #             "Supabase",
        #         ],
        #         "DevOps": [
        #             "AppStore Connect",
        #             "Fastlane",
        #             "GitHub Actions",
        #             "GitHub Pages",
        #             "TestFlight",
        #         ],
        #         "Others": [
        #             "Apple Sign-In",
        #             "Figma Make",
        #             "Figma MCP",
        #             "Pre-Commit",
        #             "Sentry",
        #             "SQLite",
        #             "XCode",
        #         ],
        #     },
        # ),
        WorkExperience(
            title="Senior Backend Developer",
            logo=MEDIA_DIR / "comp-logo-vonovia.jpeg",
            contract_type=ContractType.FREELANCE,
            company="Vonovia SE",
            start="2025/03",
            end="2025/07",
            description="Refactoring and extending Vonovia's internal elevator IoT platform to support external clients, including API design improvements.",
            bullet_points=[
                "Reference expert for Python",
                "Stepwise modernization of FastAPI, Pydantic and Dataclasses codebase with minimal regression risks",
                "Improved the API error handling, response schemas, exceptions, validation by upgrading to Pydantic v2",
                "Upgraded the Python version from 3.7 to 3.12",
                "Improved project structure and internal abstractions (modularization, clear ownership, decoupling)",
                "Introduced automated unit and integration tests and typing in a large legacy codebase",
                "Established code standards: linters, formatters, naming conventions, pre-commit, mypy and enforced them as CI checks",
                "Improved stability by handling timeouts, retries, clean error paths and resource limits in a microservice architecture",
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
        # WorkExperience(
        #     title="Lead Full-Stack Developer",
        #     logo=MEDIA_DIR / "comp-logo-teg.jpeg",
        #     contract_type=ContractType.FREELANCE,
        #     company="Tomorrow Education Group",
        #     start="2025/05",
        #     end="2025/05",
        #     description="Built a custom browser extension to automate tedious, critical workflows within a SaaS CMS.",
        #     bullet_points=[
        #         "Gathered requirements directly with non-technical stakeholders to understand the business problem",
        #         "Evaluated and selected manifest v3 Chrome extension after comparing various alternative solutions",
        #         "Managed private distribution to the Chrome Web Store",
        #         "Delivered smooth launch within 2 weeks",
        #         "Improved marketing team efficiency significantly through automation",
        #     ],
        #     technologies={
        #         "TypeScript": [
        #             "ESLint",
        #             "Jest",
        #             "Prettier",
        #         ],
        #         "Others": [
        #             "CSS",
        #             "Chrome Web Store",
        #             "GitHub Actions",
        #             "HTML",
        #             "Just",
        #             "Manifest V3",
        #             "Pre-Commit",
        #         ],
        #     },
        # ),
        WorkExperience(
            title="Senior Backend Developer",
            logo=MEDIA_DIR / "comp-logo-bayer.jpeg",
            contract_type=ContractType.FREELANCE,
            company="Bayer AG",
            start="2023/01",
            end="2025/02",
            description='Refactoring and modernizing Bayer\'s Crop Protection Innovation Lab AI-driven IoT platform for farmers (<a href="https://magicscout.app/de-DE/magictrap">magicscout.app</a>), including API design improvements. Gathering plant images via drones and other IoT devices directly in the field and analyzing them in near real-time with AI to detect diseases and pests.',
            bullet_points=[
                "Integrated custom-built AI models to deliver real-time insights to customers",
                "Built backend for mobile apps and tens of thousands of IoT devices and DJI drones",
                "Cost-effective, serverless, event-driven ingestion of GBs of image data on AWS",
                "Stepwise modernization of a legacy FastAPI codebase (upgrading to Python 3.12, to Pydantic v2)",
                "Improved the structured logging, by improving log levels for reliable alerting and adding tracing via correlation IDs and coupling it with tools like Sentry and AWS XRay",
                "Standardized API behavior: error handling, response schemas, exceptions, validation with Pydantic",
                "Established company wide coding standards for linters, formatters and naming conventions via pre-commit hooks and CI integration",
                "Defined a clean package and release management for internal built artifacts and libraries",
                "Improved on security standards like secrets handling (AWS Systems Manager SSM, KMS), input validation, safe defaults",
                "Improved stability by adding good defaults for timeouts, retries, circuit-breaker patterns, resource limits, clean error paths (internal python frameworks and terraform libraries)",
                "Collaborated with DevOps/platform team for observability (CloudWatch, Grafana, XRay, Prometheus) and operational requirements",
                "Reference expert for Python: introduced and enforced standards across teams",
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
                    "CSS",
                    "D3",
                    "Dart",
                    "Dependabot",
                    "Docker",
                    "DrawIO",
                    "FigJam",
                    "Flutter",
                    "GitHub Actions",
                    "GitHub Pages",
                    "GitLab CI",
                    "Go",
                    "HTML",
                    "ImageMagick",
                    "JavaScript",
                    "MongoDB",
                    "OAuth 2.0",
                    "OpenAPI",
                    "Pre-Commit",
                    "Sentry",
                    "SonarQube",
                    "Terraform",
                    "TestFlight",
                    "TFSec",
                    "Trivy",
                    "TypeScript",
                ],
                "Work Method": ["Scrum"],
            },
        ),
        WorkExperience(
            title="Solution Architect",
            logo=MEDIA_DIR / "comp-logo-selly.jpeg",
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
            logo=MEDIA_DIR / "comp-logo-selly.jpeg",
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
                "After less than 2 months, we launched smoothly to an international user base",
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
            logo=MEDIA_DIR / "comp-logo-lemontree.jpeg",
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
                "Implemented reporting with Apache Airflow and Metabase",
                "Created custom reports to analyze marketing ROAS and customer lifetime value",
                "Designed custom bidding algorithm for Amazon Ads",
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
        #     logo=MEDIA_DIR / "comp-logo-hellofresh.jpeg",
        #     contract_type=ContractType.CONSULTANT,
        #     company="HelloFresh",
        #     start="2020/03",
        #     end="2020/03",
        #     description="External audit of HelloFresh's Marketing Business Intelligence.",
        #     technologies={
        #         "Others": ["Facebook Ads", "Google Ads", "Google Analytics"],
        #     },
        # ),
        # WorkExperience(
        #     title="Open Source Contributor",
        #     logo=MEDIA_DIR / "comp-logo-pandas.jpeg",
        #     contract_type=None,
        #     company="Pandas",
        #     start="2019/10",
        #     end="2020/04",
        #     description="Contributed regularly to pandas to learn its internals and to give back to the community.",
        #     technologies={
        #         "Python": ["Pandas", "Pytest"],
        #     },
        # ),
        WorkExperience(
            title="Lead Backend Developer",
            logo=MEDIA_DIR / "comp-logo-zalando.jpeg",
            contract_type=ContractType.CONSULTANT,
            company="Zalando Marketing Services",
            start="2018/12",
            end="2021/07",
            location="Berlin",
            description="Built a greenfield CRM application with Django Rest Framework: defined and implemented standards for API design, error handling, project structure, code quality, and stability.",
            bullet_points=[
                "Onboarded first users after 2 months; deprecated Salesforce after 4 months",
                "Managed campaigns worth >€100M after 1 year",
                "Led the backend team, authored most backend code and defined coding quality standards",
                "Collaborated closely with CTO, PO, other teams, and users",
                "Drove architecture and feature discussions",
                "Identified bottlenecks and proactively ideated new features",
                "Defined and hands-on implemented code standards: linters, formatters, naming conventions, CI integration",
                "Build a reliable release process (CI/CD) with staging and production environments",
                "Introduced consistent logging standards (structured logs, correlation IDs, meaningful log levels)",
                "Standardized API behavior: error handling, response schemas, exceptions, validation (DRF Serializers, OpenAPI/Swagger)",
                "Built clear project structure and internal abstractions (modularization, clear ownership, decoupling)",
                "Improved stability: timeouts, retries, clean error paths, resource limits",
                "Collaborated with DevOps/platform team for observability (Grafana, Prometheus) and operational requirements",
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
        #     logo=MEDIA_DIR / "comp-logo-blablacar.jpeg",
        #     contract_type=ContractType.CONSULTANT,
        #     company="BlaBlaCar",
        #     start="2019/05",
        #     end="2019/07",
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
        # WorkExperience(
        #     title="Backend Developer",
        #     logo=MEDIA_DIR / "comp-logo-zalando.jpeg",
        #     contract_type=ContractType.CONSULTANT,
        #     company="Zalando Marketing Services",
        #     start="2018/02",
        #     end="2018/12",
        #     location="Berlin",
        #     description="Automate critical sales processes to enable growth.",
        #     bullet_points=[
        #         "Built Flask microservices to create sales reports and slide decks",
        #         "Collaborated closely with CTO, BI, and Sales teams",
        #     ],
        #     technologies={
        #         "Python": [
        #             "Flask",
        #             "Openpyxl",
        #             "Pandas",
        #             "Poetry",
        #             "Pytest",
        #             "python-pptx",
        #             "SQLAlchemy",
        #         ],
        #         "AWS": ["ALB", "EC2", "IAM", "S3"],
        #         "Others": [
        #             "BigQuery",
        #             "Docker",
        #             "DrawIO",
        #             "GitHub",
        #             "OAuth 2.0",
        #             "Presto",
        #         ],
        #         "Work Method": ["Kanban"],
        #     },
        # ),
        # WorkExperience(
        #     title="Data Engineer",
        #     logo=MEDIA_DIR / "comp-logo-clearly.jpeg",
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
        #     logo=MEDIA_DIR / "comp-logo-omio.jpeg",
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
            logo=MEDIA_DIR / "comp-logo-auto1.jpeg",
            contract_type=ContractType.EMPLOYED,
            company="Auto1 AG",
            start="2016/02",
            end="2017/02",
            location="Berlin",
            description="Dramatically improved efficiency and decision-making with custom tools for online marketing platforms.",
            bullet_points=[
                "Designed and implemented Google Ads bidding algorithm",
                "Built scripts and tools to automate online marketing campaign management",
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
        # WorkExperience(
        #     title="Web Analyst (Part-Time)",
        #     logo=MEDIA_DIR / "comp-logo-spreadshirt.jpeg",
        #     contract_type=ContractType.EMPLOYED,
        #     company="Spreadshirt AG",
        #     start="2013/02",
        #     end="2015/02",
        #     location="Leipzig & Berlin",
        #     description="In-house expert for web tracking and reporting tools.",
        #     technologies={
        #         "Others": ["Adobe Analytics", "Excel", "Google Analytics", "Jira"],
        #     },
        # ),
    ]

    # Education
    education: list[Education] = [
        Education(
            logo=MEDIA_DIR / "ed-logo-unileipzig.jpeg",
            field_of_study="Economical Mathematics",
            institution="Leipzig University",
            degree="Diplom (equal to M.Sc.)",
            start="2010/10",
            end="2016/02",
            specialisation="Mathematical optimisation of business problems",
            thesis="Design and implementation of a swarm intelligence algorithm to solve scheduling problems (flow shop)",
        ),
    ]
