# Generated Playwright Tests for blog
from playwright.sync_api import sync_playwright, expect, TimeoutError as PlaywrightTimeoutError
from blog_pom import GeneratedPage
import json
import re
import time
import os

urls = {}
from Utility import Utility


# Test Case 1 - TC-0001
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
# Global URLs dictionary (update with actual URLs as needed)
urls: dict[str, str] = {
    "home": os.environ.get("STYLEUP_HOME_URL", "https://styleup.example.com/")
}
def test_logo_click_returns_user_to_home_page() -> None:
    """
    TC-0001: Logo Click Returns User to Home Page
    Verifies that clicking the logo in the navigation bar consistently returns the user to the home page from any section.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        test_result: str = "FAILED"
        test_details: str = ""
        home_url: str = Utility.validate_and_convert_data(urls.get("home"), str)
        home_title: str = ""
        try:
            # --- Console and Dialog Handling ---
            page.on("console", Utility.log_console_message)
            page.on("dialog", lambda dialog: dialog.accept())
            # --- Given: Land on the main page of the website ---
            Utility.log_test_step("Navigating to the main page.")
            navigation_success: bool = Utility.navigate_to_page(page, home_url, timeout=15000)
            if not navigation_success:
                raise Exception("Navigation to home page failed.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            Utility.log_element_state("Search Bar", page.locator(f"xpath={generated_page._input_search_bar_xpath}"), timeout=15000)
            # Accept cookies/pop-ups if present (assuming a standard button, update selector as needed)
            cookie_accepted: bool = Utility.safe_wait_and_interact(
                page,
                "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'accept')]",
                action="click",
                timeout=5000,
                retries=2
            )
            # --- Then: The main page with the logo, navigation categories, and images is displayed ---
            Utility.log_test_step("Validating essential elements on the main page.")
            Utility.retry_assertion(
                lambda: generated_page.validate_essential_elements(),
                retries=3,
                delay=2000
            )
            # --- When: Navigate to a different section by clicking on any category ---
            # For demonstration, let's assume MEN category is available with a known XPath
            men_category_xpath: str = "//nav//a[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'men')]"
            Utility.log_test_step("Navigating to the MEN category section.")
            category_clicked: bool = Utility.safe_wait_and_interact(
                page,
                men_category_xpath,
                action="click",
                timeout=15000,
                retries=3
            )
            if not category_clicked:
                raise Exception("Failed to click on MEN category.")
            # Wait for category section to load (simulate by waiting for search bar to remain visible)
            Utility.wait_for_element_state(page, f"xpath={generated_page._input_search_bar_xpath}", state="visible", timeout=15000)
            # --- Then: The selected category section is displayed (if implemented) ---
            Utility.log_test_step("Validating category section is displayed.")
            Utility.retry_assertion(
                lambda: expect(page).not_to_have_url(home_url, timeout=15000),
                retries=3,
                delay=2000
            )
            # --- When: Click on the logo image at the top left of the navigation bar ---
            logo_xpath: str = "//nav//a[contains(@class, 'logo') or .//img[contains(@alt, 'logo')]]"
            Utility.log_test_step("Clicking on the logo to return to the home page.")
            logo_clicked: bool = Utility.safe_wait_and_interact(
                page,
                logo_xpath,
                action="click",
                timeout=15000,
                retries=3
            )
            if not logo_clicked:
                raise Exception("Failed to click on the logo.")
            # --- Then: The user is redirected back to the main (home) page ---
            Utility.log_test_step("Verifying redirection to the home page after logo click.")
            Utility.retry_assertion(
                lambda: expect(page).to_have_url(home_url, timeout=15000),
                retries=3,
                delay=2000
            )
            # --- Then: The main page content is visible and correctly loaded ---
            Utility.log_test_step("Validating main page content after logo click.")
            Utility.retry_assertion(
                lambda: generated_page.validate_essential_elements(),
                retries=3,
                delay=2000
            )
            # --- Then: The URL and title reflect the home page ---
            Utility.log_test_step("Checking URL and page title for home page.")
            Utility.retry_assertion(
                lambda: expect(page).to_have_url(home_url, timeout=15000),
                retries=3,
                delay=2000
            )
            home_title = Utility.get_element_text(page, "//title", timeout=15000)
            if not isinstance(home_title, str) or not home_title.strip():
                raise AssertionError("Home page title is missing or invalid.")
            # --- When: Repeat the logo click after navigating to another section ---
            Utility.log_test_step("Navigating to WOMEN category and repeating logo click.")
            women_category_xpath: str = "//nav//a[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'women')]"
            women_clicked: bool = Utility.safe_wait_and_interact(
                page,
                women_category_xpath,
                action="click",
                timeout=15000,
                retries=3
            )
            if not women_clicked:
                raise Exception("Failed to click on WOMEN category.")
            Utility.wait_for_element_state(page, f"xpath={generated_page._input_search_bar_xpath}", state="visible", timeout=15000)
            Utility.retry_assertion(
                lambda: expect(page).not_to_have_url(home_url, timeout=15000),
                retries=3,
                delay=2000
            )
            logo_clicked_again: bool = Utility.safe_wait_and_interact(
                page,
                logo_xpath,
                action="click",
                timeout=15000,
                retries=3
            )
            if not logo_clicked_again:
                raise Exception("Failed to click on the logo again.")
            Utility.retry_assertion(
                lambda: expect(page).to_have_url(home_url, timeout=15000),
                retries=3,
                delay=2000
            )
            Utility.retry_assertion(
                lambda: generated_page.validate_essential_elements(),
                retries=3,
                delay=2000
            )
            test_result = "PASSED"
            test_details = "Logo click consistently returns user to the home page from any section."
        except AssertionError as ae:
            test_details = f"Assertion failed: {ae}"
            Utility.log_error(test_details)
            raise
        except Exception as e:
            test_details = f"Test failed: {e}"
            Utility.log_error(test_details)
            raise
        finally:
            Utility.log_test_result(test_result, test_details)
            browser.close()
#---#

# Test Case 2 - TC-0002
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
def test_navigation_category_links_display_correct_section() -> None:
    """
    TC-0002: Category Links Display Correct Section
    This test ensures that each category link in the navigation bar displays the correct section
    and provides visual feedback for the selected category.
    """
    # Test URLs (replace with actual URL as needed)
    urls: dict[str, str] = {
        "main": os.environ.get("TEST_BASE_URL", "https://styleup.com/")  # Default fallback
    }
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        # Attach console message logger
        page.on("console", lambda msg: Utility.log_console_message(msg))
        try:
            # --- GIVEN: Land on the main page of the website ---
            Utility.log_test_step("Navigating to the main page.")
            navigation_success: bool = Utility.navigate_to_page(page, urls["main"], timeout=15000)
            if not navigation_success:
                Utility.log_test_result("FAIL", "Navigation to main page failed.")
                raise Exception("Navigation to main page failed.")
            # Wait for body and essential elements
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            Utility.log_element_state("Search Bar", page.locator(f"xpath={generated_page._input_search_bar_xpath}"), timeout=15000)
            # Accept cookies/pop-ups if present (using Utility and POM methods if available)
            # (Assume a method or logic to handle cookies/pop-ups here if defined in POM)
            # --- THEN: The navigation bar with MEN, WOMEN, KIDS, and HOME & LIVING categories is visible ---
            # Since navigation bar locators are not defined in the POM, we assume their presence is validated as part of essential elements
            # --- WHEN: Click on the MEN category link in the navigation bar ---
            # --- THEN: The MEN section or related content is displayed (if implemented) ---
            men_category_xpath: str = "//nav//a[normalize-space()='MEN']"
            Utility.log_test_step("Clicking on the MEN category link.")
            Utility.log_element_state("MEN Category Link", page.locator(f"xpath={men_category_xpath}"), timeout=15000)
            Utility.safe_wait_and_interact(page, f"xpath={men_category_xpath}", action="click", timeout=15000)
            # Wait for MEN section/content to appear (assume section has id or heading)
            men_section_xpath: str = "//section[contains(@class, 'men-section') or contains(., 'MEN')]"
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={men_section_xpath}")).to_be_visible(timeout=15000),
                retries=3,
                delay=2000
            )
            Utility.log_test_result("PASS", "MEN section displayed after clicking MEN category.")
            # --- WHEN: Click on the WOMEN category link ---
            # --- THEN: The WOMEN section or related content is displayed ---
            women_category_xpath: str = "//nav//a[normalize-space()='WOMEN']"
            Utility.log_test_step("Clicking on the WOMEN category link.")
            Utility.log_element_state("WOMEN Category Link", page.locator(f"xpath={women_category_xpath}"), timeout=15000)
            Utility.safe_wait_and_interact(page, f"xpath={women_category_xpath}", action="click", timeout=15000)
            women_section_xpath: str = "//section[contains(@class, 'women-section') or contains(., 'WOMEN')]"
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={women_section_xpath}")).to_be_visible(timeout=15000),
                retries=3,
                delay=2000
            )
            Utility.log_test_result("PASS", "WOMEN section displayed after clicking WOMEN category.")
            # --- WHEN: Click on the KIDS category link ---
            # --- THEN: The KIDS section or related content is displayed ---
            kids_category_xpath: str = "//nav//a[normalize-space()='KIDS']"
            Utility.log_test_step("Clicking on the KIDS category link.")
            Utility.log_element_state("KIDS Category Link", page.locator(f"xpath={kids_category_xpath}"), timeout=15000)
            Utility.safe_wait_and_interact(page, f"xpath={kids_category_xpath}", action="click", timeout=15000)
            kids_section_xpath: str = "//section[contains(@class, 'kids-section') or contains(., 'KIDS')]"
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={kids_section_xpath}")).to_be_visible(timeout=15000),
                retries=3,
                delay=2000
            )
            Utility.log_test_result("PASS", "KIDS section displayed after clicking KIDS category.")
            # --- WHEN: Click on the HOME & LIVING category link ---
            # --- THEN: The HOME & LIVING section or related content is displayed ---
            home_category_xpath: str = "//nav//a[contains(normalize-space(), 'HOME') and contains(normalize-space(), 'LIVING')]"
            Utility.log_test_step("Clicking on the HOME & LIVING category link.")
            Utility.log_element_state("HOME & LIVING Category Link", page.locator(f"xpath={home_category_xpath}"), timeout=15000)
            Utility.safe_wait_and_interact(page, f"xpath={home_category_xpath}", action="click", timeout=15000)
            home_section_xpath: str = "//section[contains(@class, 'home-section') or contains(., 'HOME & LIVING')]"
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={home_section_xpath}")).to_be_visible(timeout=15000),
                retries=3,
                delay=2000
            )
            Utility.log_test_result("PASS", "HOME & LIVING section displayed after clicking HOME & LIVING category.")
            # --- THEN: The selected category is visually highlighted or indicated as active ---
            # Assume active class is 'active' on the selected nav link
            for category_xpath, category_name in [
                (men_category_xpath, "MEN"),
                (women_category_xpath, "WOMEN"),
                (kids_category_xpath, "KIDS"),
                (home_category_xpath, "HOME & LIVING")
            ]:
                Utility.log_test_step(f"Verifying active state for {category_name} category.")
                locator = page.locator(f"xpath={category_xpath}")
                Utility.retry_assertion(
                    lambda: expect(locator).to_have_class(re.compile(r"\bactive\b"), timeout=15000),
                    retries=3,
                    delay=2000
                )
                Utility.log_test_result("PASS", f"{category_name} category is visually highlighted as active.")
            Utility.log_test_result("PASS", "All category links display correct sections and visual feedback.")
        except Exception as e:
            Utility.log_error(f"Test failed: {e}")
            raise
        finally:
            browser.close()
#---#

# Generated Playwright Tests for blog
from playwright.sync_api import sync_playwright, expect, TimeoutError as PlaywrightTimeoutError
from blog_pom import GeneratedPage
import json
import re
import time
import os

urls = {}
from Utility import Utility


# Test Case 1 - TC-0001
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
# Global URLs dictionary (update with actual URLs as needed)
urls: dict[str, str] = {
    "home": os.environ.get("STYLEUP_HOME_URL", "https://styleup.example.com/")
}
def test_logo_click_returns_user_to_home_page() -> None:
    """
    TC-0001: Logo Click Returns User to Home Page
    Verifies that clicking the logo in the navigation bar consistently returns the user to the home page from any section.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        test_result: str = "FAILED"
        test_details: str = ""
        home_url: str = Utility.validate_and_convert_data(urls.get("home"), str)
        home_title: str = ""
        try:
            # --- Console and Dialog Handling ---
            page.on("console", Utility.log_console_message)
            page.on("dialog", lambda dialog: dialog.accept())
            # --- Given: Land on the main page of the website ---
            Utility.log_test_step("Navigating to the main page.")
            navigation_success: bool = Utility.navigate_to_page(page, home_url, timeout=15000)
            if not navigation_success:
                raise Exception("Navigation to home page failed.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            Utility.log_element_state("Search Bar", page.locator(f"xpath={generated_page._input_search_bar_xpath}"), timeout=15000)
            # Accept cookies/pop-ups if present (assuming a standard button, update selector as needed)
            cookie_accepted: bool = Utility.safe_wait_and_interact(
                page,
                "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'accept')]",
                action="click",
                timeout=5000,
                retries=2
            )
            # --- Then: The main page with the logo, navigation categories, and images is displayed ---
            Utility.log_test_step("Validating essential elements on the main page.")
            Utility.retry_assertion(
                lambda: generated_page.validate_essential_elements(),
                retries=3,
                delay=2000
            )
            # --- When: Navigate to a different section by clicking on any category ---
            # For demonstration, let's assume MEN category is available with a known XPath
            men_category_xpath: str = "//nav//a[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'men')]"
            Utility.log_test_step("Navigating to the MEN category section.")
            category_clicked: bool = Utility.safe_wait_and_interact(
                page,
                men_category_xpath,
                action="click",
                timeout=15000,
                retries=3
            )
            if not category_clicked:
                raise Exception("Failed to click on MEN category.")
            # Wait for category section to load (simulate by waiting for search bar to remain visible)
            Utility.wait_for_element_state(page, f"xpath={generated_page._input_search_bar_xpath}", state="visible", timeout=15000)
            # --- Then: The selected category section is displayed (if implemented) ---
            Utility.log_test_step("Validating category section is displayed.")
            Utility.retry_assertion(
                lambda: expect(page).not_to_have_url(home_url, timeout=15000),
                retries=3,
                delay=2000
            )
            # --- When: Click on the logo image at the top left of the navigation bar ---
            logo_xpath: str = "//nav//a[contains(@class, 'logo') or .//img[contains(@alt, 'logo')]]"
            Utility.log_test_step("Clicking on the logo to return to the home page.")
            logo_clicked: bool = Utility.safe_wait_and_interact(
                page,
                logo_xpath,
                action="click",
                timeout=15000,
                retries=3
            )
            if not logo_clicked:
                raise Exception("Failed to click on the logo.")
            # --- Then: The user is redirected back to the main (home) page ---
            Utility.log_test_step("Verifying redirection to the home page after logo click.")
            Utility.retry_assertion(
                lambda: expect(page).to_have_url(home_url, timeout=15000),
                retries=3,
                delay=2000
            )
            # --- Then: The main page content is visible and correctly loaded ---
            Utility.log_test_step("Validating main page content after logo click.")
            Utility.retry_assertion(
                lambda: generated_page.validate_essential_elements(),
                retries=3,
                delay=2000
            )
            # --- Then: The URL and title reflect the home page ---
            Utility.log_test_step("Checking URL and page title for home page.")
            Utility.retry_assertion(
                lambda: expect(page).to_have_url(home_url, timeout=15000),
                retries=3,
                delay=2000
            )
            home_title = Utility.get_element_text(page, "//title", timeout=15000)
            if not isinstance(home_title, str) or not home_title.strip():
                raise AssertionError("Home page title is missing or invalid.")
            # --- When: Repeat the logo click after navigating to another section ---
            Utility.log_test_step("Navigating to WOMEN category and repeating logo click.")
            women_category_xpath: str = "//nav//a[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'women')]"
            women_clicked: bool = Utility.safe_wait_and_interact(
                page,
                women_category_xpath,
                action="click",
                timeout=15000,
                retries=3
            )
            if not women_clicked:
                raise Exception("Failed to click on WOMEN category.")
            Utility.wait_for_element_state(page, f"xpath={generated_page._input_search_bar_xpath}", state="visible", timeout=15000)
            Utility.retry_assertion(
                lambda: expect(page).not_to_have_url(home_url, timeout=15000),
                retries=3,
                delay=2000
            )
            logo_clicked_again: bool = Utility.safe_wait_and_interact(
                page,
                logo_xpath,
                action="click",
                timeout=15000,
                retries=3
            )
            if not logo_clicked_again:
                raise Exception("Failed to click on the logo again.")
            Utility.retry_assertion(
                lambda: expect(page).to_have_url(home_url, timeout=15000),
                retries=3,
                delay=2000
            )
            Utility.retry_assertion(
                lambda: generated_page.validate_essential_elements(),
                retries=3,
                delay=2000
            )
            test_result = "PASSED"
            test_details = "Logo click consistently returns user to the home page from any section."
        except AssertionError as ae:
            test_details = f"Assertion failed: {ae}"
            Utility.log_error(test_details)
            raise
        except Exception as e:
            test_details = f"Test failed: {e}"
            Utility.log_error(test_details)
            raise
        finally:
            Utility.log_test_result(test_result, test_details)
            browser.close()
#---#

# Test Case 2 - TC-0002
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
def test_navigation_category_links_display_correct_section() -> None:
    """
    TC-0002: Category Links Display Correct Section
    This test ensures that each category link in the navigation bar displays the correct section
    and provides visual feedback for the selected category.
    """
    # Test URLs (replace with actual URL as needed)
    urls: dict[str, str] = {
        "main": os.environ.get("TEST_BASE_URL", "https://styleup.com/")  # Default fallback
    }
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        # Attach console message logger
        page.on("console", lambda msg: Utility.log_console_message(msg))
        try:
            # --- GIVEN: Land on the main page of the website ---
            Utility.log_test_step("Navigating to the main page.")
            navigation_success: bool = Utility.navigate_to_page(page, urls["main"], timeout=15000)
            if not navigation_success:
                Utility.log_test_result("FAIL", "Navigation to main page failed.")
                raise Exception("Navigation to main page failed.")
            # Wait for body and essential elements
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            Utility.log_element_state("Search Bar", page.locator(f"xpath={generated_page._input_search_bar_xpath}"), timeout=15000)
            # Accept cookies/pop-ups if present (using Utility and POM methods if available)
            # (Assume a method or logic to handle cookies/pop-ups here if defined in POM)
            # --- THEN: The navigation bar with MEN, WOMEN, KIDS, and HOME & LIVING categories is visible ---
            # Since navigation bar locators are not defined in the POM, we assume their presence is validated as part of essential elements
            # --- WHEN: Click on the MEN category link in the navigation bar ---
            # --- THEN: The MEN section or related content is displayed (if implemented) ---
            men_category_xpath: str = "//nav//a[normalize-space()='MEN']"
            Utility.log_test_step("Clicking on the MEN category link.")
            Utility.log_element_state("MEN Category Link", page.locator(f"xpath={men_category_xpath}"), timeout=15000)
            Utility.safe_wait_and_interact(page, f"xpath={men_category_xpath}", action="click", timeout=15000)
            # Wait for MEN section/content to appear (assume section has id or heading)
            men_section_xpath: str = "//section[contains(@class, 'men-section') or contains(., 'MEN')]"
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={men_section_xpath}")).to_be_visible(timeout=15000),
                retries=3,
                delay=2000
            )
            Utility.log_test_result("PASS", "MEN section displayed after clicking MEN category.")
            # --- WHEN: Click on the WOMEN category link ---
            # --- THEN: The WOMEN section or related content is displayed ---
            women_category_xpath: str = "//nav//a[normalize-space()='WOMEN']"
            Utility.log_test_step("Clicking on the WOMEN category link.")
            Utility.log_element_state("WOMEN Category Link", page.locator(f"xpath={women_category_xpath}"), timeout=15000)
            Utility.safe_wait_and_interact(page, f"xpath={women_category_xpath}", action="click", timeout=15000)
            women_section_xpath: str = "//section[contains(@class, 'women-section') or contains(., 'WOMEN')]"
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={women_section_xpath}")).to_be_visible(timeout=15000),
                retries=3,
                delay=2000
            )
            Utility.log_test_result("PASS", "WOMEN section displayed after clicking WOMEN category.")
            # --- WHEN: Click on the KIDS category link ---
            # --- THEN: The KIDS section or related content is displayed ---
            kids_category_xpath: str = "//nav//a[normalize-space()='KIDS']"
            Utility.log_test_step("Clicking on the KIDS category link.")
            Utility.log_element_state("KIDS Category Link", page.locator(f"xpath={kids_category_xpath}"), timeout=15000)
            Utility.safe_wait_and_interact(page, f"xpath={kids_category_xpath}", action="click", timeout=15000)
            kids_section_xpath: str = "//section[contains(@class, 'kids-section') or contains(., 'KIDS')]"
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={kids_section_xpath}")).to_be_visible(timeout=15000),
                retries=3,
                delay=2000
            )
            Utility.log_test_result("PASS", "KIDS section displayed after clicking KIDS category.")
            # --- WHEN: Click on the HOME & LIVING category link ---
            # --- THEN: The HOME & LIVING section or related content is displayed ---
            home_category_xpath: str = "//nav//a[contains(normalize-space(), 'HOME') and contains(normalize-space(), 'LIVING')]"
            Utility.log_test_step("Clicking on the HOME & LIVING category link.")
            Utility.log_element_state("HOME & LIVING Category Link", page.locator(f"xpath={home_category_xpath}"), timeout=15000)
            Utility.safe_wait_and_interact(page, f"xpath={home_category_xpath}", action="click", timeout=15000)
            home_section_xpath: str = "//section[contains(@class, 'home-section') or contains(., 'HOME & LIVING')]"
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={home_section_xpath}")).to_be_visible(timeout=15000),
                retries=3,
                delay=2000
            )
            Utility.log_test_result("PASS", "HOME & LIVING section displayed after clicking HOME & LIVING category.")
            # --- THEN: The selected category is visually highlighted or indicated as active ---
            # Assume active class is 'active' on the selected nav link
            for category_xpath, category_name in [
                (men_category_xpath, "MEN"),
                (women_category_xpath, "WOMEN"),
                (kids_category_xpath, "KIDS"),
                (home_category_xpath, "HOME & LIVING")
            ]:
                Utility.log_test_step(f"Verifying active state for {category_name} category.")
                locator = page.locator(f"xpath={category_xpath}")
                Utility.retry_assertion(
                    lambda: expect(locator).to_have_class(re.compile(r"\bactive\b"), timeout=15000),
                    retries=3,
                    delay=2000
                )
                Utility.log_test_result("PASS", f"{category_name} category is visually highlighted as active.")
            Utility.log_test_result("PASS", "All category links display correct sections and visual feedback.")
        except Exception as e:
            Utility.log_error(f"Test failed: {e}")
            raise
        finally:
            browser.close()
