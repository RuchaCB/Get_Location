from flask import Flask, render_template, redirect, request
from form import LocationForm, DatesForm   
from pymongo import MongoClient, DESCENDING  
import pymongo 
import os
import geoip2.database
from datetime import datetime  
from flask_wtf import Form
#from wtforms.fields.html5 import DateField
#from wtforms.fields import DateField

app = Flask(__name__)
app.config['SECRET_KEY']='Hello'

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase1"]
mycol = mydb["users"]
lat_lan=[]
    
@app.route('/', methods=['GET', 'POST'])
def get_loc():
    location = LocationForm()
    ip = request.values.get("ip")
    details = []
    lat_lan[:] = []

    if ip:
        try:
            reader = geoip2.database.Reader("./GeoLite2-City_20200211/GeoLite2-City.mmdb")
            response = reader.city(str(ip)) 

            city = response.city.name or "N/A"
            code = response.postal.code or "N/A"
            country = response.country.name or "N/A"
            lat = response.location.latitude
            lon = response.location.longitude
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            record = {
                "ip": ip,
                "time": time,
                "Country Name": country,
                "Postal Code": code,
                "City Name": city,
                "latitude": lat,
                "longitude": lon
            }

            mycol.insert_one(record)
            details.append(record)

            lat_lan.extend([lat, lon])

        except Exception as e:
            print("GeoIP Lookup Error:", e)

    return render_template('loc_form.html', form=location, location_detail=details)

    
@app.route('/map', methods=['GET', 'POST'])
def map():
    # Make sure lat_lan has valid coordinates
    if len(lat_lan) < 2:
        # Default to some coordinates if none
        lat, lon = 0, 0
    else:
        lat, lon = lat_lan[0], lat_lan[1]
    return render_template('map.html', latitude=lat, longitude=lon)
    

@app.route("/history", methods = ['GET', 'POST'])
def history():
    dates = DatesForm()
    start_date = request.values.get("start_date")
    end_date = request.values.get("end_date")
    last_n = request.values.get("last_n")
    data =[]
    data_last_n = []
    for x in mycol.find():
        try:
            date_time = (str(x['time']).split())
            date_1 = datetime.strptime(start_date, '%Y-%m-%d')
            date_2 = datetime.strptime(end_date, '%Y-%m-%d')
            date_3 = datetime.strptime(date_time[0], '%Y-%m-%d')
            if (date_1 < date_3 < date_2):
                data.append({"ip:":x["ip"], "Contry:": x["Country Name"], "City:":x["City Name"], "Lattitude:": x["latitude"],"Longitude:" :x["longitude"]})
        except:
            continue

    mydoc = mycol.find().sort('time', pymongo.DESCENDING)
    if last_n == None or last_n == '' :
        last_n = 0
    else:
        last_n = int(last_n)
    for x in mydoc[:last_n]:
        data_last_n.append({"ip:":x["ip"], "Contry:": x["Country Name"], "City:":x["City Name"], "Lattitude:": x["latitude"],"Longitude:" :x["longitude"]})

    return render_template('history.html', form=dates, start_date= start_date, end_date=end_date, data=data, data_last_n=data_last_n )

if __name__ == "__main__":
    app.run()
