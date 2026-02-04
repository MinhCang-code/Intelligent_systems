## Bài 1: 
# 1. Chạy script, chụp màn hình đồ thị hiển thị 3 đường LẠNH – DỄ CHỊU – NÓNG.
#
# 2. Thay đổi tham số tập mờ (uncomment phần dưới để thử):
#    - LẠNH: 20–21–24
#    - DỄ CHỊU: 23–25–27
#    - NÓNG: 26–29–35
#
# 3. Nhận xét:
#    - Nếu vùng "DỄ CHỊU" rộng hơn thì hệ điều khiển có xu hướng "dễ tính" hơn
#      vì phạm vi nhiệt độ được coi là thoải mái lớn hơn, AC ít phải điều chỉnh.
#
#    - Nếu vùng "NÓNG" bắt đầu sớm hơn (ví dụ 26°C) thì AC sẽ có xu hướng chạy
#      mạnh hơn vì hệ thống nhận diện "nóng" ở nhiệt độ thấp hơn, kích hoạt
#      làm mát sớm hơn và mạnh hơn.
# 

# --- PHẦN THỬ NGHIỆM VỚI THAM SỐ MỚI (uncomment để chạy) ---
# mu_cold_new = trimf(x_T, 20, 21, 24)
# mu_comfort_new = trimf(x_T, 23, 25, 27)
# mu_hot_new = trimf(x_T, 26, 29, 35)
#
# plt.figure(figsize=(8, 4))
# plt.plot(x_T, mu_cold_new, label="Lạnh (mới)")
# plt.plot(x_T, mu_comfort_new, label="Dễ chịu (mới)")
# plt.plot(x_T, mu_hot_new, label="Nóng (mới)")
# plt.title("Tập mờ cho T_in (°C) - Tham số mới")
# plt.xlabel("T_in (°C)")
# plt.ylabel("Mức thuộc")
# plt.legend()
# plt.grid(True, alpha=0.3)
# plt.tight_layout()
# plt.show()

=============================================================================
## Bài 2:

# 1. Khi tăng AC từ 20% → 80%, membership của "AC Cao" thay đổi như thế nào?
#    - Tại AC = 20%: mu_ac_high = 0 (chưa thuộc vùng "Cao")
#    - Tại AC = 60%: mu_ac_high = 0 (bắt đầu vào vùng "Cao")
#    - Tại AC = 80%: mu_ac_high = 0.5 (thuộc một nửa vào vùng "Cao")
#    - Tại AC = 100%: mu_ac_high = 1.0 (hoàn toàn thuộc vùng "Cao")
#    => Membership tăng tuyến tính từ 0 lên khi AC vượt qua 60%
#
# 2. Nếu mở rộng vùng "AC Vừa" (ví dụ từ [20-50-80] thành [10-50-90]),
#    AC có xu hướng "ít khi lên max" hơn không?
#    - CÓ, vì vùng "AC Vừa" chiếm phạm vi rộng hơn
#    - Khi defuzzify, giá trị trung bình sẽ bị kéo về vùng giữa nhiều hơn
#    - Kết quả là AC ít khi đạt công suất tối đa 100%
#    - Hệ thống trở nên "mềm mại" hơn, ít có đầu ra cực đoan
#
# =============================================================================
## Bài 3: 
#
# 1. Kết quả AC fuzzy với luật gốc:
#    - T_in = 22°C: AC thấp (trời lạnh, không cần làm mát mạnh)
#    - T_in = 25°C: AC vừa (nhiệt độ dễ chịu, AC ở mức trung bình)
#    - T_in = 29°C: AC cao (trời nóng, cần làm mát mạnh)
#    - T_in = 32°C: AC rất cao (trời rất nóng)
#
# 2. So sánh với luật cứng (if-else truyền thống):
#    - Luật cứng: nhảy đột ngột từ 0 -> 50 -> 100%
#    - Luật mờ: thay đổi MỀM MẠI, MƯỢT MÀ hơn
#    - Ví dụ: ở 27°C, AC không nhảy đột ngột mà chuyển tiếp dần
#    => Fuzzy logic cho kết quả SÁT CẢM NHẬN THỰC TẾ hơn
#
# 3. Khi đổi luật "DỄ CHỊU -> AC THẤP":
#    - AC tiết kiệm điện hơn ở vùng nhiệt độ trung bình
#    - Phù hợp cho người thích tiết kiệm năng lượng
#    - Nhưng có thể kém thoải mái hơn một chút
#
# =============================================================================
## Bài 4:
#
# 1. Đường T_in có mượt hơn không?
#    - CÓ, đường T_in thay đổi liên tục và mượt mà
#    - So với luật cứng (tuần 2) chỉ có 3 mức AC cố định, fuzzy cho phép
#      AC thay đổi liên tục nên T_in cũng biến thiên mượt hơn
#
# 2. AC có còn nhảy 3 mức 20-50-80% hay đã mượt hơn?
#    - AC đã MƯỢT HƠN NHIỀU, không còn nhảy bậc 3 mức như luật cứng
#    - Fuzzy cho phép AC có giá trị liên tục trong khoảng 0-100%
#
# 3. Khi nào fuzzy có lợi thế rõ rệt so với luật cứng?
#    - Khi cần điều khiển mềm mại, tránh "giật cục"
#    - Khi nhiệt độ nằm ở vùng chuyển tiếp giữa các trạng thái
#    - Khi muốn tiết kiệm năng lượng (AC không nhảy đột ngột)
#
# 4. Khi nào luật cứng vẫn đủ tốt và đơn giản hơn?
#    - Khi hệ thống đơn giản, chỉ cần ON/OFF hoặc vài mức cố định
#    - Khi không cần độ chính xác cao
#    - Khi tài nguyên tính toán hạn chế
#    - Khi logic nghiệp vụ rõ ràng, dễ giải thích
#
# =============================================================================
## TRẢ LỜI CÂU HỎI TỔNG KẾT THỰC HÀNH:

