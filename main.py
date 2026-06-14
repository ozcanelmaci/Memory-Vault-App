from google.auth.transport.requests import Request as GoogleAuthRequest
from flask import Flask, request, jsonify, render_template
import requests
from google.oauth2.credentials import Credentials
import os

app = Flask(__name__)

ALBUM_ID = "album id değerinizi buraya vereceksiniz!" #album id değerini buraya yazıyoruz.
TOKEN_FILE = "token.json"

def get_credentials():
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, ['https://www.googleapis.com/auth/photoslibrary.appendonly'])
    
    # Token süresi dolmuşsa, arka planda otomatik olarak yenile
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(GoogleAuthRequest())
        
    return creds

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Dosya bulunamadı'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Dosya seçilmedi'}), 400

    try:
        creds = get_credentials()
        
        # Dosya boyutunu hesapla
        file.seek(0, os.SEEK_END)
        file_size = file.tell()
        file.seek(0)
        
        # 1. AŞAMA: Resumable Upload (Parçalı Yükleme) Oturumu Başlat
        start_headers = {
            'Authorization': f'Bearer {creds.token}',
            'X-Goog-Upload-Command': 'start',
            'X-Goog-Upload-Content-Type': file.content_type,
            'X-Goog-Upload-Protocol': 'resumable',
            'X-Goog-Upload-Raw-Size': str(file_size)
        }
        start_res = requests.post('https://photoslibrary.googleapis.com/v1/uploads', headers=start_headers)
        upload_url = start_res.headers.get('X-Goog-Upload-URL')

        if not upload_url:
            return jsonify({'error': 'Google API oturumu başlatılamadı.'}), 500

        # 2. AŞAMA: Dosya baytlarını aktar
        upload_headers = {
            'Authorization': f'Bearer {creds.token}',
            'X-Goog-Upload-Command': 'upload, finalize',
            'X-Goog-Upload-Offset': '0'
        }
        upload_response = requests.post(upload_url, headers=upload_headers, data=file.read())
        upload_token = upload_response.text

        # 3. AŞAMA: Yüklenen dosyayı albüme kaydet
        batch_create_url = 'https://photoslibrary.googleapis.com/v1/mediaItems:batchCreate'
        batch_headers = {
            'Authorization': f'Bearer {creds.token}',
            'Content-type': 'application/json',
        }
        batch_body = {
            "albumId": ALBUM_ID,
            "newMediaItems": [
                {
                    "description": "Misafir Yüklemesi - Memory Vault",
                    "simpleMediaItem": {
                        "uploadToken": upload_token
                    }
                }
            ]
        }
        
        res = requests.post(batch_create_url, headers=batch_headers, json=batch_body)
        
        if res.status_code == 200:
            return jsonify({'success': True, 'message': 'Anı başarıyla kasaya eklendi!'})
        else:
            return jsonify({'error': 'Fotoğraf albüme eklenemedi.'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)