from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
from Locators.element import Tag


class Advance_name_search(Tag):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)

    def click_page_topic(self, birth_butt, text_value):
        try:
            self.driver.execute_script("window.scrollBy(0,500)")
            page_top = self.wait.until(ec.element_to_be_clickable(self.dropdown_page_topic))
            page_top.click()
            place_birth = self.wait.until(ec.presence_of_element_located(self.button_place_birth))
            action = ActionChains(self.driver)
            action.move_to_element(place_birth).click().perform()
            search_topic_dd = self.wait.until(ec.presence_of_element_located(self.dropdown_search_topic))
            select = Select(search_topic_dd)
            select.select_by_value(birth_butt)
            page_text = self.wait.until(ec.presence_of_element_located(self.page_input_text))
            page_text.send_keys(text_value)
        except NoSuchElementException:
            print("NoSuchElement")
        except ElementClickInterceptedException:
            print("ElementClickIntercepted")
        except ElementNotInteractableException:
            print("ElementNotIntractable")

    def click_death_field(self, date_from, date_to):
        try:
            self.driver.execute_script("window.scrollBy(0,600)")
            death_date = self.wait.until(ec.element_to_be_clickable(self.dropdown_death_date))
            death_date.click()
            death_from = self.wait.until(ec.presence_of_element_located(self.date_from))
            death_from.send_keys(date_from)
            death_to = self.wait.until(ec.presence_of_element_located(self.date_to))
            death_to.send_keys(date_to)
        except NoSuchElementException:
            print("NoSuchElement")
        except ElementClickInterceptedException:
            print("ElementClickIntercepted")
        except ElementNotInteractableException:
            print("ElementNotIntractable")

    def click_gender_radio(self):
        try:
            self.driver.execute_script("window.scrollBy(0,600)")
            gender = self.wait.until(ec.element_to_be_clickable(self.dropdown_gender))
            gender.click()
            male = self.wait.until(ec.presence_of_element_located(self.male_button))
            action = ActionChains(self.driver)
            action.move_to_element(male).click().perform()
        except NoSuchElementException:
            print("NoSuchElement")
        except ElementClickInterceptedException:
            print("ElementClickIntercepted")
        except ElementNotInteractableException:
            print("ElementNotIntractable")

    def enter_credit_input(self, value_credit):
        try:
            self.driver.execute_script("window.scrollBy(0,700)")
            credit = self.wait.until(ec.element_to_be_clickable(self.dropdown_credit))
            credit.click()
            text_credit = self.wait.until(ec.presence_of_element_located(self.input_textfield_credit))
            text_credit.send_keys(value_credit)
        except NoSuchElementException:
            print("NoSuchElement")
        except ElementClickInterceptedException:
            print("ElementClickIntercepted")
        except ElementNotInteractableException:
            print("ElementNotIntractable")
