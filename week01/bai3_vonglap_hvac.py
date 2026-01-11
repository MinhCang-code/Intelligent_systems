# Khởi tạo các biến đếm
count_off = 0
count_medium = 0
count_high = 0
print("BẮT ĐẦU MỞ PHỎNG 5 BƯỚC THỜI GIAN....")
# Vòng lặp chạy từ 1 đến 5 (range(1, 6))
for step in range(1, 6):
    print(f"\n[Nhập dữ liệu cho Bước {step}]")
    # Nhập dữ liệu
    T_in = float(input("Nhập nhiệt độ trong phòng (T_in): "))
    n_people = int(input("Nhập số người hiện có (n_people): "))
    # Xử lý quyết định (Quy tắc tự định nghĩa)
    # - Nếu nhiệt độ < 25: Tắt
    # - Nếu nhiệt độ >= 30 HOẶC số người > 40: Cao
    # - Còn lại: Vừa
    quyet_dinh = ""
    if T_in <= 22 and n_people <= 10:
        quyet_dinh = "AC OFF"
        count_off += 1  # Tăng biến đếm OFF
    elif T_in > 27 or n_people > 20:
        quyet_dinh = "AC HIGH"
        count_high += 1 # Tăng biến đếm HIGH
    else:
        quyet_dinh = "AC MEDIUM"
        count_medium += 1 # Tăng biến đếm MEDIUM
    # In log ngay lập tức cho bước này
    # Sử dụng f-string 
    print(f"Bước {step}: T_in={T_in}, n_people={n_people}, Quyết định={quyet_dinh}")
# Sau khi hết vòng lặp (hết 5 bước), in tổng kết
print("\n=======================================================--")
print("TỔNG KẾT SAU 5 BƯỚC:")
print(f"- Số lần AC OFF:    {count_off}")
print(f"- Số lần AC MEDIUM: {count_medium}")
print(f"- Số lần AC HIGH:   {count_high}")