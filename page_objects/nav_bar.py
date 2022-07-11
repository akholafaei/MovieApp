"""
MovieApp project by Ali Kholafaei
"""

from selenium.webdriver.common.by import By

class NavBarLocators:
    # The XPATHs are only the placeholders
    popular_tab = (By.XPATH, "//button[text()='Popular']")
    favorite_tab = (By.XPATH, "//button[text()='Favorite']")

class NavBar:
    """This class will handle all the interactions with the Nav Bar"""

    def __init__(self, driver):
        self.driver = driver

    # region clicker
    def click_popular_tab_on_nav_bar(self):
        self.driver.find_element(*NavBarLocators.popular_tab).click()

    def click_favorite_tab_on_nav_bar(self):
        self.driver.find_element(*NavBarLocators.favorite_tab).click()