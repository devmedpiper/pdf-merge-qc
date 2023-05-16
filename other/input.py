import os
import form
# fileitem = form['filename']
# # check if the file has been uploaded
# if fileitem.filename:
# 	# strip the leading path from the file name
# 	fn = os.path.basename(fileitem.filename)
	
# # open read and write the file into the server
# 	open(fn, 'wb').write(fileitem.file.read())
	
from pypdf import PdfMerger

pdfs = form['Redcliffe report 1.pdf', 'Redcliffe 2 .pdf', 'Redcliffe report 2.pdf']
if pdfs.filename:
	# strip the leading path from the file name
	fn = os.path.basename(pdfs.filename)	
        
merger = PdfMerger()
for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")
print("Your pdf merged successfully")
merger.close()
