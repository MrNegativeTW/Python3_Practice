from flask import Flask, render_template, url_for
app = Flask(__name__)

toBuildSJson = [
    {
        "id": 1,
        "name": "果塔早午餐",
        "phone": "06-2533007",
        "times": "6:00 ~ 13:00",
        "drink": "另購",
        "soup": "null",
        "image": "https://2.bp.blogspot.com/-9l6DQBbb4dw/WyoMlGNpKQI/AAAAAAAAkCs/1WN7AFjDE_AMIkhymR6CKXdjQSCLdyFxACK4BGAYYCw/s1600/%25E6%259E%259C%25E5%25A1%2594%25E6%2597%25A9%25E5%258D%2588%25E9%25A4%2590.png",
        "menu": "https://1.bp.blogspot.com/-ZL-GaQa20fU/Wyykz1RTOII/AAAAAAAAkIk/4MlVbzOmxtE1CKC835EKC9twcv_kAUpDACK4BGAYYCw/s1600/%25E6%259E%259C%25E5%25A1%2594%25E8%25BC%2595%25E9%25A3%259F%25E6%2597%25A9%25E5%258D%2588%25E9%25A4%2590.png",
        "href": 0,
        "seat": "有"
    },
    {
        "id": 2,
        "name": "阿賢越南美食",
        "classes": "越南美食",
        "phone": "0970-402-529",
        "times": "10:00 ~ 20:00",
        "drink": "否",
        "soup": "null",
        "image": "https://1.bp.blogspot.com/-is1V6ZO5-ds/WyoMjJ98SSI/AAAAAAAAkCk/L5XkyJd8qVg2olwaLKSGuoRBnRKMqekDQCK4BGAYYCw/s1600/%25E9%2598%25BF%25E8%25B3%25A2%2B%25E8%25B6%258A%25E5%258D%2597%25E6%25B2%25B3%25E7%25B2%2589.png",
        "menu": "https://2.bp.blogspot.com/-KCwgs-j9O1k/WyylAZXqGQI/AAAAAAAAkIs/dtm2GU3J80Yu873qOra3_M3fhH9FPWcYQCK4BGAYYCw/s1600/%25E9%2598%25BF%25E8%25B3%25A2%25E8%25B6%258A%25E5%258D%2597%25E7%25BE%258E%25E9%25A3%259F.jpg",
        "href": 0,
        "seat": "有"
    },
    {
        "id": 3,
        "name": "型男老爹",
        "classes": "飯麵",
        "phone": "06-2430769 / 0915-789-856",
        "times": "午餐、晚餐",
        "drink": "是",
        "soup": "是",
        "selfclean": "否",
        "image": "http://3.bp.blogspot.com/-1z9D0Mbn9K4/Wkxcq-1R0ZI/AAAAAAAAbkI/BpmcXySs4FY7TXgalz67ZkZmnJOePqSyACK4BGAYYCw/s1600/%25E5%259E%258B%25E7%2594%25B7%25E8%2580%2581%25E7%2588%25B9.png",
        "menu": "http://1.bp.blogspot.com/-IovTa6NkAlE/WkxgZ-IPiyI/AAAAAAAAbkU/vAk3QcwcEAcFL2qywFZa8O_lTHVkpVx2wCK4BGAYYCw/s1600/%25E5%259E%258B%25E7%2594%25B7%25E8%2580%2581%25E7%2588%25B9.png",
        "href": 0,
        "seat": "有"
    },
    {
        "id": 4,
        "name": "紅豆早餐吧",
        "classes": "早午餐",
        "phone": "06-2532852",
        "times": "早餐、午餐",
        "drink": "另購",
        "delivery": "是",
        "image": "https://3.bp.blogspot.com/-XShh931NbxE/WyoMSeWhE2I/AAAAAAAAkCE/YElHf6E5VskOgYFLeUvPlHaIItTV9moiQCK4BGAYYCw/s1600/%25E7%25B4%2585%25E8%25B1%2586%25E6%2597%25A9%25E5%258D%2588%25E9%25A4%2590.png",
        "menu": 0,
        "href": 0,
        "seat": "有"
    },
    {
        "id": 5,
        "name": "李好食堂",
        "times": "午餐、晚餐",
        "image": "https://1.bp.blogspot.com/-DFXPJNyn1Nk/WyoMRIGQ7EI/AAAAAAAAkB8/zQVwHHMS1kgdGCH3sfeKEmKnkxEAf53-gCK4BGAYYCw/s1600/%25E6%259D%258E%25E5%25A5%25BD%25E9%25A3%259F%25E5%25A0%2582.png",
        "menu": 0,
        "href": 0
    },
    {
        "id": 6,
        "name": "葡萄園",
        "classes": "丼飯、麵食、焗烤",
        "phone": "06-2536968",
        "times": "11:00 ~ 14:00 週日休",
        "drink": "是",
        "image": "https://3.bp.blogspot.com/-ClRCFbSrN9Y/WyoMO_pH-eI/AAAAAAAAkB0/pawiG1NzNEMDB8ohtw0ZYtrtgovvDwPywCK4BGAYYCw/s1600/%25E8%2591%25A1%25E8%2590%2584%25E5%259C%2592.png",
        "menu": "https://4.bp.blogspot.com/-Ujz63Ppfv6M/WyylNzcapyI/AAAAAAAAkI4/mHldg58OPhUCyoKAQv5ukOouYIBlZOJiQCK4BGAYYCw/s1600/%25E8%2591%25A1%25E8%2590%2584%25E5%259C%2592.jpg",
        "href": 0,
        "seat": "有"
    },
    {
        "id": 7,
        "name": "香港陳記燒臘快餐",
        "classes": "燒臘",
        "phone": "06-2433315",
        "times": "午餐、晚餐",
        "drink": "是",
        "soup": "是",
        "delivery": "null",
        "image": "https://3.bp.blogspot.com/-p32zX6N-GuQ/WyoMNrgAlfI/AAAAAAAAkBs/7lPHYPpVELo4GYiNHOfQQN3du1sY7BZ8QCK4BGAYYCw/s1600/%25E9%25A6%2599%25E6%25B8%25AF%25E9%2599%25B3%25E8%25A8%2598%25E7%2587%2592%25E8%2587%2598%25E5%25BF%25AB%25E9%25A4%2590.png",
        "menu": "https://3.bp.blogspot.com/-bXAhTyRA6dk/WyylRnuy9JI/AAAAAAAAkJE/QTHvr89ImZIq7RJ7OFVcRr5ih1pJon1-ACK4BGAYYCw/s1600/%25E9%25A6%2599%25E6%25B8%25AF%25E9%2599%25B3%25E8%25A8%2598%25E7%2587%2592%25E8%2587%2598.png",
        "href": 0,
        "seat": "有"
    },
    {
        "id": 8,
        "name": "里查里茶",
        "classes": "飲料店",
        "phone": "06-2430698",
        "times": "午餐、晚餐",
        "drink": "他就是飲料店",
        "soup": "否",
        "selfclean": "不適用",
        "delivery": "是",
        "image": "https://3.bp.blogspot.com/-_riT98AqrM4/WyoMMZtxD0I/AAAAAAAAkBg/9_JHYTtt8Xw6tm14AFqkwPUn0KqI3hz4ACK4BGAYYCw/s1600/%25E9%2587%258C%25E6%259F%25A5%25E9%2587%258C%25E6%259F%25A5.png",
        "menu": "https://4.bp.blogspot.com/-aRenfxPx9cw/WyylWzVCD1I/AAAAAAAAkJM/JaquMmeC350vmLdApNoyznkI-tBFN43-ACK4BGAYYCw/s1600/%25E9%2587%258C%25E8%258C%25B6%25E9%2587%258C%25E8%258C%25B6.png",
        "href": 0,
        "seat": "N/A"
    },
    {
        "id": 9,
        "name": "麵店",
        "classes": "麵食",
        "image": "https://3.bp.blogspot.com/-VYD6fj3kR9c/WyoMLRKJN6I/AAAAAAAAkBY/-0md_aLkc2Yq6DGTkOI9ZNhqyjfCT4AOgCK4BGAYYCw/s1600/%25E9%25BA%25B5%25E5%25BA%2597.png",
        "menu": 0,
        "href": 0,
        "seat": "有"
    },
    {
        "id": 10,
        "name": "陽光早餐屋",
        "classes": "早餐",
        "times": "早餐",
        "drink": "另購",
        "image": "https://3.bp.blogspot.com/-8yCWDq668ls/WyoMKb6dDYI/AAAAAAAAkBQ/QSMSW8iuGi0t6kbZ_HiRVMjoee-OdWYHACK4BGAYYCw/s1600/%25E9%2599%25BD%25E5%2585%2589%25E6%2597%25A9%25E9%25A4%2590%25E5%25B1%258B.png",
        "menu": "https://4.bp.blogspot.com/-dU5UV1c-jho/WyylY-dSOEI/AAAAAAAAkJU/_KqCC2EVrGkbFuujb43zlUbLTPWeGT94QCK4BGAYYCw/s1600/%25E9%2599%25BD%25E5%2585%2589%25E6%2597%25A9%25E9%25A4%2590%25E5%25B1%258B.jpg",
        "href": 0,
        "seat": "無"
    },
    {
        "id": 11,
        "name": "南台肉粽の家",
        "classes": "肉粽、麵食、碗粿",
        "selfclean": "否",
        "image": "https://4.bp.blogspot.com/-MotviVwQSQA/WyoMIochyuI/AAAAAAAAkBI/401sIDQTVZEPnt2UMMZG-8Lhbf_MWpkFACK4BGAYYCw/s1600/%25E5%258D%2597%25E5%258F%25B0%25E8%2582%2589%25E7%25B2%25BD%25E7%259A%2584%25E5%25AE%25B6.png",
        "menu": 0,
        "href": 0,
        "seat": "有"
    },
    {
        "id": 12,
        "name": "辛新早餐店",
        "times": "早餐",
        "image": "https://2.bp.blogspot.com/-e8oFEaQTmOg/WyoMBif7NHI/AAAAAAAAkA0/HfmWnK8EY38XBPu9O8rhqLDQ9fpuzQTywCK4BGAYYCw/s1600/%25E8%25BE%259B%25E6%2596%25B0%25E6%2597%25A9%25E9%25A4%2590%25E5%25BA%2597.png",
        "menu": 0,
        "href": 0,
        "seat": "有"
    },
    {
        "id": 13,
        "name": "品味快餐",
        "classes": "便當",
        "phone": "06-2437913",
        "times": "午餐、晚餐",
        "image": "https://2.bp.blogspot.com/-UGwHFhvCXQY/WyoL9NhtUoI/AAAAAAAAkAs/_buVgu08wOcbY6JtZDSuLe956mNIJCmhQCK4BGAYYCw/s1600/%25E5%2593%2581%25E5%2591%25B3%25E5%25BF%25AB%25E9%25A4%2590.png",
        "menu": 0,
        "href": 0,
        "seat": "無"
    },
    {
        "id": 14,
        "name": "哈娜幸福廚房",
        "phone": "06-2433771",
        "image": "https://3.bp.blogspot.com/-_w0RJ0S8sHQ/WyoSTPDShRI/AAAAAAAAkC8/AZSxRCZXn8wGcV-xMz2uc4BG8aXDr48tACK4BGAYYCw/s1600/%25E5%2593%2588%25E5%25A8%259C%25E5%25B9%25B8%25E7%25A6%258F%25E5%25BB%259A%25E6%2588%25BF.png",
        "menu": "https://1.bp.blogspot.com/-UemH7qNVnes/WyylcK4yJRI/AAAAAAAAkJc/QZz-viujjsMZY2h8PJ-BAs3Ys_QZx7wVACK4BGAYYCw/s1600/%25E5%2593%2588%25E5%25A8%259C%25E5%25B9%25B8%25E7%25A6%258F%25E5%25BB%259A%25E6%2588%25BF.jpg",
        "href": 0
    },
    {
        "id": 15,
        "name": "馬來小館",
        "image": "https://4.bp.blogspot.com/-rBbRe8VYguQ/WyoL5K9XwkI/AAAAAAAAkAk/W7BB4zsTMtkycOYkDiVW9_kwq99EbAT7ACK4BGAYYCw/s1600/%25E9%25A6%25AC%25E4%25BE%2586%25E5%25B0%258F%25E9%25A4%25A8.png",
        "menu": 0,
        "href": 0
    },
    {
        "id": 16,
        "name": "原味館泡沫茶飲連鎖",
        "classes": "飲料",
        "drink": "他就是飲料店",
        "soup": "否",
        "selfclean": "不適用",
        "image": "https://3.bp.blogspot.com/-u8qTQKL-vWM/WyoLh5Qjm2I/AAAAAAAAkAY/jD0TX8JXY1s41ak6QSF7-nTEu9kEhglbACK4BGAYYCw/s1600/%25E5%258E%259F%25E5%2591%25B3%25E9%25A4%25A8%25E6%25B3%25A1%25E6%25B2%25AB%25E8%258C%25B6%25E9%25A3%25B2%25E9%2580%25A3%25E9%258E%2596.png",
        "menu": 0,
        "href": 0,
        "seat": "N/A"
    },
    {
        "id": 17,
        "name": "早! 洋蔥屋",
        "image": 0,
        "menu": 0,
        "href": 0,
        "seat": "無"
    },
    {
        "id": 18,
        "name": "老杜",
        "classes": "炒飯、燴飯、麵食",
        "times": "一~五 11:00~14:00 / 17:00~20:00",
        "drink": "是",
        "soup": "否",
        "selfclean": "否",
        "delivery": "null",
        "image": "https://1.bp.blogspot.com/-2OSYG3650lE/WyoLHoOO2mI/AAAAAAAAkAM/oRHD-oDj2gEjgKkRFikDNEp7RBSn16VdACK4BGAYYCw/s1600/%25E8%2580%2581%25E6%259D%259C.png",
        "menu": 0,
        "href": 0,
		"finalOne": 1
    }
]

@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html', toBuildSJson = toBuildSJson)

@app.route('/category')
def categorys():
	return render_template('categorys.html')

@app.route('/detail')
def detail():
	return render_template('detail.html')


if __name__ == '__main__':
	app.run(debug=True)










