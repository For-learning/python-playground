from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time

options = ChromeOptions()
driver = Chrome(ChromeDriverManager().install(), options=options)

driver.execute_cdp_cmd("Network.enable", {})
driver.execute_cdp_cmd("Network.setBlockedURLs", {"urls": ("*.png", "*.jpg", "*.jpeg")})

driver.get("https://www.makemytrip.com/")

time.sleep(10)
driver.quit()

if __name__ == '__main__':
    pass
