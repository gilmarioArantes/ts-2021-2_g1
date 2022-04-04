from lib2to3.pgen2.driver import Driver
from unittest import result
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest


class TestPrecoNacional:

    @pytest.fixture()
    def driver_init(self):
        global driver
        driver = webdriver.Chrome(
            r"C:\\Users\\Victor\\Downloads\\chromedriver.exe")
        driver.fullscreen_window()
        time.sleep(3)
        yield
        driver.close()
        time.sleep(3)
        driver.quit()

    def test_browser(self, driver_init):
        driver.get('https://www2.correios.com.br/sistemas/precosPrazos/')
        time.sleep(2)
        assert driver.title == 'home'
        print(driver.title)

    def test_preco(self, driver_init):
        driver.get('https://www2.correios.com.br/sistemas/precosPrazos/')
        parentWindow = driver.current_window_handle
        origin_CEP = driver.find_element(by=By.NAME, value='cepOrigem')
        origin_CEP.send_keys('17031-607')
        destination_CEP = driver.find_element(by=By.NAME, value='cepDestino')
        destination_CEP.send_keys('18609701')
        product_dropdown = driver.find_element(by=By.NAME, value='servico')
        product = Select(product_dropdown)
        time.sleep(5)
        product.select_by_value('04510')
        time.sleep(2)
        button_product_selection = driver.find_element(
            by=By.XPATH, value='//*[@id="spanTipoEmbalagem"]/div/div[2]/div/div[1]/div/p/button')
        button_product_selection.click()
        time.sleep(2)
        weight_dropdown = driver.find_element(
            by=By.XPATH, value='//*[@id="spanServicoSelecionado"]/span[5]/label/select')
        weight = Select(weight_dropdown)
        weight.select_by_index(10)
        time.sleep(3)
        calculate_button = driver.find_element(by=By.NAME, value="Calcular")
        calculate_button.click()
        time.sleep(3)
        handles = driver.window_handles
        childWindow = handles[1]
        driver.switch_to.window(childWindow)
        table = driver.find_element(
            by=By.CLASS_NAME, value="comparaResult")
        body = table.find_element(
            by=By.XPATH, value="/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody")
        row = body.find_element(
            by=By.XPATH, value="/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table/tfoot")
        cells = row.find_element(
            by=By.XPATH, value="/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table/tfoot/tr/td").text
        print(cells)
        assert cells == "R$ 52,50"
