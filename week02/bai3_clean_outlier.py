import os
import pandas as pd

output_dir = "./project_hvac/data"
os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv(os.path.join(output_dir, "hvac_simulated_week2.csv"))

# Cố tình chèn vài outlier
df.loc[5, "T_in"] = 99
df.loc[10, "T_in"] = -5
df.loc[20, "humidity"] = 0
df.loc[25, "humidity"] = 150

outlier_path = os.path.join(output_dir, "hvac_with_outlier.csv")
df.to_csv(outlier_path, index=False)
print(f"Đã tạo {outlier_path} với outlier.")
# Chạy file trên trước, rồi tiếp tục.
# Bước 2 – Phát hiện & xử lý outlier
# Thêm tiếp vào bai3_clean_outlier.py (hoặc tạo file mới):
# python


df = pd.read_csv(outlier_path)

def is_T_in_bad(x):
    return x < 15 or x > 45

def is_humidity_bad(x):
    return x < 10 or x > 100

bad_T = df["T_in"].apply(is_T_in_bad)
bad_H = df["humidity"].apply(is_humidity_bad)

print("Số dòng T_in bất thường:", bad_T.sum())
print("Số dòng humidity bất thường:", bad_H.sum())

# Cách xử lý: thay bằng trung bình của 2 hàng lân cận (nếu có)
for idx in df[bad_T].index:
    if 1 <= idx < len(df) - 1:
        df.loc[idx, "T_in"] = (df.loc[idx - 1, "T_in"] + df.loc[idx + 1, "T_in"]) / 2
    else:
        df.loc[idx, "T_in"] = df["T_in"].median()

for idx in df[bad_H].index:
    if 1 <= idx < len(df) - 1:
        df.loc[idx, "humidity"] = (df.loc[idx - 1, "humidity"] + df.loc[idx + 1, "humidity"]) / 2
    else:
        df.loc[idx, "humidity"] = df["humidity"].median()

cleaned_path = os.path.join(output_dir, "hvac_cleaned.csv")
df.to_csv(cleaned_path, index=False)
print(f"Đã lưu file {cleaned_path} sau khi làm sạch.")
