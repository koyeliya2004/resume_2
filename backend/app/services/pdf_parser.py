import fitz


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract all text from a PDF file using PyMuPDF.
    Returns combined text from all pages.
    """
    doc = fitz.open(pdf_path)
    all_text = []

    for page_num, page in enumerate(doc):
        text = page.get_text("text")
        if text.strip():
            all_text.append(f"--- Page {page_num + 1} ---\n{text.strip()}")

    doc.close()

    if not all_text:
        return ""

    return "\n\n".join(all_text)
