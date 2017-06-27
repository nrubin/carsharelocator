import requests
import json
from urllib import urlencode
import arrow
import random
from time import sleep
from collections import Counter

sample_getaround_url = "https://index.getaround.com/v1.0/search?product=web&uid=100004205511185&user_lat=37.7561438&user_lng=-122.43256819999999&viewport=37.740608%2C-122.465024%2C37.77168%2C-122.400112&start_time=2017-06-21T22%3A00%3A00.000Z&end_time=2017-06-22T06%3A00%3A00.000Z&properties=car_id,car_name,car_photo_v2,carkit_enabled,distance,latitude,longitude,make,model,postcode,price_daily,price_hourly,price_weekly,total_price,timezone,year,dedicated_parking&sort=best&page_sort=magic&page_size=500"
url_suffix = "&properties=car_id,car_name,car_photo_v2,carkit_enabled,distance,latitude,longitude,make,model,postcode,price_daily,price_hourly,price_weekly,total_price,timezone,year,dedicated_parking&sort=best&page_sort=magic"
url_prefix = "https://index.getaround.com/v1.0/search?product=web&"

#car_id

hours = [7, 11, 14, 19]
times = []
for i in range(7):
	for hour in hours:
		start_time = arrow.now().replace(minute=0,second=0,microsecond=0,weeks=+4,days=+i,hour=hour)
		end_time = start_time.replace(hours=+1)
		start_string = start_time.to('utc').format("YYYY-MM-DDTHH:00:00.000") + "Z"
		end_string = end_time.to('utc').format("YYYY-MM-DDTHH:00:00.000") + "Z"
		times.append([start_string,end_string])
# print times

latlngs = [{'lat': 37.7631435, 'lng': -122.41192940000002}, {'lat': 37.7494668, 'lng': -122.44277060000002}, {'lat': 37.7783076, 'lng': -122.41426100000001}, {'lat': 37.7515617, 'lng': -122.4335034}, {'lat': 37.774755, 'lng': -122.42992400000003}, {'lat': 37.75420099999999, 'lng': -122.42343499999998}, {'lat': 37.75420099999999, 'lng': -122.42343499999998}, {'lat': 37.7921445, 'lng': -122.40504390000001}, {'lat': 37.7594489, 'lng': -122.443805}]

urls = []
car_ids = []
for time in random.sample(times,5):
	for latlng in random.sample(latlngs,1):
		url_args = {}
		url_args["viewport"] = "37.706701,-122.514041,37.810776,-122.357179"
		url_args["uid"] = 100004205511185
		url_args["user_lat"] = latlng["lat"]
		url_args["user_lng"] = latlng["lng"]
		url_args["start_time"] = time[0]
		url_args["end_time"] = time[1]
		url_args["page_size"] = 10000
		url = url_prefix + urlencode(url_args) + url_suffix
		r = requests.get(url)
		cars = r.json()["cars"]
		for car in cars:
			car_ids.append(car["car_id"])

c = Counter(car_ids)
print c
cnt = 0
for key, val in c.iteritems():
	if val > 1:
		cnt += 1
print cnt
# viewport = urlencode({"viewport":"37.706701,-122.514041,37.810776,-122.357179"})
viewport = "viewport=37.740608%2C-122.465024%2C37.77168%2C-122.400112"
# print viewport
new_getaround_url = "https://index.getaround.com/v1.0/search?product=web&uid=100004205511185&user_lat=37.7561438&user_lng=-122.43256819999999&" + viewport + "&start_time=2017-06-21T22%3A00%3A00.000Z&end_time=2017-06-22T06%3A00%3A00.000Z" + url_suffix
# r = requests.get(new_getaround_url)
# cars = r.json()["cars"]
# print len(cars)
# print len(cars)
#getaround API seems to be open.
# r = requests.get("https://index.getaround.com/v1.0/search?product=web&uid=100004205511185&user_lat=37.7561438&user_lng=-122.43256819999999&viewport=37.740608%2C-122.465024%2C37.77168%2C-122.400112&start_time=2017-06-21T22%3A00%3A00.000Z&end_time=2017-06-22T06%3A00%3A00.000Z&properties=car_id,car_name,car_photo_v2,carkit_enabled,distance,latitude,longitude,make,model,postcode,price_daily,price_hourly,price_weekly,total_price,timezone,year,dedicated_parking&sort=best&page_sort=magic&page_size=500")
# cars = r.json()["cars"]
# coords = []
# for car in cars:
# 	coord = {"lat":car["latitude"],"long":car["longitude"]}
# 	coords.append(coord)
# print coords

# https://index.getaround.com/v1.0/search?product=web&
# uid=100004205511185&
# user_lat=37.7561438&
# user_lng=-122.43256819999999&
# viewport=37.740608%2C-122.465024%2C37.77168%2C-122.400112&
# start_time=2017-06-21T22%3A00%3A00.000Z&end_time=2017-06-22T06%3A00%3A00.000Z&
# properties=car_id,car_name,car_photo_v2,carkit_enabled,distance,latitude,longitude,make,model,postcode,price_daily,price_hourly,price_weekly,total_price,timezone,year,dedicated_parking&
# sort=best&
# page_sort=magic&
# page_size=500")

#strategy for parsing getaround
# their index takes a timeslot and GPS coords and a page size
# call max page size for a series of gps coords across SF, with a few different time stamps (weekends and weekdays, nights and mornings)
# how to get GPS coords? use a sample getaroudn request and take a sample of ~25 different lat/lngs (will be weighted by default)
# then playback the request for each of those. get another 10 lat/lngs from each request, and repeat, until no new cars are seen
# dates and times should be randomly generated (weekday and weekend times with a few different morning/evening times)
# if I do this enough times and don't break their API or get banned I can scan their entire vehicle DB


# Bottom right: 37.706701, -122.357179
# Top right: 37.810776, -122.357179
# Bottom left: 37.706701, -122.514041
# Top left: 37.810776, -122.514041
