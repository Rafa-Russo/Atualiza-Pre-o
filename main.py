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

def banner():
    print("""______     _            _   _           _       _       
| ___ \   (_)          | | | |         | |     | |      
| |_/ / __ _  ___ ___  | | | |_ __   __| | __ _| |_ ___ 
|  __/ '__| |/ __/ _ \ | | | | '_ \ / _` |/ _` | __/ _ \ 
| |  | |  | | (_|  __/ | |_| | |_) | (_| | (_| | ||  __/
\_|  |_|  |_|\___\___|  \___/| .__/ \__,_|\__,_|\__\___|
                             | |                        
                             |_|                        """)
def menu():
    print("1. List of monitored products.")
    print("2. Add product.")
    print("3. Remove product.")
    
    print("0. Exit.")
def menu1():
    with open("list_products.txt", encoding="utf-8") as list_products:
        for num, line in enumerate(list_products, 1):
            print(str(num)+". "+ line)

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

exit = False
while not exit == True:
    banner()
    menu()
    ch = input()
    if ch == "1":
        menu1()
    elif ch == "2":
        new_product = input("Please, enter the location of the file incluiding the file itself: ")
    elif ch == "3":
        #for linha in "list_products.txt":
            #print(str(linha+1)+ ". " + list_products.readline())
        del_product = input("Which of the products should be deleted?")
