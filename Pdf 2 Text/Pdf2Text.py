# Program to convert PDF Fie to Text

import PyPDF2

pdffile = open('Demo.pdf','rb')
pdfreader = PyPDF2.PdfFileReader(pdffile)
x = pdfreader.numPages
page = pdfreader.getPage(x-1)
text = page.extractText()

file = open(r"Demo.txt","a")
file.writelines(text)
print('File Created!')

file.close()
