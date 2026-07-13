# Generated Playwright Tests for cart
from playwright.sync_api import sync_playwright, expect, TimeoutError as PlaywrightTimeoutError
from cart_pom import GeneratedPage
import json
import re
import time
import os

urls = {}
from Utility import Utility


# Test Case 1 - TC-0001
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
# Global URLs dictionary (update with actual home page URL)
def test_logo_redirects_to_home_page() -> None:
    """
    Test Case: TC-0001
    Scenario: Logo Redirects to Home Page
    Module: Navigation & Header
    Steps:
        1. Open the main page in a new browser session.
        2. Verify the logo is visible in the top left corner of the navigation bar.
        3. Hover over the logo and verify pointer changes.
        4. Click on the logo.
        5. Verify navigation bar and cart section are displayed as on the main page.
        6. Check the browser URL is set to the main (index) page.
        7. Confirm the cart and price details are visible.
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
        console_errors: list[str] = []
        # Attach console message logger
        def on_console_message(msg):
            Utility.log_console_message(msg)
            if msg.type == "error":
                console_errors.append(msg.text)
        page.on("console", on_console_message)
        try:
            # --- Given: Setup and navigation to initial state ---
            Utility.log_test_step("Navigating to the main page.")
            url: str = Utility.validate_and_convert_data(urls.get("main_page"), str)
            if not url or len(url) > 200:
                raise ValueError("Invalid or missing main page URL.")
            navigation_success: bool = Utility.navigate_to_page(page, url, timeout=15000)
            if not navigation_success:
                raise RuntimeError("Failed to navigate to main page.")
            Utility.log_test_step("Waiting for page body to be visible.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            # --- Then: Verify the logo is visible in the top left corner of the navigation bar ---
            Utility.log_test_step("Validating essential elements (logo, cart, etc.).")
            Utility.retry_assertion(
                lambda: generated_page.validate_essential_elements(),
                retries=3,
                delay=1000
            )
            # --- When: Hover over the logo ---
            logo_xpath: str = "//a[contains(@class,'navbar-brand') or contains(@class,'logo') or contains(@href,'/')]"
            Utility.log_test_step("Checking logo visibility before hover.")
            logo_selector: str = f"xpath={logo_xpath}"
            Utility.wait_for_element_state(page, logo_selector, state="visible", timeout=15000)
            logo_element = page.locator(logo_selector)
            Utility.log_element_state("Logo", logo_element, timeout=15000)
            Utility.log_test_step("Hovering over the logo.")
            try:
                logo_element.hover(timeout=15000)
            except Exception as e:
                Utility.log_error(f"Logo hover failed: {e}")
                raise
            Utility.log_test_step("Verifying pointer changes to indicate clickability.")
            pointer_style: str = logo_element.evaluate("el => window.getComputedStyle(el).cursor")
            if pointer_style not in ["pointer", "hand"]:
                Utility.log_error("Logo does not indicate clickability on hover.")
                raise AssertionError("Logo pointer style is not 'pointer' or 'hand'.")
            # --- When: Click on the logo ---
            Utility.log_test_step("Clicking on the logo.")
            try:
                logo_element.click(timeout=15000)
            except Exception as e:
                Utility.log_error(f"Logo click failed: {e}")
                raise
            # --- Then: Verify navigation bar and cart section are displayed as on the main page ---
            Utility.log_test_step("Waiting for navigation after logo click.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            Utility.retry_assertion(
                lambda: generated_page.validate_essential_elements(),
                retries=3,
                delay=1000
            )
            # --- Then: Check the browser URL is set to the main (index) page ---
            Utility.log_test_step("Verifying URL after logo click.")
            current_url: str = Utility.validate_and_convert_data(page.url, str)
            expected_url: str = url.rstrip("/")
            actual_url: str = current_url.rstrip("/")
            if actual_url != expected_url:
                Utility.log_error(f"URL mismatch: expected '{expected_url}', got '{actual_url}'")
                raise AssertionError(f"URL after logo click is incorrect: {actual_url}")
            # --- Then: Confirm the cart and price details are visible ---
            Utility.log_test_step("Validating cart and price details section is present and loaded.")
            Utility.retry_assertion(
                lambda: generated_page.validate_essential_elements(),
                retries=3,
                delay=1000
            )
            # --- Accept cookies/pop-ups if present ---
            cookie_popup_xpath: str = "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'accept')]"
            cookie_popup_selector: str = f"xpath={cookie_popup_xpath}"
            if Utility.wait_for_element_state(page, cookie_popup_selector, state="visible", timeout=5000):
                Utility.log_test_step("Accepting cookies popup.")
                Utility.safe_wait_and_interact(page, cookie_popup_selector, action="click", timeout=5000)
            test_result = "PASSED"
            test_details = "Logo redirects to home page and all elements are present."
        except AssertionError as ae:
            test_details = f"Assertion failed: {ae}"
            Utility.log_error(test_details)
            raise
        except Exception as e:
            test_details = f"Test failed due to unexpected error: {e}"
            Utility.log_error(test_details)
            raise
        finally:
            Utility.log_test_result(test_result, test_details)
            if console_errors:
                Utility.log_error(f"Console errors during test: {console_errors}")
            browser.close()
#---#
#######
