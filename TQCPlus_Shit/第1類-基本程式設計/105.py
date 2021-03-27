# 題目說明：

# 請撰寫一程式，輸入兩個正數，代表一矩形之寬和高，計算並輸出此矩形之高（Height）、寬（Width）、周長（Perimeter）及面積（Area）。
# 提示：輸出浮點數到小數點後第二位。

h = eval(input())
w = eval(input())

print('Height = %.2f' % h)
print('Width = %.2f' % w)
print('Perimeter = %.2f' % ((w+h)*2))
print('Area = %.2f' % (w * h))
