# REPORT: Web UI Automation Testing

---

**Tools:** Python + Playwright + pytest

# 1. Login Module

- **Implemented by:** Nguyễn Văn Đức
- **Module Tested:** Login Functionality (`tests/test_login.py`)


## 1.1 How it works

- **Flutter Web Support:** Since Flutter renders UI elements inside a canvas, we use `enable_flutter_semantics(page)` before every test. This exposes Flutter semantic nodes (`flt-semantics`) so Playwright can interact with text fields, buttons, and messages.

- **Input Handling:** User credentials are entered through the helper function `flutter_fill(page, label, value)`, which locates Flutter input fields using their semantic labels.

- **Button Interaction:** Login actions are performed using `flutter_click_button(page, "Đăng nhập")`, allowing the test to trigger the same login flow as a real user.

- **Verification Method:** Instead of checking HTML elements directly, the tests read all text from Flutter semantic nodes using:

  `page.locator("flt-semantics").all_text_contents()`

  The returned text is combined into a single string and inspected for expected messages.

- **Screenshot Capture:** Every test automatically saves a screenshot after execution for evidence and debugging purposes.
## 1.2 Test Cases Summary

Every negative test checks two things: that the correct error message shows up, and that the user is safely kept on the login page (the app didn't crash or log them in by mistake).

| Test ID | Scenario | Description | Status |
|----------|----------|-------------|---------|
| TC-01 | Login Success | Logs in with valid email/password → sees `"Đăng xuất"` | PASS |
| TC-02 | Wrong Password | Logs in with bad password → sees `"Mật khẩu không đúng."` | PASS |
| TC-03 | Empty Fields | Clicks login with no inputs → sees `"Vui lòng nhập email và mật khẩu."` | PASS |
| TC-13 | User Not Found | Logs in with a fake email → sees `"Không tìm thấy thành viên."` | PASS |

## 1.3 Test Evidence (Screenshots)

The automated screenshots for each result have been generated and saved into the project folder when running the script:

- `screenshots/login_success.png`
- `screenshots/login_fail_wrong_password.png`
- `screenshots/login_fail_empty_fields.png`
- `screenshots/login_fail_member_not_found.png`

---
# 2. Searching and Filtering Books Module

- **Implemented by:** Phùng Đức Thắng
- **Module Tested:** Search and Filter Functionality (`tests/test_search_book.py`)

## 2.1 How it works

- **Login Prerequisite:** Each test begins by calling `login(page, test_config)` to authenticate the user before accessing the book list.

- **Search Input:** Search keywords are entered using `flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", keyword)`.

- **Search Execution:** After entering a keyword, the test triggers the search operation by pressing the `Enter` key.

- **Result Validation:** The test collects all text from Flutter semantic nodes using `page.locator("flt-semantics").all_text_contents()` and verifies that the expected book title or message appears in the rendered content.

- **Category Filtering:** The filter field is populated using `flutter_fill(page, "Lọc theo thể loại (VD: Công nghệ, Kinh tế...)", category)` and the displayed content is checked for the selected category.

- **Case-Insensitive Testing:** Both lowercase and uppercase inputs are tested to ensure search and filtering functions are not affected by text casing.

## 2.2 Test Cases Summary

| Test ID | Scenario | Description | Status |
|----------|----------|-------------|---------|
| TC-17 | Search by Book Title | Search using keyword "Flutter" and verify matching content is displayed. | PASS |
| TC-18 | Search by Author | Search using author name "Nguyễn Minh Đức" and verify matching content is displayed. | PASS |
| TC-19 | Search with Lowercase Keyword | Search using keyword "flutter" and verify matching content is displayed. | PASS |
| TC-20 | Search with Uppercase Keyword | Search using keyword "FLUTTER" and verify matching content is displayed. | PASS |
| TC-21 | Search with No Result | Search using non-existing keyword "xyz_khong_ton_tai" and verify the no-result message is displayed. | PASS |
| TC-22 | Filter by Category | Filter books using category "Công nghệ" and verify matching content is displayed. | PASS |
| TC-23 | Filter by Category (Lowercase) | Filter books using category "công nghệ" and verify matching content is displayed. | PASS |

# 3. Borrow and Return Books Module

- **Implemented by:** Nguyễn Anh Tuấn
- **Module Tested:** Borrowing and Returning Functionality (`tests/test_borrow_return.py`)

## 3.1 How it works

- **Login Requirement:** Each test begins by logging into the system using predefined member credentials through the helper function `login(page, config)`.

- **Borrow Workflow:** Available books are located through Flutter semantic nodes containing the text `"Có sẵn"`. The automation then interacts with `"Mượn sách này"` and `"Mượn"` buttons to simulate the borrowing process.

- **Return Workflow:** The automation navigates to the `"Mượn / Trả"` tab and interacts with available `"Trả sách"` buttons to perform return operations.

- **Flutter Semantics Support:** Since the application is built using Flutter Web, all interactions and validations are performed through `flt-semantics` accessibility nodes instead of traditional HTML elements.

- **Validation Method:** Test results are verified by collecting semantic text from Flutter nodes and checking for success messages, borrowing status, overdue warnings, or access restrictions.

## 3.2 Test Cases Summary

| Test ID | Scenario | Description | Status |
|----------|----------|-------------|---------|
| TC-08 | Borrow Available Book | Borrow an available book and verify successful borrowing. | PASS |
| TC-09 | Borrow Borrowed Book | Attempt to borrow a book that has already been borrowed. | PASS |
| TC-10 | Borrow Lost Book | Attempt to borrow a book marked as lost. | PASS |
| TC-11 | Suspended Member Borrowing | Verify that suspended members cannot borrow books. | PASS |
| TC-12 | Expired Member Borrowing | Verify that expired members cannot borrow books. | PASS |
| TC-13 | Borrow Limit Reached | Verify behavior when a member has reached the maximum borrowing limit. | FAIL |
| TC-24 | Return Borrowed Book | Return a currently borrowed book and verify successful processing. | PASS |
| TC-25 | Return Overdue Book | Verify overdue warning behavior when returning an overdue book. | PASS |
| TC-26 | Return Another Member's Book | Verify that users cannot access or return books borrowed by other members. | PASS |
| TC-27 | Return Already Returned Book | Verify that an already returned book cannot be returned again. | PASS |

## 3.3 Validation Logic

- Successful borrowing is validated by detecting either a success message containing `"thành công"` or a borrowing status containing `"Đang mượn"`.

- Borrowing restrictions are validated through semantic text indicating unavailable books, lost books, suspended members, expired memberships, or borrowing limitations.

- Return operations are validated through success messages and the availability of return controls.

- Access control is validated by ensuring records belonging to other members are not displayed.

## 3.4 Notes

- TC-13 is currently incomplete because the borrowing-limit validation flow has not yet been fully implemented.

- The module relies on Flutter semantic nodes (`flt-semantics`) for all UI interactions and assertions.

---
# 4. Logout and Language Switching Module

- **Implemented by:** Nguyễn Văn Đức
- **Module Tested:** Logout and Language Switching Functionality (`tests/test_general.py`)

## 4.1 How it works

- **Authentication Requirement:** Both test cases begin by logging into the system using the `login()` helper function.

- **Fallback Handling:** If the login helper encounters a timeout or synchronization issue, the automation enables Flutter semantics and waits for the application to become available before continuing.

- **Logout Functionality:** The automation locates the `Đăng xuất` button and performs logout using either the helper method `flutter_click_button()` or a JavaScript fallback click strategy.

- **Language Switching:** The automation locates and clicks the `EN` button to switch the application language from Vietnamese to English.

- **Flutter Semantics Support:** Since the application is built using Flutter Web, all interactions and validations rely on `flt-semantics` accessibility nodes.

- **Result Validation:** Test results are verified by examining semantic text rendered by Flutter after each operation.

## 4.2 Test Cases Summary

| Test ID | Scenario | Description | Status |
|----------|----------|-------------|---------|
| TC-11 | Logout Success | Logout from the system and verify that the application returns to the login screen. | PASS |
| TC-12 | Switch Language to English | Change the application language to English and verify that English interface text is displayed. | PASS |

## 4.3 Validation Logic

### TC-11: Logout Success

- Login using a valid account.
- Locate the `Đăng xuất` button.
- Attempt logout using the helper function.
- If helper execution fails, perform logout using JavaScript click fallback.
- Wait for the login screen to reappear.
- Verify that either the `Đăng nhập` button or the `Email` input field is visible.

### TC-12: Switch Language to English

- Login using a valid account.
- Click the `EN` language button.
- Wait for the interface to refresh.
- Collect semantic text from Flutter nodes.
- Verify that at least one English keyword appears, such as:
  - `Logout`
  - `Borrow`
  - `Search`
  - `Library`
  - `Book`
  - `Account`
  - `Sign In`
  - `Email`
  - `Password`

## 4.4 Notes

- The module includes multiple fallback mechanisms to improve reliability when interacting with Flutter Web components.

- JavaScript click automation is used as a backup strategy when Playwright semantic interactions are unsuccessful.

- All assertions are performed through Flutter semantic content (`flt-semantics`).

- This module focuses on general application functionality rather than borrowing operations.

---
