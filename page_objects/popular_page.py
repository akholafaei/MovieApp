"""
MovieApp project by Ali Kholafaei
"""

from selenium.webdriver.common.by import By


class PopularPageLocators:
    # The XPATHs are only the placeholders
    page_title = (By.XPATH, "//h2[text()='Popular']")
    all_movies_links = (By.XPATH, "//a[@href]")

class PopularPage:
    """This class will handle all the interactions with the Popular page"""
    def __init__(self, driver):
        self.driver = driver

    # region getter
    def get_page_title(self):
        # * is added to deserialize the tuple of the locator
        return self.driver.find_element(*PopularPageLocators.page_title).text

    def get_all_videos_links(self):
        return self.driver.find_elements(*PopularPageLocators.all_movies_links)














"""
try:
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.ID, 'objGrafPosiInv')))
        except Exception as ex:
            raise Exception('Nao foi possivel logar no CEI. Possivelmente usuario/senha errada ou indisponibilidade do site')
"""



