from selenium import webdriver
from pathlib import Path
import

#myPath = os.path.abspath(os.path.dirname(__file__))

myPath = Path(__file__).parent

print(myPath)

geckoPath = os.path.join(myPath,"..\geckodriver-v0.24.0-win64\geckodriver.exe")

webdriverObj = webdriver.Firefox(executable_path = geckoPath)

webdriverObj.get("http://www.google.com")

webdriverObj.quit()