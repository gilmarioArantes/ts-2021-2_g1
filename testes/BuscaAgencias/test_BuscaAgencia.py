from lib2to3.pgen2.driver import Driver
from unittest import result
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest


class TestBuscaAgencia:

    @pytest.fixture()
    def driver_init(self):
        global driver
        driver = webdriver.Chrome(r"chromedriver.exe")
        driver.fullscreen_window()
        time.sleep(3)
        yield
        driver.close()
        time.sleep(3)
        driver.quit()

    def test_browser(self, driver_init):
        driver.get('https://mais.correios.com.br/app/index.php')
        time.sleep(2)
        assert driver.title == 'Agências'
        print(driver.title)

    def test_buscaAgenciaProximidade(self, driver_init):
        driver.get('https://mais.correios.com.br/app/index.php')
        initial_button = driver.find_element_by_id('span-proximidade')
        initial_button.click()
        time.sleep(3)
        option_button = driver.find_element_by_id('meio')
        option_button.click()
        time.sleep(3)
        result = driver.find_element(
            by=By.XPATH, value="//*[@id='divsemresultado']/pre").text
        assert result == "Nenhuma agência encontrada."
        print(result)

    def test_buscaAgenciaLocalidade(self, driver_init):
        driver.get('https://mais.correios.com.br/app/index.php')
        initial_button = driver.find_element_by_id('span-localidade')
        initial_button.click()
        state_dropdown = driver.find_element(by=By.NAME, value='cmbEstado')
        state = Select(state_dropdown)
        state.select_by_index(9)
        city_dropdown = driver.find_element(
            by=By.XPATH, value='//*[@id="cmbMunicipio"]')
        city = Select(city_dropdown)
        time.sleep(5)
        city.select_by_index(10)
        div = driver.find_element(
            by=By.XPATH, value="//*[@id='lista_agencias']")
        time.sleep(3)
        table = div.find_element(
            by=By.XPATH, value="//*[@id='lista_agencias']/table")
        body = table.find_element(
            by=By.XPATH, value="//*[@id='lista_agencias']/table/tbody")
        tr = body.find_element(
            by=By.XPATH, value="//*[@id='base-00006926']")
        td = tr.find_element(
            by=By.XPATH, value="//*[@id='base-00006926']/td")
        table2 = td.find_element(
            by=By.XPATH, value='//*[@id="base-00006926"]/td/table')
        body2 = table2.find_element(by=By.XPATH, value="//*[@id='primeiro']")
        tr2 = body2.find_element(
            by=By.XPATH, value="//*[@id='primeiro']/tr[1]")
        td2 = tr2.find_element(
            by=By.XPATH, value="//*[@id='primeiro']/tr[1]/td[1]")
        search_result = td2.find_element(
            by=By.XPATH, value="//*[@id='primeiro']/tr[1]/td[1]/span[2]").text
        assert search_result == "AVENIDA GETULIO VARGAS, 75 A"
        print(search_result)
        time.sleep(5)
