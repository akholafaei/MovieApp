"""
MovieApp project by Ali Kholafaei
"""

import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    """ Setup and Tear down the driver"""
    path = "/Users/ali.kholafaei/Desktop/chromedriver"
    driver = webdriver.Chrome(executable_path=path)
    driver.implicitly_wait(10)
    driver.get('https://www.url_of_movie_app/')
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()