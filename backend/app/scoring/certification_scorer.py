from sqlalchemy.orm import Session
from app.database.models import CertificationDB


def score_certifications(extracted_certifications: list, db: Session) -> dict:
    """
    Compare extracted certifications with certification_db.
    Returns score 0-100 based on matched cert values.
    """
    if not extracted_certifications:
        return {"score": 0.0, "matched": []}

    matched = []
    total_score = 0.0
    all_certs = db.query(CertificationDB).all()

    for cert in extracted_certifications:
        cert_name = cert.get("name", "").lower()
        issuer = cert.get("issuer", "").lower()

        best_cert_score = 0.0
        best_cert_name = None

        for db_cert in all_certs:
            # Match by name similarity or issuer
            db_name = db_cert.cert_name.lower()
            db_issuer = db_cert.issuer.lower()

            name_match = any(word in db_name for word in cert_name.split() if len(word) > 3)
            issuer_match = db_issuer in issuer or issuer in db_issuer

            if name_match or issuer_match:
                if db_cert.score_value > best_cert_score:
                    best_cert_score = db_cert.score_value
                    best_cert_name = db_cert.cert_name

        if best_cert_name:
            matched.append(best_cert_name)
            total_score += best_cert_score

    # Normalize: max score from 3 top certs = 100
    max_possible = sum(sorted([c.score_value for c in all_certs], reverse=True)[:3])
    score = min((total_score / max_possible) * 100, 100.0) if max_possible > 0 else 0.0

    return {
        "score": round(score, 2),
        "matched": matched
    }
