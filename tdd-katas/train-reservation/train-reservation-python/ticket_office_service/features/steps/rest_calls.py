import urllib.request
import json

url = "http://127.0.0.1:8081"

def book_seats(train_id, seats, booking_reference):
    form_data = {"train_id": train_id, "seats": json.dumps(seats), "booking_reference": booking_reference}
    data = urllib.parse.urlencode(form_data)
    req = urllib.request.Request(url + "/reserve", bytes(data, encoding="ISO-8859-1"))
    return json.loads(urllib.request.urlopen(req).read().decode("utf-8"))

def get_data_for(train_id):
    train_data = urllib.request.urlopen(url + "/data_for_train/" + train_id)
    return json.loads(train_data.read().decode("utf-8"))