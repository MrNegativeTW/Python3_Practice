# HW_P3
# Author / 10611171_李政霖
# Date / 20180915
# -----------------------------------------------
# 在 macOS 中的 Treminal 執行以獲得最佳體驗
# RUN IN macOS TREMINAL FOR BEST USER EXPERIENCE
# 需求 Python 3.7
# Require Python 3.7
# -----------------------------------------------
# Test Sentences / 
# the princess was speechless. she felt very sorry indeed that she had been so unkind to the frog.
# next, the frog drank from her little golden cup until it was quite empty.

# Clean Terminal Screen / 清除 Treminal 畫面
import os
os.system('clear')

# Let user enter sentences that need to convert / 讓使用者輸入要轉換的字串
print('Please Enter a sentence: (Ctrl+C to exit)')

# Save user enter into 'text' / 儲存輸入的字串到 text
text = str(input())

# If user enter number '0', end this program / 若輸入 0 則結束程式
while text != '0':
	# Split sentences/text by dot, save in otext / 使用句點分割句子，存於 otext
	otext = text.split('. ')
	# Remove dot and space / 移除句首和句尾的空格和句點
	trimmed = [
		sentence.strip()
		for sentence in otext
		]
	# Change first letter to upper / 句首變大寫
	upper = [
		sentence[0].upper() + sentence[1:]	
		for sentence in trimmed
		]
	# Add dot and space to final results / 加入句點和空格
	results = '. '.join(upper)
	# Print Final Result / 輸出最後結果
	print(results)
	# Let user can contiune enter sentence / 讓使用者繼續輸入
	text = str(input())