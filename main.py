
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from PIL import Image
from urllib import request
from PIL import Image
import pytesseract
import cv2
import numpy as np
from pytesseract import Output
import requests

browser = webdriver.Chrome(executable_path=r'C:/Users/pegas/OneDrive/Masaüstü/sreCaptcha/chromedriver.exe')
browser.get('https://ebelediye.elazig.bel.tr/webportal/index.php')
time.sleep(2)
url = r'https://ebelediye.elazig.bel.tr/webportal/lib/button.php?guvenlik=1'
resp = requests.get(url, stream=True).raw
image = np.asarray(bytearray(resp.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
custom_config = r'-l eng --oem 3 --psm 6' 
text = pytesseract.image_to_string(image,config=custom_config)
print(text)
my_username = 'GreatAxe'
my_pass ='zxcvbnm.zxcvbnm'
my_captcha = text
def query(num,password,captcha):
    try:
        input_1 = browser.find_element(By.NAME,'uyekod')
        input_2 = browser.find_element(By.NAME,'sifre')
        input_3 = browser.find_element(By.CLASS_NAME,'stan_input_ort1')
        input_1.send_keys(my_username)
        time.sleep(2)
        input_2.send_keys(my_pass)
        time.sleep(2)
        input_3.send_keys(my_captcha)
        time.sleep(2)
        input_3.send_keys(Keys.ENTER)
    except Exception as er:
        print(er)
        browser.quit()
query(my_username,my_pass, my_captcha)


