from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


# Generates a PDF report
def generate_report(attachment, title, paragrapgh):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles['h1'])
    paragrapgh = Paragraph(paragrapgh)
    report.build([report_title, paragrapgh])