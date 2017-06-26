import requests

#getaround API seems to be open.
# r = requests.get("https://index.getaround.com/v1.0/search?product=web&uid=100004205511185&user_lat=37.7561438&user_lng=-122.43256819999999&viewport=37.740608%2C-122.465024%2C37.77168%2C-122.400112&start_time=2017-06-21T22%3A00%3A00.000Z&end_time=2017-06-22T06%3A00%3A00.000Z&properties=car_id,car_name,car_photo_v2,carkit_enabled,distance,latitude,longitude,make,model,postcode,price_daily,price_hourly,price_weekly,total_price,timezone,year,dedicated_parking&sort=best&page_sort=magic&page_size=500")

#enterprise API is a PHP endpoint that requests form data
data = {"start_date":"06/21/17","start_time":"61200","end_date":"06/21/17","end_time":"68400",}
headers = {}
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
headers["Host"]= "reserve.enterprisecarshare.com"
headers["Origin"]= "https://reserve.enterprisecarshare.com"
headers["Referer"]= "https://reserve.enterprisecarshare.com/"
# headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
cookies = {"AMCVS_30545A0C536B768C0A490D44%40AdobeOrg":"1","AMCV_30545A0C536B768C0A490D44%40AdobeOrg":"-1330315163%7CMCIDTS%7C17339%7CMCMID%7C48605311736134434352568213763788726018%7CMCAAMLH-1498689286%7C9%7CMCAAMB-1498689286%7CNRX38WO0n5BH8Th-nqAG_A%7CMCOPTOUT-1498091686s%7CNONE%7CMCAID%7CNONE","IR_PI":"1498084486931-1lwbgbzaeds","sid":"crvqndnh3kfh4q7ep1e9g50s95","s_intCmp":"%5B%5BB%5D%5D","s_sq":"%5B%5BB%5D%5D","CSRF-token-oerjoijtr0mtrg0m34kl45082nh4nj4":"3683ceff81","MVSessionExpire":"15","MVSessionCountdown":"60","IR_4720":"1498087468364%7C0%7C1498084486931","s_pers":"%20s_vs%3D1%7C1498089268567%3B%20gpv_v5%3D%252F%7C1498089268574%3B%20s_visit%3D1%7C1498089268580%3B","s_pvs":"%5B%5BB%5D%5D","s_tps":"%5B%5BB%5D%5D","s_cc":"true","__CT_Data":"gpv=3&apv_16674_www03=3&cpv_16674_www03=3","s_sess":"%20SC_LINKS%3D%3B%20s_ppvl%3D%252F%252C96%252C96%252C798%252C1440%252C404%252C1440%252C900%252C2%252CL%3B%20s_ptc%3D0.00%255E%255E0.01%255E%255E0.01%255E%255E0.13%255E%255E4.33%255E%255E0.07%255E%255E0.72%255E%255E0.07%255E%255E5.36%3B%20s_ppv%3D%252F%252C49%252C49%252C404%252C1440%252C404%252C1440%252C900%252C2%252CL%3B"}
r = requests.post("https://reserve.enterprisecarshare.com/results.php",data=data,headers=headers,cookies=cookies)

print r.text