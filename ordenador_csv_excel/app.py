import os
from flask import Flask, request, render_template, send_from_directory
import pandas as pd
from datetime import datetime

#Enrique@KikeDesktop MINGW64 ~/Documents/REPOSITORIO DE PRUEBA/REPOSITORIO-DE-PRUEBAS/ordenador_csv_excel (main)     
#$ source venv/Scripts/activate


#python app.py


app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html', excel_file=None)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file and file.filename.endswith('.csv'):
        filename = datetime.now().strftime('%Y%m%d%H%M%S') + '.csv'
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        # Leer CSV con pandas y generar Excel bonito
        df = pd.read_csv(filepath)
        df = df.sort_values(by=df.columns[0])  # Ordenar por primera columna

        excel_filename = filename.replace('.csv', '.xlsx')
        excel_path = os.path.join(OUTPUT_FOLDER, excel_filename)

        # Estilo bonito con pandas y xlsxwriter
        with pd.ExcelWriter(excel_path, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Datos Ordenados')
            workbook = writer.book
            worksheet = writer.sheets['Datos Ordenados']
            format1 = workbook.add_format({'text_wrap': True, 'align': 'center', 'valign': 'vcenter', 'border': 1})
            worksheet.set_column(0, len(df.columns)-1, 20, format1)

        return render_template('index.html', excel_file=excel_filename)
    return 'Archivo inválido', 400

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(OUTPUT_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
