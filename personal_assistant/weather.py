import requests
import time

rus = {
	''
}

# par = {
# 	"lang":"ru",
# 	"lat": 53,
# 	"lon": 30,
# 	"appid": "84061a2a5ff54b490d63bd38d557b06d",
# 	"units": "metric"
# }

print("Соединение с сервером...")
#http://api.openweathermap.org/geo/1.0/direct?q={703448}&limit={limit}&appid={API key}
#http://api.openweathermap.org/data/2.5/weather?q=Kyiv,uk&APPID=4e3618f6b30f226c0a29137c8cc0519d
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Kyiv,uk&APPID=4e3618f6b30f226c0a29137c8cc0519d')
#r_hourly = requests.get('http://api.openweathermap.org/data/2.5/forecast?', params = par)


""" CURRENT """

print("-------------------Погода сейчас-------------------")

data = r.json()
print('***********', end ='')
descript = data.get("weather")[0].get("description")
print(descript, end = '')
print('***********')

temp = data.get("main").get("temp")
#temp = round(1.8*(temp-273)+32)
#temp = round((5/9)*(temp-32))
print("Температура(*C)",temp)

hum = data.get("main").get("humidity")
print("Влажность", hum,"%")

wind_speed = data.get("wind").get("speed")
print('Скорость ветра', wind_speed)

"""BY HOURS"""

# print("-------------------На ближайшее время-------------------")

# forecast = r_hourly.json().get('list')[:5]

# for i in forecast:
# 	dt = i.get('dt_txt')
# 	print(dt,':')

# 	print("Будет {}".format(i.get("weather")[0].get("description")))
# 	print("Подробно:")
# 	print("	Температура:", i.get("main").get("temp"), "*C")
# 	print("	Влажность:",i.get("main").get("humidity"), "%")
# 	press = int(i.get("main").get("pressure"))
# 	print("	Давление(мм.рт.ст):", press/133)
# 	print("-----------------------------------------------------------------------------")


# print("Данные от openweathermap.org")
