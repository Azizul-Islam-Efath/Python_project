


#NB: jei pdf gulo merge korte chai ogulo merger.py er same lopcation a thakte hobe


from PyPDF2 import PdfMerger   # Importing pdfmerger from pre installed PyPdf2

ALLPDF = ["Data Types.pdf","Time.pdf"]  # Storing the pdfs in a variable

Merger= PdfMerger()   # storing the PdfMerger() method in a variable

for NewPDF in ALLPDF:   # creating an array
    Merger.append(NewPDF)  # executing the append function to merge the pdfs

Merger.write("NEW PDF.pdf")  # storing the merged pdf in a renamed pdf
Merger.close()  # closing the merger


