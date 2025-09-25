import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDemoQA:
    @pytest.mark.usefixtures("setup_browser")
    def test_textbox(self, setup_browser):
        driver = setup_browser
        driver.get("https://demoqa.com/")
        pytest.skip()
        expected_title = "DEMOQA"
        assert expected_title == driver.title

    @pytest.mark.skip(reason= "Code has not been deployed")
    def test_blaze(self, setup_browser):
        driver = setup_browser
        driver.get("https://www.demoblaze.com/")
        expected_title = "STORE"
        assert expected_title == driver.title


    @pytest.mark.skipif()
    def test_blaze_store(self, setup_browser):
        driver = setup_browser
        driver.get("https://www.demoblaze.com/")


