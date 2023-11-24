import pdb

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url="http://manten.grupogamma.com/sim2/login.php"

driver.get(url)

title = driver.title

print(title)
#html_content = driver.page_source

#with open("salida.html", "w", encoding="utf-8") as file:
#    file.write(html_content)

pdb.set_trace()

driver.quit()