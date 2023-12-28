from methods import Advance_name_search
from Data.value import Source
import pytest

class Test_Imdb(Source):

    @pytest.mark.usefixtures("setup_teardown")
    def test_imdb_page(self):
        data = Advance_name_search(self.driver)
        data.click_page_topic(self.DD_value_birthplace, self.page_text_value)
        data.click_death_field(self.date_from_value, self.date_to_value)
        data.click_gender_radio()
        data.enter_credit_input(self.value_credit)
