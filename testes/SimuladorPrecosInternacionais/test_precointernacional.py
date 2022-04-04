from lib2to3.pgen2.driver import Driver
from select import select
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pytest


class TestPrecoInternacional:

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
        driver.get(
            'https://efi.correios.com.br/app/simulaPrecoPrazoInternacional/index.php')
        time.sleep(2)
        assert driver.title == 'Pré-Postagem Internacional'
        print(driver.title)

    def test_precointercional(self, driver_init):
        driver.get(
            'https://efi.correios.com.br/app/simulaPrecoPrazoInternacional/index.php')
        product_type = driver.find_element(
            by=By.XPATH, value='//*[@id="conteudo"]')
        product_t = Select(product_type)
        product_t.select_by_value('M')
        time.sleep(2)
        Cep = driver.find_element(
            by=By.XPATH, value='//*[@id="codigoPostalSimulacao"]')
        time.sleep(2)
        Cep.send_keys('75388-322')
        time.sleep(2)
        destiny_country = driver.find_element(
            by=By.XPATH, value='//*[@id="siglaPaisDestinatario"]')
        destiny = Select(destiny_country)
        destiny.select_by_value('DE')
        time.sleep(2)
        destiny_city = driver.find_element(
            by=By.XPATH, value='//*[@id="nomeCidadeDestinatario"]').send_keys('BERLIN')
        time.sleep(2)
        box_type = driver.find_element(
            by=By.XPATH, value='//*[@id="tipoEmbalagem"]')
        box = Select(box_type)
        box.select_by_index(0)
        time.sleep(2)
        length = driver.find_element(
            by=By.XPATH, value='//*[@id="comprimentoObjeto"]').send_keys('1000')
        time.sleep(2)
        width = driver.find_element(
            by=By.XPATH, value='//*[@id="larguraObjeto"]').send_keys('1000')
        time.sleep(2)
        height = driver.find_element(
            by=By.XPATH, value='//*[@id="alturaObjeto"]').send_keys('1000')
        time.sleep(2)
        weight = driver.find_element(
            by=By.XPATH, value='//*[@id="pesoObjeto"]').send_keys('1000')
        time.sleep(2)
        calculate_button = driver.find_element(
            by=By.ID, value="simulaPrecoPrazo")
        calculate_button.click()
        time.sleep(5)
        table = driver.find_element(
            by=By.XPATH, value="//*[@id='tbServicos']")
        body = table.find_element(
            by=By.XPATH, value="//*[@id='tbServicos']/tbody")
        row = body.find_element(
            by=By.XPATH, value="//*[@id='tbServicos']/tbody/tr[1]")
        cells = row.find_element(
            by=By.XPATH, value='//*[@id="tbServicos"]/tbody/tr[1]/td[3]').text
        assert cells == "278,30"
        print(cells)
        time.sleep(5)
