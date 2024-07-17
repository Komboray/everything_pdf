# INSTALLATION
# pip install PyPDF2

from PyPDF2 import PdfReader

pdf_file_name = 'pdf_files/sample.pdf'

with open(pdf_file_name, 'rb') as pdf_file:
    pdf_reader = PdfReader(pdf_file)

    # Use len(pdf_reader.pages) to get the number of pages
    page_nums = len(pdf_reader.pages)

    for page_num in range(page_nums):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        print(text)