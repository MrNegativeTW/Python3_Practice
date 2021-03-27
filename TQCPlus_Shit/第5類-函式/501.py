# 題目說明：

# 請撰寫一程式，呼叫函式compute()，該函式功能為讓使用者輸入系別（Department）、
# 學號（Student ID）和姓名（Name）並顯示這些訊息。

def compute():
    department = input()
    ids = input()
    name = input()
    print("Department: %s" % department)
    print("Student ID: %s" % ids)
    print("Name: %s" % name)

compute()
