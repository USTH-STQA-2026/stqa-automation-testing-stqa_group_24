"""
Logout & Language Tests (*Kiểm thử Đăng xuất & Chuyển ngôn ngữ*) — Library Book Borrowing System (*Hệ thống Mượn sách thư viện*)

Students must complete ALL 2 test cases in this file.
(*Sinh viên cần hoàn thành TẤT CẢ 2 test case trong file này.*)

Hints (*Gợi ý*):
    - Use login() helper to log in (*Dùng login() helper để đăng nhập*)
    - Logout button: 'flt-semantics[role="button"]:has-text("Đăng xuất")'
      (*Nút Đăng xuất*)
    - Language switch EN button: 'flt-semantics[role="button"]:has-text("EN")'
      (*Nút chuyển ngôn ngữ EN*)
    - After logout: page returns to login (has "Đăng nhập" button and "Email" input)
      (*Sau đăng xuất: trang quay về login*)
    - After switching to EN: text "Logout", "Borrow", "Search", "Library" may appear
      (*Sau chuyển EN: text tiếng Anh có thể xuất hiện*)
"""
import os
import time
import pytest
from conftest import (
    enable_flutter_semantics, flutter_fill, flutter_click_button,
    login, SCREENSHOT_DIR,
)


def test_logout(page, test_config):
    """TC-11: Logout success"""

    # Step 1: Login
    login(page, test_config)

    # Step 2: Enable Flutter semantics
    enable_flutter_semantics(page)

    # Step 3: Click Logout button
    flutter_click_button(page, "Logout")

    # Step 4: Wait for UI update
    page.wait_for_timeout(3000)

    # Step 5: Re-enable semantics after navigation
    enable_flutter_semantics(page)

    # Take screenshot
    page.screenshot(
        path=os.path.join(SCREENSHOT_DIR, "logout_success.png")
    )

    # Step 6: Verify user is back on login page
    sem_text = " ".join(
        page.locator("flt-semantics").all_text_contents()
    )

    has_login_button = (
        "Login" in sem_text
        or "Sign In" in sem_text
    )

    has_email_input = (
        "Email" in sem_text
    )

    assert has_login_button or has_email_input, \
        "Logout failed: Login page not displayed"


def test_switch_language_to_english(page, test_config):
    """TC-12: Switch language to English"""

    # Step 1: Login
    login(page, test_config)

    # Step 2: Enable Flutter semantics
    enable_flutter_semantics(page)

    # Step 3: Click EN button
    flutter_click_button(page, "EN")

    # Step 4: Wait for UI update
    page.wait_for_timeout(2000)

    # Step 5: Re-enable semantics
    enable_flutter_semantics(page)

    # Take screenshot
    page.screenshot(
        path=os.path.join(SCREENSHOT_DIR, "switch_language_english.png")
    )

    # Step 6: Get semantics text
    sem_text = " ".join(
        page.locator("flt-semantics").all_text_contents()
    )

    # Step 7: Verify English UI appears
    has_english_ui = (
        "Logout" in sem_text
        or "Borrow" in sem_text
        or "Library" in sem_text
        or "Search" in sem_text
    )

    assert has_english_ui, \
        "Language switch failed: English UI not detected"
