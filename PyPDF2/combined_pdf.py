import os
import PyPDF2


pdf_files = []

for file in os.listdir("."):
    if file.endswith(".pdf"):
        pdf_files.append(file)

pdf_files.sort(key=str.lower)
pdf_writer = PyPDF2.PdfFileWriter()

for pdf_file in pdf_files:
    print ( f"Opening {pdf_file}" )
    pdf_file_obj = open ( pdf_file , 'rb' )
    pdf_reader = PyPDF2.PdfFileReader ( pdf_file_obj )
    if pdf_reader.isEncrypted:
        continue
    else:
        first_page = pdf_reader.getPage ( 0 )
        pdf_writer.addPage ( first_page )
        for page_num in range ( 1 , pdf_reader.numPages ):
            pdf_writer.addPage ( pdf_reader.getPage ( page_num ) )

new_file = open("all_files.pdf","wb")
pdf_writer.write(new_file)
new_file.close()
