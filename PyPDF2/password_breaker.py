import PyPDF2

file = "all_files_encrypted.pdf"
dict = "dictionary.txt"

with open(file,"rb") as pdf_file:
    with open(dict,"r") as dict_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        for word in dict_file:
            if pdf_reader.decrypt(word.upper().strip()) == 1 or pdf_reader.decrypt(word.lower().strip()) == 1:
                print(f"Password: {word}")
                break
            else:
                continue
