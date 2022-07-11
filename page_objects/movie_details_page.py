"""
MovieApp project by Ali Kholafaei
"""

from selenium.webdriver.common.by import By


class MovieDetailsPageLocators:
    # The XPATHs are only the placeholders
    page_title = (By.XPATH, "//h2[text()='Movie Dtails']")
    movie_title = (By.XPATH, "//h2[text()='movie_title']")
    add_favorite_star_button = (By.XPATH, "//button[text()='star']")
    add_favorite_confirm_modal = (By.XPATH, "//div[@class='TMDB']")


class MovieDetailsPage:
    """This class will handle all the interactions with the Movie Details page"""

    def __init__(self, driver):
        self.driver = driver

    # region getter
    def get_page_title(self):
        return self.driver.find_element(*MovieDetailsPageLocators.page_title).text

    def get_movie_title(self):
        return self.driver.find_element(*MovieDetailsPageLocators.movie_title).text

    def get_add_favorite_confirm_button(self):
        return self.driver.find_element(*MovieDetailsPageLocators.add_favorite_confirm_modal)

    def get_add_remove_favorite_movie_star_button(self):
        return self.driver.find_element(*MovieDetailsPageLocators.add_favorite_star_button)

    # region clicker
    def click_add_favorite_star_button(self):
        self.get_add_remove_favorite_movie_star_button().click()

    def click_add_favorite_confirm_button(self):
        self.get_add_favorite_confirm_button().click()

    # region boolean
    def is_add_favorite_confirm_modal_visible(self):
        return  self.driver.find_element(*MovieDetailsPageLocators.add_favorite_star_button).isDiplayed()

    def is_add_favorite_star_button_selected(self):
        return self.driver.find_element(*MovieDetailsPageLocators.add_favorite_star_button).isSelected()



"""
 element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
    (By.XPATH, "//*[@class='ng-binding ng-scope' and @id='tabla_evolucion']")))
    
    
    
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))
"""