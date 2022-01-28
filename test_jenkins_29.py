from selenium import webdriver
from selenium.webdriver.common.by import By


def test_jenkins_plugin(browser):
    browser.get('https://plugins.jenkins.io/shiningpanda')
    title_element = browser.find_element(By.XPATH, '//h1[@class="title"]')
    assert title_element.text == 'ShiningPanda'
