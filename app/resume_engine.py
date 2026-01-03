from docx import Document
from pathlib import Path

BASE_RESUME = "/app/templates/base_resume.docx"
OUTPUT_DIR = Path("/app/output")
OUTPUT_DIR.mkdir(exist_ok=True)

doc = Document(BASE_RESUME)

# Placeholder update (next step me dynamic hoga)
doc.add_paragraph("\n[Auto-updated for JD specific ATS optimization]")

output_file = OUTPUT_DIR / "resume_updated.docx"
doc.save(output_file)

print(f"Updated resume generated at {output_file}")

