import PyPDF2

pdf_file = open('example.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)
num_pages = len(pdf_reader.pages)

for page in range(num_pages):
    page_obj = pdf_reader.pages[page]
    text = page_obj.extract_text()
    print(text)

pdf_file.close()

// "api_key": "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"