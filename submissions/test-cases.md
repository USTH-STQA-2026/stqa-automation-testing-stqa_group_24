# Test Cases — Bảng trường hợp kiểm thử

> **Hướng dẫn**: Viết tối thiểu **20 TC** phủ đủ các chức năng chính (REQ-01 → REQ-08).
> Xem [examples/sample-test-case.md](../examples/sample-test-case.md) để hiểu cách viết TC tốt.
> Tự tổ chức và phân nhóm test case theo cách hợp lý nhất.

| Thông tin | |
|---|---|
| **Nhóm** | Group 24 |
| **Ngày tạo** | 20/05/2026 |
| **Hệ thống** | https://stqa.rbc.vn |
| **Tham chiếu** | SRS v1.0 |

---

## Bước 1: Mô hình hóa miền đầu vào — Input Domain Modeling (IDM)

> 📖 **Textbook:** Chương 6 — *Input Domain Modeling*, Paul Ammann & Jeff Offutt.
>
> **Trước khi viết Test Case**, nhóm **phải** phân tích miền đầu vào bằng bảng IDM bên dưới.
> Mỗi chức năng cần xác định: **Đặc tính (Characteristic)**, **Phân vùng (Block/Partition)**, và **Giá trị đại diện (Value)**.

### IDM — Đăng nhập (REQ-01)

| Đặc tính (Characteristic) | Phân vùng (Block) | Giá trị đại diện (Value) | Kết quả mong đợi |
|---|---|---|---|
| Email có tồn tại trong DB? | Có | `librarian@library.com` | Đăng nhập thành công |
| | Không | `noone@email.com` | Thông báo lỗi |
| Mật khẩu có đúng? | Đúng | `admin123` | Đăng nhập thành công |
| | Sai | `wrongpass` | Thông báo lỗi |
| Ô nhập có rỗng? | Không rỗng | (giá trị bất kỳ) | Xử lý bình thường |
| | Rỗng | `""` | Thông báo "Vui lòng nhập..." |

### IDM — Xem danh sách sách / View Book List (REQ-02)

| Đặc tính (Characteristic) | Phân vùng (Block/Partition) | Giá trị đại diện (Value) | Kết quả mong đợi |
|---|---|---|---|
| Vai trò người dùng | Thủ thư | `librarian@library.com` / `admin123` | Thủ thư xem được danh sách sách |
| | Thành viên | `ba.nguyen@email.com` / `password123` | Thành viên xem được danh sách sách |
| Thông tin sách | Đầy đủ thông tin | BOOK001 | Hiển thị tên sách, tác giả, thể loại, năm xuất bản và trạng thái |
| Trạng thái sách | Có sẵn | BOOK001 | Sách hiển thị trạng thái `Có sẵn` |
| | Đã mượn | BOOK003 | Sách hiển thị trạng thái `Đã mượn` |
| | Thất lạc | BOOK007 | Sách hiển thị trạng thái `Thất lạc` |
| Cập nhật real-time | Sau khi trả sách | BOOK013 sau khi trả BR003 | Trạng thái sách đổi về `Có sẵn` ngay lập tức |

### IDM — Tìm kiếm sách (REQ-03)

| Đặc tính (Characteristic) | Phân vùng (Block) | Giá trị đại diện (Value) | Kết quả mong đợi |
|---|---|---|---|
| Từ khóa có tồn tại trong DB? | Có (tên sách) | `"Flutter"` | Hiển thị sách chứa "Flutter" |
| | Có (tên tác giả) | `"Nguyễn"` | Hiển thị sách của tác giả Nguyễn |
| | Không | `"XYZ123"` | Danh sách rỗng |
| Phân biệt HOA/thường? | Chữ thường | `"flutter"` | Kết quả giống "Flutter" |
| | Chữ HOA | `"FLUTTER"` | Kết quả giống "Flutter" |

### IDM — Mượn sách / Borrow Book (REQ-04)

