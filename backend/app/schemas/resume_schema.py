resume_json_schema = {
    "type": "json_schema",
    "json_schema": {
        "name": "resume_extraction",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "overview": {
                    "type": "string",
                    "description": "Brief professional summary or objective from the resume"
                },
                "skills": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "All technical and soft skills mentioned"
                },
                "experience": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "job_title": {"type": "string"},
                            "company": {"type": "string"},
                            "duration": {"type": "string"},
                            "description": {"type": "string"}
                        },
                        "required": ["job_title", "company", "duration", "description"],
                        "additionalProperties": False
                    }
                },
                "projects": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "project_name": {"type": "string"},
                            "technologies": {
                                "type": "array",
                                "items": {"type": "string"}
                            },
                            "description": {"type": "string"}
                        },
                        "required": ["project_name", "technologies", "description"],
                        "additionalProperties": False
                    }
                },
                "education": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "degree": {"type": "string"},
                            "institution": {"type": "string"},
                            "year": {"type": "string"},
                            "score": {"type": "string"}
                        },
                        "required": ["degree", "institution", "year", "score"],
                        "additionalProperties": False
                    }
                },
                "certifications": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "issuer": {"type": "string"},
                            "year": {"type": "string"}
                        },
                        "required": ["name", "issuer", "year"],
                        "additionalProperties": False
                    }
                }
            },
            "required": [
                "overview",
                "skills",
                "experience",
                "projects",
                "education",
                "certifications"
            ],
            "additionalProperties": False
        }
    }
}
