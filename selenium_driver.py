from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

def get_driver(url):

    try:
        chrome_driver_location = r"D:\CS\Python\Automate Everything with Python\chromedriver-win64\chromedriver.exe"
        print_log(f"Using chrome driver at location: {chrome_driver_location}")
        service = Service(chrome_driver_location)
        
        print_log("Setting browser options")
        options = webdriver.ChromeOptions()
        options.add_argument("disable-infobars")
        options.add_argument("--headless")
        options.add_argument('--log-level=3')
        options.add_argument("start-maximized")
        options.add_argument("no-sandbox")
        options.add_argument("disable-dev-shm-usage")
        options.add_argument("disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        
        driver = webdriver.Chrome(options=options, service=service)
        print_log("Opening X.com")
        driver.get(url)
        return driver

    except Exception as e:
        print_log(f'{type(e).__name__}: {e}')
        print(f'{type(e).__name__}: {e}')