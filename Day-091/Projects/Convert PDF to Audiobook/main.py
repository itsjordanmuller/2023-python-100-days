from PyPDF2 import PdfReader
from gtts import gTTS

filePath = "Python (Programming Language).pdf"
reader = PdfReader(filePath)

page = reader.pages[0]
text = page.extract_text()
# print(text)

total_pages = len(reader.pages)
print(f"The document has {total_pages} pages.")

num_pages = int(input("Enter the number of pages to convert to MP3: "))
num_pages = min(num_pages, total_pages)
# print(num_pages)

language = "en"

textToSpeech = gTTS(text=text, lang=language, slow=False)
textToSpeech.save("test.mp3")
