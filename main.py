from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from typing import List, Optional, Union
from pydantic import BaseModel, Field
from datetime import datetime

# from dotenv import load_dotenv
# load_dotenv()

model = init_chat_model("gpt-4o-mini", model_provider="openai")

prompt_template_str = """
You are an expert job posting analysis assistant.

Your task is to extract structured job posting information from the provided job description.

Extract the following fields:
- job_id
- job_title
- required_skills
- posting_timestamp
- location
- preferred_skills
- years_of_experience
- company_name
- salary_range
- coding_languages
- work_environment
- work_schedule
- tools_to_use_on_job
- location_type
- remote_locations
- office_locations

Rules:
- Return valid JSON only
- If a field is not present, return null
- required_skills should always be a list
- preferred_skills should always be a list if present
- coding_languages should always be a list if present
- tools_to_use_on_job should always be a list if present
- salary_range should contain an object with min and max int values and currency as a str

Job Posting:
{input}
"""



class SalaryRange(BaseModel):
    min: int = Field(
        ...,
        description="Minimum salary value"
    )

    max: int = Field(
        ...,
        description="Maximum salary value"
    )

    currency: str = Field(
        ...,
        description="Currency code for the salary range (e.g. USD)"
    )


class JobPosting(BaseModel):
    job_id: str = Field(
        ...,
        description="Unique identifier for the job posting"
    )

    job_title: str = Field(
        ...,
        min_length=2,
        description="Title of the job position"
    )

    required_skills: List[str] = Field(
        ...,
        min_length=1,
        description="List of required skills for the position"
    )

    posting_timestamp: datetime = Field(
        ...,
        description="Timestamp when the job posting was created"
    )

    location: str = Field(
        ...,
        description="Primary job location"
    )

    preferred_skills: Optional[List[str]] = Field(
        default=None,
        description="Optional preferred or bonus skills"
    )

    years_of_experience: Optional[Union[int, str]] = Field(
        default=None,
        description="Years of experience required (e.g. 3 or '3-5')"
    )

    company_name: str = Field(
        ...,
        description="Company offering the job"
    )

    salary_range: SalaryRange = Field(
        ...,
        description="Structured salary range information"
    )

    coding_languages: Optional[List[str]] = Field(
        default=None,
        description="Programming languages required or preferred"
    )

    work_environment: Optional[str] = Field(
        default=None,
        description="Type of work environment (e.g. startup, enterprise)"
    )

    work_schedule: Optional[str] = Field(
        default=None,
        description="Employment schedule (e.g. full-time, contract)"
    )

    tools_to_use_on_job: Optional[List[str]] = Field(
        default=None,
        description="Tools, platforms, or frameworks used in the role"
    )

    location_type: Optional[str] = Field(
        default=None,
        description="Work location type: remote, hybrid, or onsite"
    )

    remote_locations: Optional[List[str]] = Field(
        default=None,
        description="Allowed remote work regions or countries"
    )

    office_locations: Optional[List[str]] = Field(
        default=None,
        description="Physical office locations for hybrid or onsite roles"
    )

prompt_template = PromptTemplate.from_template(prompt_template_str)
structured_llm = model.with_structured_output(JobPosting)

def get_response(input):
    prompt = prompt_template.format(input=input)
    response = structured_llm.invoke(prompt)
    return response

input = """
Senior Frontend Software Engineer

Company: FinTech Analytics Group
Location: Hybrid — New York, NY
Salary: $150,000–$190,000 USD

We are seeking a Senior Frontend Software Engineer to join our growing engineering team.

Required qualifications:
- 5+ years of frontend engineering experience
- Strong experience with React, TypeScript, JavaScript, HTML, and CSS
- Experience working with REST APIs and CI/CD pipelines

Preferred qualifications:
- Experience with Node.js
- Experience with Docker and Kubernetes

Schedule: Full-time
"""

print(get_response(input))

