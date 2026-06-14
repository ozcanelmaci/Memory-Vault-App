# Anı Kasası (Memory Vault) 📸✨

Anı Kasası, özel davetlerde ve etkinliklerde misafirlerin çektikleri o en doğal anları (fotoğraf ve videoları) doğrudan ev sahibinin **Google Fotoğraflar (Google Photos)** albümüne yüklemelerini sağlayan, sunucusuz (serverless) bir bulut otomasyon platformudur.

Misafirleri uygulama indirme, üye olma veya şifre girme derdinden kurtarır. Sadece masadaki QR kodu okutup tarayıcı üzerinden doğrudan yükleme yapmalarını sağlar.

## 🚀 Öne Çıkan Özellikler

* **Kusursuz Kullanıcı Deneyimi:** Herhangi bir login duvarı yoktur. Tıkla ve yükle.
* **Çoklu Dosya Yükleme (Batch Upload):** Misafirler tek seferde 10-20 fotoğraf seçebilir. Sistem, sunucuyu yormamak için dosyaları asenkron sırayla yükler.
* **Gelişmiş Boyut Desteği (Resumable Upload):** Google Photos API'nin standart 50 MB sınırını aşmak için *Parçalı Yükleme Protokolü* entegre edilmiştir. Dosya başına **250 MB'a kadar** video yüklemeyi destekler.
* **Modern HTTP/2 Altyapısı:** Eşzamanlı asenkron veri transferleri için `Hypercorn` ASGI sunucusu kullanılmıştır.
* **Lüks ve Şık Arayüz:** Derin slate ve altın sarısı tonlarında modern, minimalist ve mobil öncelikli ön yüz tasarımı.

## 🛠 Teknoloji Yığını

* **Backend:** Python, Flask
* **Frontend:** HTML5, CSS3, Vanilla JavaScript (Asenkron Fetch API)
* **Sunucu:** Hypercorn (HTTP/2 Destekli ASGI)
* **Bulut Altyapısı:** Google Cloud Run, Google Photos Library API

---

## 💻 Kurulum ve Yerel Geliştirme

Projeyi kendi bilgisayarınızda kurmak ve Google Cloud bağlantısını sağlamak için aşağıdaki adımları sırasıyla izleyin.

### Adım 1: Gereksinimleri Yükleme
Öncelikle bilgisayarınızda Python yüklü olduğundan emin olun ve projenin gereksinimlerini kurun:

```bash
pip install -r requirements.txt
