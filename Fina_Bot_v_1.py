from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def login(driver, username, password):
    driver.find_element(By.ID, "Login").send_keys(username)
    driver.find_element(By.ID, "Password").send_keys(password)
    driver.find_element(By.NAME, "autenf").click()


def navigate_to_desired_page(driver):
    try:
        driver.find_element(By.CLASS_NAME, "sidebar-toggle.visible-sm.visible-xs.main-toggle").click()
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href*="TABLE_DOC_VENDOR"]')))
        driver.execute_script("arguments[0].scrollIntoView();", button)
        button.click()
    except:
        pass


def click_button(driver, button_xpath):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
    driver.find_element(By.XPATH, button_xpath).click()


def click_buttons(driver):
    button_xpaths = [
        '/html/body/div[2]/aside[1]/section/ul/li[2]/a/i',
        '//*[@id="rs-button"]',
        '/html/body/div[1]/div/div/form/div[2]/div[3]/ul/li/a',
        '/html/body/div[1]/div/div/div[2]/div/div/div[1]/ng-include/div/input[1]',
        '/html/body/div[1]/div/div/div[2]/div/div/div[1]/ng-include/div/div[1]/ul/li[2]/span/button[2]'
    ]

    for button_xpath in button_xpaths:
        click_button(driver, button_xpath)

    # Entering date
    driver.find_element(By.XPATH,
                        "/html/body/div[1]/div/div/div[2]/div/div/div[1]/ng-include/div/input[1]").send_keys(
        '01/01/2023')

    # Clicking button 6
    click_button(driver, '/html/body/div[1]/div/div/div[2]/button[2]/i')
    click_button(driver, '/html/body/div[1]/div/div/div[2]/button[2]/i')
def perform_actions(driver):
    while True:
        try:
            if driver.find_element(By.CLASS_NAME, 'skin-blue.sidebar-mini.modal-open.ngdialog-open'):
                click_button(driver, '/html/body')
                break
            elif driver.find_element(By.CLASS_NAME, 'skin-blue.sidebar-mini.modal-open'):
                break
        except:
            continue

    while True:
        try:
            click_button(driver, '/html/body')
            click_button(driver, '//*[@id="columntablejqxGrid2"]/div[14]/div/div[2]')
            break
        except:
            continue

    n = 0
    while True:
        if n == 20:
            raise ValueError
        try:
            for i in range(n):
                click_button(driver, '/html/body')
            click_button(driver, f'//*[@id="row{n}jqxGrid2"]')

            m = 0
            while True:

                try:
                    first_price = driver.find_element(By.XPATH,f'//*[@id="row{m}jqxGrid3"]/div[5]').text
                    secobd_price = driver.find_element(By.XPATH,f'//*[@id="row{m}jqxGrid3"]/div[6]').text

                    if float(first_price) == float(secobd_price):
                        pass
                    else:
                        document = driver.find_element(By.XPATH, f'//*[@id="row{n}jqxGrid2"]/div[5]').text

                        print(f"Check Document N: {document}")
                        n+=1
                        break
                    m+=1
                except:
                    pass

            while True:
                try:
                    pass
                    click_button(driver, '/html/body/div[1]/div/div/div[2]/button[1]/i')
                    click_button(driver, '/html/body/div[1]/div/div/div[2]/button[1]/i')
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn.btn-success.btn-save.btn-flat.ng-binding.ng-scope')))
                    driver.find_element(By.CLASS_NAME, 'btn.btn-success.btn-save.btn-flat.ng-binding.ng-scope').click()
                    driver.find_element(By.CLASS_NAME, 'btn.btn-success.btn-save.btn-flat.ng-binding.ng-scope').click()
                    return print("done")

                except:
                    n += 1
                    break
        except:
            continue


def main(username, password, url):

    options = webdriver.ChromeOptions()
    # options.add_argument("--window-size=800,600")
    # options.add_argument("--headless")

    with webdriver.Chrome(options=options) as driver:
        driver.get(url)

        login(driver, username, password)
        navigate_to_desired_page(driver)
        click_buttons(driver)
        perform_actions(driver)


if __name__ == "__main__":
    username = "vanotatulashvili@fina.ge"
    password = "fina"
    url = "https://web.fina24.ge/Main/?tag=TABLE_DOC_VENDOR"
    while True:
        try:
            main(username, password, url)
        except ValueError:
            print("All Done")
            break
        else:
            continue


