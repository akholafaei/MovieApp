"""
MovieApp project by Ali Kholafaei
"""

from selenium.webdriver.common.by import By

class FavoritePageLocators:
    # The XPATHs are only the placeholders
    page_title = (By.XPATH, "//h2[text()='Favorite']")
    added_movie_title = (By.XPATH, "//h2[text()='movie_title']")
    added_movie_link = (By.XPATH, "//a[contains(@href, 'movie name')]")

class FavoritesPage:
    """This class will handle all the interactions with the Favorite page"""

    def __init__(self, driver):
        self.driver = driver

    # region getter
    def get_page_title(self):
        # * is added to deserialize the tuple of the locator
        return self.driver.find_element(*FavoritePageLocators.page_title).text

    def get_added_movie_title(self):
        # * is added to deserialize the tuple of the locator
        return self.driver.find_element(*FavoritePageLocators.added_movie_title).text

    def get_added_movie_link(self):
        return self.driver.find_element(*FavoritePageLocators.added_movie_link)

    # region clicker
    def click_added_favorite_movie_link(self):
        self.get_added_movie_link().click()