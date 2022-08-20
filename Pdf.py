import PyPDF2
import  os
from PyPDF2 import  PdfReader,PdfMerger,PdfWriter


#Note that if you use 'r' you might encounter some binary mode errors
# Rather use 'rb'(Read Binary)

def pdf():
    with open('Test.pdf','rb') as file:#
        read_file = PyPDF2.PdfFileReader(file)
        read_file.numPages  #get number of pages
        page = read_file.getPage((0))
        page.rotateClockwise(90)  #returns page properties as object..
                                         # the object is saved in memory
        writer = PyPDF2.PdfWriter()
        writer.addPage(page)
        with open('rotated.pdf','wb') as rotated_file:  #open & write file in binary
            writer.write(rotated_file)


def extractTextFromPdf():
    reader = PdfReader("Test.pdf")
    page = reader.pages[0]
    print(page.extract_text())

def pdfMerger():
    merger = PdfMerger()
    if os.path.exists('pdfs'):
        for pdf in os.listdir('pdfs'):
            merger.append('pdfs/'+ pdf)

        merger.write("merged-pdf.pdf")
        merger.close()

def encryptPdf():
    reader = PdfReader("merged-pdf.pdf")
    writer = PdfWriter()
    # Add all pages to the writer
    for page in reader.pages:
        writer.add_page(page)
    writer.encrypt("12345")
    # Save the new PDF to a file
    with open("encrypted-pdf.pdf", "wb") as f:
        writer.write(f)

def decryptPdf():
    reader = PdfReader("encrypted-pdf.pdf")
    writer = PdfWriter()

    if reader.is_encrypted:
        reader.decrypt("12345")

    # Add all pages to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Save the new PDF to a file
    with open("decrypted-pdf.pdf", "wb") as f:
        writer.write(f)

def pdfCompressor(file):
    reader = PdfReader(file)
    writer = PdfWriter()

    for page in reader.pages:
        page.compress_content_streams()  # This is CPU intensive!
        writer.add_page(page)

    with open("out.pdf", "wb") as f:
        writer.write(f)
#pdf()
#extractTextFromPdf()
# pdfMerger()
#encryptPdf()
# decryptPdf()
pdfCompressor("Test.pdf")