from playwright.sync_api import Page, expect, TimeoutError as PlaywrightTimeoutError

class GeneratedPage:
    """
    Page Object Model for the United Techno Chat page.
    Encapsulates element XPaths and safe interaction methods.
    """

    def __init__(self, page: Page, timeout: int = 5000):
        """
        Initializes the GeneratedPage with the given Playwright Page and timeout.
        """
        self._page = page
        self._timeout = timeout

        # Element XPaths
        self._input_email_xpath = "//input[@id='userEmail']"
        self._input_phone_xpath = "//input[@id='userNumber']"
        self._input_company_xpath = "//input[@id='userCompany']"
        self._btn_submit_xpath = "//button[@id='detailsSubmit']"
        self._input_chat_xpath = "//input[@id='chat-input']"
        self._btn_send_xpath = "//i[@id='send-btn']"
        self._btn_end_chat_xpath = "//button[@id='end-chat-btn']"

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

    def fill_email_field(self, email: str):
        """
        Fills the email address input field.
        """
        self._safe_fill(self._input_email_xpath, email)

    def fill_phone_field(self, phone: str):
        """
        Fills the phone number input field.
        """
        self._safe_fill(self._input_phone_xpath, phone)

    def fill_company_field(self, company: str):
        """
        Fills the organization name input field.
        """
        self._safe_fill(self._input_company_xpath, company)

    def click_submit_button(self):
        """
        Clicks the Submit button.
        """
        self._safe_click(self._btn_submit_xpath)

    def fill_chat_input(self, message: str):
        """
        Fills the chat input field with a message.
        """
        self._safe_fill(self._input_chat_xpath, message)

    def click_send_button(self):
        """
        Clicks the Send button in the chat input section.
        """
        self._safe_click(self._btn_send_xpath)

    def click_end_chat_button(self):
        """
        Clicks the End Chat button.
        """
        self._safe_click(self._btn_end_chat_xpath)

    def validate_essential_elements(self):
        """
        Validates that all essential elements are visible on the page.
        """
        locator = self._page.locator(f"xpath={self._input_email_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)

        locator = self._page.locator(f"xpath={self._input_phone_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)

        locator = self._page.locator(f"xpath={self._input_company_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)

        locator = self._page.locator(f"xpath={self._btn_submit_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)

        locator = self._page.locator(f"xpath={self._input_chat_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)

        locator = self._page.locator(f"xpath={self._btn_send_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)

        locator = self._page.locator(f"xpath={self._btn_end_chat_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)