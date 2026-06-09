# Bug Reports — Báo cáo lỗi

> **Hướng dẫn**: Tạo 1 mục bug cho mỗi TC có kết quả **Fail**.
> Xem [examples/sample-bug-report.md](../examples/sample-bug-report.md) để hiểu cách viết bug report tốt.
> Mỗi bug cần: tiêu đề mô tả hành vi lỗi, bước tái hiện, expected vs actual, severity + giải thích.

| Information | |
|---|---|
| **Group** | GROUP 24 |
| **Report Date** | 06/06/2026 |

**Environment:**
- Browser: Google Chrome
- Operating System: Windows 11
- Interface Language: Vietnamese/English
---

## BUG-01: System displays "Expired" error message instead of "Suspended" message when a suspended member attempts to borrow a book.

| Thuộc tính | Chi tiết |
|-----------|---------|
| **Mã lỗi** | BUG-01 |
| **TC liên quan** | TC-11 |
| **REQ liên quan** | REQ-04 |
| **Mức độ** | Medium |
| **Người phát hiện** | Đoàn Quốc Việt |
| **Ngày phát hiện** | 27/05/2026 |
| **Trạng thái** | Open |

**Điều kiện tiên quyết:**
The suspended user is at the Books tab and the data is refreshed.

**Bước tái hiện:**
1. Log into the library application using a suspended member account (e.g., Account: cu.le@email.com / Member ID: MEM004).<br>
2. Navigate to the Books tab.<br>
3. Select any available book (e.g., BOOK001 - Lập trình Flutter cơ bản) and click the "Borrow" button.<br>
4. Confirm the transaction in the confirmation pop-up window.

**Kết quả mong đợi:**
The system denies the borrowing request and displays the exact error message indicating account suspension: "The member's account is currently suspended."

**Kết quả thực tế:**
The system successfully blocks the transaction but displays an incorrect red error banner at the bottom of the screen stating: "Thành viên đã hết hạn. Không thể mượn sách." (Member has expired. Cannot borrow book.)

**Tác động:**
Directly violates the explicit business rule in REQ-04 (suspended ≠ expired). This misleads both the library staff and the member regarding the true operational status of the account, causing confusion on how to resolve the restriction (e.g., attempting subscription renewal instead of lifting a penalty).

**Minh chứng:**
![prove](./assets/REQ-04/11-3.png)

**Đề xuất xử lý:**
Update the backend verification logic or localization mapping for business rule constraints. Ensure that when checking member status, an account matching the Suspended flag triggers its dedicated warning string block instead of routing to the Expired message block.

---

## BUG-02: System allows a member who already has 3 borrowed books to borrow a 4th book.

| Thuộc tính | Chi tiết |
|-----------|---------|
| **Mã lỗi** | BUG-02 |
| **TC liên quan** | TC-13 |
| **REQ liên quan** | REQ-04 |
| **Mức độ** | High |
| **Người phát hiện** | Đoàn Quốc Việt |
| **Ngày phát hiện** | 27/05/2026 |
| **Trạng thái** | Open |

**Điều kiện tiên quyết:**
The data is refreshed. The member account used in this test already has exactly 3 active borrowed books.

**Bước tái hiện:**
1. Log into the library application using a member account that already has 3 active borrowed books.<br>
2. Navigate to the Books tab.<br>
3. Select any available book, for example BOOK001 - Lập trình Flutter cơ bản.<br>
4. Click the "Borrow" button.<br>
5. Confirm the transaction in the confirmation pop-up window.

**Kết quả mong đợi:**
The system denies the borrowing request and displays an error message indicating that the member has reached the maximum borrowing limit of 3 books.

**Kết quả thực tế:**
The system allows the member to borrow one more book successfully and displays a success message.

**Tác động:**
This violates the explicit business rule in REQ-04 that a member can borrow a maximum of 3 books. The bug allows members to exceed the borrowing limit, which may affect book availability and library inventory control.

**Minh chứng:**
![prove 1](./assets/REQ-04/13-1.png)<br>
![prove 2](./assets/REQ-04/13-4.png)<br>
![prove 3](./assets/REQ-04/13-5.png)

**Đề xuất xử lý:**
Add a validation step before creating a new borrow record. If the member already has 3 active borrowed books, the system must block the transaction and display a clear maximum-limit error message.