#---#

# Test Case 1 - TC-0034
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
# Test URLs dictionary (update as needed)
urls: dict[str, str] = {
    "index": os.environ.get("TEST_INDEX_URL", "http://localhost:8000/"),
}
def test_products_page_section_displays_all_categories_correctly_and_in_order() -> None:
    """
    TC-0034: Newly added products_page section displays all category names correctly and in order.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        page.on("console", lambda msg: Utility.log_console_message(msg))
        test_passed: bool = False
        try:
            # Given: Navigate to the index page and ensure it loads successfully
            Utility.log_test_step("Navigate to the index page of the web application.")
            navigation_success: bool = Utility.navigate_to_page(page, urls["index"], timeout=15000)
            if not navigation_success:
                Utility.log_test_result("FAIL", "Navigation to index page failed.")
                raise Exception("Navigation to index page failed.")
            Utility.log_test_step("Wait for the body element to be visible.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            # Accept cookies/pop-ups if present (using Utility, fallback to POM if available)
            # (Assume cookie banner is handled by Utility or POM if present)
            # When: Scroll down to locate the section with id="products_page"
            Utility.log_test_step("Scroll to the products_page section.")
            page.evaluate("document.getElementById('products_page').scrollIntoView({behavior: 'smooth'})")
            Utility.wait_for_element_state(page, "#products_page", state="visible", timeout=15000)
            Utility.log_element_state("products_page section", page.locator("#products_page"), timeout=15000)
            # Then: Verify the products_page section is visible
            expect(page.locator("#products_page")).to_be_visible(timeout=15000)
            # Then: Verify four separate divs are present within the products_page section
            Utility.log_test_step("Verify four category divs are present inside products_page.")
            category_divs_selector: str = "#products_page > div"
            div_count: int = 0
            for attempt in range(3):
                try:
                    div_count = page.locator(category_divs_selector).count()
                    if div_count == 4:
                        break
                except Exception as e:
                    if attempt == 2:
                        Utility.log_error(f"Failed to count category divs: {e}")
                        raise
                    time.sleep(1)
            if div_count != 4:
                Utility.log_test_result("FAIL", f"Expected 4 category divs, found {div_count}.")
                raise AssertionError(f"Expected 4 category divs, found {div_count}.")
            # Then: Verify the text content of each div in order
            expected_categories: list[str] = [
                "BATMAN",
                "WONDERWOMEN",
                "SPIDERKIDS",
                "HOME & LIVING"
            ]
            actual_categories: list[str] = []
            for i in range(4):
                div_xpath: str = f"//div[@id='products_page']/div[{i+1}]"
                Utility.log_element_state(f"Category div {i+1}", page.locator(f"xpath={div_xpath}"), timeout=15000)
                # Use Utility to get text
                div_text: str = Utility.get_element_text(page, f"xpath={div_xpath}", timeout=15000)
                div_text = Utility.validate_and_convert_data(div_text, str).strip()
                actual_categories.append(div_text)
                # Retry assertion for flaky rendering
                def assertion_func() -> None:
                    assert div_text == expected_categories[i], f"Expected '{expected_categories[i]}', got '{div_text}' in div {i+1}"
                Utility.retry_assertion(assertion_func, retries=3, delay=1000)
            # Then: Check the order of the category names
            Utility.log_test_step("Verify the order of category names.")
            for idx, (actual, expected) in enumerate(zip(actual_categories, expected_categories)):
                if actual != expected:
                    Utility.log_test_result("FAIL", f"Category at position {idx+1} expected '{expected}', got '{actual}'.")
                    raise AssertionError(f"Category at position {idx+1} expected '{expected}', got '{actual}'.")
            Utility.log_test_result("PASS", "All category names are displayed correctly and in order in products_page section.")
            test_passed = True
        except AssertionError as ae:
            Utility.log_error(f"Assertion failed: {ae}")
            raise
        except Exception as e:
            Utility.log_error(f"Test failed due to unexpected error: {e}")
            raise
        finally:
            if not test_passed:
                Utility.log_test_result("FAIL", "Test did not complete successfully.")
            else:
                Utility.log_test_result("PASS", "Test completed successfully.")
            browser.close()
#---#
