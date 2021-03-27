# 題目說明：

# 請撰寫一程式，讀取read.txt的內容（內容為數字，以空白分隔）並將這些數字加總後輸出。
# 檔案讀取完成後要關閉。

with open("902.txt", "r") as file:
    data = file.read()
    aa = [int(i) for i in data.split(" ")]
    print(sum(aa))
    file.close()