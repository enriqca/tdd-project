from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
import time
MAX_WAIT = 5

options = Options()
options.binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
options.set_preference("browser.download.folderList",2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir","/Data")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,application/vnd.ms-excel")
# browser = webdriver.Firefox(executable_path=r'C:\Users\RICKC\Desktop\S.I\sem2022-2\TST\tdd-project/geckodriver.exe', options=options)

class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        # Edith entra na home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # Ela nota que o input box está centralizado
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

        # Ela inicia uma nova lista e nota que o input
        # também está centralizado
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: testing')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )