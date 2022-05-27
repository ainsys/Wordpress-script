import time
import gspread

from selenium import webdriver
from selenium.webdriver.common.by import By

from settings import *
from consts import *


options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--incognito")

driver = webdriver.Chrome(
    executable_path="chromedriver",
    options=options
)


credentials = gspread.service_account(filename=FILE_NAME)

sheet = credentials.open_by_url(PATH_TABLE)

connectors_sheet = sheet.worksheet(WORKSHEET)

driver.get(path_admin_panel)

driver.find_element(By.XPATH, LOGIN_INPUT).send_keys(login)
driver.find_element(By.XPATH, PASSWORD_INPUT).send_keys(password)
driver.find_element(By.XPATH, BUTTON_INPUT).click()

for i in range(2,108):

    name = connectors_sheet.acell(f'A{i}').value
    category = connectors_sheet.acell(f'C{i}').value
    description = connectors_sheet.acell(f'D{i}').value
    logo = connectors_sheet.acell(f'F{i}').value

    print(name)

    time.sleep(3)

    driver.get(path_add_product)
    driver.implicitly_wait(80)

    driver.find_element(By.XPATH, BUTTON_ADD_PRODUCT).click()
    driver.implicitly_wait(80)

    driver.find_element(By.XPATH, FILE_NAME).send_keys(name)
    driver.find_element(By.XPATH, FIELD_DESCRIPRTION).send_keys(description)
    driver.implicitly_wait(80)

    driver.find_element(By.XPATH, BUTTON_TAB).click()
    driver.implicitly_wait(80)

    driver.find_element(By.XPATH, FIELD_CATEGORY).send_keys(category)
    driver.implicitly_wait(80)

    driver.find_element(By.XPATH, FIELD_LOGO).send_keys(logo)
    driver.implicitly_wait(80)

    driver.find_element(By.XPATH, BUTTON_PUBLIC).submit()
    time.sleep(3)
    driver.refresh()
    time.sleep(2)
    driver.find_element(By.XPATH, BUTTON_PUBLIC).click()
    time.sleep(4)

    print(FINAL_PHRASE)



