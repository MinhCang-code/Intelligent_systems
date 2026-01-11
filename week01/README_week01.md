# python 3.14.2
# IDE sử dụng là VS Code
# extension đã cài: Python, Python Debugger, Python Environments, Pylance
# Ghi chú nếu có lỗi khi cài đặt: 

## Bài 1: Kiểm tra nhiệt độ phòng (bai1_nhietdo.py)
**Mục đích:** Chương trình đơn giản để phân loại nhiệt độ trong phòng

**Các bước thực hiện:**
1. Nhập nhiệt độ từ người dùng (sử dụng `float()` để chuyển đổi input thành số thực)
2. Sử dụng câu lệnh `if-elif-else` để phân loại:
   - Nếu < 22°C: Lạnh
   - Nếu từ 22°C đến < 27°C: Vừa, mát mẻ
   - Nếu >= 27°C: Nóng
3. In kết quả ra màn hình

**Kiến thức sử dụng:** Input/Output, If-elif-else, Float conversion

---

## Bài 2: Tính công suất điều hòa (bai2_congsuat_ac.py)
**Mục đích:** Tính toán công suất điều hòa dựa trên nhiều yếu tố môi trường

**Các bước thực hiện:**
1. Nhập 3 thông số:
   - Nhiệt độ trong phòng (T_in)
   - Nhiệt độ ngoài trời (T_out)
   - Số người trong phòng (n_people)
2. Bắt đầu với công suất cơ bản 30%
3. Áp dụng các quy tắc cộng dồn:
   - Nếu T_in > 28°C: Cộng thêm 20%
   - Nếu T_out > 35°C: Cộng thêm 20%
   - Nếu n_people > 30: Cộng thêm 20%
4. Giới hạn công suất tối đa là 100%
5. In ra khuyến nghị công suất

**Kiến thức sử dụng:** Multiple inputs, If statements, Arithmetic operations, Variable accumulation

---

## Bài 3: Mô phỏng hệ thống HVAC với vòng lặp (bai3_vonglap_hvac.py)
**Mục đích:** Mô phỏng hệ thống điều hòa không khí trong 5 bước thời gian và thống kê quyết định

**Các bước thực hiện:**
1. Khởi tạo 3 biến đếm: count_off, count_medium, count_high
2. Sử dụng vòng lặp `for` chạy 5 lần (step 1-5)
3. Mỗi bước:
   - Nhập T_in (nhiệt độ phòng) và n_people (số người)
   - Áp dụng quy tắc quyết định:
     * AC OFF: Nếu T_in <= 22°C VÀ n_people <= 10
     * AC HIGH: Nếu T_in > 27°C HOẶC n_people > 20
     * AC MEDIUM: Các trường hợp còn lại
   - Tăng biến đếm tương ứng
   - In log ngay lập tức
4. Sau 5 bước, in tổng kết số lần mỗi trạng thái được chọn

**Kiến thức sử dụng:** For loop, Range, Counter variables, Logical operators (and, or), F-string formatting

**Điểm chú ý:**
- Sử dụng `range(1, 6)` để tạo vòng lặp từ 1 đến 5
- Sử dụng `f-string` để format output đẹp và dễ đọc
- Biến đếm giúp thống kê kết quả sau khi mô phỏng

#