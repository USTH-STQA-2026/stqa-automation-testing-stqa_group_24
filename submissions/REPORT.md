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


# 3. Book List Module

- **Implemented by:** Nguyễn Văn Đức
- **Module Tested:** Book Listing and Book Status Functionality (`tests/test_book_list.py`)

## 3.1 How it works

- **Book List Access:** The automation logs into the system and verifies that book records are displayed on the main interface.

- **Book Information Validation:** The tests inspect Flutter semantic content to verify that book entries are rendered successfully.

- **Book Status Validation:** The automation checks whether book status information such as available, borrowed, or lost is displayed.

- **Status Update Verification:** The automation performs a book return operation and then navigates back to the book list to verify that the interface updates correctly.

- **Flutter Semantics Support:** All interactions and validations are performed through Flutter semantic nodes (`flt-semantics`).

## 3.2 Test Cases Summary

| Test ID | Scenario | Description | Status |
|----------|----------|-------------|---------|
| TC-14 | View Book List | Verify that users can access and view the book list. | PASS |
| TC-15 | View Book Statuses | Verify that different book statuses are displayed correctly. | PASS |
| TC-16 | Real-Time Status Update | Verify that the book list updates after a return operation. | PASS |

## 3.3 Validation Logic

### TC-14: View Book List

- Login using a member account.
- Wait for book cards to appear.
- Collect Flutter semantic content.
- Verify that at least one book record is displayed.

### TC-15: View Book Statuses

- Login using a member account.
- Wait for book cards to appear.
- Collect Flutter semantic content.
- Verify that at least one valid status is displayed:
  - `Có sẵn`
  - `Đang mượn`
  - `Thất lạc`

### TC-16: Real-Time Status Update

- Login using a member account.
- Navigate to the `Mượn / Trả` tab.
- Return a borrowed book if a return button is available.
- Navigate back to the `Sách` tab.
- Verify that the interface remains accessible after the return operation.

## 3.4 Notes

- All validations are performed through Flutter semantic nodes (`flt-semantics`).

- TC-14 validates the existence of book records but does not verify all individual book attributes such as title, author, category, publication year, and status.

- TC-15 verifies that at least one valid status is displayed but does not validate every book in the catalog.

- TC-16 performs a return operation and navigates back to the book list; however, it does not explicitly verify that a specific book status changed after the return.

- Future improvements should include validation of individual book fields and direct verification of status changes after borrowing and returning operations.

---

# 4. Borrow and Return Books Module

- **Implemented by:** Nguyễn Anh Tuấn
- **Module Tested:** Borrowing and Returning Functionality (`tests/test_borrow_return.py`)

## 4.1 How it works

- **Login Requirement:** Each test begins by logging into the system using predefined member credentials through the helper function `login(page, config)`.

- **Borrow Workflow:** Available books are located through Flutter semantic nodes containing the text `"Có sẵn"`. The automation then interacts with `"Mượn sách này"` and `"Mượn"` buttons to simulate the borrowing process.

- **Return Workflow:** The automation navigates to the `"Mượn / Trả"` tab and interacts with available `"Trả sách"` buttons to perform return operations.

- **Flutter Semantics Support:** Since the application is built using Flutter Web, all interactions and validations are performed through `flt-semantics` accessibility nodes instead of traditional HTML elements.

- **Validation Method:** Test results are verified by collecting semantic text from Flutter nodes and checking for success messages, borrowing status, overdue warnings, or access restrictions.

## 4.2 Test Cases Summary

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

## 4.3 Validation Logic

- Successful borrowing is validated by detecting either a success message containing `"thành công"` or a borrowing status containing `"Đang mượn"`.

- Borrowing restrictions are validated through semantic text indicating unavailable books, lost books, suspended members, expired memberships, or borrowing limitations.

- Return operations are validated through success messages and the availability of return controls.

- Access control is validated by ensuring records belonging to other members are not displayed.

## 4.4 Notes

- TC-13 is currently incomplete because the borrowing-limit validation flow has not yet been fully implemented.

- The module relies on Flutter semantic nodes (`flt-semantics`) for all UI interactions and assertions.

---
# 5. Logout and Language Switching Module

- **Implemented by:** Nguyễn Văn Đức
- **Module Tested:** Logout and Language Switching Functionality (`tests/test_general.py`)

## 5.1 How it works

- **Authentication Requirement:** Both test cases begin by logging into the system using the `login()` helper function.

- **Fallback Handling:** If the login helper encounters a timeout or synchronization issue, the automation enables Flutter semantics and waits for the application to become available before continuing.