| Đặc tính (Characteristic) | Phân vùng (Block) | Giá trị đại diện (Value) | Kết quả mong đợi |
|---|---|---|---|
| Trạng thái sách? | Có sẵn | BOOK001 | Cho phép mượn |
| | Đang mượn | BOOK003 | Không cho phép |
| | Thất lạc | BOOK007 | Không cho phép |
| Trạng thái thành viên? | Hoạt động | MEM002 | Cho phép mượn |
| | Tạm ngưng | MEM004 | Từ chối, thông báo lỗi |
| | Hết hạn | MEM005 | Từ chối, thông báo lỗi |
| Số sách đang mượn? | < 3 (BVA: 0, 1, 2) | MEM006 (0 sách) | Cho phép mượn |
| | = 3 (BVA: giới hạn) | MEM đã mượn 3 sách | Từ chối, thông báo vượt giới hạn |

### IDM — Trả sách / Return Book (REQ-05)

| Đặc tính (Characteristic) | Phân vùng (Block/Partition) | Giá trị đại diện (Value) | Kết quả mong đợi |
|---|---|---|---|
| Quyền sở hữu phiếu mượn | Phiếu của chính mình | MEM006 trả BR003 / BOOK013 | Cho phép trả sách |
| | Phiếu của người khác | MEM002 cố truy cập BR003 của MEM006 | Không cho xem hoặc trả sách |
| Trạng thái phiếu mượn | Đang mượn | BR003 / BOOK013 | Có thể trả sách |
| | Đã trả | BR004 / BOOK005 | Không được trả lại lần nữa |
| Thời điểm trả | Trả quá hạn | BR001 / BOOK003, hạn trả 15/09/2024 | Hiển thị cảnh báo quá hạn |
| Trạng thái sách sau khi trả | Sách đã được trả | BOOK013 | Sách chuyển về trạng thái `Có sẵn` |

### IDM — Xử lý quá hạn / Overdue Handling (REQ-06)

| Đặc tính (Characteristic) | Phân vùng (Block/Partition) | Giá trị đại diện (Value) | Kết quả mong đợi |
|---|---|---|---|
| Vai trò kích hoạt kiểm tra quá hạn | Thủ thư | `librarian@library.com` / `admin123` | Có thể nhấn nút kiểm tra quá hạn |
| | Thành viên thường | `ba.nguyen@email.com` / `password123` | Không thể kích hoạt kiểm tra quá hạn |
| Điều kiện ngày hết hạn | dueDate ≤ ngày hiện tại | BR001, hạn trả 15/09/2024 | Phiếu được đánh dấu `Quá hạn` |
| | dueDate ≤ ngày hiện tại | BR003, hạn trả 15/10/2024 | Phiếu được đánh dấu `Quá hạn` |
| Hiển thị phiếu quá hạn | Thủ thư xem | Tài khoản thủ thư | Thủ thư thấy tất cả phiếu quá hạn |
| | Thành viên xem | MEM002 xem BR001 | Thành viên thấy phiếu quá hạn của chính mình |

### IDM — Quản lý thành viên / Member Management (REQ-07)

| Đặc tính (Characteristic) | Phân vùng (Block/Partition) | Giá trị đại diện (Value) | Kết quả mong đợi |
|---|---|---|---|
| Vai trò truy cập quản lý thành viên | Thủ thư | `librarian@library.com` / `admin123` | Có thể truy cập chức năng thêm thành viên |
| | Thành viên thường | `ba.nguyen@email.com` / `password123` | Không thể truy cập chức năng quản lý thành viên |
| Định dạng email | Hợp lệ | `user@domain.com` | Tạo thành viên thành công |
| | Thiếu dấu chấm trong domain | `user@domain` | Từ chối vì email không hợp lệ |
| Tính duy nhất của email | Email đã tồn tại | `ba.nguyen@email.com` | Từ chối vì email bị trùng |

### IDM — Tra cứu phiếu mượn / Borrow Record Lookup (REQ-08)

