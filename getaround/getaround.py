import requests
import json
import urlparse

sample_getaround_url = "https://index.getaround.com/v1.0/search?product=web&uid=100004205511185&user_lat=37.7561438&user_lng=-122.43256819999999&viewport=37.740608%2C-122.465024%2C37.77168%2C-122.400112&start_time=2017-06-21T22%3A00%3A00.000Z&end_time=2017-06-22T06%3A00%3A00.000Z&properties=car_id,car_name,car_photo_v2,carkit_enabled,distance,latitude,longitude,make,model,postcode,price_daily,price_hourly,price_weekly,total_price,timezone,year,dedicated_parking&sort=best&page_sort=magic&page_size=500"

# query = urlparse.urlsplit(sample_getaround_url).query
# params = urlparse.parse_qs(query)
# print params

#getaround API seems to be open.
r = requests.get("https://index.getaround.com/v1.0/search?product=web&uid=100004205511185&user_lat=37.7561438&user_lng=-122.43256819999999&viewport=37.740608%2C-122.465024%2C37.77168%2C-122.400112&start_time=2017-06-21T22%3A00%3A00.000Z&end_time=2017-06-22T06%3A00%3A00.000Z&properties=car_id,car_name,car_photo_v2,carkit_enabled,distance,latitude,longitude,make,model,postcode,price_daily,price_hourly,price_weekly,total_price,timezone,year,dedicated_parking&sort=best&page_sort=magic&page_size=500")
cars = r.json()["cars"]
coords = []
for car in cars:
	coord = {"lat":car["latitude"],"long":car["longitude"]}
	coords.append(coord)
print coords

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