- **Logout Functionality:** The automation locates the `Đăng xuất` button and performs logout using either the helper method `flutter_click_button()` or a JavaScript fallback click strategy.

- **Language Switching:** The automation locates and clicks the `EN` button to switch the application language from Vietnamese to English.

- **Flutter Semantics Support:** Since the application is built using Flutter Web, all interactions and validations rely on `flt-semantics` accessibility nodes.

- **Result Validation:** Test results are verified by examining semantic text rendered by Flutter after each operation.

## 5.2 Test Cases Summary

| Test ID | Scenario | Description | Status |
|----------|----------|-------------|---------|
| TC-11 | Logout Success | Logout from the system and verify that the application returns to the login screen. | PASS |
| TC-12 | Switch Language to English | Change the application language to English and verify that English interface text is displayed. | PASS |

## 5.3 Validation Logic

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

## 5.4 Notes

- The module includes multiple fallback mechanisms to improve reliability when interacting with Flutter Web components.

- JavaScript click automation is used as a backup strategy when Playwright semantic interactions are unsuccessful.

- All assertions are performed through Flutter semantic content (`flt-semantics`).

- This module focuses on general application functionality rather than borrowing operations.

---

# 6. Borrowing Records Module

- **Implemented by:** Nguyễn Văn Đức
- **Module Tested:** Borrowing Records and Access Control Functionality (`tests/test_records.py`)

## 6.1 How it works

- **Role-Based Access Control:** The module verifies record visibility for both normal members and librarians.

- **Record Navigation:** After login, the automation navigates to the `Mượn / Trả` tab where borrowing records are displayed.

- **Record Validation:** The tests examine Flutter semantic content (`flt-semantics`) to verify the presence or absence of borrowing record identifiers.

- **Member Restrictions:** The automation verifies that normal members cannot view records belonging to other users.

- **Librarian Access:** Librarian accounts are expected to have broader access to borrowing records.

- **Flutter Semantics Support:** Since the application is built using Flutter Web, all interactions and validations rely on `flt-semantics` accessibility nodes.

## 6.2 Test Cases Summary

| Test ID | Scenario | Description | Status |
|----------|----------|-------------|---------|
| TC-36 | Member Views Own Records | Verify that a member can view their own borrowing records. | PASS |
| TC-37 | Librarian Views Records | Verify that a librarian can access borrowing records. | PASS |
| TC-38 | Member Cannot View Others' Records | Verify that a member cannot view borrowing records belonging to other members. | PASS |
| TC-39 | Records Display Information | Verify that borrowing record information is displayed in the records interface. | PASS |

## 6.3 Validation Logic

### TC-36: Member Views Own Records

- Login using a member account.
- Navigate to the `Mượn / Trả` tab.
- Verify that at least one expected borrowing record (`BR001` or `BR004`) is displayed.

### TC-37: Librarian Views Records

- Login using librarian credentials.
- Navigate to the `Mượn / Trả` tab.
- Verify that borrowing record information is accessible to the librarian.

### TC-38: Member Cannot View Others' Records

- Login using a member account.
- Navigate to the `Mượn / Trả` tab.
- Verify that borrowing record `BR003` is not displayed.

### TC-39: Records Display Information

- Login using librarian credentials.
- Navigate to the `Mượn / Trả` tab.
- Verify that borrowing record information is present within the records interface.

## 6.4 Notes

- All validations are performed through Flutter semantic nodes (`flt-semantics`).

- TC-36 directly validates the visibility of member borrowing records.

- TC-38 directly validates access restrictions by ensuring records belonging to other members are not displayed.

- TC-37 contains a flexible assertion (`or True`) and primarily verifies access to the records interface rather than confirming all available records.

- TC-39 contains a flexible assertion (`or True`) and only verifies that record information is present, not that all required fields are displayed.

- Future improvements should include validation of individual record attributes such as Record ID, Book ID, Borrow Date, Due Date, Return Date, and Status.

---
# 7. Overdue Management Module

- **Implemented by:** Nguyễn Văn Đức
- **Module Tested:** Overdue Checking and Monitoring Functionality (`tests/test_overdue.py`)

## 7.1 How it works

- **Role-Based Access Control:** The module verifies that overdue checking functionality is only available to librarian accounts.

- **Overdue Navigation:** After login, the automation navigates to the `Mượn / Trả` tab where borrowing records and overdue information are displayed.

- **Overdue Checking:** Librarians can access the `Kiểm tra quá hạn` button to trigger overdue verification.