| Đặc tính (Characteristic) | Phân vùng (Block/Partition) | Giá trị đại diện (Value) | Kết quả mong đợi |
|---|---|---|---|
| Vai trò xem phiếu mượn | Thủ thư | `librarian@library.com` / `admin123` | Thủ thư xem được tất cả phiếu mượn |
| | Thành viên | `ba.nguyen@email.com` / `password123` | Thành viên chỉ xem được phiếu của chính mình |
| Quyền sở hữu phiếu mượn | Phiếu của chính mình | MEM002 xem BR001 và BR004 | Hiển thị phiếu của MEM002 |
| | Phiếu của người khác | MEM002 cố xem BR003 của MEM006 | Không hiển thị BR003 cho MEM002 |
| Thông tin phiếu mượn | Đầy đủ thông tin | BR001 | Hiển thị mã phiếu, sách mượn, ngày mượn, ngày hết hạn và trạng thái |

> 💡 **Gợi ý kỹ thuật**: Sử dụng **Phân lớp tương đương (EP)** cho các phân vùng rời rạc, **Phân tích giá trị biên (BVA)** cho các phân vùng số hoặc điều kiện giới hạn, và **Bảng quyết định (Decision Table)** cho các luật kết hợp nhiều điều kiện như vai trò người dùng, trạng thái sách, trạng thái thành viên và quyền truy cập.

---

## Bước 2: Test Cases

<!-- Mỗi nhóm chức năng được tách thành một bảng riêng để dễ đọc và dễ truy vết theo REQ. -->

### REQ-01: Đăng nhập / Login

| Mã TC | Mục tiêu kiểm thử | Tiền điều kiện | Bước thực hiện | Dữ liệu đầu vào | Kết quả mong đợi | REQ | Kỹ thuật |
|-------|-------------------|---------------|---------------|-----------------|------------------|-----|---------|
| TC-01 | Test successful login with valid email and password | 1. User is on the login page.<br>2. Account already exists in the system. | 1. Enter a valid Email.<br>2. Enter a valid Password.<br>3. Click the "Login" button. | Email: `librarian@library.com`<br>Password: `admin123` | - Redirected to the homepage successfully.<br>- The AppBar accurately displays the username + role. | REQ-01 | Decision Table |
| TC-02 | Test error message when entering an unregistered Email | 1. User is on the login page. | 1. Enter a non-existent Email.<br>2. Enter any Password.<br>3. Click the "Login" button. | Email: `nobody@test.com`<br>Password: `anything` | Displays error message: `Không tìm thấy thành viên`. | REQ-01 | Decision Table |
| TC-03 | Test error message when entering a correct Email but incorrect Password | 1. User is on the login page.<br>2. Email already exists in the system. | 1. Enter the correct Email.<br>2. Enter an incorrect Password.<br>3. Click the "Login" button. | Email: `ba.nguyen@email.com`<br>Password: `wrongpassword` | Displays error message: `Mật khẩu không đúng`. | REQ-01 | Decision Table |
| TC-04 | Test error message when leaving both Email and Password blank | 1. User is on the login page. | 1. Leave the Email field blank.<br>2. Leave the Password field blank.<br>3. Click the "Login" button. | Email: blank<br>Password: blank | Displays error message: `Vui lòng nhập email và mật khẩu`. | REQ-01 | Decision Table |
| TC-05 | Test error message when entering only Password and leaving Email blank | 1. User is on the login page. | 1. Leave the Email field blank.<br>2. Enter any Password.<br>3. Click the "Login" button. | Email: blank<br>Password: `anything` | Displays error message: `Vui lòng nhập email và mật khẩu`. | REQ-01 | EP |
| TC-06 | Test error message when entering only Email and leaving Password blank | 1. User is on the login page. | 1. Enter a valid Email.<br>2. Leave the Password field blank.<br>3. Click the "Login" button. | Email: `librarian@library.com`<br>Password: blank | Displays error message: `Vui lòng nhập email và mật khẩu`. | REQ-01 | EP |
| TC-07 | Test error message when entering both an incorrect Email and incorrect Password | 1. User is on the login page. | 1. Enter a non-existent Email.<br>2. Enter an incorrect Password.<br>3. Click the "Login" button. | Email: `nobody@test.com`<br>Password: `wrongpassword` | Displays error message: `Không tìm thấy thành viên`. | REQ-01 | Decision Table |