---

## BUG-03: Category filter is case-sensitive and returns no results for lowercase category input.

| Thuộc tính | Chi tiết |
|-----------|---------|
| **Mã lỗi** | BUG-03 |
| **TC liên quan** | TC-23 |
| **REQ liên quan** | REQ-03 |
| **Mức độ** | Medium |
| **Người phát hiện** | Trần Quốc Việt |
| **Ngày phát hiện** | 07/06/2026 |
| **Trạng thái** | Open |

**Điều kiện tiên quyết:**
The data is refreshed. The user is logged in successfully and is currently at the Books tab.

**Bước tái hiện:**
1. Navigate to the Books tab.<br>
2. Enter `công nghệ` into the category filter field.<br>
3. Observe the displayed book list.

**Kết quả mong đợi:**
The system displays books in the `Công nghệ` category, such as BOOK001, BOOK002, BOOK003, BOOK005, and BOOK008.

**Kết quả thực tế:**
The system displays the message: `Không tìm thấy sách nào.`

**Tác động:**
Users may fail to find books even when they enter a valid category name, only because the input uses lowercase characters. This reduces the usability and reliability of the search/filter function.

**Minh chứng:**
![prove](./assets/REQ-03/TC-23-filter-lowercase-cong-nghe-no-result.png)

**Đề xuất xử lý:**
Normalize both the category input and stored category values before comparison. For example, convert both values to lowercase before filtering.

---

## BUG-04: The system does not display an overdue warning when an overdue book is returned.

| Thuộc tính | Chi tiết |
|-----------|---------|
| **Mã lỗi** | BUG-04 |
| **TC liên quan** | TC-25 |
| **REQ liên quan** | REQ-05 |
| **Mức độ** | Medium |
| **Người phát hiện** | Trần Quốc Việt |
| **Ngày phát hiện** | 07/06/2026 |
| **Trạng thái** | Open |

**Điều kiện tiên quyết:**
The data is refreshed. The user is logged in with member account `ba.nguyen@email.com`. BR001 exists in the initial data and has due date 15/09/2024.

**Bước tái hiện:**
1. Log into the library application using account `ba.nguyen@email.com`.<br>
2. Navigate to the Borrow / Return tab.<br>
3. Find borrow record BR001 for BOOK003 - Kiểm thử phần mềm nhập môn.<br>
4. Click the "Return Book" button.<br>
5. Observe the system message after returning the book.

**Kết quả mong đợi:**
The system allows the book to be returned and displays an overdue warning because BR001 is overdue.

**Kết quả thực tế:**
The system only displays the success message `Trả sách thành công.` and does not display any overdue warning.

**Tác động:**
This violates REQ-05 because the system must warn the user when an overdue book is returned. Without the warning, the user and librarian may not know that the book was returned late.

**Minh chứng:**
![prove 1](./assets/REQ-05/TC-25-before-return-overdue-br001.png)<br>
![prove 2](./assets/REQ-05/TC-25-after-return-overdue-br001-no-warning.png)<br>
![prove 3](./assets/REQ-05/TC-25-book003-available-after-return.png)

**Đề xuất xử lý:**
Add overdue checking logic during the return action. If the borrow record due date is earlier than or equal to the current date, the system should display an overdue warning.

---

## BUG-05: A member can view and return another member’s borrowed book.

| Thuộc tính | Chi tiết |
|-----------|---------|
| **Mã lỗi** | BUG-05 |
| **TC liên quan** | TC-26, TC-38 |
| **REQ liên quan** | REQ-05, REQ-08 |
| **Mức độ** | High |
| **Người phát hiện** | Trần Quốc Việt |
| **Ngày phát hiện** | 07/06/2026 |
| **Trạng thái** | Open |

**Điều kiện tiên quyết:**
The data is refreshed. The user is logged in with member account `ba.nguyen@email.com` / MEM002. BR003 belongs to MEM006, not MEM002.

**Bước tái hiện:**
1. Log into the library application using account `ba.nguyen@email.com`.<br>
2. Navigate to the Borrow / Return tab.<br>
3. Open the borrow record lookup area.<br>
4. Search for `MEM006`.<br>
5. Observe whether BR003 is displayed.<br>
6. If BR003 is displayed, click the "Return Book" button.<br>
7. Observe whether the return action is successful.

