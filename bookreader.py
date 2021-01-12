import pyttsx3
import PyPDF2
book=open('sciencebook.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
print(pages)
engine = pyttsx3.init()
for num in range(8,pages):
    page=pdfReader.getPage(8)
    text=page.extractText()
    rate = engine.getProperty('rate')
    print (rate)
    engine.setProperty('rate', 110)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()