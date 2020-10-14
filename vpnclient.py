import requests
import pytesseract
import cv2
try:
    from PIL import Image
except ImportError:
    import Image



url = 'https://www.vpnbook.com/password.php'
r = requests.get(url, allow_redirects=True)

open('password.png', 'wb').write(r.content)


path = "password.png"
path2 = "password2.png"
crop_img2 = cv2.imread(str(path))
img_scaled = cv2.resize(crop_img2, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
cv2.imwrite(str(path2), img_scaled)
crop_img2 = Image.open(path2)


text = pytesseract.image_to_string(Image.open(path2))
print(text)