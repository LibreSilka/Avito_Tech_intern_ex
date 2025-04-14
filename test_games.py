import pytest
from games_page import GamesPage


@pytest.fixture(scope="module")
def games_page(driver):
    """Фикстура для страницы с играми"""
    return GamesPage(driver)


def test_open_game_card(games_page):
    """Тест открытия карточки игры"""
    games_page.open()
    games_page.open_game()


def test_qty_select(games_page):
    """Тест выбора кол-ва игр на странице"""
    games_page.open()
    assert games_page.qty_filter_game("20") == 20


def test_page_select(games_page):
    """Тест перехода по страницам"""
    games_page.open()
    games_page.page_game()
