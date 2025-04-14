from base_page import BasePage
from locators import GamesLocators
from selenium.webdriver.common.keys import Keys


class GamesPage(BasePage):
    """Страница с играми"""

    BASE_URL = "https://makarovartem.github.io/frontend-avito-tech-test-assignment/"

    def open(self):
        super().open(self.BASE_URL)

    def open_game(self):
        """Открытие карточки игры"""
        self.wait_for_element(GamesLocators.GAME_CARD)
        self.click(GamesLocators.GAME_CARD)
        self.wait_for_element(GamesLocators.ADDITIONAL_INFO)
        self.wait_for_element(GamesLocators.TECH_INFO)
        self.click(GamesLocators.BACK_TM_BUTTON)

    def qty_filter_game(self, qty):
        """Фильтрация по кол-ву на странице игр"""
        self.wait_for_element(GamesLocators.QTY_INPUT)
        self.send_keys(GamesLocators.QTY_INPUT, qty + Keys.ENTER)
        count = len(self.find_element('xpath', GamesLocators.LIST_GAMES[1]))
        return count

    def page_game(self):
        """Проверка пагинации"""
        self.wait_for_element(GamesLocators.PAGE_LIST_UP)
        self.click(GamesLocators.PAGE_LIST_UP)
        element = self.get_attr('xpath', GamesLocators.PAGE_LIST_UP[1])
        assert "ant-pagination-item-active" in element
        self.wait_for_element(GamesLocators.PAGE_LIST_DOWN)
        self.click(GamesLocators.PAGE_LIST_DOWN)
        element = self.get_attr('xpath', GamesLocators.PAGE_LIST_DOWN[1])
        assert "ant-pagination-item-active" in element
