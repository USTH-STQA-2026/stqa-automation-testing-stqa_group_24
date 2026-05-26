"""
Search & Filter Tests (*Kiểm thử Tìm kiếm & Lọc sách*) — Library Book Borrowing System (*Hệ thống Mượn sách thư viện*)

Students must complete ALL 4 test cases in this file.
(*Sinh viên cần hoàn thành TẤT CẢ 4 test case trong file này.*)

Hints (*Gợi ý*):
    - After logging in, use flutter_fill() to type into the search box
      (*Sau khi đăng nhập, dùng flutter_fill() để nhập vào ô tìm kiếm*)
    - Search box aria-label: "Tìm kiếm theo tên sách hoặc tác giả..."
    - Category filter aria-label: "Lọc theo thể loại (VD: Công nghệ, Kinh tế...)"
    - Each book card has role="group" and aria-label containing book info
      (*Mỗi card sách có role="group" và aria-label chứa thông tin sách*)
    - Use login() helper from conftest.py to log in before testing
      (*Dùng login() helper từ conftest.py để đăng nhập trước khi test*)
"""
import os
import time
import pytest
from conftest import (
    enable_flutter_semantics, flutter_fill, flutter_click_button,
    login, SCREENSHOT_DIR, wait_for_flutter
)


def test_search_book_by_name(page, test_config):
    """TC-04: Search book by name – results found (*Tìm kiếm sách theo tên — tìm thấy kết quả*)

    🔴 NOT COMPLETED (*CHƯA HOÀN THÀNH*)

    Description (*Mô tả*):
        Log in → search keyword "Flutter" → verify Flutter books appear in results.
        (*Đăng nhập → tìm kiếm từ khóa "Flutter" → kiểm tra có sách Flutter trong kết quả.*)

    Hints (*Gợi ý*):
        - login(page, test_config)
        - flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Flutter")
        - Verify: page.locator('flt-semantics[aria-label*="Flutter"]').count() > 0
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)
    login(page, test_config)
    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Flutter")
    wait_for_flutter(page, text="Flutter")
    assert page.locator('flt-semantics[aria-label*="Flutter"]').count() >= 1


def test_search_book_no_result(page, test_config):
    """TC-05: Search book – no results (*Tìm kiếm sách — không có kết quả*)

    🔴 NOT COMPLETED (*CHƯA HOÀN THÀNH*)

    Description (*Mô tả*):
        Log in → search a non-existent keyword (e.g. "xyz_khong_ton_tai_12345")
        → verify no books are displayed.
        (*Đăng nhập → tìm kiếm từ khóa không tồn tại → kiểm tra không có sách nào hiển thị.*)

    Hints (*Gợi ý*):
        - Verify: page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"]').count() == 0
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)
    login(page, test_config)
    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "xyz_khong_ton_tai_12345")
    page.wait_for_timeout(2000) # Đợi danh sách cập nhật (trường hợp rỗng khó dùng wait_for_flutter(text) nên đành dùng wait_for_timeout)
    assert page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"]').count() == 0


def test_filter_by_category(page, test_config):
    """TC-06: Filter books by category 'Công nghệ' (*Lọc sách theo thể loại 'Công nghệ'*)

    🔴 NOT COMPLETED (*CHƯA HOÀN THÀNH*)

    Description (*Mô tả*):
        Log in → enter "Công nghệ" in the category filter → verify all displayed books
        belong to the "Công nghệ" category.
        (*Đăng nhập → nhập "Công nghệ" vào ô lọc thể loại → kiểm tra tất cả sách
        hiển thị đều thuộc thể loại Công nghệ.*)

    Hints (*Gợi ý*):
        - flutter_fill(page, "Lọc theo thể loại (VD: Công nghệ, Kinh tế...)", "Công nghệ")
        - Get book list: page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"]')
          (*Lấy danh sách sách*)
        - Loop through each book, verify aria-label contains "Công nghệ"
          (*Lặp qua từng sách, kiểm tra aria-label chứa "Công nghệ"*)
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)
    login(page, test_config)
    flutter_fill(page, "Lọc theo thể loại (VD: Công nghệ, Kinh tế...)", "Công nghệ")
    wait_for_flutter(page, text="Công nghệ")
    books = page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"]')
    assert books.count() > 0, "Không tìm thấy sách nào cho thể loại công nghệ"
    for i in range(books.count()):
        assert "Công nghệ" in books.nth(i).get_attribute("aria-label")


def test_search_by_author(page, test_config):
    """TC-07: Search book by author name (*Tìm kiếm sách theo tên tác giả*)

    🔴 NOT COMPLETED (*CHƯA HOÀN THÀNH*)

    Description (*Mô tả*):
        Log in → search author name (e.g. "Nguyễn Minh Đức") → verify results found.
        (*Đăng nhập → tìm kiếm tên tác giả → kiểm tra có kết quả.*)

    Hints (*Gợi ý*):
        - flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Nguyễn Minh Đức")
        - Verify: page.locator('flt-semantics[aria-label*="Nguyễn Minh Đức"]').count() > 0
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)
    login(page, test_config)
    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Nguyễn Minh Đức")
    wait_for_flutter(page, text="Nguyễn Minh Đức")
    assert page.locator('flt-semantics[aria-label*="Nguyễn Minh Đức"]').count() > 0
