from fpdf import FPDF 
import pandas as pd

df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="portrait", unit="mm", format="A4")
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=24, txt=row["Topic"], align="L", ln=1, border=0)
    pdf.line(x1=10, y1=28, x2=200, y2=28)
    for i in range(1, row["Pages"]):
        pdf.add_page()

pdf.output(f"output.pdf")
