import pyttsx3
import PyPDF2


# =====================================================================
# Accessing PDF
# =====================================================================
book = open('OOP.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(book)

# Getting the number of pages in the PDF
pages = len(pdfReader.pages)
print(pages)

# =====================================================================
# Text to speach
# =====================================================================
speaker = pyttsx3.init()
speaker.say('Look child I can talk')
speaker.runAndWait()