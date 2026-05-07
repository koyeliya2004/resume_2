import json
from groq import Groq
from app.config import GROQ_API_KEY, GROQ_MODEL
from app.schemas.resume_schema import resume_json_schema

client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = """
You are an expert resume parser.
Extract resume information into the exact JSON schema provided.

Rules:
- Do not invent or guess missing information.
- If a field is missing from the resume, return empty string "" or empty array [].
- Normalize skill names where possible (e.g. "js" -> "JavaScript").
- Keep certifications separate from education.
- Extract ALL skills mentioned anywhere in the resume.
- Keep output strictly valid JSON matching the schema exactly.
"""


def extract_resume_sections(resume_text: str) -> dict:
    """
    Use Groq LLM to extract structured sections from raw resume text.
    Returns a dict with: overview, skills, experience, projects, education, certifications.
    """
    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"Extract structured data from this resume:\n\n{resume_text}"
            }
        ],
        response_format=resume_json_schema,
        temperature=0
    )

    content = response.choices[0].message.content
    return json.loads(content)
