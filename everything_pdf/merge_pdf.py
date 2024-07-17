# INSTALL PyPDF2
# we are going to merge two pdfs

from PyPDF2 import PdfMerger
import os

def merge_two():
    merger = PdfMerger()

    pdf_files = ['pdf_files/sample.pdf', 'pdf_files/Code-iris.pdf']

    for pdf_file in pdf_files:
        merger.append(pdf_file)

    merger.write('merged.pdf')
    merger.close()

# MERGING MANY FILES
def merge_many():
    merger = PdfMerger()

    path_to_files = r'pdf_files/'
    # OS.WALK METHOD GETS ALL THE FILES IN A GIVEN DIRECTORY

    for root, dirs, file_names in os.walk(path_to_files):

        for file_name in file_names:
            merger.append(path_to_files + file_name)

    merger.write('merge_multiple.pdf')
    merger.close()

# merge_many()
