from flask import Flask  
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

@app.route("/")
def index() :
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get("https://www.google.com")
    return "Hello World !!"

if __name__ == '__main__' : 
    app.run(port=5000,debug=False)