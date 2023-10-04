from mouth.Speak import Speak
import PyPDF2

Book = open('bookname', 'rb')
pdfReader = PyPDF2.PdfFileReader(Book)
pages = pdfReader.numPages
print(pages)
Speak("Hello sir")