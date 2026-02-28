from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

def create_pdf(data):

    filepath = "Scriptoria_PreProduction.pdf"
    doc = SimpleDocTemplate(filepath)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("SCRIPTORIA PRE-PRODUCTION PLAN", styles["Title"]))
    elements.append(Spacer(1, 0.5 * inch))

    sections = [
        ("Screenplay", data["screenplay"]),
        ("Characters", data["characters"]),
        ("Sound Design", data["sound"]),
        ("Cinematography", data["cinematography"]),
        ("Storyboard Concepts", data["storyboard"]),
        ("Budget Estimation", data["budget"]),
    ]

    for title, content in sections:
        elements.append(Paragraph(title, styles["Heading2"]))
        elements.append(Spacer(1, 0.2 * inch))
        elements.append(Paragraph(content.replace("\n", "<br/>"), styles["Normal"]))
        elements.append(Spacer(1, 0.5 * inch))

    doc.build(elements)
    return filepath