# Test Summary — Báo cáo tổng hợp kiểm thử

> **Hướng dẫn**: Đây là hoạt động **Quality Assurance** — nhóm đánh giá chất lượng tổng thể của phần mềm, không chỉ liệt kê lỗi.

---

## 1. Thông tin nhóm

| Mục | Thông tin |
|-----|----------|
| **Nhóm** | Group 24 |
| **Lớp** | ICT |
| **Ngày báo cáo** | 07/06/2026 |
| **Hệ thống kiểm thử** | https://stqa.rbc.vn — v1.0 |

---

## 2. Tổng quan kết quả

| Chỉ số | Giá trị |
|--------|---------|
| Tổng số test case | 39 |
| Pass | 30 |
| Fail | 9 |
| Blocked | 0 |
| Not Run | 0 |
| **Tỷ lệ Pass** | 76.92% |
| **Số bug phát hiện** | 8 |

### Phân bổ theo nhóm chức năng

| Nhóm chức năng | TC | Pass | Fail | Bug | Đánh giá |
|---------------|-----|------|------|-----|---------|
| Login | 7 | 7 | 0 | 0 | Stable. Login works correctly for valid, invalid, and empty input cases. |
| Borrow Book | 6 | 4 | 2 | 2 | Partially stable. Basic borrow restrictions work, but important business rules are violated. |
| View Book List | 3 | 3 | 0 | 0 | Stable. Book information and book status are displayed correctly. |
| Search and Filter Books | 7 | 6 | 1 | 1 | Mostly stable. Search works correctly, but category filtering has a case-sensitivity issue. |
| Return Book | 4 | 2 | 2 | 2 | Needs improvement. The system misses overdue warning and has an access control problem. |
| Overdue Handling | 4 | 4 | 0 | 0 | Stable. The overdue checking function works correctly for tested cases. |
| Member Management | 4 | 1 | 3 | 3 | Weak. Email validation and duplicate email handling have several issues. |
| Borrow Record Lookup | 4 | 3 | 1 | 1 | Mostly stable, but member access control is not properly enforced. |

### Phân bổ bug theo mức độ

| Mức độ | Số lượng | Bug IDs |
|--------|---------|---------|
| High | 2 | BUG-02, BUG-05 |
| Medium | 6 | BUG-01, BUG-03, BUG-04, BUG-06, BUG-07, BUG-08 |
| Low | 0 | - |

---

## 3. Kỹ thuật thiết kế đã sử dụng

| Kỹ thuật | Áp dụng cho REQ nào? | Số TC sử dụng | Giải thích cách áp dụng |
|----------|---------------------|---------------|------------------------|
| Equivalence Partitioning (EP) | REQ-01, REQ-02, REQ-03, REQ-04, REQ-05, REQ-07, REQ-08 | 25 | EP was used to divide inputs into valid and invalid partitions, such as valid/invalid login fields, available/borrowed/lost books, valid/invalid email formats, own/other borrow records, and existing/non-existing search keywords. |
| Boundary Value Analysis (BVA) | REQ-04, REQ-05, REQ-06 | 5 | BVA was used for boundary-related rules, such as the maximum limit of 3 borrowed books, overdue due dates, and records whose due date is less than or equal to the current date. |
| Decision Table | REQ-01, REQ-04, REQ-05, REQ-06, REQ-07, REQ-08 | 13 | Decision Table was used for rules that depend on multiple conditions, such as login email/password combinations, book status, member status, user role, and borrow record ownership. |

---

## 4. Phân tích chất lượng phần mềm

### 4.1. Điểm mạnh

- The login function is reliable. All login test cases passed, including valid login, wrong email, wrong password, empty email, empty password, and combined invalid input.
- The book list function works well. The system displays book information and book status correctly.
- The search function works correctly for title, author, lowercase keyword, uppercase keyword, and no-result cases.
- The overdue checking function works correctly when triggered by the librarian. The system updates overdue records and prevents normal members from accessing the overdue checking function.
- Basic borrow and return flows work in normal cases, such as borrowing an available book and returning the member’s own borrowed book.

### 4.2. Điểm yếu

- The system has a serious access control issue. A member can view and return another member’s borrow record. This affects both Return Book and Borrow Record Lookup.
- The borrowing limit rule is not enforced correctly. A member who already has 3 active borrowed books can still borrow another book.
- Member Management has several email validation problems. The system rejects a valid email, accepts an invalid email, and displays the wrong message for duplicate email.
- The system does not display an overdue warning when an overdue book is returned.
- Category filtering is case-sensitive, so valid lowercase category input may return no result.
- Some error messages are misleading, especially the suspended-member case where the system displays an expired-member message.

---

## 5. Đề xuất ưu tiên sửa lỗi

> Tiêu chí ưu tiên: nhóm ưu tiên sửa các lỗi có mức độ nghiêm trọng cao trước, đặc biệt là lỗi ảnh hưởng đến quyền truy cập dữ liệu, quy tắc nghiệp vụ chính và tính đúng đắn của dữ liệu.

| Thứ tự | Bug | Mức độ | Lý do ưu tiên |
|--------|-----|--------|---------------|
| 1 | BUG-05 | High | This is the most serious issue because a member can view and return another member’s borrowed book. It violates access control and can modify another user’s data. |
| 2 | BUG-02 | High | The system allows a member to exceed the maximum borrowing limit of 3 books, which violates a core borrowing rule and affects inventory control. |
| 3 | BUG-06 | Medium | The librarian cannot add a new member with a valid email format, which blocks a normal member management workflow. |
| 4 | BUG-07 | Medium | The system accepts invalid email data, which reduces data quality and violates the email validation rule. |
| 5 | BUG-08 | Medium | The system displays the wrong error message for duplicate email, which can confuse the librarian and make the issue harder to correct. |
| 6 | BUG-04 | Medium | The system does not warn users when an overdue book is returned, which violates the overdue return requirement. |
| 7 | BUG-03 | Medium | Category filtering fails for lowercase input, reducing usability of the search/filter function. |
| 8 | BUG-01 | Medium | The system blocks suspended members correctly, but displays the wrong reason. This should be fixed to avoid confusion between suspended and expired accounts. |

---

## 6. Kết luận

Overall, the system is **not ready for release**.

Although several basic functions work correctly, such as login, viewing the book list, searching books, checking overdue records, and basic borrow/return flows, the system still contains important defects. The most serious problems are related to access control, borrowing limit enforcement, and member email validation.

The system should not be released until the high-severity issues are fixed, especially BUG-05 and BUG-02. After fixing these bugs, the team should rerun the related test cases and perform regression testing on Borrow Book, Return Book, Borrow Record Lookup, and Member Management.

---

## 7. Bài học rút ra

- Test cases should be designed directly from the SRS because the SRS is the main source of truth for expected results.
- Negative test cases are important because many serious bugs were found in invalid or restricted scenarios.
- Access control must be tested carefully, especially when the system has different roles such as librarian and member.
- Combining EP, BVA, and Decision Table helps cover different types of rules, such as input validation, boundary conditions, and role-based decisions.
- Screenshots and clear evidence make bug reports easier to understand and verify.

---

## 8. Khai báo sử dụng AI

| Công cụ AI | Dùng cho phần nào | Bạn đã kiểm tra/chỉnh sửa thế nào |
|------------|-------------------|-----------------------------------|
| ChatGPT | Support writing and improving test cases, test execution, bug reports, and summary. | The group reviewed the generated content, compared it with the SRS, checked it against actual screenshots and execution results, and manually edited the final files before submission. |