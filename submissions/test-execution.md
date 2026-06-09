# Test Execution — Kết quả thực thi kiểm thử

> **Hướng dẫn**: Chạy từng TC trên hệ thống https://stqa.rbc.vn, ghi lại kết quả thực tế.
> Kết luận: **Pass** (kết quả đúng), **Fail** (kết quả sai → tạo bug report), **Blocked** (không thực hiện được vì lỗi khác chặn), **Not Run** (chưa chạy).

| Thông tin | |
|---|---|
| **Nhóm** | Group 24 |
| **Ngày thực thi** | 19/05/2026 |
| **Trình duyệt** | Google Chrome |
| **Hệ điều hành** | Windows 11 |

---

## Kết quả chi tiết

### REQ-01: Login

| Mã TC | Nhóm chức năng | Kết quả mong đợi (tóm tắt) | Kết quả thực tế | Kết luận | Minh chứng | Bug |
|-------|---------------|---------------------------|-----------------|---------|-----------|----|
| TC-01 | Login | Redirected to the homepage successfully | Successfully redirected to the homepage and displayed username + role | Pass | ![Login Success Screen](./assets/REQ-01/Login-success.png) | - |
| TC-02 | Login | Displays error message: `Member not found`. | Displayed error message under the email input field: `Member not found`. | Pass | ![User Not Found](./assets/REQ-01/user-not-found.png) | - |
| TC-03 | Login | Displays error message: `Incorect password`. | Displayed error message under the email input field: `Mật khẩu không đúng`. | Pass | ![Incorrect Password](./assets/REQ-01/Incorrect-password.png) | - |
| TC-04 | Login | Displays error message: `Please enter email and password`. | Displayed error message under the email input field: `Please enter email and password`. | Pass | ![Blank Email and Pass](./assets/REQ-01/Blank-email-pass.png) | - |
| TC-05 | Login | Displays error message: `Please enter email and password`. | Displayed error message under the email input field: `Please enter email and password`. | Pass | ![Blank Email](./assets/REQ-01/Blank-email.png) | - |
| TC-06 | Login | Displays error message: `Please enter email and password`. | Displayed error message under the email input field: `Please enter email and password`. | Pass | ![Blank Password](./assets/REQ-01/Blank-pass.png) | - |
| TC-07 | Login | Displays error message: `Member not found`. | Displayed error message under the email input field: `Member not found`. | Pass | ![Wrong Email and Password](./assets/REQ-01/Wrong-Email-Pass.png) | - |

### REQ-04: Borrow Book

| Mã TC | Nhóm chức năng | Kết quả mong đợi (tóm tắt) | Kết quả thực tế | Kết luận | Minh chứng | Bug |
|-------|---------------|---------------------------|-----------------|---------|-----------|----|
| TC-08 | Borrow Book | Successful book borrowing with correct status transition and 14-day loan period calculation. | - The member borrowed BOOK001 successfully.<br>- Book status transitioned to `Borrowed`.<br>- A 14-day loan period was added from the borrow date.<br>- The system displayed `Book borrowed successfully!`. | Pass | ![](./assets/REQ-04/08-1.png)<br>![](./assets/REQ-04/08-2.png)<br>![](./assets/REQ-04/08-3.png)<br>![](./assets/REQ-04/08-4.png) | - |
| TC-09 | Borrow Book | The system denies the borrowing request if the book is unavailable. | The system displayed a disabled button labeled `Borrowed` next to BOOK003, preventing the user from triggering a borrowing request. | Pass | ![](./assets/REQ-04/09-1.png) | - |
| TC-10 | Borrow Book | The system denies the borrowing request if the book is lost. | The system displayed a disabled button labeled `Lost` next to BOOK007, preventing the user from triggering a borrowing request. | Pass | ![](./assets/REQ-04/10-1.png) | - |
| TC-11 | Borrow Book | The system denies the borrowing request if the member status is suspended. | The system displayed a red error banner: `Member membership has expired. Cannot borrow books.` instead of a suspended-member message. | Fail | ![](./assets/REQ-04/11-1.png)<br>![](./assets/REQ-04/11-2.png)<br>![](./assets/REQ-04/11-3.png) | BUG-01 |
| TC-12 | Borrow Book | The system denies the borrowing request if the member status is expired. | The system displayed a red error banner: `Member membership has expired. Cannot borrow books.` | Pass | ![](./assets/REQ-04/12-1.png)<br>![](./assets/REQ-04/12-2.png)<br>![](./assets/REQ-04/12-3.png) | - |
| TC-13 | Borrow Book | The system denies the borrowing request because the member has already reached the maximum limit of 3 borrowed books. | The system allowed the borrowing transaction and displayed `Book borrowed successfully!`. | Fail | ![](./assets/REQ-04/13-1.png)<br>![](./assets/REQ-04/13-2.png)<br>![](./assets/REQ-04/13-3.png)<br>![](./assets/REQ-04/13-4.png)<br>![](./assets/REQ-04/13-5.png) | BUG-02 |

