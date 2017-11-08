# coding: utf-8
import unittest
import time
import datetime

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from seleniumUtil import SeleniumUtil

class GoogleTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #cls.driver = webdriver.Firefox()
        cls.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_case01(self):
        page = NewWindowPage(self, self.driver)
        page.open()
        page2 = page.popup()
        page2.open()
        page3 = page2.submit()
        page3.open()
        page3.close()

    def test_case02(self):
        page = InputPage(self, self.driver)
        page.open()
        page.link()
        page2 = page.submit()
        page2.check()
        page3 = page2.submit()
        page3.check()

class InputPage():
    def __init__(self, unit, driver):
        self.unit = unit
        self.driver = driver
        self.util = SeleniumUtil(unit, driver)

    def open(self):
        self.driver.get("http://example.selenium.jp/reserveApp_Renewal/")

    def link(self):
        # リンクをクリック
        item = self.driver.find_element_by_id("reserve_info")
        item = item.find_element_by_tag_name("a")
        item.click()

        # アラートにスイッチ
        alert = self.driver.switch_to_alert()
        
        # アラートがオープンするまで待機
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.alert_is_present())

        # アラートがオープンするまで待機
        #self.util.wait_func(lambda: alert.text, 10)

        # ボタン押下
        alert.accept()

    def submit(self):
        # 入力項目
        item = self.driver.find_element_by_id("datePick")
        item.clear()
        d = datetime.datetime.today()
        d = d + datetime.timedelta(days=1)
        dt = "{0:04d}/{1:02d}/{2:02d}".format(d.year, d.month, d.day)
        item.send_keys(dt)

        item = self.driver.find_element_by_id("reserve_term")
        select = Select(item)
        #options = select.options
        select.select_by_value("9")

        item = self.driver.find_element_by_id("breakfast_off")
        item.click()

        item = self.driver.find_element_by_id("guestname")
        item.clear()
        item.send_keys("YujiKonishi")

        self.driver.save_screenshot("/work/input_page.png")

        # 画面遷移
        item = self.driver.find_element_by_id("agree_and_goto_next")
        item.submit()

        return ConfPage(self.unit, self.driver)

class ConfPage():
    def __init__(self, unit, driver):
        self.unit = unit
        self.driver = driver
        self.util = SeleniumUtil(unit, driver)

    def check(self):
        # ウインドウオープン待ち＆タイトルチェック
        title = u"予約内容確認"
        WebDriverWait(self.driver, 10).until(EC.title_contains(title))
        self.unit.assertIn(title, self.driver.title)

        # gnameが生成されるまで待機
        #self.util.wait_func(
        #    lambda: self.driver.find_element_by_id("gname"),
        #    10)

        # gnameが生成されるまで待機
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(
            expected_conditions.presence_of_element_located((By.ID, "gname")))

        # gnameの値チェック
        item = self.driver.find_element_by_id("gname")
        self.unit.assertEqual(u"YujiKonishi", item.text)

    def submit(self):
        # 画面遷移
        item = self.driver.find_element_by_id("commit")
        item.submit()
        return DefPage(self.unit, self.driver)

class DefPage():
    def __init__(self, unit, driver):
        self.unit = unit
        self.driver = driver

    def check(self):
        title = u"予約完了"
        WebDriverWait(self.driver, 10).until(EC.title_contains(title))
        self.unit.assertIn(title, self.driver.title)

class NewWindowPage():
    def __init__(self, unit, driver):
        self.unit = unit
        self.driver = driver
        self.util = SeleniumUtil(unit, driver)

    def open(self):
        self.driver.get("https://web-designer.cman.jp/javascript_ref/window/open/")

    def popup(self):
        # 親のハンドルを取得
        handle = self.driver.current_window_handle

        # 入力項目
        item = self.driver.find_element_by_name("gurlTxt")
        item.clear()
        item.send_keys("http://example.selenium.jp/reserveApp_Renewal/")
        item = self.driver.find_element_by_id("gwinName1")
        item.click()
        item = self.driver.find_element_by_name("gwinNameTxt")
        item.send_keys("mywindow")

        # 子のウインドウをオープン
        item = self.driver.find_element_by_id("goSample")
        item = item.find_element_by_tag_name("input")
        item.click()

        # 子のウインドウにスイッチ
        self.driver.switch_to_window("mywindow")

        return PopupPage(self.unit, self.driver, handle)

class PopupPage():
    def __init__(self, unit, driver, handle):
        self.unit = unit
        self.driver = driver
        self.util = SeleniumUtil(unit, driver)
        self.handle = handle

    def open(self):
        # agree_and_goto_nextが生成されるまで待機
        self.util.wait_func(
            lambda: self.driver.find_element_by_id("agree_and_goto_next"),
            10)

    def submit(self):
        # 画面遷移
        item = self.driver.find_element_by_id("agree_and_goto_next")
        item.submit()

        return Popup2Page(self.unit, self.driver, self.handle)
   
class Popup2Page():
    def __init__(self, unit, driver, handle):
        self.unit = unit
        self.driver = driver
        self.util = SeleniumUtil(unit, driver)
        self.handle = handle

    def open(self):
        # ウインドウオープン待ち＆タイトルチェック
        title = u"予約エラー"
        WebDriverWait(self.driver, 10).until(EC.title_contains(title))
        self.unit.assertIn(title, self.driver.title)

    def close(self):
        # 子のウインドウをクローズ
        self.driver.close()
        # 親のウインドウにスイッチ
        self.driver.switch_to_window(self.handle)


if __name__ == '__main__':
    unittest.main(verbosity=2)
