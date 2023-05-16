from flask import Flask, render_template, request, send_file
from io import BytesIO
from PyPDF2 import PdfMerger

app = Flask(__name__)

@app.route('/dashboard/merge', methods = ['GET', 'POST'])
def home():
     if request.method== 'POST':
            pdf_files=request.files.getlist("pdf_files")
            merger = PdfMerger()

            for pdf in pdf_files:
                merger.append(pdf)
                # return jsonify("Congratulations! Your Document in PDF format merged successfully!")

            buffer= BytesIO()
            merger.write(buffer)
            buffer.seek(0)
            return send_file(buffer,as_attachment=True,download_name="Merged_report.pdf")
     return render_template("new.html")
        
if __name__ == '__main__':
	app.run(debug = True)