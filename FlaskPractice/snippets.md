# GasPricePerKm
## 依照可用公里數讓文字變色
				{% if result <= 25 %}
					<h3 style="color: #FF4136">{{ result }} 公里</h3>
				{% elif result > 25 and result < 50 %}
					<h3 style="color: #FFDC00">{{ result }} 公里</h3>
				{% elif result >= 50 %}
					<h3 style="color: #01FF70">{{ result }} 公里</h3>
				{% else %}
					<h3>很多公里</h3>
				{% endif %}