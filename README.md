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

git clone : https://github.com/your-username/food-truck-locator.git

**2. Navigate to the project directory:**

cd food-truck-locator

**3. Install dependencies:**

pip install -r requirements.txtll -r requirem

**4. Run the Flask application:**

python app.py

Open your web browser and go to[http://localhost:5000](http://localhost:5000/).

## **User Interface Design**

The user interface is designed for ease of use and clarity:

- Clean and simple layout.
- Form for selecting location options, categories, and halal filter.
- Buttons to trigger specific functionalities (Get Nearby Food Trucks, Filter Halal Carts, Filter by Category).
- Results are displayed below the form, showing relevant information about food trucks.