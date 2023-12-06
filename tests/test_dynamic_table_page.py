import allure
import pytest

from pages.DynamicTablePage import DynamicTablePage
from data.data_for_dynamic_table import data1, data2, data3

URL = "https://testpages.eviltester.com/styled/tag/dynamic-table.html"


class Test:
    @pytest.mark.parametrize("tdata, caption, tid", [data1, data2, data3])
    @allure.title("Dynamic table page test")
    def test_1(self, driver, tdata, caption, tid):
        page = DynamicTablePage(driver=driver, url=URL)
        page.open()
        page.assert_page_title("Table HTML Tag - JavaScript Created")
        page.check_table_content(input_table_data=tdata, input_table_caption=caption, input_table_id=tid)
