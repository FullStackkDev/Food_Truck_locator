##
# **Food Truck Locator**

This web application allows users to find nearby food trucks based on their location or specific criteria. The application is built using Flask for the backend and JavaScript for the frontend.

## **Functionalities**

### **1. Get Nearby Food Trucks**

- Users can choose to get nearby food trucks based on either their geolocation or manually entered coordinates.
- If geolocation is selected, the browser's geolocation feature is used to retrieve the user's current location.
- If manual coordinates are selected, users can enter latitude and longitude values manually.
- User get nearby truck around 10

### **2. Filter Halal Carts**

- Users can filter food trucks to show only those offering halal options.
- The backend uses the Haversine formula to calculate distances.

### **3. Filter by Category**

- Users can filter food trucks based on predefined categories (e.g., hot dogs, coffee, beverages, vegan options, tacos).
- Add more categories according to need.
- An additional option allows users to filter halal food trucks within the selected category.

## **Project Structure**

- get\_nearby\_food\_truck.py: Flask application script containing API endpoints.
- static/: Static files (CSS, JavaScript).
- templates/: HTML templates.
- food-truck-data.csv: Sample food truck data in CSV format.
- README.md: Documentation on how to set up and run the application.

## **Technologies Used**

- Flask: Python web framework for the backend.
- JavaScript (AJAX): For dynamic interactions on the frontend.

## **Setup and Run**

1. **Clone the repository** :

git clone https://github.com/FullStackkDev/Food_Truck_locator.git food-truck-locator

**2. Navigate to the project directory:**

cd food-truck-locator

**3. Install dependencies:**

pip install -r requirements.txt

**4. Run the Flask application:**

python app.py

Open your web browser and go to[http://localhost:5000](http://localhost:5000/).

## **User Interface Design**

The user interface is designed for ease of use and clarity:

- Clean and simple layout.
- Form for selecting location options, categories, and halal filter.
- Buttons to trigger specific functionalities (Get Nearby Food Trucks, Filter Halal Carts, Filter by Category).
- Results are displayed below the form, showing relevant information about food trucks.

# Screenshots of task
- ![image](https://github.com/FullStackkDev/Food_Truck_locator/assets/36064269/9bd00422-0b28-4220-ad48-68dc27745df7)
- ![image](https://github.com/FullStackkDev/Food_Truck_locator/assets/36064269/74762560-5d70-47d6-b986-10732aaefffc)
- ![image](https://github.com/FullStackkDev/Food_Truck_locator/assets/36064269/be858b53-061f-41ca-af26-dbbbd46c2016)
- ![image](https://github.com/FullStackkDev/Food_Truck_locator/assets/36064269/f7199053-24fc-4188-8b5c-1a0c5e91f6cb)
- ![image](https://github.com/FullStackkDev/Food_Truck_locator/assets/36064269/b8a682a2-8648-4f57-bfa9-f45774edc7c6)

