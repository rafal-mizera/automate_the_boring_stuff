import PyPDF2

# pdf_file_obj = open("combinedminutes.pdf","rb")
# pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
# print(pdf_reader.numPages)
#
# page_obj = pdf_reader.getPage(0)
# print(page_obj.extractText())

# pdf_reader = PyPDF2.PdfFileReader(open("encrypted.pdf","rb"))
# print(pdf_reader.isEncrypted)
# # print(pdf_reader.getPage(0))
# print(pdf_reader.decrypt("rosebud"))
# print(pdf_reader.getPage(0))

# pdf_file = open("meetingminutes.pdf","rb")
# pdf_file2 = open("meetingminutes2.pdf","rb")
# pdf_reader = PyPDF2.PdfFileReader(pdf_file)
# print(pdf_reader.numPages)
# pdf_reader2 = PyPDF2.PdfFileReader(pdf_file2)
# print(pdf_reader2.numPages)
# pdf_writer = PyPDF2.PdfFileWriter()
#
# for page in range(pdf_reader.numPages):
#     page_obj = pdf_reader.getPage(page)
#     pdf_writer.addPage(page_obj)
#
# for page in range(pdf_reader2.numPages):
#     page_obj = pdf_reader2.getPage(page)
#     pdf_writer.addPage(page_obj)
#
# pdf_output_file = open("combinedminutes.pdf","wb")
# pdf_writer.write(pdf_output_file)
#
# pdf_output_file.close()
# pdf_file.close()
# pdf_file2.close()

# minutes_file = open("meetingminutes.pdf", "rb")
# pdf_reader = PyPDF2.PdfFileReader(minutes_file)
# page = pdf_reader.getPage(0)
# page.rotateClockwise(90)
#
# pdf_writer = PyPDF2.PdfFileWriter()
# pdf_writer.addPage(page)
# result_pdf_page = open("rotated_page.pdf", "wb")
# pdf_writer.write(result_pdf_page)
# minutes_file.close()
# result_pdf_page.close()

# minutes_file = open("meetingminutes.pdf", "rb")
# pdf_reader = PyPDF2.PdfFileReader(minutes_file)
# watermark_file = open("watermark.pdf", "rb")
# pdf_watermark_reader = PyPDF2.PdfFileReader(watermark_file)
# minutes_first_page = pdf_reader.getPage(0)
# minutes_first_page.mergePage(pdf_watermark_reader.getPage(0))
# pdf_writer = PyPDF2.PdfFileWriter()
# pdf_writer.addPage(minutes_first_page)
#
# for page_num in range(1,pdf_reader.numPages):
#     page_obj = pdf_reader.getPage(page_num)
#     pdf_writer.addPage(page_obj)
#
# result_file = open("watermarked.pdf","wb")
# pdf_writer.write(result_file)
# minutes_file.close()
# result_file.close()

minutes_file = open("meetingminutes.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(minutes_file)
pdf_writer = PyPDF2.PdfFileWriter()
for pageNum in range(pdf_reader.numPages):
    pdf_writer.addPage(pdf_reader.getPage(pageNum))

pdf_writer.encrypt("swordfish")
result_pdf = open("encrypted_minutes.pdf","wb")
pdf_writer.write(result_pdf)
result_pdf.close()