
import PyPDF2
import pyttsx3
import pdfplumber ## pdfplumber is built on pdfminer.six which is why it has the built-in-function extract_text()

PDF_FILE = "LordoftheFlies.pdf"

def pdf_to_text(pdf_file):
     # Open the PDF
    book = open(pdf_file, "rb")
    pdf_reader = PyPDF2.PdfReader(book)

    # Calculate the number of pages to loop through
    pages = len(pdf_reader.pages)
    # print(pages)

    text = ""
    for page in range(5, pages):
        page_content = pdf_reader.pages[page] # pdf_reader is the object that is accessing the pages attribute which is a list and the '[page]' is referring to the current iteration of the loop

        text += page_content.extract_text()

    return text

def text_to_speech(text):

    # Initialize speaker/audio player
    speaker = pyttsx3.init()

    speaker.say(text)
    speaker.runAndWait()

text = pdf_to_text(PDF_FILE)
text_to_speech(text)






