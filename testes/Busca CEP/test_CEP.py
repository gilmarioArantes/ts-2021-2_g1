from email import header
from lib2to3.pgen2.driver import Driver
from unittest import result
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest


class TestCEP:

    @pytest.fixture()
    def driver_init(self):
        global driver
        driver = webdriver.Chrome(
            r"")
        driver.fullscreen_window()
        time.sleep(3)
        yield
        driver.close()
        time.sleep(3)
        driver.quit()

    def test_browser(self, driver_init):
        driver.get('https://www.correios.com.br/')
        time.sleep(2)
        assert driver.title == 'Correios — Correios, o maior operador logístico do Brasil.'
        print(driver.title)

    def test_cep(self, driver_init):
        driver.get('https://www.correios.com.br/')
        parentWindow = driver.current_window_handle
        search_box = driver.find_element(by=By.NAME, value='relaxation')
        search_box.send_keys('17031-607')
        time.sleep(4)
        search_box.submit()
        handles = driver.window_handles
        childWindow = handles[1]
        driver.switch_to.window(childWindow)
        table = driver.find_element(
            by=By.ID, value="resultado-DNEC")
        body = table.find_element(
            by=By.XPATH, value="//*[@id='resultado-DNEC']/tbody")
        row = body.find_element(
            by=By.XPATH, value="//*[@id='resultado-DNEC']/tbody/tr")
        cells = row.find_element(
            by=By.XPATH, value="//*[@id='resultado-DNEC']/tbody/tr/td[1]").text
        assert cells == "Rua Um"
        print(cells)
        time.sleep(3)
