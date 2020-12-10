from selenium import webdriver
import allure


@allure.title('Результат поиска больше 10')
@allure.severity(severity_level='BLOCKER')
def test_yandex_search():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    with allure.step('Открываем страницу поиска'):
        driver.get('https://ya.ru')

    with allure.step('Ищем market.yandex.ru'):
        search_input = driver.find_element_by_css_selector('[name="text"]')
        search_button = driver.find_element_by_css_selector('[type="submit"]')
        search_input.send_keys('market.yandex.ru')
        search_button.click()
        search_results = driver.find_elements_by_css_selector('[class="serp-item"]')

    with allure.step('Ожидаем что количество результатов теста будет больше 10'):
        assert len(search_results) >= 10, 'Количество результатов поиска меньше 10'

    with allure.step('Переходим по ссылке второго результата'):
        link = search_results[1].find_element_by_css_selector('[class="organic__url-text"]')
        link.click()

    driver.switch_to.window(driver.window_handles[1])
    with allure.step('Проверяем корректность title страницы'):
        assert driver.title == 'Яндекс.Маркет — выбор и покупка товаров из проверенных интернет-магазинов'

