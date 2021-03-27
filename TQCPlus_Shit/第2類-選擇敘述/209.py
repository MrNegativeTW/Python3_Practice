# 設計說明：

# 請使用選擇敘述撰寫一程式，讓使用者輸入一個點的平面座標x和y值，
# 判斷此點是否與點(5, 6)的距離小於或等於15，
# 如距離小於或等於15顯示【Inside】，反之顯示【Outside】。
# 提示：計算平面上兩點距離的公式： √((x1−x2)^2 + (y1−y2^2)

import math

x = eval(input())
y = eval(input())

result = math.sqrt((x-5) ** 2 + (y - 6) ** 2)

if result <= 15:
    print("Inside")
else: 
    print("Outside")