## Câu 1: Nếu tập mờ "DỄ CHỊU" quá rộng, hệ thống sẽ thiên về tiết kiệm điện hay thiên về thoải mái?
# Trả lời: Hệ thống sẽ thiên về TIẾT KIỆM ĐIỆN.
# Giải thích:
# Dựa trên bộ luật mờ trong `bai3_fuzzy_controller.py`:
# - IF T_in is LẠNH → AC Thấp
# - IF T_in is DỄ CHỊU → AC Vừa  
# - IF T_in is NÓNG → AC Cao

# Khi tập mờ "DỄ CHỊU" quá rộng:

1. **Về phía nhiệt độ cao (nóng):**
   - Nhiều giá trị nhiệt độ cao hơn sẽ bị phân loại là "Dễ chịu" thay vì "Nóng"
   - Hệ thống chỉ kích hoạt AC Vừa thay vì AC Cao
   - → Tiết kiệm điện nhưng người dùng có thể cảm thấy nóng

2. **Về phía nhiệt độ thấp (lạnh):**
   - Nhiều giá trị nhiệt độ thấp hơn sẽ bị phân loại là "Dễ chịu" thay vì "Lạnh"
   - Hệ thống kích hoạt AC Vừa thay vì AC Thấp
   - → Tốn điện hơn một chút nhưng tác động nhỏ

3. **Tổng thể:**
   - Vùng "Nóng" bị thu hẹp → AC Cao ít được kích hoạt hơn
   - AC Cao tiêu thụ năng lượng nhiều nhất (60-100%)
   - → **Tổng năng lượng tiêu thụ giảm = Tiết kiệm điện**


## Câu 2: Nếu có log dữ liệu thực và phản hồi người dùng, em sẽ sử dụng như thế nào để điều chỉnh tập mờ và luật mờ?

# Trả lời:

# A. Thu thập và phân tích dữ liệu

1. **Cấu trúc dữ liệu log:**
   ```
   | Timestamp | T_in | T_out | AC_power | Feedback |
   |-----------|------|-------|----------|----------|
   | 10:00     | 28°C | 32°C  | 55%      | Hơi nóng |
   | 10:30     | 26°C | 32°C  | 50%      | Vừa      |
   | 11:00     | 24°C | 30°C  | 35%      | Hơi lạnh |
   ```

2. **Phân tích thống kê:**
   - Tính phân bố feedback theo từng mức nhiệt độ
   - Xác định ngưỡng nhiệt độ mà người dùng cảm thấy thay đổi (nóng ↔ vừa ↔ lạnh)

# B. Điều chỉnh tập mờ (Membership Functions)

1. **Phương pháp thống kê:**
   ```python
   # Ví dụ: Tìm ngưỡng mới cho tập "NÓNG"
   hot_feedback = data[data['Feedback'].isin(['Rất nóng', 'Hơi nóng'])]
   new_hot_start = hot_feedback['T_in'].quantile(0.25)  # Điểm bắt đầu
   new_hot_peak = hot_feedback['T_in'].median()         # Điểm đỉnh
   ```