### REQ-04: Mượn sách / Borrow Book

| Mã TC | Mục tiêu kiểm thử | Tiền điều kiện | Bước thực hiện | Dữ liệu đầu vào | Kết quả mong đợi | REQ | Kỹ thuật |
|-------|-------------------|---------------|---------------|-----------------|------------------|-----|---------|
| TC-08 | Verify successful borrowing for an active member with available borrowing slots and an available book | - Logged in as MEM006 (`biet.hoang@email.com`) (Status: Active, currently borrowing 1 books). | 1. Go to Books tab.<br>2. Select book BOOK001.<br>3. Click "Borrow". | - Member: MEM006<br>- Book ID: BOOK001<br>- Book Status: Available | - System allows borrowing.<br>- Due date is set to 14 days from the day the member start borrowing.<br>- Book status transitions to "Borrowed". | REQ-04 | EP |
| TC-09 | Reject borrowing when the selected book is borrowed by another member | - Logged in as MEM006 (`biet.hoang@email.com`) (Status: Active). | 1. Go to Books tab.<br>2. Attempt to borrow book BOOK003. | - Member: MEM006<br>- Book ID: BOOK003<br>- Book Status: Borrowed by MEM002 | - System denies borrowing.<br>- Expected Error: "The book is currently unavailable (Already borrowed)." | REQ-04 | Decision Table, EP |
| TC-10 | Reject borrowing if a book's status is "Lost" | - Logged in as MEM006 (`biet.hoang@email.com`) (Status: Active). | 1. Go to Books tab.<br>2. Attempt to borrow book BOOK007. | - Member: MEM006<br>- Book ID: BOOK007<br>- Book Status: Lost | - System denies borrowing.<br>- Expected Error: "The book is currently unavailable (Lost)." | REQ-04 | Decision Table, EP |
| TC-11 | Reject borrowing when the member account status is "Suspended" | - Logged in as MEM004 (`cu.le@email.com`) (Status: Suspended). | 1. Go to Books tab.<br>2. Select book BOOK001.<br>3. Click "Borrow". | - Member: MEM004<br>- Book ID: BOOK001<br>- Book Status: Available | - System denies borrowing.<br>- Expected Error: "The member's account is currently suspended." (Must not say expired). | REQ-04 | Decision Table, EP |
| TC-12 | Reject borrowing when the member account status is "Expired" | - Logged in as MEM005 (`binh.pham@email.com`) (Status: Expired). | 1. Go to Books tab.<br>2. Select book BOOK001.<br>3. Click "Borrow". | - Member: MEM005<br>- Book ID: BOOK001<br>- Book Status: Available | - System denies borrowing.<br>- Expected Error: "The member's account has expired." | REQ-04 | Decision Table, EP |
| TC-13 | Reject borrowing when the member has already reached the maximum limit of 3 books | - The data has been reset.<br>- The test member already has exactly 3 active borrow records before executing this test. | 1. Log in with the prepared member account.<br>2. Go to Books tab.<br>3. Select book BOOK001.<br>4. Click "Borrow". | - Member: prepared member with exactly 3 active borrow records<br>- Book ID: BOOK001<br>- Book Status: Available | - System denies borrowing.<br>- Expected Error: "Member has reached the maximum limit of 3 books." | REQ-04 | BVA |

### REQ-02: Xem danh sách sách / View Book List

