"""
MovieApp project by Ali Kholafaei
"""

import random

from page_objects.nav_bar import NavBar
from page_objects.popular_page import PopularPage
from page_objects.movie_details_page import MovieDetailsPage
from page_objects.favorite_page import FavoritesPage
from utilities.base_class import BaseClass

class TestAddFavoriteMovie(BaseClass):
    """
    This class contains tests for adding a favorite movie app
    """
    def test_add_favorite_movie(self):
        """
        1- Verify user in on the popular page with correct title
        2- Verify user is on the Movie Details page
        3- Verify add favorite confirm modal is visible
        4- verify the star button is selected
        5- verify user is on Favorite page with expected title
        6- Verify the actual added movie has the same title of the expected added movie
        """
        popular_page = PopularPage(self.driver)
        # Test 1- verify user in on the page with correct title
        popular_page_title = popular_page.get_page_title()
        assert popular_page_title == "Popular", "Expected the page name be 'Popular' but its {0}".format(popular_page_title)

        # Get all movies links on popular page
        movies_list = popular_page.get_all_videos_links()
        # Get a random movie link from the list
        random_movie_link = random.choice(movies_list)
        # Click on the random movies link
        random_movie_link.click()

        movie_details_page = MovieDetailsPage(self.driver)
        # Test 2- verify user is on the Movie Details page
        movie_details_page_title = movie_details_page.get_page_title()
        assert movie_details_page_title == "Movie Details", "Expected the page name be 'Movie Details' but its {0}".format(movie_details_page_title)

        # Take the movies name
        expected_added_movie_title = movie_details_page.get_movie_title()
        # Click add/remove favorite movie star button
        movie_details_page.click_add_favorite_star_button()
        # Test 3- verify add favorite confirm modal is visible
        assert movie_details_page.is_add_favorite_confirm_modal_visible()

        # Click on conform/ok button on confirm modal
        movie_details_page.click_add_favorite_confirm_button()
        # Test 4- verify the star button is selected
        assert movie_details_page.is_add_favorite_star_button_selected()

        favorites_page = FavoritesPage(self.driver)
        # Test 5- verify user is on Favorite page with expected title
        favorites_movie_page_title = favorites_page.get_page_title()
        assert favorites_movie_page_title == "Favorites", "Expected the page name be 'Favorites' but its {0}".format(favorites_movie_page_title)

        nav_bar = NavBar(self.driver)
        # Click Favorite tab on Nav Bar
        nav_bar.click_favorite_tab_on_nav_bar()

        # Click the added favorite movie on favorite page
        favorites_page.click_added_favorite_movie_link()
        actual_added_movie_title = favorites_page.get_added_movie_title()
        # Test 6- Verify the actual added movie has the same title of the expected added movie
        assert actual_added_movie_title == expected_added_movie_title, "Expected added movie title be {0}, but its {1}".format(expected_added_movie_title, actual_added_movie_title)

