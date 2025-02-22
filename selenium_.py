import sys
sys.path.append(r'C:\Users\dell\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages')
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('bookcover')
    print('found <%s> element with that class name!' %(elem.tag_name))
except:
    print("no elements with that name")

