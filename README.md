## 🌍 Flask IP Geolocation Tracker with Map Visualization

This project is a web application built with **Flask**, **GeoLite2**, **MongoDB**, and **Leaflet.js** that allows users to:

- Lookup location details for any IPv4 address.
- Store and retrieve the search history in MongoDB.
- Visualize IP locations interactively on a Leaflet map.

---

## 🔧 Features

- **IP Address Lookup:**  
  Enter any valid IPv4 address (format `000.000.000.000`) to get:  
  • City, Country, Postal Code  
  • Latitude and Longitude coordinates  
  • Timestamp of the query

- **Search History:**  
  This page shows the scope of the project, one of the multiple functionalities that can be added
  -View a complete list of past IP searches stored in the MongoDB database.

- **Interactive Map:**  
  Visualize the geolocation of the searched IP using **Leaflet.js** with dynamic centering and marker placement.

- **User-friendly UI:**  
  Clean forms and buttons with consistent styling.

---

## 🛠️ Tech Stack

- **Backend:** `Flask` (Python)  
- **Database:** `MongoDB`  
- **Geolocation:** MaxMind GeoLite2 City database with `geoip2` Python library  
- **Frontend:** HTML, CSS, Bootstrap, `Leaflet.js` for interactive maps  
- **Form Handling:** WTForms  
- **Others:** `pymongo` for MongoDB connection

---

## 📁 Project Structure

├── templates/
│ ├── base.html # Base layout template
│ ├── loc_form.html # IP lookup form and results page
│ ├── history.html # Search history display
│ ├── map.html # Leaflet map visualization page
├── example_2.py # Flask app routes and logic
├── forms.py # WTForms for IP input validation
├── GeoLite2-City_20200211/ # MaxMind GeoLite2 City database
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## 📷 Output Preview

![get_location_1_USA](https://github.com/user-attachments/assets/3f8cbf34-20a9-4e5f-8937-162f4f60c574)
![get_location_2_Canada](https://github.com/user-attachments/assets/2479e13f-fb27-4aa1-978c-82afcc455685)
![get_location_3_China](https://github.com/user-attachments/assets/44bfed72-09d4-4a92-a333-df6ebb8f592b)


---
