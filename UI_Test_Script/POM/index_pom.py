from playwright.sync_api import Page, Locator, expect, TimeoutError as PlaywrightTimeoutError

class GeneratedPage:
    """
    Page Object Model for the Styleup page.
    Encapsulates element XPaths, safe interaction helpers, and action methods.
    """

    def __init__(self, page: Page, timeout: int = 5000):
        """
        Initializes the GeneratedPage with the Playwright Page object and optional timeout.
        """
        self._page = page
        self._timeout = timeout

        # Element XPaths
        self._input_search_bar_xpath = "//input[@id='search-bar']"
        self._btn_invite_now_xpath = "//button[normalize-space()='Invite Now >']"
        self._btn_invite_superhero_xpath = "//button[normalize-space()='Invite superhero >']"
        self._btn_crauser1_prev_xpath = "//button[@class='prev']"
        self._btn_crauser1_next_xpath = "//button[@class='next']"
        self._btn_crauser2_prev_xpath = "//button[@class='prev1']"
        self._btn_crauser2_next_xpath = "//button[@class='next1']"
        self._link_contact_us_xpath = "//a[normalize-space()='Contact Us']"
        self._link_blog_xpath = "//a[normalize-space()='Blog']"
        self._link_about_us_xpath = "//a[normalize-space()='About Us']"
        self._link_terms_of_use_xpath = "//a[normalize-space()='Terms of use']"

    def _safe_click(self, xpath: str):
        """
        Safely clicks an element specified by its XPath.
        """
        locator = self._page.locator(f"xpath={xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)
        locator.click()

    def _safe_fill(self, xpath: str, text: str):
        """
        Safely fills an input or textarea specified by its XPath.
        """
        locator = self._page.locator(f"xpath={xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)
        locator.clear()
        locator.fill(text)

    def _safe_check(self, xpath: str):
        """
        Safely checks a checkbox or radio button specified by its XPath.
        """
        locator = self._page.locator(f"xpath={xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)
        if not locator.is_checked():
            locator.check()

    def _safe_select(self, xpath: str, value: str):
        """
        Safely selects an option in a select element specified by its XPath.
        """
        locator = self._page.locator(f"xpath={xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)
        locator.select_option(value)

    def fill_search_bar(self, text: str):
        """
        Fills the search bar input with the provided text.
        """
        self._safe_fill(self._input_search_bar_xpath, text)

    def click_invite_now_button(self):
        """
        Clicks the 'Invite Now >' button.
        """
        self._safe_click(self._btn_invite_now_xpath)

    def click_invite_superhero_button(self):
        """
        Clicks the 'Invite superhero >' button.
        """
        self._safe_click(self._btn_invite_superhero_xpath)

    def click_crauser1_prev_button(self):
        """
        Clicks the previous button on the first carousel.
        """
        self._safe_click(self._btn_crauser1_prev_xpath)

    def click_crauser1_next_button(self):
        """
        Clicks the next button on the first carousel.
        """
        self._safe_click(self._btn_crauser1_next_xpath)

    def click_crauser2_prev_button(self):
        """
        Clicks the previous button on the second carousel.
        """
        self._safe_click(self._btn_crauser2_prev_xpath)

    def click_crauser2_next_button(self):
        """
        Clicks the next button on the second carousel.
        """
        self._safe_click(self._btn_crauser2_next_xpath)

    def click_contact_us_link(self):
        """
        Clicks the 'Contact Us' link in the footer.
        """
        self._safe_click(self._link_contact_us_xpath)

    def click_blog_link(self):
        """
        Clicks the 'Blog' link in the footer.
        """
        self._safe_click(self._link_blog_xpath)

    def click_about_us_link(self):
        """
        Clicks the 'About Us' link in the footer.
        """
        self._safe_click(self._link_about_us_xpath)

    def click_terms_of_use_link(self):
        """
        Clicks the 'Terms of use' link in the footer.
        """
        self._safe_click(self._link_terms_of_use_xpath)

    def validate_essential_elements(self):
        """
        Validates that all essential elements are visible on the page.
        """
        locator = self._page.locator(f"xpath={self._input_search_bar_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)

        locator = self._page.locator(f"xpath={self._btn_invite_now_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)

        locator = self._page.locator(f"xpath={self._btn_invite_superhero_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)

        locator = self._page.locator(f"xpath={self._btn_crauser1_prev_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)

        locator = self._page.locator(f"xpath={self._btn_crauser1_next_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)

        locator = self._page.locator(f"xpath={self._btn_crauser2_prev_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)

        locator = self._page.locator(f"xpath={self._btn_crauser2_next_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)

        locator = self._page.locator(f"xpath={self._link_contact_us_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)

        locator = self._page.locator(f"xpath={self._link_blog_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)

        locator = self._page.locator(f"xpath={self._link_about_us_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)

        locator = self._page.locator(f"xpath={self._link_terms_of_use_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)