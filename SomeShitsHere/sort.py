# sort 是方法, 直接改變數組
# sorted 是函數, 不改變數組, 另創數組

a = ['a', 'bb', 'ccc']
b = ['a', 'bb', 'ccc']

a.sort(reverse = True)
b.sort(key = len)

print(a, b)