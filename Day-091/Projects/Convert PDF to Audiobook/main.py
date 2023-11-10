from PyPDF2 import PdfReader
from gtts import gTTS

filePath = "Python (Programming Language).pdf"
reader = PdfReader(filePath)

total_pages = len(reader.pages)
print(f"The document has {total_pages} pages.")

num_pages = int(input("Enter the number of pages to convert to MP3: "))
num_pages = min(num_pages, total_pages)

print()
choice = input(
    "\nChoose an Option:\n1. Create Single MP3 (1 for All Pages)\n2. Create Multiple MP3s (1 for Each Page)\n"
)

language = "en"

if choice == "1":
    full_text = ""
    for i in range(num_pages):
        page = reader.pages[i]
        text = page.extract_text()
        if text:
            full_text += text + "\n"

    tts = gTTS(text=full_text, lang=language, slow=False)
    tts.save("combined_audio.mp3")

elif choice == "2":
    for i in range(num_pages):
        page = reader.pages[i]
        text = page.extract_text()
        if text:
            tts = gTTS(text=text, lang=language, slow=False)
            tts.save(f"page_{i+1}.mp3")
else:
    print("Invalid choice. Please enter '1' or '2'.")
