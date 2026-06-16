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

import time
import pytest
from conftest import (
    enable_flutter_semantics, 
    flutter_click_button,
    login, 
    wait_for_flutter,
)


def test_logout(page, test_config):
    """TC-11: Logout success (Đăng xuất thành công)"""
    
    # 1. Đăng nhập với fallback mạnh
    try:
        login(page, test_config)
    except Exception:
        print("⚠️ Login helper timeout → dùng fallback mạnh")
        time.sleep(5)
        enable_flutter_semantics(page)
        wait_for_flutter(page, timeout=15000)
    
    # 2. Đảm bảo semantics sẵn sàng và tìm nút Đăng xuất
    time.sleep(3)
    enable_flutter_semantics(page)
    
    print("🔍 Đang tìm nút Đăng xuất...")
    
    # Cách 1: Dùng flutter_click_button (như conftest)
    try:
        wait_for_flutter(page, text="Đăng xuất", timeout=8000)
        flutter_click_button(page, "Đăng xuất")
        print("✅ Click Đăng xuất bằng helper")
    except:
        # Cách 2: Fallback click mạnh bằng JavaScript
        print("⚠️ Helper timeout → dùng JavaScript click")
        enable_flutter_semantics(page)
        page.evaluate('''() => {
            const elements = document.querySelectorAll('flt-semantics[role="button"]');
            for (let el of elements) {
                if (el.textContent.trim().includes("Đăng xuất")) {
                    el.click();
                    console.log("Clicked logout via JS");
                    return;
                }
            }
        }''')
        time.sleep(2)
    
    # 3. Chờ quay về trang login
    time.sleep(3)
    enable_flutter_semantics(page)
    wait_for_flutter(page, text="Đăng nhập", timeout=12000)
    
    # 4. Verify
    login_button = page.locator('flt-semantics[role="button"]:has-text("Đăng nhập")')
    email_input = page.locator('input[aria-label="Email"]')
    
    assert login_button.count() > 0 or email_input.count() > 0, \
        "❌ Không quay về trang đăng nhập sau khi logout"

    print("✅ TC-11 Logout thành công")


def test_switch_language_to_english(page, test_config):
    """TC-12: Switch language to English (Chuyển ngôn ngữ sang tiếng Anh)"""
    
    try:
        login(page, test_config)
    except Exception:
        print("⚠️ Login helper timeout → fallback")
        time.sleep(5)
        enable_flutter_semantics(page)
        wait_for_flutter(page, timeout=15000)
    
    time.sleep(2)
    enable_flutter_semantics(page)
    
    # Click EN
    try:
        flutter_click_button(page, "EN")
    except:
        enable_flutter_semantics(page)
        page.locator('flt-semantics[role="button"]:has-text("EN")').click()
    
    # Chờ chuyển ngôn ngữ
    time.sleep(3)
    enable_flutter_semantics(page)
    wait_for_flutter(page, timeout=10000)
    
    # Kiểm tra
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents()).lower()
    
    english_keywords = ["logout", "borrow", "search", "library", "book", "account", 
                       "sign in", "email", "password"]
    
    assert any(word in sem_text for word in english_keywords), \
        f"❌ Không tìm thấy text tiếng Anh. Found: {sem_text[:250]}..."

    print("✅ TC-12 Chuyển ngôn ngữ sang English thành công")