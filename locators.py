from selenium.webdriver.common.by import By


class GamesLocators:
    GAME_CARD = (By.XPATH, "//li[1]/div/div")
    ADDITIONAL_INFO = (By.XPATH, "//div[text()='Additional information']")
    TECH_INFO = (By.XPATH, "//div[text()='Minimum system requirements']")
    BACK_TM_BUTTON = (By.XPATH, "//span[text()='Back to Main']")
    QTY_INPUT = (By.XPATH, "(//input[@type='search'])[4]")
    LIST_GAMES = (By.XPATH, "//*[@id='root']/div/div[5]/div[2]/div/ul/li")
    PAGE_LIST_UP = (By.XPATH, "(//li[@title=2])[1]")
    PAGE_LIST_DOWN = (By.XPATH, "(//li[@title=3])[2]")
