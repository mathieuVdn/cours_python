from PyPDF2 import PdfReader, PdfWriter

f = open("recap.pdf", "rb")
reader = PdfReader(f)

page0 = reader.pages[0]
text = page0.extract_text()

print(text)
f.close()