| Mã TC | Mục tiêu kiểm thử | Tiền điều kiện | Bước thực hiện | Dữ liệu đầu vào | Kết quả mong đợi | REQ | Kỹ thuật |
|-------|-------------------|---------------|---------------|-----------------|------------------|-----|---------|
| TC-14 | Verify that a user can view the book list with complete book information | 1. The data has been reset.<br>2. The user is logged in successfully. | 1. Log in with `ba.nguyen@email.com`.<br>2. Open the **Books** tab.<br>3. Observe the displayed book list. | Account: `ba.nguyen@email.com` / `password123` | The system displays the book list.<br>Each book shows title, author, category, publication year, and status. | REQ-02 | EP |
| TC-15 | Verify that books with different initial statuses are displayed correctly | 1. The data has been reset.<br>2. The user is logged in successfully. | 1. Open the **Books** tab.<br>2. Find BOOK001, BOOK003, and BOOK007.<br>3. Observe their displayed statuses. | BOOK001: Available<br>BOOK003: Borrowed by MEM002<br>BOOK007: Lost | BOOK001 is displayed as `Có sẵn`.<br>BOOK003 is displayed as `Đã mượn`.<br>BOOK007 is displayed as `Thất lạc`. | REQ-02 | EP |
| TC-16 | Verify real-time book status update after returning a borrowed book | 1. The data has been reset.<br>2. The user is logged in as MEM006.<br>3. BR003 belongs to MEM006 and BOOK013 is initially borrowed. | 1. Log in with `biet.hoang@email.com`.<br>2. Open the **Borrow / Return** tab.<br>3. Return BOOK013 from BR003.<br>4. Open the **Books** tab.<br>5. Check the status of BOOK013. | Account: `biet.hoang@email.com` / `password123`<br>Borrow record: BR003<br>Book: BOOK013 | After the book is returned, BOOK013 changes back to `Có sẵn` immediately. | REQ-02 | EP |

### REQ-03: Tìm kiếm và lọc sách / Search and Filter Books

| Mã TC | Mục tiêu kiểm thử | Tiền điều kiện | Bước thực hiện | Dữ liệu đầu vào | Kết quả mong đợi | REQ | Kỹ thuật |
|-------|-------------------|---------------|---------------|-----------------|------------------|-----|---------|
| TC-17 | Verify book search by title | 1. The data has been reset.<br>2. The user is logged in successfully. | 1. Open the **Books** tab.<br>2. Enter `Flutter` in the search box.<br>3. Observe the result list. | Keyword: `Flutter` | The system displays BOOK001 — `Lập trình Flutter cơ bản`.<br>Unrelated books are not displayed. | REQ-03 | EP |
| TC-18 | Verify book search by author | 1. The data has been reset.<br>2. The user is logged in successfully. | 1. Open the **Books** tab.<br>2. Enter `Nguyễn Minh Đức` in the search box.<br>3. Observe the result list. | Keyword: `Nguyễn Minh Đức` | The system displays books written by Nguyễn Minh Đức, including BOOK001 and BOOK009. | REQ-03 | EP |
| TC-19 | Verify case-insensitive search using lowercase keyword | 1. The data has been reset.<br>2. The user is logged in successfully. | 1. Open the **Books** tab.<br>2. Enter `flutter` in the search box.<br>3. Observe the result list. | Keyword: `flutter` | The system still displays BOOK001 — `Lập trình Flutter cơ bản`. | REQ-03 | EP |
| TC-20 | Verify case-insensitive search using uppercase keyword | 1. The data has been reset.<br>2. The user is logged in successfully. | 1. Open the **Books** tab.<br>2. Enter `FLUTTER` in the search box.<br>3. Observe the result list. | Keyword: `FLUTTER` | The system still displays BOOK001 — `Lập trình Flutter cơ bản`. | REQ-03 | EP |
| TC-21 | Verify search with no matching result | 1. The data has been reset.<br>2. The user is logged in successfully. | 1. Open the **Books** tab.<br>2. Enter `xyz_khong_ton_tai` in the search box.<br>3. Observe the result list. | Keyword: `xyz_khong_ton_tai` | The system displays no books and shows the message `Không tìm thấy sách`. | REQ-03 | EP |
| TC-22 | Verify filtering books by Technology category | 1. The data has been reset.<br>2. The user is logged in successfully. | 1. Open the **Books** tab.<br>2. Select or enter category `Công nghệ`.<br>3. Observe the result list. | Category: `Công nghệ` | The system displays only books in the `Công nghệ` category, including BOOK001, BOOK002, BOOK003, BOOK005, BOOK008, BOOK009, BOOK010, and BOOK011. | REQ-03 | EP |
| TC-23 | Verify that category filtering is case-insensitive for lowercase input | 1. The data has been reset.<br>2. The user has logged in successfully. | 1. Open the **Books** tab.<br>2. Enter lowercase category `công nghệ` in the category filter field.<br>3. Observe the result list. | Category filter: `công nghệ` | The system should display books in the `Công nghệ` category, such as BOOK001, BOOK002, BOOK003, BOOK005, and BOOK008.<br>It should not return no results only because the input is lowercase. | REQ-03 | EP |

