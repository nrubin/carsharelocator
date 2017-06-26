pods = document.querySelectorAll(".pod");
data = {}
for (var i = 0; i < pods.length; i++) {
    var parking = {};
    var pod_container = pods[i];
    var parking_container = pod_container.querySelector(".pod_top");
    var parking_anchor = parking_container.querySelector(".pod_head > h4 > a");
    var parking_link = parking_anchor.href;
    parking["name"] = parking_anchor.innerText;
    parking["link"] = parking_link;
    parking["cars"] = [];
    var cars = pod_container.querySelectorAll(".pod_bot");
    for (var j = 0; j < cars.length; j++) {
        var car = {};
        car["image"] = cars[j].querySelector("div.list_left > div.v_img > img").src;
        car["name"] = cars[j].querySelector("div.list_left > div.v_name > h4").innerText;
        car["price"] = cars[j].querySelector("div.list_right > div.price > div > nobr > strong").innerText;
        var amenity_containers = cars[j].querySelectorAll("div.list_left > div.v_amenities > ul > li > img");
        var amenities = [];
        for (var k = 0; k < amenity_containers.length; k++) {
            amenities.push(amenity_containers[k].title);
        }
        car["amenities"] = amenities;
        parking["cars"].push(car);
    }
    data[parking_link] = parking;
}