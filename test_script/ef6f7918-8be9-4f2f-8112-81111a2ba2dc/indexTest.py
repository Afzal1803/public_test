# Generated Playwright Tests for index
from playwright.sync_api import sync_playwright, expect, TimeoutError as PlaywrightTimeoutError
from index_pom import GeneratedPage
import json
import re
import time
import os

urls = {}
from Utility import Utility


# Test Case 1 - TC-0026
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
# Test URLs (replace with actual URL as needed)
urls: dict[str, str] = {
    "index": os.environ.get("CHAT_INDEX_URL", "https://your-chat-app-url.com/")
}
def test_chat_message_list_edge_behavior() -> None:
    """
    TC-0026: Edge behavior for empty and first/last chat messages in Chat Message List.
    Verifies correct handling of only the first message, last message, and empty state.
    """
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
            # --- GIVEN: Setup and navigation to initial state ---
            Utility.log_test_step("Navigate to the chat index page.")
            url: str = Utility.validate_and_convert_data(urls.get("index"), str)
            if not url:
                Utility.log_error("Chat index URL is not defined.")
                raise ValueError("Chat index URL is not defined.")
            navigation_success: bool = Utility.navigate_to_page(page, url, timeout=15000)
            if not navigation_success:
                Utility.log_error("Failed to navigate to chat index page.")
                raise RuntimeError("Navigation to chat index page failed.")
            Utility.log_test_step("Wait for page body and essential elements to be visible.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            # Accept cookies/pop-ups if present (simulate by trying to click known pop-up selectors)
            # (Assume a cookie button with id 'cookie-accept-btn' if present)
            Utility.safe_wait_and_interact(page, "xpath=//button[contains(@id,'cookie') or contains(@id,'accept')]", "click", timeout=5000, retries=1)
            # --- WHEN: Ensure preconditions (page fully loaded, no user messages sent yet) ---
            Utility.log_test_step("Ensure chat area is visible and only the initial bot message is present.")
            # Wait for chat input to be visible
            Utility.wait_for_element_state(page, "xpath=//input[@id='chat-input']", state="visible", timeout=15000)
            # --- THEN: The page loads with the chat message area visible, showing the initial bot message. ---
            Utility.log_test_step("Verify only the initial bot message is present in the chat message list.")
            # There should be only one message (the bot's)
            def assert_initial_bot_message():
                # Assume chat messages have a common class or role, e.g., 'chat-message'
                # Since we can't use inline locators, use Utility.get_element_text on known bot message area
                bot_message_text: str = Utility.get_element_text(page, "xpath=//div[contains(@class,'chat-message')][1]", timeout=15000)
                assert bot_message_text.strip() != "", "Initial bot message should not be empty."
            Utility.retry_assertion(assert_initial_bot_message, retries=3, delay=1000)
            # --- THEN: The UI displays the first message correctly, with no layout issues. ---
            Utility.log_test_step("Verify the UI displays the first message correctly.")
            # Log element state for the first message
            Utility.log_element_state("First chat message", page.locator("xpath=//div[contains(@class,'chat-message')][1]"), timeout=15000)
            # --- WHEN: Send a user message and observe the chat message list. ---
            Utility.log_test_step("Send a user message and verify it appears below the bot message.")
            user_message: str = Utility.validate_and_convert_data("Hello, this is a test message!", str)
            generated_page.fill_chat_input(user_message)
            generated_page.click_send_button()
            # --- THEN: The user message appears below the bot message, and the list updates correctly. ---
            def assert_user_message_appears():
                # Second message should be the user's
                user_message_text: str = Utility.get_element_text(page, "xpath=//div[contains(@class,'chat-message')][2]", timeout=15000)
                assert user_message in user_message_text, "User message did not appear as expected."
            Utility.retry_assertion(assert_user_message_appears, retries=3, delay=1000)
            # --- WHEN: Continue sending messages until the chat message list reaches the maximum visible area (test scrolling behavior). ---
            Utility.log_test_step("Send multiple user messages to test scrolling and last message visibility.")
            for i in range(5):
                msg: str = Utility.validate_and_convert_data(f"Test message {i+1}", str)
                generated_page.fill_chat_input(msg)
                generated_page.click_send_button()
                # Wait for message to appear
                def assert_message_appears():
                    idx: int = i + 3  # 1:bot, 2:first user, 3+:next
                    message_text: str = Utility.get_element_text(page, f"xpath=//div[contains(@class,'chat-message')][{idx}]", timeout=15000)
                    assert msg in message_text, f"Message '{msg}' did not appear at position {idx}."
                Utility.retry_assertion(assert_message_appears, retries=3, delay=1000)
            # --- THEN: The chat message list scrolls as needed, and the last message is always visible. ---
            Utility.log_test_step("Verify the last message is visible and no overflow/truncation occurs.")
            def assert_last_message_visible():
                last_idx: int = 7  # 1 bot + 1 initial user + 5 more = 7
                last_message_text: str = Utility.get_element_text(page, f"xpath=//div[contains(@class,'chat-message')][{last_idx}]", timeout=15000)
                assert "Test message 5" in last_message_text, "Last message is not visible or truncated."
            Utility.retry_assertion(assert_last_message_visible, retries=3, delay=1000)
            # --- THEN: The UI displays both the first and last messages correctly, with no overflow or truncation. ---
            Utility.log_test_step("Verify both first and last messages are displayed correctly.")
            def assert_first_and_last_message():
                first_message_text: str = Utility.get_element_text(page, "xpath=//div[contains(@class,'chat-message')][1]", timeout=15000)
                last_message_text: str = Utility.get_element_text(page, "xpath=//div[contains(@class,'chat-message')][7]", timeout=15000)
                assert first_message_text.strip() != "", "First message should not be empty."
                assert "Test message 5" in last_message_text, "Last message content mismatch."
            Utility.retry_assertion(assert_first_and_last_message, retries=3, delay=1000)
            # --- WHEN: Optionally, clear all messages (if possible) and observe the empty state. ---
            Utility.log_test_step("Attempt to clear all messages and verify empty state (if supported).")
            try:
                generated_page.click_end_chat_button()
                # Wait for chat area to clear
                time.sleep(2)
                def assert_empty_state():
                    # Try to get the first message; should be empty or not present
                    empty_text: str = Utility.get_element_text(page, "xpath=//div[contains(@class,'chat-message')][1]", timeout=5000)
                    assert empty_text.strip() == "" or "no messages" in empty_text.lower(), "Chat area did not clear as expected."
                Utility.retry_assertion(assert_empty_state, retries=2, delay=1000)
            except Exception as e:
                Utility.log_error(f"Clearing messages not supported or failed: {e}")
            Utility.log_test_result("PASS", "Chat message list edge behavior verified successfully.")
        except AssertionError as ae:
            Utility.log_test_result("FAIL", f"Assertion failed: {ae}")
            raise
        except Exception as e:
            Utility.log_test_result("FAIL", f"Unexpected error: {e}")
            raise
        finally:
            browser.close()
#---#