### REQ-02: View Book List

| Mã TC | Nhóm chức năng | Kết quả mong đợi (tóm tắt) | Kết quả thực tế | Kết luận | Minh chứng | Bug |
|-------|---------------|---------------------------|-----------------|---------|-----------|----|
| TC-14 | View Book List | The user can view the book list with complete book information. | After logging in as `ba.nguyen@email.com`, the Books tab displayed the book list. Each visible book showed title, author, category, publication year, and status. | Pass | ![TC-14 member view book list](./assets/REQ-02/TC-14-member-view-book-list.png) | - |
| TC-15 | View Book List | Books with different initial statuses are displayed correctly. | BOOK001 was displayed as `Available`, BOOK003 was displayed as `Borrowed`, and BOOK007 was displayed as `Lost`. | Pass | ![TC-15 status available borrowed](./assets/REQ-02/TC-15-status-available-borrowed.png)<br>![TC-15 status lost](./assets/REQ-02/TC-15-status-lost.png) | - |
| TC-16 | View Book List | Book status updates immediately after returning a borrowed book. | After logging in as MEM006 and returning BOOK013 from BR003, the system displayed `Book returned successfully.` Then BOOK013 changed back to `Available` in the Books tab. | Pass | ![TC-16 return BOOK013 success](./assets/REQ-02/TC-16-return-book013-success.png)<br>![TC-16 BOOK013 available after return](./assets/REQ-02/TC-16-book013-available-after-return.png) | - |

### REQ-03: Search and Filter Books

| Mã TC | Nhóm chức năng | Kết quả mong đợi (tóm tắt) | Kết quả thực tế | Kết luận | Minh chứng | Bug |
|-------|---------------|---------------------------|-----------------|---------|-----------|----|
| TC-17 | Search and Filter Books | Searching by book title displays the matching book. | Searching `Flutter` displayed BOOK001 — `Lập trình Flutter cơ bản`. | Pass | ![TC-17 search title Flutter](./assets/REQ-03/TC-17-search-title-flutter.png) | - |
| TC-18 | Search and Filter Books | Searching by author displays matching books. | Searching `Nguyễn Minh Đức` displayed BOOK001 and BOOK009, both written by Nguyễn Minh Đức. | Pass | ![TC-18 search author Nguyen Minh Duc](./assets/REQ-03/TC-18-search-author-nguyen-minh-duc.png) | - |
| TC-19 | Search and Filter Books | Search is case-insensitive for lowercase keyword. | Searching lowercase `flutter` still displayed BOOK001 — `Lập trình Flutter cơ bản`. | Pass | ![TC-19 search lowercase flutter](./assets/REQ-03/TC-19-search-lowercase-flutter.png) | - |
| TC-20 | Search and Filter Books | Search is case-insensitive for uppercase keyword. | Searching uppercase `FLUTTER` still displayed BOOK001 — `Lập trình Flutter cơ bản`. | Pass | ![TC-20 search uppercase FLUTTER](./assets/REQ-03/TC-20-search-uppercase-flutter.png) | - |
| TC-21 | Search and Filter Books | Searching with no matching result shows no-result message. | Searching `xyz_khong_ton_tai` displayed no books and showed `Không tìm thấy sách nào.` | Pass | ![TC-21 search no result](./assets/REQ-03/TC-21-search-no-result.png) | - |
| TC-22 | Search and Filter Books | Filtering by `Công nghệ` displays only Technology books. | Filtering by `Công nghệ` displayed books in the Technology category, such as BOOK001, BOOK002, BOOK003, BOOK005, and BOOK008. | Pass | ![TC-22 filter Cong nghe](./assets/REQ-03/TC-22-filter-cong-nghe.png) | - |
| TC-23 | Search and Filter Books | Filtering by lowercase `công nghệ` should still display books in the `Công nghệ` category. | After entering lowercase `công nghệ`, the system displayed `Không tìm thấy sách nào.` instead of showing Technology books. | Fail | ![TC-23 lowercase category filter no result](./assets/REQ-03/TC-23-filter-lowercase-cong-nghe-no-result.png) | BUG-03 |

