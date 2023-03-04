import codecs
import PyPDF2

def pdf_to_text(filename):
    # Open the PDF file in read binary mode
    with open(filename, 'rb') as pdf_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)

        # Extract the text from each page of the PDF file
        text = ''
        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            text += page.extract_text()#.replace('\n', '')  # Use extract_text() and remove newlines

        return text

if __name__ == '__main__':
    # Example usage
    filename = 'C:\Users\mason\Downloads\morphemeML.pdf'
    text = pdf_to_text(filename)
    with codecs.open('C:\Users\mason\Downloads\morphPdfText.txt', 'w', encoding='utf-8') as out_file:  # Open output file with codecs module
        out_file.write('hi' + text)  # Write text to output file without newlines
