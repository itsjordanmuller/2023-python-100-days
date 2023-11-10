from PyPDF2 import PdfReader


reader = PdfReader("Python (Programming Language).pdf")

page = reader.pages[0]

text = page.extract_text()
print(text)
