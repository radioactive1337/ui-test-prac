import allure
import pytest

from pages.DynamicTablePage import DynamicTablePage
from data.data_for_dynamic_table import data1, data2, data3

URL = "https://testpages.eviltester.com/styled/tag/dynamic-table.html"


class Test:
    @pytest.mark.parametrize("table_data, caption, table_id", [data1, data2, data3])
    @allure.title("Dynamic table page test")
    def test_1(self, driver, table_data, caption, table_id):
        page = DynamicTablePage(driver=driver, url=URL)
        page.open()
        page.assert_page_title("Table HTML Tag - JavaScript Created")
        page.check_table_content(input_table_data=table_data, input_table_caption=caption, input_table_id=table_id)
