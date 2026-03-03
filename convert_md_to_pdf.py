from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas

md_path = Path("GenAI_Course_Work/m25ai2010_assignment_2.md")
pdf_path = md_path.with_suffix(".pdf")

text = md_path.read_text(encoding="utf-8", errors="ignore")
lines = text.splitlines()

c = canvas.Canvas(str(pdf_path), pagesize=A4)
width, height = A4
left = 2 * cm
top = height - 2 * cm
line_height = 14
y = top

c.setFont("Helvetica", 10)
for raw_line in lines:
    line = raw_line.expandtabs(4)
    if not line:
        y -= line_height
    else:
        while len(line) > 110:
            chunk, line = line[:110], line[110:]
            c.drawString(left, y, chunk)
            y -= line_height
            if y < 2 * cm:
                c.showPage()
                c.setFont("Helvetica", 10)
                y = top
        c.drawString(left, y, line)
        y -= line_height

    if y < 2 * cm:
        c.showPage()
        c.setFont("Helvetica", 10)
        y = top

c.save()
print(f"Created: {pdf_path}")
