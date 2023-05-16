from flask import Flask, jsonify, request
from PyPDF2 import PdfMerger

app = Flask(__name__)

@app.route('/dashboard/merge', methods = ['GET', 'POST'])
def home():
     pdfs = ['Redcliffe report 1.pdf', 'Redcliffe 2 .pdf', 'Redcliffe report 2.pdf']
     merger = PdfMerger()
     for pdf in pdfs:
            merger.append(pdf)
     merger.write("merged.pdf")
    #  data = {"data": "Your pdf our merged successfully"}
     return jsonify("Congratulations! Your Document in PDF format merged successfully, Enjoy Learnings!")
     merger.close()

if __name__ == '__main__':
	app.run(debug = True)
        
        