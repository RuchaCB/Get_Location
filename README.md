## 🌍 Flask IP Geolocation Tracker with Map Visualization
This project is a web application built with Flask, GeoLite2, MongoDB, and Leaflet.js that allows users to:
Lookup location details for any IPv4 address.
Store and retrieve the search history in MongoDB.
Visualize IP locations interactively on a Leaflet map.

## 🔧 Features
IP Address Lookup: Enter any valid IPv4 address (format 000.000.000.000) to get:
City, Country, Postal Code
Latitude and Longitude coordinates
Timestamp of the query
Search History: View a complete list of past IP searches stored in the MongoDB database.
Interactive Map: Visualize the geolocation of the searched IP using Leaflet.js with dynamic centering and marker placement.
User-friendly UI: Clean forms and buttons with consistent styling.

## 🛠️ Tech Stack
Backend: `Flask` (Python)
Database: `MongoDB`
Geolocation: MaxMind GeoLite2 City database with geoip2 Python library
Frontend: HTML, CSS, Bootstrap, `Leaflet.js` for interactive maps
Form Handling: WTForms
Others: pymongo for MongoDB connection

## 📁 Project Structure

├── templates/
│   ├── base.html           # Base layout template
│   ├── loc_form.html       # IP lookup form and results page
│   ├── history.html        # Search history display
│   ├──map.html            # Leaflet map visualization page
├── example_2.py                  # Flask app routes and logic
├── forms.py                # WTForms for IP input validation
├── GeoLite2-City_20200211/ # MaxMind GeoLite2 City database
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
## 📷 Output Preview
