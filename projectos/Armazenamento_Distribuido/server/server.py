from flask import Flask, request, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def list_files():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return files

def handle_upload():
    file = request.files['file']
    filename = file.filename
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    print(f'Arquivo {filename} enviado com sucesso e salvo em {file_path}!')
    return f'Arquivo {filename} enviado com sucesso!'

@app.route('/upload', methods=['POST'])
def upload_file():
    return handle_upload()

@app.route('/files', methods=['GET'])
def list_uploaded_files():
    files = list_files()
    return jsonify(files)

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if not os.path.isfile(file_path):
        return 'Arquivo não encontrado!', 404
    return send_file(file_path, as_attachment=True)

@app.errorhandler(404)
def page_not_found(error):
    print('Endpoint não encontrado.')
    return 'Endpoint não encontrado.', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
