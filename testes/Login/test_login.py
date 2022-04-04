from lib2to3.pgen2.driver import Driver
from unittest import result
from pandas import value_counts
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest
import json


class TestLogin:

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
        driver.get(
            'https://cas.correios.com.br/login?service=https%3A%2F%2Fmeucorreios.correios.com.br%2Fcore%2Fseguranca%2Fservice.php')
        time.sleep(2)
        assert driver.title == 'Login - CAS – Central Authentication Service'
        print(driver.title)

    def test_login_correto(self, driver_init):
        driver.get(
            'https://cas.correios.com.br/login?service=https%3A%2F%2Fmeucorreios.correios.com.br%2Fcore%2Fseguranca%2Fservice.php')
        with open('dados.json', 'r') as f:
            config = json.load(f)
        username = driver.find_element(
            by=By.XPATH, value="//*[@id='username']")
        password = driver.find_element(
            by=By.XPATH, value="//*[@id='password']")
        username.send_keys(config['user']['name'])
        password.send_keys(config['user']['password'])
        btn = driver.find_element(
            by=By.XPATH, value="//*[@id='fm1']/div[2]/button")
        time.sleep(4)
        btn.submit()
        time.sleep(4)
        result = driver.find_element(
            by=By.XPATH, value="//*[@id='menu']/a[4]").text
        assert result == "Abigail De Jesus Arruda"
        print(result)

    def test_login_errado(self, driver_init):
        driver.get(
            'https://cas.correios.com.br/login?service=https%3A%2F%2Fmeucorreios.correios.com.br%2Fcore%2Fseguranca%2Fservice.php')
        with open('dados.json', 'r') as f:
            config = json.load(f)
        username = driver.find_element(
            by=By.XPATH, value="//*[@id='username']")
        password = driver.find_element(
            by=By.XPATH, value="//*[@id='password']")
        username.send_keys('aaaaaaa')
        password.send_keys('aaaaaa')
        btn = driver.find_element(
            by=By.XPATH, value="//*[@id='fm1']/div[2]/button")
        time.sleep(4)
        btn.submit()
        result = driver.find_element(
            by=By.XPATH, value="//*[@id='alerta']/div[1]").text
        time.sleep(4)
        assert result == "Usuário ou senha inválidos."
        print(result)
