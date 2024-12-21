**SmartRecipeAssistant**, based on the structure and code provided for managing ingredients, recipes, and inventory. You can customize it further as per your requirements.

---

# SmartRecipeAssistant

**SmartRecipeAssistant** is a backend system built with Django and Django REST Framework (DRF) that helps manage ingredients, track inventory, and recommend recipes based on available ingredients. The project includes functionalities to add, update, and remove ingredients from the inventory, store favorite recipes, and a flexible API to retrieve recipes based on ingredient availability.

---





## Features

- **Ingredient Management**: Add, update, and remove ingredients in the inventory.
- **Recipe Management**: Add and retrieve recipes with details like taste, cuisine type, preparation time, and ingredients.
- **Inventory Tracking**: Keep track of inventory changes with action logs (add/remove).
- **APIs for CRUD Operations**: Use REST APIs to interact with ingredients, recipes, and inventory logs.

---

## Installation

### Prerequisites

Before setting up the project, ensure you have the following installed:

- Python 3.x
- pip (Python package installer)
- Django
- Django REST Framework

### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone <your-repository-url>
cd SmartRecipeAssistant
```

### Step 2: Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### Step 3: Set up the Database

Run the following commands to set up the database and apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 4: Run the Development Server

Run the development server using:

```bash
python manage.py runserver
```

The server should now be running at `http://127.0.0.1:8000/`.

---

## API Endpoints

The application exposes several RESTful endpoints for managing ingredients, recipes, and inventory logs.

### Ingredient Management

- **GET /api/inventory-items/**  
  Retrieve all inventory items (ingredients).

- **POST /api/inventory-items/**  
  Add a new inventory item (ingredient).

  Example Request Body:
  ```json
  {
      "name": "Eggs",
      "quantity": "5",
      "unit": "pieces"
  }
  ```

- **PUT /api/inventory-items/{id}/**  
  Update an existing inventory item.

- **DELETE /api/inventory-items/{id}/**  
  Remove an inventory item.

### Recipe Management

- **GET /api/dishes/**  
  Retrieve all saved recipes.

- **POST /api/dishes/**  
  Add a new recipe.

  Example Request Body:
  ```json
  {
      "name": "Pancakes",
      "ingredients": "Eggs, Milk, Flour, Sugar, Baking Powder",
      "instructions": "Mix ingredients and cook on a hot pan.",
      "cuisine_type": "American",
      "taste": "Sweet",
      "reviews": "Delicious!",
      "prep_time": 15
  }
  ```

- **PUT /api/dishes/{id}/**  
  Update an existing recipe.

- **DELETE /api/dishes/{id}/**  
  Remove a recipe.

### Inventory Update Log

- **GET /api/inventory-update-logs/**  
  Retrieve the logs of inventory updates (add/remove).

- **POST /api/inventory-update-logs/**  
  Add a new inventory update (e.g., after shopping or cooking).

---

## Project Structure

Here’s an overview of the project structure:

```
SmartRecipeAssistant/
    manage.py                    # Django management script
    SmartRecipeAssistant/         # Project configuration folder
        settings.py               # Project settings
        urls.py                   # URL routing for the project
        wsgi.py                   # WSGI entry point
    inventory_manager/            # Main app for managing inventory and recipes
        __init__.py               # Package initialization
        models.py                 # Database models (InventoryItem, Dish, InventoryUpdateLog)
        views.py                  # API views for inventory and recipes
        serializers.py            # Serializers for API responses
        urls.py                   # URL routing for inventory-related endpoints
    requirements.txt              # List of dependencies (Django, DRF, etc.)
```

---

## Technologies Used

- **Django**: A high-level Python web framework.
- **Django REST Framework (DRF)**: A powerful toolkit for building Web APIs.
- **SQLite**: Default database for development (can be swapped with other databases).

---

## Future Enhancements

- **OCR Integration**: Ability to input recipes from images.
- **Chatbot Integration**: Implement an LLM-powered chatbot to suggest recipes based on available ingredients.
- **User Authentication**: Add user authentication to allow personalized recipe suggestions.

---


