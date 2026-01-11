ten_bien = float(input("Nhập nhiệt độ trong phòng (độ C):  "))

if ten_bien < 22:
    print("Nhiệt độ trong phòng lạnh")
elif ten_bien < 27:
    print("Nhiệt độ trong phòng vừa, mát mẻ.")
else:
    print("Nhiệt độ trong phòng nóng")