# Program to create PDF file from Text

from fpdf import FPDF

pdf=FPDF()
pdf.add_page()
pdf.set_font("Arial",size=18)
pdf.cell(200,10,txt="Hello World!", ln=1,align="C")
pdf.cell(200,10,txt="This is also Demo.pdf!", ln=2,align="L")
pdf.cell(200,10,txt="Jatin", ln=2,align="R")

pdf.output("Demo.pdf")
