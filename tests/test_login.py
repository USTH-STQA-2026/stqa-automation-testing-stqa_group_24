import os
import pytest
from conftest import enable_flutter_semantics, flutter_fill, flutter_click_button, wait_for_flutter, SCREENSHOT_DIR

def test_login_success(page, test_config):
    """TC-01: Login success with valid credentials"""
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)

    flutter_fill(page, "Email", test_config["email"])
    flutter_fill(page, "Mật khẩu", test_config["password"])
    flutter_click_button(page, "Đăng nhập")

    wait_for_flutter(page, text="Đăng xuất")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "login_success.png"))

    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    has_user_name = test_config["display_name"] in sem_text
    has_logout = "Đăng xuất" in sem_text or "Logout" in sem_text
    assert has_user_name or has_logout, \
        f"Login failed: '{test_config['display_name']}' or Logout button not found"

@pytest.mark.parametrize("email, password, expected_text, tc_id", [
    ("nobody@test.com", "anything", "Không tìm thấy thành viên", "TC-02"),
    ("ba.nguyen@email.com", "wrongpassword", "Mật khẩu không đúng", "TC-03"),
    ("", "", "Vui lòng nhập", "TC-04"),
    ("", "anything", "Vui lòng nhập", "TC-05"),
    ("librarian@library.com", "", "Vui lòng nhập", "TC-06"),
    ("nobody@test.com", "wrongpassword", "Không tìm thấy", "TC-07"),
])
def test_login_fail(page, test_config, email, password, expected_text, tc_id):
    """TC-02 to TC-07: Login fail cases"""
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)

    if email:
        flutter_fill(page, "Email", email)
    if password:
        flutter_fill(page, "Mật khẩu", password)
    
    flutter_click_button(page, "Đăng nhập")
    
    # give it some time for error message to appear
    page.wait_for_timeout(2000)
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, f"{tc_id}.png"))

    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert expected_text in sem_text, f"{tc_id} failed: Expected error '{expected_text}' not found."
