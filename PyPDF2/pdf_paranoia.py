import os
import PyPDF2
from PyPDF2.utils import PdfReadError


def encrypt_pdf(folder):
    for foldername,subfolders,filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(".pdf") :
                print(filename)
                with open(filename,"rb") as file:
                    with open(f"{os.path.splitext(filename)[0]}" + "_encrypted.pdf","wb") as encrypted_file:
                        pdf_reader = PyPDF2.PdfFileReader(file)
                        if not pdf_reader.isEncrypted:
                            pdf_writer = PyPDF2.PdfFileWriter()
                            for page_num in range(pdf_reader.numPages):
                                pdf_writer.addPage(pdf_reader.getPage(page_num))
                            pdf_writer.encrypt("abrading")
                            pdf_writer.write(encrypted_file)

def encryption_checker(folder):
    for foldername,subfolders,filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith ("_encrypted.pdf"):
                print(f"Opening {filename}")
                file = open(os.path.join(foldername,filename),"rb")
                pdf_reader = PyPDF2.PdfFileReader(file)
                if pdf_reader.isEncrypted:
                    print(f"File {filename} is encrypted")
                    try:
                        pdf_reader.decrypt("password")
                        pdf_reader.getPage(0)
                        print("File has been decrypted correctly")
                    except PyPDF2.utils.PdfReadError:
                        print("Password is incorrect...")

def encrypted_to_decrypted(folder,password):
    for foldername,subfolders,filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith ("_encrypted.pdf"):
                with open(filename,"rb") as file:
                    with open("decrypted_" + f"{filename}", "wb") as decrypted_file:
                        pdf_reader = PyPDF2.PdfFileReader(file)
                        try:
                            pdf_reader.decrypt(password)
                            pdf_writer = PyPDF2.PdfFileWriter()
                        except PyPDF2.utils.PdfReadError:
                            print("Password is incorrect...")
                            continue
                        for page_num in range(pdf_reader.numPages):
                            pdf_writer.addPage(pdf_reader.getPage(page_num))
                            pdf_writer.write(decrypted_file)



encrypt_pdf(r"C:\Users\RMZ\PycharmProjects\automate_boring_stuff")
# encryption_checker(r"C:\Users\RMZ\PycharmProjects\automate_boring_stuff")
# encrypted_to_decrypted(r"C:\Users\RMZ\PycharmProjects\automate_boring_stuff","password")