2. **Điều chỉnh tham số (a, b, c) của hàm tam giác:**

   | Feedback phổ biến | Điều chỉnh |
   |-------------------|------------|
   | "Rất nóng" ở 27°C (hiện tại đang là Dễ chịu) | Dịch tập NÓNG sang trái: (25, 28, 35) |
   | "Hơi lạnh" ở 25°C (hiện tại đang là Dễ chịu) | Dịch tập LẠNH sang phải: (20, 24, 27) |
   | Nhiều phản hồi "Vừa" ở 26-28°C | Mở rộng tập DỄ CHỊU: (23, 26, 29) |

3. **Áp dụng vào code:**
   ```python
   # Trước điều chỉnh (bai3_fuzzy_controller.py)
   mu_cold = trimf(T_in, 20, 22, 25)
   mu_comfort = trimf(T_in, 24, 26, 28)
   mu_hot = trimf(T_in, 27, 30, 35)
   
   # Sau điều chỉnh (dựa trên feedback)
   mu_cold = trimf(T_in, 20, 23, 26)     # Điều chỉnh theo feedback "lạnh"
   mu_comfort = trimf(T_in, 25, 27, 29)  # Thu hẹp nếu người dùng nhạy cảm
   mu_hot = trimf(T_in, 28, 31, 35)      # Điều chỉnh theo feedback "nóng"
   ```

# C. Điều chỉnh luật mờ (Fuzzy Rules)

1. **Phân tích mẫu phản hồi:**
   ```
   Nếu: T_in = 26°C (Dễ chịu), AC = 50% → Feedback: "Hơi nóng"
   → Cần thay đổi luật: DỄ CHỊU → AC Vừa-Cao (thay vì chỉ AC Vừa)
   ```

2. **Thêm luật mới hoặc sửa luật cũ:**
   ```python
   # Luật gốc
   IF T_in is DỄ_CHỊU → AC Vừa
   
   # Luật mới (dựa trên feedback)
   IF T_in is DỄ_CHỊU AND T_out is CAO → AC Vừa-Cao
   IF T_in is DỄ_CHỊU AND Occupancy is ĐÔNG → AC Vừa-Cao
   ```

3. **Thêm biến đầu vào mới:**
   - Nếu feedback cho thấy T_in không đủ để quyết định, thêm biến như:
     - Độ ẩm (Humidity)
     - Số người (Occupancy)
     - Thời gian trong ngày

# D. Phương pháp tối ưu hóa tự động

1. **Gradient Descent:**
   ```python
   # Tối ưu tham số (a, b, c) để minimize sai số với feedback
   def loss_function(params, data, feedbacks):
       # Tính sai số giữa output hệ thống và feedback người dùng
       return mean_squared_error(predicted_comfort, actual_feedback)
   
   # Sử dụng gradient descent để tìm params tối ưu
   optimal_params = optimize(loss_function, initial_params, data)
   ```

2. **Genetic Algorithm (GA):**
   - Mã hóa tham số tập mờ thành chromosome
   - Fitness function: Độ hài lòng người dùng
   - Tiến hóa qua nhiều thế hệ để tìm bộ tham số tối ưu

3. **Reinforcement Learning:**
   - State: T_in, T_out, Occupancy
   - Action: Điều chỉnh AC
   - Reward: Feedback người dùng (Vừa = +1, Hơi nóng/lạnh = -0.5, Rất nóng/lạnh = -1)

# E. Quy trình tổng quát

┌─────────────────────────────────────────────────────────────┐
│  1. Thu thập dữ liệu: T_in, T_out, AC, Feedback             │
│                           ↓                                 │
│  2. Phân tích: Tìm mẫu feedback không khớp với hệ thống     │
│                           ↓                                 │
│  3. Điều chỉnh tập mờ: Thay đổi (a, b, c) của trimf         │
│                           ↓                                 │
│  4. Điều chỉnh luật mờ: Thêm/sửa rules                      │
│                           ↓                                 │
│  5. Kiểm thử: Chạy mô phỏng với dữ liệu mới                 │
│                           ↓                                 │
│  6. Đánh giá: So sánh feedback trước/sau điều chỉnh         │
│                           ↓                                 │
│  7. Lặp lại: Tiếp tục thu thập và cải thiện                 │
└─────────────────────────────────────────────────────────────┘
