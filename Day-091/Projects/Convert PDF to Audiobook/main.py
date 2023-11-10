from PyPDF2 import PdfReader
from gtts import gTTS

filePath = "Python (Programming Language).pdf"
reader = PdfReader(filePath)

total_pages = len(reader.pages)
print(f"The document has {total_pages} pages.")

num_pages = int(input("Enter the number of pages to convert to MP3: "))
num_pages = min(num_pages, total_pages)
# print(num_pages)

full_text = ""
for i in range(num_pages):
    page = reader.pages[i]
    text = page.extract_text()
    if text:
        full_text += text + "\n"


language = "en"

tts = gTTS(text=full_text, lang=language, slow=False)
tts.save("test.mp3")
