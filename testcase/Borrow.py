import os
import time
import pytest


def test_borrow_book(page, test_config, login, wait_for_flutter, flutter_click_button, SCREENSHOT_DIR):
    # [R] Reachability: Access the website
    login(page, test_config)
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "before_borrow.png"))

    # [I] Infection: Borrow a book
    buttons = page.get_by_role("button", name="Mượn sách này")
    if buttons.count() > 0:
        buttons.first.click()
    else:
        assert buttons.count() > 0, "No books to borrow"

    wait_for_flutter(page, "Xác nhận mượn sách")
    flutter_click_button(page, "Mượn")

    # [P] Propagation
    wait_for_flutter(page, "Mượn sách thành công")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "after_borrow.png"))

    # [R] Revealability
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "thành công" in sem_text, \
        "Borrow book wasn't successful: expecting \"thành công\""


def test_view_borrowed_books(page, test_config, login, wait_for_flutter, SCREENSHOT_DIR):
    login(page, test_config)

    page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]').click()
    wait_for_flutter(page, "Phiếu mượn của tôi")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "view_borrowed_books.png"))

    sem_text = "".join(page.content())
    assert "Đang mượn" in sem_text, "Fault : No display of 'Đang mượn'!"
    assert "Trả sách" in sem_text, "Fault : No display of 'Trả sách'!"
    assert "Đã trả" in sem_text, "Fault : No display of 'Đã trả'"


def test_return_book(page, test_config, login, wait_for_flutter, flutter_click_button, SCREENSHOT_DIR):
    login(page, test_config)

    page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]').click()
    wait_for_flutter(page, "Phiếu mượn của tôi")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "before_return.png"))

    flutter_click_button(page, "Trả sách")

    wait_for_flutter(page, "Trả sách thành công")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "after_return.png"))

    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "thành công" in sem_text, \
        "Return book wasn't successful: expecting \"thành công\""


def test_book_limit(page, test_config, enable_flutter_semantics, flutter_fill,
                    flutter_click_button, wait_for_flutter, SCREENSHOT_DIR):

    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
    flutter_fill(page, "Email", "dam.tran@email.com")
    flutter_fill(page, "Mật khẩu", test_config["password"])
    flutter_click_button(page, "Đăng nhập")
    wait_for_flutter(page, "Đăng xuất")

    for i in range(1, 5):
        buttons = page.get_by_role("button", name="Mượn sách này")
        if buttons.count() > 0:
            buttons.first.click()
        else:
            assert buttons.count() > 0, "No books to borrow"

        wait_for_flutter(page, "Xác nhận mượn sách")
        flutter_click_button(page, "Mượn")
        wait_for_flutter(page, "Mượn sách thành công")

        page.screenshot(path=os.path.join(SCREENSHOT_DIR, f"borrow_number_{i}.png"))

        if i < 4:
            page.wait_for_timeout(3800)
            page.mouse.wheel(0, 30)
            page.wait_for_timeout(1000)
        else:
            sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
            assert "Đã đạt giới hạn mượn tối đa" in sem_text, \
                "Fault : The book limit counting is false"


def test_borrow_permission_expired(page, test_config, enable_flutter_semantics,
                                  flutter_fill, flutter_click_button,
                                  wait_for_flutter, SCREENSHOT_DIR):

    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
    flutter_fill(page, "Email", "binh.pham@email.com")
    flutter_fill(page, "Mật khẩu", test_config["password"])
    flutter_click_button(page, "Đăng nhập")
    wait_for_flutter(page, "Đăng xuất")

    buttons = page.get_by_role("button", name="Mượn sách này")
    if buttons.count() > 0:
        buttons.first.click()
    else:
        assert buttons.count() > 0, "No books to borrow"

    wait_for_flutter(page, "Xác nhận mượn sách")
    flutter_click_button(page, "Mượn")
    wait_for_flutter(page, "Không thể mượn sách")

    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "borrow_from_expired_acc.png"))

    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "hết hạn" in sem_text


def test_borrow_permission_suspended(page, test_config, enable_flutter_semantics,
                                    flutter_fill, flutter_click_button,
                                    wait_for_flutter, SCREENSHOT_DIR):

    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
    flutter_fill(page, "Email", "cu.le@email.com")
    flutter_fill(page, "Mật khẩu", test_config["password"])
    flutter_click_button(page, "Đăng nhập")
    wait_for_flutter(page, "Đăng xuất")

    buttons = page.get_by_role("button", name="Mượn sách này")
    if buttons.count() > 0:
        buttons.first.click()
    else:
        assert buttons.count() > 0, "No books to borrow"

    wait_for_flutter(page, "Xác nhận mượn sách")
    flutter_click_button(page, "Mượn")
    wait_for_flutter(page, "Không thể mượn sách")

    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "borrow_from_suspended_acc.png"))

    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "tạm ngưng" in sem_text


def test_librarian_view_borrow_overdue(page, enable_flutter_semantics,
                                      flutter_fill, flutter_click_button,
                                      wait_for_flutter, SCREENSHOT_DIR):

    page.goto("http://localhost:3000", wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
    flutter_fill(page, "Email", "librarian@library.com")
    flutter_fill(page, "Mật khẩu", "admin123")
    flutter_click_button(page, "Đăng nhập")
    wait_for_flutter(page, "Đăng xuất")

    page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]').click()
    wait_for_flutter(page, "Kiểm tra sách quá hạn")
    flutter_click_button(page, "Kiểm tra sách quá hạn")

    page.wait_for_timeout(1000)
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "librarian_view_borrow_overdue.png"))

    sem_text = "".join(page.content())
    assert "Kiểm thử phần mềm nhập môn" in sem_text
    assert "Quá hạn" in sem_text