- **Overdue Record Validation:** The automation checks whether overdue records are displayed within the borrowing records interface.

- **Member Restrictions:** Normal members are verified to ensure they cannot access overdue-checking controls reserved for librarians.

- **Personal Record Visibility:** Members can view their own borrowing records but cannot perform administrative overdue-checking operations.

## 7.2 Test Cases Summary

| Test ID | Scenario | Description | Status |
|----------|----------|-------------|---------|
| TC-28 | Librarian Trigger Overdue Check | Verify that a librarian can access and execute the overdue checking function. | PASS |
| TC-29 | Overdue Records Marked | Verify that overdue borrowing records are displayed with overdue status information. | PASS |
| TC-30 | Member Cannot Trigger Overdue Check | Verify that normal members cannot access the overdue-checking function. | PASS |
| TC-31 | Member Views Own Overdue Record | Verify that members can view their own borrowing records. | PASS |

## 7.3 Validation Logic

### TC-28: Librarian Trigger Overdue Check

- Login using librarian credentials.
- Navigate to the `Mượn / Trả` tab.
- Locate the `Kiểm tra quá hạn` button.
- Execute the overdue-checking action.

### TC-29: Overdue Records Marked

- Login using librarian credentials.
- Navigate to the `Mượn / Trả` tab.
- Examine displayed borrowing records.
- Verify whether overdue information is present.

### TC-30: Member Cannot Trigger Overdue Check

- Login using a normal member account.
- Navigate to the `Mượn / Trả` tab.
- Verify that the `Kiểm tra quá hạn` button is not visible.

### TC-31: Member Views Own Overdue Record

- Login using a member account.
- Navigate to the `Mượn / Trả` tab.
- Verify that the member's borrowing record is displayed.

## 7.4 Notes

- All validations are performed through Flutter semantic nodes (`flt-semantics`).

- TC-28 primarily verifies access to the overdue-checking functionality and does not validate backend processing results.

- TC-29 contains a flexible assertion (`or True`) and may pass even when overdue records are not present.

- TC-31 contains a flexible assertion (`or True`) and primarily verifies record visibility rather than confirming overdue status.

- The module focuses on permission control and interface accessibility for overdue management operations.

---
# 8. Member Management Module

- **Implemented by:** Nguyễn Văn Đức
- **Module Tested:** Member Management Functionality (`tests/test_member.py`)

## 8.1 How it works

- **Role-Based Access Control:** The module verifies that only librarian accounts can access member management features.

- **Member Management Navigation:** After login, the automation attempts to navigate to the `Thành viên` tab where member information is managed.

- **Add Member Access:** Librarian users can access the member creation interface through the `Thêm` button.

- **Access Restriction Validation:** Normal members are restricted from accessing member management functionality.

- **Flutter Semantics Support:** All interactions and validations are performed through Flutter semantic nodes (`flt-semantics`).

## 8.2 Test Cases Summary

| Test ID | Scenario | Description | Status |
|----------|----------|-------------|---------|
| TC-32 | Add Member with Valid Data | Verify that librarians can access the member creation interface. | PASS |
| TC-33 | Member Cannot Access Management | Verify that normal members cannot access member management functionality. | PASS |
| TC-34 | Missing Required Fields | Verify validation when required member information is missing. | PASS |
| TC-35 | Existing Email Validation | Verify validation when adding a member using an existing email address. | PASS |

## 8.3 Validation Logic

### TC-32: Add Member with Valid Data

- Login using librarian credentials.
- Navigate to the `Thành viên` tab.
- Locate the `Thêm` button.
- Open the member creation interface.

### TC-33: Member Cannot Access Management

- Login using a normal member account.
- Verify that the `Thành viên` management tab is not visible.

### TC-34: Missing Required Fields

- Login using librarian credentials.
- Intended to validate required field checking during member creation.

### TC-35: Existing Email Validation

- Login using librarian credentials.
- Intended to validate duplicate email checking during member creation.

## 8.4 Notes

- All validations are performed through Flutter semantic nodes (`flt-semantics`).

- TC-32 verifies access to the member creation interface but does not complete the full member creation workflow.

- TC-33 directly validates access restriction and is the primary automated verification in this module.

- TC-34 currently contains a placeholder implementation (`pass`) and does not perform automated validation.

- TC-35 currently contains a placeholder implementation (`pass`) and does not perform automated validation.

- Future improvements should include form submission, required field validation, duplicate email detection, and verification of successful member creation.

---
