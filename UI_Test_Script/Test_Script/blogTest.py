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
    "home": os.environ.get("TEST_HOME_URL", "https://your-website-url.com/"),
    "secondary": os.environ.get("TEST_SECONDARY_URL", "https://your-website-url.com/secondary")
}
def test_logo_click_returns_user_to_home_page() -> None:
    """
    TC-0001: Logo Click Returns User to Home Page
    This test verifies that clicking the logo in the header always returns the user to the home page,
    regardless of their current location on the site.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        page.on("console", Utility.log_console_message)
        test_passed: bool = False
        try:
            # --- GIVEN: Land on the main page of the website ---
            Utility.log_test_step("Navigating to the home page.")
            home_url: str = Utility.validate_and_convert_data(urls.get("home"), str)
            if not home_url:
                Utility.log_error("Home URL is not defined or invalid.")
                raise ValueError("Home URL is not defined or invalid.")
            navigation_success: bool = Utility.navigate_to_page(page, home_url, timeout=15000)
            if not navigation_success:
                Utility.log_error("Failed to navigate to the home page.")
                raise RuntimeError("Navigation to home page failed.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            Utility.log_test_step("Validating essential elements on the home page.")
            Utility.retry_assertion(lambda: generated_page.validate_essential_elements(), retries=3, delay=2000)
            # --- Accept cookies/pop-ups if present ---
            # (Assume a method or logic in POM for cookies if needed; skip if not defined)
            # --- THEN: The logo is visible in the header section ---
            Utility.log_test_step("Verifying logo visibility in the header.")
            # Assuming the logo has a known XPath in the POM (add to POM if missing)
            logo_xpath: str = "//header//a[contains(@class, 'logo') or contains(@href, '/') or contains(@aria-label, 'logo')]"
            # Use Utility to check visibility
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={logo_xpath}")).to_be_visible(timeout=15000),
                retries=3,
                delay=2000
            )
            Utility.log_element_state("Header Logo", page.locator(f"xpath={logo_xpath}"), timeout=15000)
            # --- WHEN: Navigate to a different section or scroll down the page ---
            Utility.log_test_step("Navigating to a secondary page/section.")
            secondary_url: str = Utility.validate_and_convert_data(urls.get("secondary"), str)
            if not secondary_url:
                Utility.log_error("Secondary URL is not defined or invalid.")
                raise ValueError("Secondary URL is not defined or invalid.")
            navigation_success = Utility.navigate_to_page(page, secondary_url, timeout=15000)
            if not navigation_success:
                Utility.log_error("Failed to navigate to the secondary page.")
                raise RuntimeError("Navigation to secondary page failed.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            Utility.log_test_step("Validating essential elements on the secondary page.")
            Utility.retry_assertion(lambda: generated_page.validate_essential_elements(), retries=3, delay=2000)
            # --- THEN: The logo remains visible and accessible in the header ---
            Utility.log_test_step("Verifying logo visibility after navigation.")
            Utility.retry_assertion(
                lambda: expect(page.locator(f"xpath={logo_xpath}")).to_be_visible(timeout=15000),
                retries=3,
                delay=2000
            )
            Utility.log_element_state("Header Logo (after navigation)", page.locator(f"xpath={logo_xpath}"), timeout=15000)
            # --- WHEN: Hover over the logo ---
            Utility.log_test_step("Hovering over the logo to check pointer cursor.")
            logo_locator = page.locator(f"xpath={logo_xpath}")
            Utility.wait_for_element_state(page, f"xpath={logo_xpath}", state="visible", timeout=15000)
            logo_locator.hover()
            # Check cursor style (pointer)
            cursor_style: str = logo_locator.evaluate("el => window.getComputedStyle(el).cursor")
            if cursor_style != "pointer":
                Utility.log_error(f"Logo cursor is not pointer on hover (actual: {cursor_style})")
                raise AssertionError("Logo cursor is not pointer on hover.")
            # --- WHEN: Click on the logo ---
            Utility.log_test_step("Clicking the logo to return to the home page.")
            Utility.safe_wait_and_interact(page, f"xpath={logo_xpath}", action="click", timeout=15000)
            # --- THEN: The page navigates or refreshes to the main (home) page ---
            Utility.log_test_step("Waiting for navigation to the home page after logo click.")
            Utility.retry_assertion(
                lambda: expect(page).to_have_url(home_url, timeout=15000),
                retries=3,
                delay=2000
            )
            # --- THEN: The main page content is displayed, confirming navigation ---
            Utility.log_test_step("Validating essential elements on the home page after logo click.")
            Utility.retry_assertion(lambda: generated_page.validate_essential_elements(), retries=3, delay=2000)
            # --- THEN: The URL and title correspond to the home page ---
            Utility.log_test_step("Verifying URL and page title after logo click.")
            current_url: str = Utility.validate_and_convert_data(page.url, str)
            if not current_url.startswith(home_url):
                Utility.log_error(f"URL after logo click does not match home page. Actual: {current_url}")
                raise AssertionError("URL after logo click does not match home page.")
            page_title: str = Utility.validate_and_convert_data(page.title(), str)
            if not page_title or "home" not in page_title.lower():
                Utility.log_error(f"Page title after logo click does not indicate home page. Actual: {page_title}")
                raise AssertionError("Page title after logo click does not indicate home page.")
            test_passed = True
            Utility.log_test_result("PASS", "Logo click successfully returned user to the home page.")
        except AssertionError as ae:
            Utility.log_test_result("FAIL", f"Assertion failed: {ae}")
            raise
        except Exception as e:
            Utility.log_test_result("FAIL", f"Test failed due to unexpected error: {e}")
            raise
        finally:
            if not test_passed:
                Utility.log_error("Test did not complete successfully.")
            browser.close()
#---#
#######

# Test Case 2 - TC-0002
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
# Global URLs dictionary (update with actual URL as needed)
def test_category_links_display_correct_product_sections() -> None:
    """
    Test Case TC-0002: Category Links Display Correct Product Sections
    Given: User lands on the main page of the website.
    When: User hovers and clicks on each category link in the header.
    Then: The correct product section is displayed or highlighted for each category.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        test_result = "PASSED"
        test_details = ""
        # --- Enhanced dialog and console handling ---
        page.on("console", lambda msg: Utility.log_console_message(msg))
        try:
            # --- Given: Navigate to main page ---
            Utility.log_test_step("Navigating to the main page.")
            navigation_success = Utility.navigate_to_page(page, urls["main_page"], timeout=15000)
            if not navigation_success:
                raise Exception("Navigation to main page failed.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            Utility.log_test_step("Validated essential elements on the main page.")
            # --- Accept cookies/pop-ups if present ---
            # (Assume a cookie accept button with a known XPath, update if needed)
            cookie_accept_xpath = "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'accept')]"
            try:
                Utility.safe_wait_and_interact(page, f"xpath={cookie_accept_xpath}", "click", timeout=5000)
                Utility.log_test_step("Accepted cookies/pop-ups.")
            except Exception:
                Utility.log_test_step("No cookie pop-up detected or already accepted.")
            # --- Then: Verify category links are visible in the header ---
            category_xpaths = {
                "MEN": "//a[normalize-space()='MEN']",
                "WOMEN": "//a[normalize-space()='WOMEN']",
                "KIDS": "//a[normalize-space()='KIDS']",
                "HOME & LIVING": "//a[normalize-space()='HOME & LIVING']"
            }
            for category, xpath in category_xpaths.items():
                Utility.log_test_step(f"Checking visibility of '{category}' category link.")
                locator = page.locator(f"xpath={xpath}")
                Utility.log_element_state(f"{category} link", locator, timeout=15000)
                Utility.retry_assertion(
                    lambda: expect(locator).to_be_visible(timeout=15000),
                    retries=3,
                    delay=2000
                )
            # --- When: Hover over each category link and check hover effect ---
            for category, xpath in category_xpaths.items():
                Utility.log_test_step(f"Hovering over '{category}' category link.")
                locator = page.locator(f"xpath={xpath}")
                Utility.retry_assertion(
                    lambda: expect(locator).to_be_visible(timeout=15000),
                    retries=3,
                    delay=2000
                )
                locator.hover()
                time.sleep(1)  # Allow hover effect to render
                # Optionally, check for hover effect (color/underline) if CSS class changes are known
            # --- Then: Click each category link and verify correct section is displayed ---
            section_verification = {
                "MEN": "//section[contains(@id, 'men') or contains(@class, 'men')]",
                "WOMEN": "//section[contains(@id, 'women') or contains(@class, 'women')]",
                "KIDS": "//section[contains(@id, 'kids') or contains(@class, 'kids')]",
                "HOME & LIVING": "//section[contains(@id, 'home') or contains(@class, 'home')]"
            }
            for category, link_xpath in category_xpaths.items():
                Utility.log_test_step(f"Clicking on '{category}' category link.")
                generated_page._safe_click(link_xpath)
                # Wait for the corresponding section to be visible
                section_xpath = section_verification[category]
                section_locator = page.locator(f"xpath={section_xpath}")
                Utility.log_element_state(f"{category} section", section_locator, timeout=15000)
                Utility.retry_assertion(
                    lambda: expect(section_locator).to_be_visible(timeout=15000),
                    retries=3,
                    delay=2000
                )
                Utility.log_test_step(f"Verified '{category}' product section is displayed or highlighted.")
                time.sleep(1)  # Allow UI to settle before next interaction
            test_details = "All category links are visible, interactive, and display correct product sections."
            Utility.log_test_result(test_result, test_details)
        except AssertionError as ae:
            test_result = "FAILED"
            test_details = f"Assertion failed: {ae}"
            Utility.log_error(test_details)
            raise
        except Exception as e:
            test_result = "FAILED"
            test_details = f"Test failed: {e}"
            Utility.log_error(test_details)
            raise
        finally:
            Utility.log_test_result(test_result, test_details)
            browser.close()
#---#
#######
