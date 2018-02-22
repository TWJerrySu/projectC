from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from util.screenshot import screenshot
import time
import subprocess


class Catch(screenshot):
    def __init__(self):
        # put it in setUp
        self.save_path = 'C:/Users/Administrator/Desktop/stock_img'
        self.upload = ['node','C:/Users/Administrator/Desktop/stock_img/Porshche/upload.js']
        self.hts_path = 'C:/JihSun/HTS2/JSCOM.exe'
        self.password = "atk2395"
        self.driver = webdriver.Remote(command_executor='http://localhost:9999',
                                       desired_capabilities={'app': self.hts_path})  # put it in test method body
        self.driver.implicitly_wait(10)


    def login(self):
        self.driver.find_element_by_class_name('TEdit').find_element_by_name("").send_keys(self.password)
        self.driver.find_element_by_class_name('TEdit').submit()

    def open_taget_windows(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "TimMainFrm")))
        window = self.driver.find_element_by_class_name('TimMainFrm')
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "4500")))
        win = window.find_element_by_id("1001")
        win.send_keys("4000")

    def entry_stock_number(self):
        w = self.driver.find_element_by_class_name('TfrmSniperPro').find_element_by_name('TAB')
        q = w.find_element_by_class_name('TCodeForm').find_element_by_class_name('TCHARTINPUT')
        fc = q.find_element_by_class_name('TCodeEdit').find_element_by_class_name("TCdEdit")
        actions = ActionChains(self.driver)
        actions.move_to_element(fc).move_by_offset(20, 0).click().perform()
        stk_list = self.get_stock_number_list()
        for stk in stk_list:
            fc.clear()
            while fc.text != "":
                fc.clear()
            # fc.send_keys(Keys.CONTROL + 'a')
            # fc.send_keys(Keys.DELETE)
            fc.send_keys(stk)
            time.sleep(1)
            fc.click()
            time.sleep(1.5)
            self.take_screen_from_list(stk)

    def upload_files(self):
        process = subprocess.Popen(self.upload)
        process.communicate(input=None)

    def quit(self):
        self.driver.quit()
        self.driver.close()


if __name__ == "__main__":
    s = Catch()
    s.login()
    s.open_taget_windows()
    s.entry_stock_number()
    s.upload_files()
    s.quit()
