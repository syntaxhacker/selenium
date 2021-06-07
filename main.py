from optparse import OptionParser
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from dotenv import dotenv_values

config = dotenv_values(".env")
print(config)
# import undetected_chromedriver.v2 as uc
# driver = uc.Chrome()


CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/home/rohit/Downloads/selenium/chromedriver'
# WINDOW_SIZE = "600,400"
WINDOW_SIZE = "1920,1080"


chrome_options = webdriver.ChromeOptions()
# chrome_options = Options()
# chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-web-security')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument(
    "user-agent=User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")
# chrome_options.add_extension("./extension_2_9_4_0.crx")
chrome_options.binary_location = CHROME_PATH
driver = webdriver.Chrome(options=chrome_options)

# url = 'https://www.python.org'
# driver.get(url)
# print(driver.title)

# search_bar = driver.find_element_by_name("q")


# search_bar.clear()
# search_bar.send_keys("getting started with python")
# search_bar.send_keys(Keys.RETURN)

# print(driver.current_url)
# print(driver.window_handles)


def make_screenshot(url, output='./test.png'):
    if not url.startswith('http'):
        raise Exception('URLs need to start with "http"')

    driver.get(url)
    driver.switch_to.window(driver.window_handles[0])
    driver.save_screenshot(output)
    driver.close()


def gmailSignIn():
    try:
        driver.get('https://mail.google.com/mail/u/0/#inbox')
        driver.implicitly_wait(15)

        loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
        loginBox.send_keys(config['GMAIL_EMAIL'])

        nextButton = driver.find_elements_by_xpath(
            '//*[@id ="identifierNext"]')
        nextButton[0].click()

        passWordBox = driver.find_element_by_xpath(
            '//*[@id ="password"]/div[1]/div / div[1]/input')
        passWordBox.send_keys(config['GMAIL_PASSWORD'])
        nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
        nextButton[0].click()
        time.sleep(20)
    except TimeoutException as e:
        print("Wait Timed out")
        print(e)
    driver.close()


if __name__ == '__main__':
    gmailSignIn()
    # make_screenshot(
    # 'https://www.rapidtables.com/tools/notepad.html')
    # make_screenshot(
    #     'https://www.detectadblock.com/')
    # usage = "usage: %prog [options] <url> <output>"
    # parser = OptionParser(usage=usage)

    # (options, args) = parser.parse_args()

    # if len(args) < 2:
    #     parser.error("please specify a URL and an output")


# class ChromeSearch(unittest.TestCase):
#     def setUp(self):
#         self.driver = driver

#     def test_search_in_python_org(self):
#         driver = self.driver
#         driver.get("https://www.python.org")
#         self.assertIn("Python", driver.title)
#         elem = driver.find_element_by_name("q")
#         elem.send_keys("getting started with python")
#         elem.send_keys(Keys.RETURN)
#         assert "https://www.python.org/search/?q=getting+started+with+python&submit=" == driver.current_url

#     def tearDown(self):
#         self.driver.close()


# if __name__ == "__main__":
#     unittest.main()
