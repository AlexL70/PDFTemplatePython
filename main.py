from fpdf import FPDF 
import pandas as pd

df = pd.read_csv("topics.csv")


def draw_lines(pdf):
    for y in range(28, 280, 10):
        pdf.line(x1=10, y1=y, x2=200, y2=y)


def add_footer(pdf, mm):
    # add footer
    pdf.ln(mm)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 220)
    pdf.cell(w=0, h=8, txt=f"{row['Topic']}. Page {pdf.page_no()}.", align="R", ln=1, border=0)


pdf = FPDF(orientation="portrait", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
for index, row in df.iterrows():
    pdf.add_page()
    # add header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=24, txt=row["Topic"], align="L", ln=1, border=0)
    draw_lines(pdf)
    add_footer(pdf, 248)

    for i in range(1, row["Pages"]):
        pdf.add_page()
        draw_lines(pdf)
        add_footer(pdf, 272)

pdf.output(f"output.pdf")