### REQ-05: Trả sách / Return Book

| Mã TC | Mục tiêu kiểm thử | Tiền điều kiện | Bước thực hiện | Dữ liệu đầu vào | Kết quả mong đợi | REQ | Kỹ thuật |
|-------|-------------------|---------------|---------------|-----------------|------------------|-----|---------|
| TC-24 | Verify that a member can return their own currently borrowed book | 1. The data has been reset.<br>2. The user is logged in as MEM006.<br>3. BR003 exists and belongs to MEM006. | 1. Log in with `biet.hoang@email.com`.<br>2. Open the **Borrow / Return** tab.<br>3. Find BR003 for BOOK013.<br>4. Click **Return Book**.<br>5. Open the **Books** tab.<br>6. Check the status of BOOK013. | Account: `biet.hoang@email.com` / `password123`<br>Member: MEM006<br>Borrow record: BR003<br>Book: BOOK013 | The system allows MEM006 to return BOOK013.<br>The borrow record changes to `Đã trả`.<br>BOOK013 changes back to `Có sẵn`. | REQ-05 | EP |
| TC-25 | Verify overdue warning when returning an overdue book | 1. The data has been reset.<br>2. BR001 exists in the initial seed data.<br>3. BR001 belongs to MEM002 and has due date 15/09/2024. | 1. Log in with `ba.nguyen@email.com`.<br>2. Open the **Borrow / Return** tab.<br>3. Find BR001 for BOOK003.<br>4. Click **Return Book**.<br>5. Observe the message displayed by the system.<br>6. Open the **Books** tab and check BOOK003. | Account: `ba.nguyen@email.com` / `password123`<br>Borrow record: BR001<br>Book: BOOK003<br>Due date: 15/09/2024 | The system allows the book to be returned.<br>The system displays an overdue warning.<br>BOOK003 changes back to `Có sẵn`. | REQ-05 | BVA |
| TC-26 | Verify that a member cannot view or return another member’s borrowed book | 1. The data has been reset.<br>2. The user is logged in as MEM002.<br>3. BR003 belongs to MEM006. | 1. Log in with `ba.nguyen@email.com`.<br>2. Open the **Borrow / Return** tab.<br>3. Open the borrow record lookup area.<br>4. Search for `MEM006`.<br>5. Check whether BR003 is displayed.<br>6. If BR003 is displayed, check whether the **Return Book** action is available. | Logged-in member: MEM002<br>Other member: MEM006<br>Borrow record: BR003<br>Book: BOOK013 | The system must not display BR003 to MEM002.<br>The system must not allow MEM002 to return BOOK013. | REQ-05, REQ-08 | Decision Table |
| TC-27 | Verify that an already returned record cannot be returned again | 1. The data has been reset.<br>2. The user is logged in as MEM002.<br>3. BR004 already has returned status in the initial seed data. | 1. Log in with `ba.nguyen@email.com`.<br>2. Open the **Borrow / Return** tab.<br>3. Find BR004 for BOOK005 if it is displayed.<br>4. Check whether the **Return Book** action is available. | Account: `ba.nguyen@email.com` / `password123`<br>Borrow record: BR004<br>Book: BOOK005 | The system must not allow returning BR004 again because it is already returned. | REQ-05 | EP |

### REQ-06: Xử lý quá hạn / Overdue Handling

