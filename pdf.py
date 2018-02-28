import PyPDF2

pdfFileObj = open('Sample.pdf' , 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
