from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
import re


def generate_pdf(notes, filename="lecture_notes.pdf"):

    styles = getSampleStyleSheet()

    story = []

    lines = notes.split("\n")

    for line in lines:

        line = line.strip()

        if not line:
            story.append(Spacer(1, 8))
            continue

        # Headings
        if line.startswith("###"):
            text = line.replace("###", "").strip()
            story.append(Paragraph(f"<b>{text}</b>", styles["Heading3"]))

        elif line.startswith("##"):
            text = line.replace("##", "").strip()
            story.append(Paragraph(f"<b>{text}</b>", styles["Heading2"]))

        elif line.startswith("#"):
            text = line.replace("#", "").strip()
            story.append(Paragraph(f"<b>{text}</b>", styles["Heading1"]))

        # Bullet points
        elif line.startswith("*"):
            text = line.replace("*", "").strip()
            story.append(Paragraph(f"• {text}", styles["BodyText"]))

        # Bold text
        else:
            text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", line)
            story.append(Paragraph(text, styles["BodyText"]))

        story.append(Spacer(1, 4))

    doc = SimpleDocTemplate(filename, pagesize=letter)

    doc.build(story)

    return filename