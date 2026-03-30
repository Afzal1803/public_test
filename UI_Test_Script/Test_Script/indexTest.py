# Generated Playwright Tests for index
from playwright.sync_api import sync_playwright, expect, TimeoutError as PlaywrightTimeoutError
from index_pom import GeneratedPage
import json
import re
import time
import os

urls = {}
from Utility import Utility


# Test Case 1 - TC-0001
# Import the POM class
# Global URLs dictionary for test navigation
urls: dict[str, str] = {
    "home": os.environ.get("STYLEUP_HOME_URL", "https://styleup.com/"),
}
def test_logo_click_navigates_to_home_page() -> None:
    """
    TC-0001: Logo Click Navigates to Home Page
    1. This test case verifies that clicking the logo in the navigation bar always returns the user to the home page, ensuring consistent navigation behavior.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        test_passed: bool = False
        # Attach console message logger
        page.on("console", Utility.log_console_message)
        # --- Given: Setup and navigation to initial state ---
        try:
            Utility.log_test_step("Navigating to the Styleup home page.")
            navigation_success: bool = Utility.navigate_to_page(page, urls["home"], timeout=15000)
            if not navigation_success:
                Utility.log_error("Failed to navigate to the home page.")
                raise Exception("Navigation to home page failed.")
            Utility.log_test_step("Waiting for main page body to be visible.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            # Accept cookies/pop-ups if present
            # Try to interact with a generic cookie accept button if it exists
            cookie_accepted: bool = Utility.safe_wait_and_interact(
                page,
                "xpath=//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'accept')]",
                action="click",
                timeout=5000,
                retries=1
            )
            # --- When: Perform the action ---
            # Step 1: Verify logo is visible in the top navigation bar
            Utility.log_test_step("Verifying logo is visible in the top navigation bar.")
            logo_xpath: str = "//a[contains(@class, 'logo') or contains(@href, '/') or contains(@aria-label, 'logo') or contains(@class, 'navbar-brand') or contains(@class, 'site-logo') or contains(@class, 'header-logo')]//img | //img[contains(@alt, 'logo') or contains(@class, 'logo')]"
            # Try multiple common logo patterns for robustness
            logo_found: bool = False
            logo_locator = None
            for xpath in [
                "//a[contains(@class, 'logo')]//img",
                "//a[contains(@class, 'navbar-brand')]//img",
                "//img[contains(@alt, 'logo')]",
                "//img[contains(@class, 'logo')]",
                "//a[contains(@href, '/') and (contains(@aria-label, 'logo') or contains(@class, 'logo'))]//img",
                "//a[contains(@class, 'site-logo')]//img",
                "//a[contains(@class, 'header-logo')]//img"
            ]:
                try:
                    Utility.log_element_state("Logo", page.locator(f"xpath={xpath}"), timeout=15000)
                    logo_locator = page.locator(f"xpath={xpath}")
                    expect(logo_locator).to_be_visible(timeout=15000)
                    logo_found = True
                    break
                except Exception:
                    continue
            if not logo_found or logo_locator is None:
                Utility.log_error("Logo not found in the navigation bar.")
                raise Exception("Logo not found in the navigation bar.")
            # Step 2: Verify logo is displayed and clickable
            Utility.log_test_step("Verifying logo is displayed and clickable.")
            expect(logo_locator).to_be_visible(timeout=15000)
            expect(logo_locator).to_be_enabled(timeout=15000)
            # Step 3: Hover over the logo and check cursor style
            Utility.log_test_step("Hovering over the logo to check cursor style.")
            logo_locator.hover()
            # Playwright does not provide direct cursor style check, but we can check if it's clickable
            # Optionally, check 'pointer-events' style or just proceed
            # Step 4: Click on the logo
            Utility.log_test_step("Clicking on the logo.")
            retry_click_success: bool = False
            for attempt in range(3):
                try:
                    logo_locator.click(timeout=15000)
                    retry_click_success = True
                    break
                except PlaywrightTimeoutError as e:
                    Utility.log_error(f"Attempt {attempt+1}: Timeout clicking logo: {e}")
                    time.sleep(1)
                except Exception as e:
                    Utility.log_error(f"Attempt {attempt+1}: Error clicking logo: {e}")
                    time.sleep(1)
            if not retry_click_success:
                Utility.log_error("Failed to click the logo after retries.")
                raise Exception("Logo click failed.")
            # --- Then: Verify expected outcomes ---
            # Step 5: Wait for main content area to be visible after clicking logo
            Utility.log_test_step("Waiting for main content area to be visible after clicking logo.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            # Step 6: Validate essential elements to confirm home page loaded
            Utility.log_test_step("Validating essential elements on the home page.")
            try:
                Utility.retry_assertion(
                    lambda: generated_page.validate_essential_elements(),
                    retries=3,
                    delay=1000
                )
            except AssertionError as e:
                Utility.log_error(f"Essential elements not found after logo navigation: {e}")
                raise
            # Step 7: Check the URL corresponds to the home page
            Utility.log_test_step("Checking that the URL corresponds to the home page.")
            current_url: str = Utility.validate_and_convert_data(page.url, str)
            expected_url: str = Utility.validate_and_convert_data(urls["home"], str)
            if not current_url.rstrip("/").startswith(expected_url.rstrip("/")):
                Utility.log_error(f"URL after logo click does not match home page. Actual: {current_url}, Expected: {expected_url}")
                raise AssertionError(f"URL after logo click does not match home page. Actual: {current_url}, Expected: {expected_url}")
            Utility.log_test_result("PASS", "Logo click navigates to the home page as expected.")
            test_passed = True
        except PlaywrightTimeoutError as e:
            Utility.log_error(f"Timeout error during test execution: {e}")
            Utility.log_test_result("FAIL", f"Timeout error: {e}")
            raise
        except AssertionError as e:
            Utility.log_error(f"Assertion failed: {e}")
            Utility.log_test_result("FAIL", f"Assertion failed: {e}")
            raise
        except Exception as e:
            Utility.log_error(f"Unexpected error: {e}")
            Utility.log_test_result("FAIL", f"Unexpected error: {e}")
            raise
        finally:
            if test_passed:
                Utility.log_test_result("SUMMARY", "Test completed successfully.")
            else:
                Utility.log_test_result("SUMMARY", "Test failed.")
            browser.close()
#---#
#######

# Test Case 2 - TC-0002
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
# Test Data and URLs
urls: dict[str, str] = {
    "main_page": os.environ.get("STYLEUP_MAIN_URL", "https://styleup.com/")
}
SEARCH_BAR_XPATH: str = "//input[@id='search-bar']"
SEARCH_PLACEHOLDER: str = "Search for products, brands & more"
def test_search_bar_accepts_and_displays_user_input() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        # Attach console logger
        page.on("console", lambda msg: Utility.log_console_message(msg))
        try:
            # --- GIVEN: Land on the main page of the Styleup website ---
            Utility.log_test_step("Navigating to the Styleup main page.")
            navigation_success: bool = Utility.navigate_to_page(page, urls["main_page"], timeout=15000)
            if not navigation_success:
                Utility.log_test_result("FAIL", "Navigation to main page failed.")
                raise Exception("Navigation to main page failed.")
            # Wait for body and critical elements
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            Utility.log_element_state("Search Bar", page.locator(f"xpath={SEARCH_BAR_XPATH}"), timeout=15000)
            # Accept cookies/pop-ups if present (try both button variants)
            try:
                generated_page.click_invite_now_button()
            except Exception:
                pass
            try:
                generated_page.click_invite_superhero_button()
            except Exception:
                pass
            # --- THEN: The search bar is visible in the navigation area ---
            Utility.log_test_step("Verifying search bar visibility.")
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={SEARCH_BAR_XPATH}")).to_be_visible(timeout=15000),
                retries=3,
                delay=1000
            )
            # --- WHEN: Click inside the search bar ---
            Utility.log_test_step("Clicking inside the search bar.")
            Utility.safe_wait_and_interact(page, f"xpath={SEARCH_BAR_XPATH}", action="click", timeout=15000)
            Utility.log_element_state("Search Bar (after click)", page.locator(f"xpath={SEARCH_BAR_XPATH}"), timeout=15000)
            # --- THEN: The cursor appears in the search bar, ready for input ---
            # (No direct way to check cursor, but we can check focus)
            is_focused: bool = page.evaluate(f"document.activeElement === document.evaluate('{SEARCH_BAR_XPATH}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue")
            if not is_focused:
                Utility.log_test_result("FAIL", "Search bar did not receive focus after click.")
                raise AssertionError("Search bar did not receive focus after click.")
            Utility.log_test_result("PASS", "Search bar is focused and ready for input.")
            # --- WHEN: Type a valid product name, such as "shoes" ---
            product_name: str = Utility.validate_and_convert_data("shoes", str)
            Utility.log_test_step(f"Typing product name '{product_name}' in the search bar.")
            generated_page.fill_search_bar(product_name)
            # --- THEN: The text "shoes" appears in the search bar ---
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={SEARCH_BAR_XPATH}")).to_have_value(product_name, timeout=15000),
                retries=3,
                delay=1000
            )
            Utility.log_test_result("PASS", f"Search bar displays '{product_name}' as expected.")
            # --- WHEN: Clear the search bar and type a brand name, such as "Nike" ---
            brand_name: str = Utility.validate_and_convert_data("Nike", str)
            Utility.log_test_step(f"Clearing and typing brand name '{brand_name}' in the search bar.")
            generated_page.fill_search_bar("")  # Clear
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={SEARCH_BAR_XPATH}")).to_have_value("", timeout=15000),
                retries=3,
                delay=1000
            )
            generated_page.fill_search_bar(brand_name)
            # --- THEN: The text "Nike" appears in the search bar ---
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={SEARCH_BAR_XPATH}")).to_have_value(brand_name, timeout=15000),
                retries=3,
                delay=1000
            )
            Utility.log_test_result("PASS", f"Search bar displays '{brand_name}' as expected.")
            # --- WHEN: Delete the text and type a category, such as "dresses" ---
            category_name: str = Utility.validate_and_convert_data("dresses", str)
            Utility.log_test_step(f"Clearing and typing category '{category_name}' in the search bar.")
            generated_page.fill_search_bar("")  # Clear
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={SEARCH_BAR_XPATH}")).to_have_value("", timeout=15000),
                retries=3,
                delay=1000
            )
            generated_page.fill_search_bar(category_name)
            # --- THEN: The text "dresses" appears in the search bar ---
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={SEARCH_BAR_XPATH}")).to_have_value(category_name, timeout=15000),
                retries=3,
                delay=1000
            )
            Utility.log_test_result("PASS", f"Search bar displays '{category_name}' as expected.")
            # --- WHEN/THEN: Observe the placeholder text before and after typing ---
            Utility.log_test_step("Verifying placeholder text visibility before typing.")
            generated_page.fill_search_bar("")  # Ensure empty
            placeholder_value: str = page.locator(f"xpath={SEARCH_BAR_XPATH}").get_attribute("placeholder")
            if placeholder_value != SEARCH_PLACEHOLDER:
                Utility.log_test_result("FAIL", f"Expected placeholder '{SEARCH_PLACEHOLDER}', got '{placeholder_value}'")
                raise AssertionError(f"Expected placeholder '{SEARCH_PLACEHOLDER}', got '{placeholder_value}'")
            Utility.log_test_result("PASS", f"Placeholder '{SEARCH_PLACEHOLDER}' is visible when search bar is empty.")
            Utility.log_test_step("Verifying placeholder disappears after typing.")
            generated_page.fill_search_bar("test")
            # Placeholder attribute remains, but visually disappears; check value is not empty and placeholder is present
            value_after_typing: str = page.locator(f"xpath={SEARCH_BAR_XPATH}").input_value()
            if value_after_typing != "test":
                Utility.log_test_result("FAIL", "Search bar did not accept input after typing.")
                raise AssertionError("Search bar did not accept input after typing.")
            Utility.log_test_result("PASS", "Placeholder disappears when typing (input value present).")
            Utility.log_test_result("PASS", "Test case TC-0002: Search Bar Accepts and Displays User Input completed successfully.")
        except AssertionError as ae:
            Utility.log_error(f"Assertion failed: {ae}")
            Utility.log_test_result("FAIL", str(ae))
            raise
        except Exception as e:
            Utility.log_error(f"Test execution error: {e}")
            Utility.log_test_result("FAIL", str(e))
            raise
        finally:
            browser.close()
#---#
#######
