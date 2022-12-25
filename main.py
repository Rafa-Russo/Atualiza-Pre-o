from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from win10toast import ToastNotifier
import datetime


toast = ToastNotifier()
price = 0
name = ""


chrome_options = Options()
chrome_options.add_argument("--headless")


def get_info(URL,price_tag,name_tag):
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(URL)
    driver.implicitly_wait(1)
    price_element = driver.find_element(By.CLASS_NAME,price_tag)
    price = price_element.text

    name_element = driver.find_element(By.CLASS_NAME,name_tag)
    name = name_element.text
    driver.close()
    return price,name

def notification():
    toast.show_toast(
        name,
        "The price for this product today is: " + price,
        duration = 10,
        icon_path=None,
        threaded = True
    )

def write_data():
    date = str(datetime.date.today())
    data = open(name+".txt", "a")
    data.write(date+","+price+"\n")
    data.close()