**Kết quả mong đợi:**
The system must not display BR003 to MEM002 because BR003 belongs to MEM006. MEM002 must not be able to return BOOK013 from another member’s borrow record.

**Kết quả thực tế:**
The system displays BR003 of MEM006 to MEM002. In TC-38, MEM002 can view the record through borrow record lookup. In TC-26, MEM002 can also return that record successfully.

**Tác động:**
This is a serious access control issue. It violates REQ-05 and REQ-08 because a member can access and modify borrow records that do not belong to them. This can cause incorrect borrow history and unauthorized changes to another member’s records.

**Minh chứng:**
![prove 1](./assets/REQ-05/TC-26-member-view-other-record-br003.png)<br>
![prove 2](./assets/REQ-05/TC-26-member-return-other-record-success.png)<br>
![prove 3](./assets/REQ-08/TC-38-member-lookup-other-member-record.png)

**Đề xuất xử lý:**
Restrict borrow record lookup and return actions for member accounts. A member should only be able to view and return borrow records whose member ID matches the currently logged-in user.

---

## BUG-06: The system rejects a valid email address when adding a new member.

| Thuộc tính | Chi tiết |
|-----------|---------|
| **Mã lỗi** | BUG-06 |
| **TC liên quan** | TC-32 |
| **REQ liên quan** | REQ-07 |
| **Mức độ** | Medium |
| **Người phát hiện** | Trần Quốc Việt |
| **Ngày phát hiện** | 07/06/2026 |
| **Trạng thái** | Open |

**Điều kiện tiên quyết:**
The data is refreshed. The user is logged in with the librarian account and is currently at the Add Member screen.

**Bước tái hiện:**
1. Log into the library application using account `librarian@library.com`.<br>
2. Navigate to the Members tab.<br>
3. Click the Add Member button.<br>
4. Enter a full name.<br>
5. Enter email `user@domain.com`.<br>
6. Enter a phone number.<br>
7. Click the "Add Member" button.

**Kết quả mong đợi:**
The system creates the new member successfully because `user@domain.com` is a valid email format. It contains `@` and has a dot `.` in the domain part.

**Kết quả thực tế:**
The system displays the error message `Email không hợp lệ.` and does not create the new member.

**Tác động:**
This blocks a valid member-management workflow. The librarian cannot add a member even when the email follows the valid format defined in REQ-07.

**Minh chứng:**
![prove](./assets/REQ-07/TC-32-valid-email-rejected.png)

**Đề xuất xử lý:**
Review the email validation logic. The system should accept emails in the format `user@domain.com`, because this format satisfies the SRS requirement.

---

## BUG-07: The system displays the wrong error message when adding a member with an existing email.

| Thuộc tính | Chi tiết |
|-----------|---------|
| **Mã lỗi** | BUG-07 |
| **TC liên quan** | TC-35 |
| **REQ liên quan** | REQ-07 |
| **Mức độ** | Medium |
| **Người phát hiện** | Trần Quốc Việt |
| **Ngày phát hiện** | 07/06/2026 |
| **Trạng thái** | Open |

**Điều kiện tiên quyết:**
The data is refreshed. The user is logged in with the librarian account. Email `ba.nguyen@email.com` already exists in the initial seed data.

**Bước tái hiện:**
1. Log into the library application using account `librarian@library.com`.<br>
2. Navigate to the Members tab.<br>
3. Click the Add Member button.<br>
4. Enter a full name.<br>
5. Enter existing email `ba.nguyen@email.com`.<br>
6. Enter a phone number.<br>
7. Click the "Add Member" button.

**Kết quả mong đợi:**
The system does not create the new member and displays an error message indicating that the email already exists or is duplicated.

**Kết quả thực tế:**
The system displays the error message `Email không hợp lệ.` instead of an email duplication error.

**Tác động:**
The error message is misleading. The librarian may think the email format is invalid, while the real issue is duplicate email. This reduces clarity and makes it harder for the user to correct the input.

**Minh chứng:**
![prove 1](./assets/REQ-07/TC-35-existing-email-input.png)<br>
![prove 2](./assets/REQ-07/TC-35-existing-email-wrong-error.png)

**Đề xuất xử lý:**
Validate the email format first, then check whether the email already exists. If the email is duplicated, the system should display a duplicate-email error instead of an invalid-email error.

---
