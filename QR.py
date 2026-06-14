import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer

# QR kod tasarım ayarları
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H, # Yüksek hata düzeltme (üzerine logo eklenebilir)
    box_size=20,
    border=4,
)

qr.add_data('Canlı deploy linkiniz buraya gelecek') #canlı linkiniz buraya gelecek!
qr.make(fit=True)

# TASARIM DOKUNUŞU:
# fill_color="#fbbf24" -> Sitedeki o şık Altın Sarısı rengi.
# Yuvarlatılmış köşeler (RoundedModuleDrawer) ile daha yumuşak bir görünüm.
img = qr.make_image(image_factory=StyledPilImage, 
                    module_drawer=RoundedModuleDrawer(),
                    fill_color="#fbbf24", 
                    back_color="white")
img.save("Ani_Kasasi_Masa_Kodu.png")