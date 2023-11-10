from PyPDF2 import PdfReader
from gtts import gTTS

reader = PdfReader("Python (Programming Language).pdf")

page = reader.pages[0]
text = page.extract_text()
print(text)

language = "en"

textToSpeech = gTTS(text=text, lang=language, slow=False)
textToSpeech.save("1.mp3")
