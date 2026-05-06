````
# Job Posting Structured Extraction with LangChain + Pydantic

This project uses LangChain, OpenAI GPT models, and Pydantic to extract structured data from unstructured job postings.

The application takes a raw job description and converts it into a strongly typed `Pydantic` model for downstream processing, analytics, filtering, or storage.

---

# Features

- Structured extraction from raw job postings
- Uses OpenAI GPT models through LangChain
- Strong schema validation with Pydantic
- Typed nested salary model
- Optional and required field handling
- Easy to extend for recruiting or job-search applications

---

# Technologies Used

- Python
- LangChain
- OpenAI
- Pydantic
- GPT-4o-mini

---

# Project Structure

```bash
.
├── main.py
├── README.md
└── requirements.txt
```

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/job-posting-parser.git

cd job-posting-parser
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Mac/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Requirements

Example `requirements.txt`

```txt
langchain
langchain-openai
pydantic
python-dotenv
```

---

# Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

Then uncomment:

```python
from dotenv import load_dotenv
load_dotenv()
```

---

# How It Works

## 1. Define Prompt Template

The prompt instructs the LLM to extract structured job posting information.

```python
prompt_template = PromptTemplate.from_template(prompt_template_str)
```

---

## 2. Define Structured Output Schema

The schema is defined using Pydantic models.

```python
class JobPosting(BaseModel):
```

This ensures:
- validation
- typing
- structured JSON output

---

## 3. Bind Structured Output to the LLM

```python
structured_llm = model.with_structured_output(JobPosting)
```

LangChain automatically validates the model response against the schema.

---

## 4. Invoke the Model

```python
response = structured_llm.invoke(prompt)
```

---

# Example Input

```python
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
```

---

# Example Output

```python
JobPosting(
    job_id='generated-id',
    job_title='Senior Frontend Software Engineer',
    required_skills=[
        'React',
        'TypeScript',
        'JavaScript',
        'HTML',
        'CSS',
        'REST APIs',
        'CI/CD'
    ],
    posting_timestamp=datetime(...),
    location='New York, NY',
    preferred_skills=[
        'Node.js',
        'Docker',
        'Kubernetes'
    ],
    years_of_experience='5+',
    company_name='FinTech Analytics Group',
    salary_range=SalaryRange(
        min=150000,
        max=190000,
        currency='USD'
    ),
    work_schedule='Full-time',
    location_type='hybrid'
)
```

---

# Supported Fields

| Field | Required |
|---|---|
| job_id | Yes |
| job_title | Yes |
| required_skills | Yes |
| posting_timestamp | Yes |
| location | Yes |
| preferred_skills | No |
| years_of_experience | No |
| company_name | Yes |
| salary_range | Yes |
| coding_languages | No |
| work_environment | No |
| work_schedule | No |
| tools_to_use_on_job | No |
| location_type | No |
| remote_locations | No |
| office_locations | No |

---

# Running the Application

```bash
python main.py
```

---

# Future Improvements

- Add FastAPI endpoint
- Store extracted jobs in a database
- Add vector search for job matching
- Add resume-to-job matching
- Add salary normalization
- Add batch processing pipeline
- Export results to CSV or JSON

---
````
