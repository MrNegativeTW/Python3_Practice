print('上次加滿後跑了多少公里？')
mileage = float(input())
print('上次加了幾公升的油？')
oil = float(input())

x = mileage / oil
y = f'您的油耗為 每公升可跑 {x} 公里'

print(y)