### REQ-05: Return Book

| Mã TC | Nhóm chức năng | Kết quả mong đợi (tóm tắt) | Kết quả thực tế | Kết luận | Minh chứng | Bug |
|-------|---------------|---------------------------|-----------------|---------|-----------|----|
| TC-24 | Return Book | A member can return their own currently borrowed book. | After logging in as MEM006 and returning BR003 for BOOK013, the system displayed `Book returned successfully.` BOOK013 then changed back to `Available` in the Books tab. | Pass | ![TC-24 return BR003 success](./assets/REQ-05/TC-24-return-br003-success.png)<br>![TC-24 BOOK013 available after return](./assets/REQ-05/TC-24-book013-available-after-return.png) | - |
| TC-25 | Return Book | Returning an overdue book displays an overdue warning. | BR001 was overdue with due date 15/09/2024. After returning BR001, the system only displayed `Book returned successfully.` and did not display any overdue warning. BOOK003 changed back to `Available`. | Fail | ![TC-25 before returning overdue BR001](./assets/REQ-05/TC-25-before-return-overdue-br001.png)<br>![TC-25 after returning overdue BR001 without warning](./assets/REQ-05/TC-25-after-return-overdue-br001-no-warning.png)<br>![TC-25 BOOK003 available after return](./assets/REQ-05/TC-25-book003-available-after-return.png) | BUG-04 |
| TC-26 | Return Book / Borrow Record Lookup | A member must not be able to view or return another member’s borrowed book. | MEM002 searched for MEM006 and the system displayed BR003 of MEM006 with a **Return Book** button. After clicking it, the system displayed `Book returned successfully.` and BR003 changed to `Returned`. | Fail | ![TC-26 member views other record BR003](./assets/REQ-05/TC-26-member-view-other-record-br003.png)<br>![TC-26 member returns other record successfully](./assets/REQ-05/TC-26-member-return-other-record-success.png) | BUG-05 |
| TC-27 | Return Book | An already returned record cannot be returned again. | BR004 was displayed with status `Returned`, and no **Return Book** button was available for BR004. | Pass | ![TC-27 returned record BR004 no return button](./assets/REQ-05/TC-27-returned-record-br004-no-return-button.png) | - |

### REQ-06: Overdue Handling

| Mã TC | Nhóm chức năng | Kết quả mong đợi (tóm tắt) | Kết quả thực tế | Kết luận | Minh chứng | Bug |
|-------|---------------|---------------------------|-----------------|---------|-----------|----|
| TC-28 | Overdue Handling | The librarian can trigger overdue checking. | After the librarian clicked **Kiểm tra sách quá hạn**, the system displayed ` Updated: 2 overdue borrow records.` and marked overdue records. | Pass | ![TC-28 overdue check success](./assets/REQ-06/TC-28-check-overdue-success.png) | - |
| TC-29 | Overdue Handling | Overdue borrow records are marked as `Overdue`. | Before overdue checking, BR001 and BR003 were still active borrowed records. After clicking **Check Overdue Books**, BR001 and BR003 were marked as `Overdue`. | Pass | ![TC-29 before overdue check](./assets/REQ-06/TC-29-before-overdue-check.png)<br>![TC-29 after overdue check](./assets/REQ-06/TC-29-after-overdue-check.png) | - |
| TC-30 | Overdue Handling | A normal member cannot trigger overdue checking. | After logging in as a normal member, the **Check Overdue** function was not available in the Borrow / Return tab. | Pass | ![TC-30 member no check overdue](./assets/REQ-06/TC-30-member-no-check-overdue.png) | - |
| TC-31 | Overdue Handling | A member can view their own overdue record after overdue checking. | After the librarian performed overdue checking, MEM002 could view their own BR001 marked as `Overdue`. | Pass | ![TC-31 librarian check overdue](./assets/REQ-06/TC-31-librarian-check-overdue.png)<br>![TC-31 member own overdue record](./assets/REQ-06/TC-31-member-own-overdue-record.png) | - |