| Mã TC | Mục tiêu kiểm thử | Tiền điều kiện | Bước thực hiện | Dữ liệu đầu vào | Kết quả mong đợi | REQ | Kỹ thuật |
|-------|-------------------|---------------|---------------|-----------------|------------------|-----|---------|
| TC-28 | Verify that the librarian can trigger overdue checking | 1. The data has been reset.<br>2. The user is on the login page. | 1. Log in with `librarian@library.com`.<br>2. Open the **Borrow / Return** tab.<br>3. Click **Check Overdue**.<br>4. Observe the system response. | Account: `librarian@library.com` / `admin123` | The system checks overdue records and updates records whose due date is less than or equal to the current date to `Quá hạn`. | REQ-06 | BVA |
| TC-29 | Verify that overdue borrow records are marked as `Quá hạn` | 1. The data has been reset.<br>2. The user is logged in as librarian.<br>3. BR001 and BR003 exist in the initial seed data. | 1. Log in with `librarian@library.com`.<br>2. Open the **Borrow / Return** tab.<br>3. Observe BR001 and BR003 before overdue checking.<br>4. Click **Check Overdue**.<br>5. Observe BR001 and BR003 again. | BR001 due date: 15/09/2024<br>BR003 due date: 15/10/2024 | BR001 and BR003 are marked as `Quá hạn` if their due dates are less than or equal to the current date. | REQ-06 | BVA |
| TC-30 | Verify that a normal member cannot trigger overdue checking | 1. The data has been reset.<br>2. The user is logged in as a normal member. | 1. Log in with `ba.nguyen@email.com`.<br>2. Open the **Borrow / Return** tab.<br>3. Check whether the **Check Overdue** function is available. | Account: `ba.nguyen@email.com` / `password123`<br>Role: Member | A normal member cannot access or trigger the overdue checking function. | REQ-06 | Decision Table |
| TC-31 | Verify that a member can view their own overdue record after overdue checking | 1. The data has been reset.<br>2. The librarian has performed overdue checking.<br>3. BR001 belongs to MEM002. | 1. Log in as librarian.<br>2. Click **Check Overdue**.<br>3. Log out.<br>4. Log in with `ba.nguyen@email.com`.<br>5. Open the **Borrow / Return** tab.<br>6. Observe BR001. | Member: MEM002<br>Borrow record: BR001 | MEM002 can see their own borrow record BR001 marked as `Quá hạn`. | REQ-06 | BVA |

### REQ-07: Quản lý thành viên / Member Management

| Mã TC | Mục tiêu kiểm thử | Tiền điều kiện | Bước thực hiện | Dữ liệu đầu vào | Kết quả mong đợi | REQ | Kỹ thuật |
|-------|-------------------|---------------|---------------|-----------------|------------------|-----|---------|
| TC-32 | Verify that the librarian can add a new member with a valid email format | 1. The data has been reset.<br>2. The user is logged in as librarian. | 1. Log in with `librarian@library.com`.<br>2. Open the **Members** tab.<br>3. Select **Add Member**.<br>4. Enter a non-empty full name.<br>5. Enter email `user@domain.com`.<br>6. Enter a phone number.<br>7. Click **Add Member**. | Account: `librarian@library.com` / `admin123`<br>Email: `user@domain.com` | The system creates the new member successfully because the email contains `@` and a dot `.` in the domain part. | REQ-07 | EP |
| TC-33 | Verify that a normal member cannot access member management | 1. The data has been reset.<br>2. The user is logged in as a normal member. | 1. Log in with `ba.nguyen@email.com`.<br>2. Observe the navigation menu or available tabs.<br>3. Check whether the **Members** tab or **Add Member** function is available. | Account: `ba.nguyen@email.com` / `password123`<br>Role: Member | A normal member cannot access member management and cannot add a new member. | REQ-07 | Decision Table |
| TC-34 | Verify that the system rejects adding a new member when required fields are missing | 1. The data has been reset.<br>2. The user is logged in as librarian. | 1. Log in with `librarian@library.com`.<br>2. Open the **Members** tab.<br>3. Select **Add Member**.<br>4. Leave the full name field blank.<br>5. Enter email `new.member@email.com`.<br>6. Enter phone number `0912345678`.<br>7. Click **Add Member**. | Account: `librarian@library.com` / `admin123`<br>Full name: blank<br>Email: `new.member@email.com`<br>Phone: `0912345678` | The system does not create the new member and displays an error message indicating that the full name field is required. | REQ-07 | EP |
| TC-35 | Verify that the system rejects an existing email | 1. The data has been reset.<br>2. The user is logged in as librarian.<br>3. Email `ba.nguyen@email.com` already exists in the initial seed data. | 1. Log in with `librarian@library.com`.<br>2. Open the **Members** tab.<br>3. Select **Add Member**.<br>4. Enter a non-empty full name.<br>5. Enter email `ba.nguyen@email.com`.<br>6. Enter a phone number.<br>7. Click **Add Member**. | Account: `librarian@library.com` / `admin123`<br>Existing email: `ba.nguyen@email.com` | The system does not create the new member.<br>The system displays an error message indicating that the email already exists or is duplicated. | REQ-07 | EP |

