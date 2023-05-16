from pypdf import PdfMerger

pdfs = ['Redcliffe report 1.pdf', 'Redcliffe 2 .pdf', 'Redcliffe report 2.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")
print("Your pdf merged successfully")
merger.close()