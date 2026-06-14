import os
import json
import requests
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# Kapsam: Fotoğraflar ve Albümler üzerinde okuma/yazma izni
SCOPES = ['https://www.googleapis.com/auth/photoslibrary.appendonly']

def authenticate():
    creds = None
    # Daha önce yetkilendirme yaptıysak token.json dosyasından okuyoruz
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # Geçerli bir kimlik bilgisi yoksa giriş ekranını aç (Sadece ilk çalışmada olur)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
        creds = flow.run_local_server(port=0)
        # Web sitemizde kullanmak üzere token'ı kaydediyoruz
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def create_album(creds, album_name):
    url = 'https://photoslibrary.googleapis.com/v1/albums'
    headers = {
        'Authorization': f'Bearer {creds.token}',
        'Content-Type': 'application/json'
    }
    body = {
        "album": {
            "title": album_name
        }
    }
    
    response = requests.post(url, headers=headers, json=body)
    
    if response.status_code == 200:
        album_id = response.json().get('id')
        print("--------------------------------------------------")
        print(f"Albüm başarıyla oluşturuldu!\nAlbüm Adı: {album_name}")
        print(f"ALBÜM ID: {album_id}")
        print("--------------------------------------------------")
        print("Lütfen bu Album ID'yi kopyala, web sitemizin kodlarında bunu kullanacağız.")
        return album_id
    else:
        print(f"Hata oluştu: {response.text}")
        return None

if __name__ == '__main__':
    print("Google ile yetkilendirme yapılıyor...")
    credentials = authenticate()
    
    # Uygulamanın yetkisinde olacak albümü oluşturuyoruz
    create_album(credentials, "Nikah & Davet (Memory Vault)")
