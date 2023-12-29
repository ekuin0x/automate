from flask import Flask  
from selenium import webdriver

app = Flask(__name__)

@app.route("/")
def index() :
    browser = webdriver.Chrome()
    browser.get("https://www.google.com")
    return "Hello World !!"

if __name__ == '__main__' : 
    app.run(port=5000,debug=False)