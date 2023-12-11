from flask import Flask, request, jsonify
import pandas as pd
from math import radians, sin, cos, sqrt, atan2

app = Flask(__name__)

# Load the dataset
food_truck_data = pd.read_csv('D:\\Django\\venv\\food-truck-data.csv')

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in kilometers
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

@app.route('/api/foodtrucks/nearby', methods=['GET'])
def get_nearby_food_trucks():
    try:
        lat = float(request.args.get('lat'))
        lon = float(request.args.get('lon'))
        radius = float(request.args.get('radius', 1))
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid parameters'}), 400

    # Filter food trucks within the specified radius
    nearby_food_trucks = []
    for index, row in food_truck_data.iterrows():
        truck_lat = row['Latitude']
        truck_lon = row['Longitude']
        distance = haversine(lat, lon, truck_lat, truck_lon)
        if distance <= radius:
            nearby_food_trucks.append({
                'name': row['Applicant'],
                'latitude': truck_lat,
                'longitude': truck_lon,
                'distance': distance
            })

    # Sort by distance and return the top 5
    nearby_food_trucks = sorted(nearby_food_trucks, key=lambda x: x['distance'])[:5]

    return jsonify({'food_trucks': nearby_food_trucks})

if __name__ == '__main__':
    app.run(debug=True)