### REQ-07: Member Management

| Mã TC | Nhóm chức năng | Kết quả mong đợi (tóm tắt) | Kết quả thực tế | Kết luận | Minh chứng | Bug |
|-------|---------------|---------------------------|-----------------|---------|-----------|----|
| TC-32 | Member Management | The librarian can add a new member with valid email format `user@domain.com`. | After entering full name, phone number, and valid email `user@domain.com`, the system displayed `Invalid email.` and did not create the new member. | Fail | ![TC-32 valid email rejected](./assets/REQ-07/TC-32-valid-email-rejected.png) | BUG-06 |
| TC-33 | Member Management | A normal member cannot access member management. | After logging in as a normal member, the interface did not show the **Members** tab or the **Add Member** function. | Pass | ![TC-33 member no member management](./assets/REQ-07/TC-33-member-no-member-management.png) | - |
| TC-34 | Member Management | The system rejects adding a new member when required fields are missing. | After leaving the full name field blank and entering the remaining information, the system blocked the new member creation and displayed `Full name cannot be empty.` | Pass | ![TC-34 missing required field blocked](./assets/REQ-07/TC-34-missing-required-field-blocked.png) | - |
| TC-35 | Member Management | The system rejects an existing email with a duplicate email error. | After entering existing email `ba.nguyen@email.com`, the system displayed `Invalid email.` instead of an email duplication error. | Fail | ![TC-35 existing email input](./assets/REQ-07/TC-35-existing-email-input.png)<br>![TC-35 existing email wrong error](./assets/REQ-07/TC-35-existing-email-wrong-error.png) | BUG-07 |

### REQ-08: Borrow Record Lookup

| Mã TC | Nhóm chức năng | Kết quả mong đợi (tóm tắt) | Kết quả thực tế | Kết luận | Minh chứng | Bug |
|-------|---------------|---------------------------|-----------------|---------|-----------|----|
| TC-36 | Borrow Record Lookup | A member can view only their own borrow records. | After logging in as MEM002, the system displayed BR001 and BR004, which belong to MEM002. No records of other members were shown in the **My Borrow Records** tab. | Pass | ![TC-36 member own borrow records](./assets/REQ-08/TC-36-member-own-borrow-records.png) | - |
| TC-37 | Borrow Record Lookup | The librarian can view all borrow records. | After logging in as the librarian, the system displayed borrow records of multiple members, including BR001, BR002, BR003, BR004, and BR005. | Pass | ![TC-37 librarian all records top](./assets/REQ-08/TC-37-librarian-all-records-top.png)<br>![TC-37 librarian all records bottom](./assets/REQ-08/TC-37-librarian-all-records-bottom.png) | - |
| TC-38 | Borrow Record Lookup | A member must not be able to look up another member’s borrow records. | After logging in as MEM002 and searching for `MEM006`, the system displayed BR003 of MEM006. The record also showed the **Return Book** button. | Fail | ![TC-38 member lookup other member record](./assets/REQ-08/TC-38-member-lookup-other-member-record.png) | BUG-05 |
| TC-39 | Borrow Record Lookup | Borrow records display all required fields. | BR001 displayed the required information, including record ID, borrowed book, borrow date, due date, and status. | Pass | ![TC-39 borrow record required fields](./assets/REQ-08/TC-39-borrow-record-required-fields.png) | - |

---

## Tổng hợp kết quả

| Chỉ số | Giá trị |
|--------|---------|
| Tổng số test case | 39 |
| Pass | 30 |
| Fail | 9 |
| Blocked | 0 |
| Not Run | 0 |
| **Tỷ lệ Pass** | 76.92% |

### Kết quả theo nhóm chức năng

| Nhóm | Tổng TC | Pass | Fail | Tỷ lệ Pass |
|------|---------|------|------|------------|
| Login | 7 | 7 | 0 | 100% |
| Borrow Book | 6 | 4 | 2 | 66.67% |
| View Book List | 3 | 3 | 0 | 100% |
| Search and Filter Books | 7 | 6 | 1 | 85.71% |
| Return Book | 4 | 2 | 2 | 50% |
| Overdue Handling | 4 | 4 | 0 | 100% |
| Member Management | 4 | 1 | 3 | 25% |
| Borrow Record Lookup | 4 | 3 | 1 | 75% |
| **Tổng** | **39** | **30** | **9** | **76.92%** |