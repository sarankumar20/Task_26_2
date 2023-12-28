
from selenium.webdriver.common.by import By
class Tag:
    dropdown_page_topic = (By.ID, 'pageTopicsAccordion')
    button_place_birth = (By.XPATH, '//span[text()="Place of birth"]')
    dropdown_search_topic = (By.ID, 'within-topic-dropdown-id')
    page_input_text = (By.NAME, 'within-topic-input')
    dropdown_death_date = (By.ID, 'deathDateAccordion')
    date_from = (By.NAME, 'death-date-start-input')
    date_to = (By.NAME, 'death-date-end-input')
    dropdown_gender = (By.ID, 'genderIdentityAccordion')
    male_button = (By.XPATH, '//span[text()="Male"]')
    dropdown_credit = (By.ID, 'filmographyAccordion')
    input_textfield_credit = (By.XPATH, '//div[@id="accordion-item-filmographyAccordion"]/div/div/div/div[1]/input')
