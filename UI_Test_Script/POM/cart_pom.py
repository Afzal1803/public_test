from playwright.sync_api import Page, Locator, expect, TimeoutError as PlaywrightTimeoutError

class GeneratedPage:
    """
    Page Object Model for the generated cart page.
    """

    def __init__(self, page: Page, timeout: int = 5000):
        """
        Initializes the GeneratedPage with XPath locators for interactable elements.

        :param page: Playwright Page object.
        :param timeout: Timeout for element interactions in milliseconds.
        """
        self._page = page
        self._timeout = timeout

        self._input_coupan_xpath = "//input[@id='coupan']"
        self._btn_apply_coupan_xpath = "//input[@type='submit' and @value='Apply Coupan']"
        self._btn_place_order_xpath = "//button[@id='address']"
        self._link_place_order_xpath = "//button[@id='address']/a"

    def _safe_click(self, xpath: str):
        """
        Safely clicks an element specified by its XPath.

        :param xpath: XPath string of the element to click.
        """
        locator = self._page.locator(f"xpath={xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)
        locator.click()

    def _safe_fill(self, xpath: str, text: str):
        """
        Safely fills an input field specified by its XPath.

        :param xpath: XPath string of the input element.
        :param text: Text to fill into the input.
        """
        locator = self._page.locator(f"xpath={xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)
        locator.clear()
        locator.fill(text)

    def _safe_check(self, xpath: str):
        """
        Safely checks a checkbox or radio button specified by its XPath.

        :param xpath: XPath string of the checkbox or radio element.
        """
        locator = self._page.locator(f"xpath={xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)
        if not locator.is_checked():
            locator.check()

    def _safe_select(self, xpath: str, value: str):
        """
        Safely selects an option in a select dropdown specified by its XPath.

        :param xpath: XPath string of the select element.
        :param value: Value attribute of the option to select.
        """
        locator = self._page.locator(f"xpath={xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)
        locator.select_option(value)

    def fill_coupan_code(self, code: str):
        """
        Fills the coupon code input field.

        :param code: Coupon code to enter.
        """
        self._safe_fill(self._input_coupan_xpath, code)

    def click_apply_coupan(self):
        """
        Clicks the 'Apply Coupan' button.
        """
        self._safe_click(self._btn_apply_coupan_xpath)

    def click_place_order_button(self):
        """
        Clicks the 'PLACE ORDER for the Products' button.
        """
        self._safe_click(self._btn_place_order_xpath)

    def click_place_order_link(self):
        """
        Clicks the link inside the 'PLACE ORDER for the Products' button.
        """
        self._safe_click(self._link_place_order_xpath)

    def validate_essential_elements(self):
        """
        Validates that all essential elements are visible on the page.
        """
        locator = self._page.locator(f"xpath={self._input_coupan_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)

        locator = self._page.locator(f"xpath={self._btn_apply_coupan_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)

        locator = self._page.locator(f"xpath={self._btn_place_order_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)