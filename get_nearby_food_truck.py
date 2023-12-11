from flask import Flask, render_template, request, jsonify
import pandas as pd
from math import radians, sin, cos, sqrt, atan2

app = Flask(__name__)

# Load the dataset
food_truck_data = pd.read_csv('https://raw.githubusercontent.com/RAKT-Innovations/P1-django-take-home-assignment/main/food-truck-data.csv')

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # radius of earth km
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/foodtrucks/nearby', methods=['GET'])
def get_nearby_food_trucks():
    
    try:
        lat = float(request.args.get('lat'))
        lon = float(request.args.get('lon'))
        radius = float(request.args.get('radius', 2))
        halal_filter = request.args.get('halal', '').lower() == 'true'
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid parameters'}), 400
    
    # filter trucks within the specified range of distance 
    nearby_food_trucks = []
    for index, row in food_truck_data.iterrows():
        truck_lat = row['Latitude']
        truck_lon = row['Longitude']
        distance = haversine(lat, lon, truck_lat, truck_lon)

        # Check if 'FoodItems' and 'Applicant' are strings before applying 'lower()'
        food_items_lower = row['FoodItems'].lower() if isinstance(row['FoodItems'], str) else ''
        applicant_lower = row['Applicant'].lower() if isinstance(row['Applicant'], str) else ''

        # Apply filters based on distance and halal
        if distance <= radius and (not halal_filter or 'halal' in food_items_lower or 'halal' in applicant_lower):
            nearby_food_trucks.append({
                'name': row['Applicant'],
                'latitude': truck_lat,
                'longitude': truck_lon,
                'distance': distance,
                'food_items': row['FoodItems'].split(', ') if isinstance(row['FoodItems'], str) else [],
                'location_description': row['LocationDescription']
            })

    # Sort by distance and return the top 10
    nearby_food_trucks = sorted(nearby_food_trucks, key=lambda x: x['distance'])[:10]

    return jsonify({'food_trucks': nearby_food_trucks})
  
 # endpoint of Halal carts
@app.route('/api/foodtrucks/filter/halal', methods=['GET'])
def filter_halal_carts():
   
    # Check if 'FoodItems' and 'Applicant' columns exist
    if 'FoodItems' not in food_truck_data.columns or 'Applicant' not in food_truck_data.columns:
        return jsonify({'error': 'FoodItems or Applicant column not found in the dataset'}), 500

    # Filter rows where 'halal' is in 'FoodItems' or 'Applicant' (case-insensitive)
    halal_carts = food_truck_data[food_truck_data['FoodItems'].str.contains('halal', case=False) | 
                                  food_truck_data['Applicant'].str.contains('halal', case=False)]

    halal_carts_data = []
    for index, row in halal_carts.iterrows():
        distance = haversine(row['Latitude'], row['Longitude'], 0, 0)
        halal_carts_data.append({
            'name': row['Applicant'],
            'latitude': row['Latitude'],
            'longitude': row['Longitude'],
            'food_items': row['FoodItems'].split(', ') if isinstance(row['FoodItems'], str) else [],
            'distance': distance,  # distance calculation
            'location_description': row['LocationDescription']
        })
        halal_carts_data = sorted(halal_carts_data, key=lambda x: x['distance'])

    return jsonify({'food_trucks': halal_carts_data})
  
 # categories defined here 
 
@app.route('/api/foodtrucks/filter/category', methods=['GET'])
def filter_by_category():
    category = request.args.get('category', '').lower()
    halal = request.args.get('halal', '').lower() == 'true'
    if not category:
        return jsonify({'error': 'Category parameter is required'}), 400

        # Filter rows where the specified category is in 'FoodItems' (case-insensitive)
    category_food_trucks = food_truck_data[food_truck_data['FoodItems'].notna() &
                                          food_truck_data['FoodItems'].str.lower().str.contains(category, case=False)]
    
    if halal:
    # Additional filter for halal trucks
        category_food_trucks = category_food_trucks[
            (category_food_trucks['FoodItems'].str.lower().str.contains('halal', case=False)) |
            (category_food_trucks['Applicant'].str.lower().str.contains('halal', case=False))
        ]
    category_food_trucks_data = []
    for index, row in category_food_trucks.iterrows():
        category_food_trucks_data.append({
            'name': row['Applicant'],
            'latitude': row['Latitude'],
            'longitude': row['Longitude'],
            'food_items': row['FoodItems'].split(', ') if isinstance(row['FoodItems'], str) else [],
            'distance': haversine(row['Latitude'], row['Longitude'], 0, 0)  # Distance calculation
            
        })

    return jsonify({'food_trucks': category_food_trucks_data})

if __name__ == '__main__':
    app.run(debug=True)