### REQ-08: Tra cứu phiếu mượn / Borrow Record Lookup

| Mã TC | Mục tiêu kiểm thử | Tiền điều kiện | Bước thực hiện | Dữ liệu đầu vào | Kết quả mong đợi | REQ | Kỹ thuật |
|-------|-------------------|---------------|---------------|-----------------|------------------|-----|---------|
| TC-36 | Verify that a member can view only their own borrow records | 1. The data has been reset.<br>2. The user is logged in as MEM002. | 1. Log in with `ba.nguyen@email.com`.<br>2. Open the **Borrow / Return** tab.<br>3. Open **My Borrow Records** or the equivalent section.<br>4. Observe the displayed records. | Account: `ba.nguyen@email.com` / `password123`<br>Member: MEM002<br>Own records: BR001 and BR004 | The system displays records belonging to MEM002, including BR001 and BR004.<br>The system does not display records of other members. | REQ-08 | EP |
| TC-37 | Verify that the librarian can view all borrow records | 1. The data has been reset.<br>2. The user is logged in as librarian. | 1. Log in with `librarian@library.com`.<br>2. Open the **Borrow / Return** tab.<br>3. View the borrow record list.<br>4. Observe whether records of all members are displayed. | Account: `librarian@library.com` / `admin123`<br>Records: BR001, BR002, BR003, BR004, BR005 | The librarian can view all borrow records of all members.<br>Each record displays record ID, borrowed book, borrow date, due date, and status. | REQ-08 | EP |
| TC-38 | Verify that a member cannot look up another member’s borrow records | 1. The data has been reset.<br>2. The user is logged in as MEM002.<br>3. BR003 belongs to MEM006. | 1. Log in with `ba.nguyen@email.com`.<br>2. Open the **Borrow / Return** tab.<br>3. Open the borrow record lookup area.<br>4. Search for `MEM006`.<br>5. Observe whether BR003 is displayed. | Logged-in member: MEM002<br>Other member: MEM006<br>Borrow record: BR003 | The system must not display BR003 to MEM002 because a member can only view their own borrow records. | REQ-08 | Decision Table |
| TC-39 | Verify that borrow records display all required fields | 1. The data has been reset.<br>2. The user is logged in as librarian. | 1. Log in with `librarian@library.com`.<br>2. Open the **Borrow / Return** tab.<br>3. Find BR001.<br>4. Observe the displayed fields. | Borrow record: BR001 | BR001 displays record ID, borrowed book, borrow date, due date, and status. | REQ-08 | EP |

---

## Tổng hợp

| Nhóm chức năng | Số TC | REQ phủ | Kỹ thuật IDM áp dụng |
|----------------|-------|---------|----------------------|
| Login | 7 | REQ-01 | EP, Decision Table |
| Borrow Book | 6 | REQ-04 | EP, BVA, Decision Table |
| View Book List | 3 | REQ-02 | EP |
| Search and Filter Books | 7 | REQ-03 | EP |
| Return Book | 4 | REQ-05 | EP, BVA, Decision Table |
| Overdue Handling | 4 | REQ-06 | BVA, Decision Table |
| Member Management | 4 | REQ-07 | EP, Decision Table |
| Borrow Record Lookup | 4 | REQ-08 | EP, Decision Table |
| **Tổng** | **39** | **REQ-01 → REQ-08** | **EP, BVA, Decision Table** |