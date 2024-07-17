import fitz  # PyMuPDF
from docx import Document


def pdf_to_docx(pdf_file, docx_file):
    # Open the PDF file
    pdf_document = fitz.open(pdf_file)

    # Create a new Document object for DOCX
    docx_document = Document()

    # Loop through each page of the PDF
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)

        # Extract text from the page
        text = page.get_text()

        # Add text to the DOCX document
        docx_document.add_paragraph(text)

    # Save the DOCX file
    docx_document.save(docx_file)

    # Close the PDF document
    pdf_document.close()


if __name__ == "__main__":
    pdf_file = 'pdf_files/Stages.pdf'  # Replace with your PDF file path
    docx_file = 'stage.docx'  # Replace with desired output DOCX file path
    pdf_to_docx(pdf_file, docx_file)
