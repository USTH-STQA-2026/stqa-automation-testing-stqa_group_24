import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from web_detector import detect_technology, WebTech

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://stqa.rbc.vn")
TEST_EMAIL = os.getenv("TEST_EMAIL", "")
TEST_PASSWORD = os.getenv("TEST_PASSWORD", "")
TEST_DISPLAY_NAME = os.getenv("TEST_DISPLAY_NAME", "")
SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


# ---------------------------------------------------------------------------
# Smart Wait — Chờ thông minh (thay vì time.sleep)
# ---------------------------------------------------------------------------
# Playwright hỗ trợ auto-wait cho hầu hết thao tác (click, fill, assert).
# Tuy nhiên, Flutter Web (CanvasKit) render toàn bộ UI trên <canvas>, nên
# Semantics Tree cần thời gian cập nhật sau mỗi thay đổi giao diện.
#
# ✅ Nên dùng:
#   wait_for_flutter(page, text="Đăng xuất")      # Chờ text xuất hiện
#   page.locator("...").wait_for(timeout=5000)     # Chờ element cụ thể
#
# ❌ Tránh dùng:
#   time.sleep(3)    # Hard sleep — chậm, không ổn định (flaky)
# ---------------------------------------------------------------------------


def wait_for_flutter(page, text=None, selector=None, timeout=10000):
    """Smart Wait: chờ Flutter Semantics Tree cập nhật.

    Args:
        text: Chờ text xuất hiện trong flt-semantics
        selector: Chờ CSS selector khớp element
        timeout: Thời gian tối đa (ms), mặc định 10s

    Examples:
        wait_for_flutter(page)                              # Chờ semantics sẵn sàng
        wait_for_flutter(page, text="Đăng xuất")            # Chờ thấy "Đăng xuất"
        wait_for_flutter(page, selector='input[aria-label="Email"]')
    """
    if text:
        # Flutter Web dùng cả textContent và aria-label — chờ cả hai
        page.locator(
            f'flt-semantics:has-text("{text}"), flt-semantics[aria-label*="{text}"]'
        ).first.wait_for(state="attached", timeout=timeout)
    elif selector:
        page.locator(selector).first.wait_for(state="attached", timeout=timeout)
    else:
        page.locator("flt-semantics").first.wait_for(state="attached", timeout=timeout)


@pytest.fixture(scope="session")
def browser():
    # Use explicit HEADLESS env so CI can choose headed mode with xvfb when needed.
    headless = os.getenv("HEADLESS", "false").lower() == "true"
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=headless,
            args=["--force-renderer-accessibility"],
        )
        yield browser
        browser.close()


@pytest.fixture()
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture()
def test_config():
    """Cung cấp thông tin cấu hình test từ biến môi trường."""
    return {
        "base_url": BASE_URL,
        "email": TEST_EMAIL,
        "password": TEST_PASSWORD,
        "display_name": TEST_DISPLAY_NAME,
        "screenshot_dir": SCREENSHOT_DIR,
    }


@pytest.fixture()
def web_tech(page) -> WebTech:
    """Phát hiện công nghệ web và trả về WebTech object.
    Dùng trong test để biết trang đang dùng công nghệ gì."""
    page.goto(BASE_URL, wait_until="networkidle", timeout=60000)
    page.locator("flt-glass-pane").wait_for(state="attached", timeout=15000)
    tech = detect_technology(page)
    print(f"\n[web_detector] {tech.name.value}", end="")
    if tech.renderer:
        print(f" ({tech.renderer})", end="")
    print()
    return tech


def enable_flutter_semantics(page, timeout=15000):
    """Bật Flutter Semantics Tree để tạo DOM elements tương tác được.
    Tự động chờ Flutter render xong trước khi bật (Smart Wait)."""
    # Already enabled.
    if page.locator("flt-semantics").count() > 0:
        return

    enable_btn = page.locator('flt-semantics-placeholder[role="button"]').first
    try:
        enable_btn.wait_for(state="attached", timeout=timeout)
        enable_btn.focus()
        enable_btn.dispatch_event("click")
    except Exception:
        # Fallback for headless runs where placeholder click is flaky.
        page.keyboard.press("Tab")
        page.keyboard.press("Enter")

    page.locator("flt-semantics, input[aria-label], textarea[aria-label]").first.wait_for(
        state="attached",
        timeout=timeout,
    )


def flutter_fill(page, label, value):
    """Nhập text vào Flutter text field thông qua semantics input."""
    field = page.locator(f'input[aria-label="{label}"]').first
    field.wait_for(state="attached", timeout=10000)
    field.click()

    # Flutter tạo input ẩn khi editing — chờ nó xuất hiện thay vì sleep
    active_input = page.locator("flt-text-editing-host input, flt-text-editing-host textarea")
    try:
        active_input.first.wait_for(state="attached", timeout=3000)
        active_input.first.fill(value)
    except Exception:
        field.fill(value)


def flutter_click_button(page, text):
    """Click Flutter button thông qua semantics element."""
    btn = page.locator(f'flt-semantics[role="button"]:has-text("{text}")')
    btn.click()


# ---------------------------------------------------------------------------
# Universal helpers — tự chọn chiến lược theo công nghệ web
# ---------------------------------------------------------------------------

def smart_fill(page, label, value, tech: WebTech = None):
    """Nhập text vào field — tự chọn cách tương tác phù hợp.

    Args:
        label: aria-label (Flutter) hoặc placeholder/label (HTML thường)
        value: Giá trị cần nhập
        tech:  WebTech object (nếu None sẽ tự detect)
    """
    if tech is None:
        tech = detect_technology(page)

    if tech.is_flutter_canvaskit:
        enable_flutter_semantics(page)
        flutter_fill(page, label, value)
    else:
        # HTML thường: tìm theo label, placeholder, hoặc aria-label (fallback chain)
        by_label = page.get_by_label(label)
        if by_label.count() > 0:
            by_label.first.fill(value)
            return
        by_placeholder = page.get_by_placeholder(label)
        if by_placeholder.count() > 0:
            by_placeholder.first.fill(value)
            return
        page.locator(f'input[aria-label="{label}"]').fill(value)


def login(page, test_config):
    """Helper: đăng nhập và chờ trang chính load (Smart Wait)."""
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
    flutter_fill(page, "Email", test_config["email"])
    flutter_fill(page, "Mật khẩu", test_config["password"])
    flutter_click_button(page, "Đăng nhập")
    # Smart Wait: chờ trang chính load — nút "Đăng xuất" xuất hiện
    wait_for_flutter(page, text="Đăng xuất")
    enable_flutter_semantics(page)


def smart_click(page, text, tech: WebTech = None):
    """Click button — tự chọn cách tương tác phù hợp.

    Args:
        text: Text hiển thị trên button
        tech: WebTech object (nếu None sẽ tự detect)
    """
    if tech is None:
        tech = detect_technology(page)

    if tech.is_flutter_canvaskit:
        enable_flutter_semantics(page)
        flutter_click_button(page, text)
    else:
        # HTML thường: tìm button theo text
        page.get_by_role("button", name=text).click()