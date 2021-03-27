# 題目說明：

# 請撰寫一程式，讀取read.txt（每一列的格式為名字和身高、體重，以空白分隔）
# 並顯示檔案內容、所有人的平均身高、平均體重以及最高者、最重者。

# 提示：輸出浮點數到小數點後第二位。

# readlines 讀出後，迴圈分析每一資料，replace \n 和 split(" ")
# 並存到各自的 list 去，然後就可以做運算了

with open("904.txt", "r") as file:
    name, height, weight = [], [], []
    for i in file:
        print(i)
        name.append(i.split()[0])
        height.append(int(i.split()[1]))
        weight.append(int(i.split()[2]))
    print("Average height: {:.2f}".format(sum(height) / 3))
    print("Average weight: {:.2f}".format(sum(weight) / 3))
    print("The tallest is {} with {:.2f}cm".format(name[height.index(max(height))], max(height)))
    print("The heaviest is {} with {:.2f}kg".format(name[weight.index(max(weight))], max(weight)))