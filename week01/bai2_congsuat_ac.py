T_in = float(input("Nhập nhiệt độ trong phòng (°C): "))
T_out = float(input("Nhập nhiệt độ ngoài trời (°C): "))
n_people = int(input("Nhập số người trong phòng (số nguyên): "))

# Tính toán công suất: Bắt đầu với mức cơ bản 30%
cong_suat = 30
# Nếu phòng đang nóng
if T_in > 28:
    cong_suat += 20

# Nếu trời quá nóng
if T_out > 35:
    cong_suat = cong_suat + 20  # Cộng thêm 20%

# Nếu quá đông người
if n_people > 30:
    cong_suat += 20  

# Giới hạn tối đa 100% 
if cong_suat > 100:
    cong_suat = 100
print(f"Thông số: Nhiệt độ trong phòng={T_in}, Nhiệt độ ngoài trời={T_out}, Số Người={n_people}")
print(f"Khuyến nghị công suất điều hoà là: {cong_suat}%")