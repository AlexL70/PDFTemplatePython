from fpdf import FPDF 

pdf = FPDF(orientation="portrait", unit="mm", format="A4")
pdf.add_page()
pdf.set_font(family="Times", style="B", size=12)
pdf.cell(w=0, h=12, txt="Hello there!", align="L", ln=1, border=0)
pdf.set_font(family="Times", size=10)
pdf.cell(w=0, h=12, txt="Hi there!", align="L", ln=1, border=0)
pdf.add_page()
pdf.output("output.pdf")