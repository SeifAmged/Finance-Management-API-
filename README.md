
## **📝 Description**

A RESTful API built using Django REST Framework for managing financial transactions with user authentication via JSON Web Tokens (JWT). The API supports secure CRUD operations for transactions, filtering by categories, user-specific reports, and more.

## **✨Features**

- **🔐 JWT Authentication**: User login and token-based authentication for secure access.
- **💰Transaction Management**: Create, read, update, and delete financial transactions.
- **🏷Category Filtering**: Filter transactions by categories such as Groceries, Shopping, Travel, etc.
- **📈User Reports**: Generate financial reports for users based on specific date ranges.
- **🔧Easy Integration**: Fully RESTful API with JSON responses, suitable for integration with front-end applications.

## **🛠Installation**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/finance-api.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd finance-api
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access):**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

   The API will now be running at `http://127.0.0.1:8000/`.

## **📖Usage**

To access the API, you will need a valid JWT access token. Obtain a token by sending a POST request to the `/api/token/` endpoint with your username and password.

### **🔑 Authentication Workflow**

1. **Obtain Access and Refresh Tokens**

   - **Endpoint:** `/api/token/`
   - **Method:** `POST`
   - **Request Body:**

     ```json
     {
       "username": "your_username",
       "password": "your_password"
     }
     ```

   - **Response:**

     ```json
     {
       "access": "your_access_token",
       "refresh": "your_refresh_token"
     }
     ```

2. **Access Protected Endpoints**

   - Include the access token in the `Authorization` header of your requests:

     ```
     Authorization: Bearer your_access_token
     ```

3. **Refresh Access Token**

   - **Endpoint:** `/api/token/refresh/`
   - **Method:** `POST`
   - **Request Body:**

     ```json
     {
       "refresh": "your_refresh_token"
     }
     ```

   - **Response:**

     ```json
     {
       "access": "new_access_token"
     }
     ```

## **🌐 API Endpoints**

### **🔄 Transactions**

#### **List All Transactions**

- **Endpoint:** `/api/transactions/`
- **Method:** `GET`
- **Description:** Retrieve a list of all transactions. Requires authentication.
- **Response:**

  ```json
  [
    {
      "id": 1,
      "transaction_date": "2024-09-25",
      "description": "Bought groceries from supermarket",
      "amount": 100.50,
      "category": "groceries",
      "user": 1
    },
    {
      "id": 2,
      "transaction_date": "2024-09-26",
      "description": "Dinner at a local restaurant",
      "amount": 45.00,
      "category": "restaurant",
      "user": 1
    }
    // More transactions...
  ]
  ```

#### **Create a New Transaction**

- **Endpoint:** `/api/transactions/`
- **Method:** `POST`
- **Description:** Create a new transaction. Requires authentication.
- **Request Body:**

  ```json
  {
    "transaction_date": "2024-09-27",
    "description": "Monthly gym membership",
    "amount": 60.00,
    "category": "health",
    "user": 1
  }
  ```

- **Response:**

  ```json
  {
    "id": 3,
    "transaction_date": "2024-09-27",
    "description": "Monthly gym membership",
    "amount": 60.00,
    "category": "health",
    "user": 1
  }
  ```

#### **Retrieve a Specific Transaction**

- **Endpoint:** `/api/transactions/{id}/`
- **Method:** `GET`
- **Description:** Retrieve details of a specific transaction by its ID. Requires authentication.
- **Response:**

  ```json
  {
    "id": 1,
    "transaction_date": "2024-09-25",
    "description": "Bought groceries from supermarket",
    "amount": 100.50,
    "category": "groceries",
    "user": 1
  }
  ```

#### **Update a Transaction**

- **Endpoint:** `/api/transactions/{id}/`
- **Method:** `PUT`
- **Description:** Update an existing transaction's details. Requires authentication.
- **Request Body:**

  ```json
  {
    "transaction_date": "2024-09-25",
    "description": "Updated description",
    "amount": 105.00,
    "category": "groceries",
    "user": 1
  }
  ```

- **Response:** Returns the updated transaction details.

#### **Delete a Transaction**

- **Endpoint:** `/api/transactions/{id}/`
- **Method:** `DELETE`
- **Description:** Delete a transaction by its ID. Requires authentication.
- **Response:** Returns a success message upon deletion.

### **🏷 Categories**

#### **List All Categories**

- **Endpoint:** `/api/categories/`
- **Method:** `GET`
- **Description:** Retrieve a list of all available transaction categories.
- **Response:**

  ```json
  [
    "general",
    "groceries",
    "shopping",
    "restaurant",
    "transport",
    "travel",
    "entertainment",
    "utilities",
    "health",
    "services",
    "charity"
  ]
  ```

#### **List Transactions by Category**

- **Endpoint:** `/api/categories/{category_name}/transactions/`
- **Method:** `GET`
- **Description:** Retrieve all transactions under a specific category. Requires authentication.
- **Response:** Same format as the transactions list but filtered by the specified category.

### **👥 Users**

#### **List All Users**

- **Endpoint:** `/api/users/`
- **Method:** `GET`
- **Description:** Retrieve a list of all users. Requires admin privileges.
- **Response:**

  ```json
  [
    {
      "id": 1,
      "username": "Ahmed",
      "email": "ahmed@example.com"
    },
    {
      "id": 2,
      "username": "Noura",
      "email": "noura@example.com"
    }
    // More users...
  ]
  ```

#### **Retrieve User's Transactions**

- **Endpoint:** `/api/users/{user_id}/transactions/`
- **Method:** `GET`
- **Description:** Retrieve all transactions for a specific user. Requires authentication.
- **Response:** Same format as the transactions list but filtered by the specified user.

### **📊 Reports**

#### **Generate User Transaction Report**

- **Endpoint:** `/api/reports/`
- **Method:** `GET`
- **Description:** Generate a report of a user's transactions within a specific date range. Requires authentication.
- **Query Parameters:**
  - `user_id` (required)
  - `start_date` (optional) - Format: `YYYY-MM-DD`
  - `end_date` (optional) - Format: `YYYY-MM-DD`

- **Example Request:**

  ```
  GET /api/reports/?user_id=1&start_date=2024-09-01&end_date=2024-09-30
  ```

- **Response:**

  ```json
  {
    "user_id": 1,
    "total_amount": 500.00,
    "number_of_transactions": 10,
    "date_range": ["2024-09-01", "2024-09-30"],
    "transactions": [
      {
        "id": 1,
        "transaction_date": "2024-09-05",
        "description": "Bought groceries from supermarket",
        "amount": 100.50,
        "category": "groceries",
        "user": 1
      }
      // More transactions...
    ]
  }
  ```

## **⚠️Error Handling**

The API uses standard HTTP response codes to indicate the success or failure of an API request. Common error responses include:

- **400 Bad Request:** The request could not be understood or was missing required parameters.
- **401 Unauthorized:** Authentication failed or user does not have permissions for the desired action.
- **403 Forbidden:** Authentication succeeded but authenticated user does not have access to the requested resource.
- **404 Not Found:** The requested resource could not be found.
- 500 Internal Server Error:An error occurred on the server.

## **💻 Technologies Used**

- **Django**: High-level Python Web framework.
- **Django REST Framework**: Toolkit for building Web APIs.
- **SQLite**: Lightweight disk-based database for development.
- **JWT (JSON Web Tokens)**: For user authentication.
- **Django Filters**: For filtering querysets based on parameters.
- **Postman**: For API testing and development.

## **Setup and Configuration**

- **Dependencies:**

  All dependencies are listed in the `requirements.txt` file. Install them using:

  ```bash
  pip install -r requirements.txt
  ```

- **Migrations:**

  Ensure you run migrations to apply database schema:

  ```bash
  python manage.py migrate
  ```

- **Creating a Superuser (Optional):**

  If you need access to the Django admin interface:

  ```bash
  python manage.py createsuperuser
  ```

## **Testing the API with Postman**

- **Import the API Collection:**

  You can create and import a Postman collection to test the API endpoints.

- **Set Up Authentication:**

  Obtain the JWT access token and include it in the `Authorization` header for authenticated requests.

  ```
  Authorization: Bearer your_access_token
  ```

- **Example Request:**

  ```http
  GET http://127.0.0.1:8000/api/transactions/
  ```

  - **Headers:**

    ```
    Authorization: Bearer your_access_token
    ```

## **Contributing**

Contributions are welcome! Please fork the repository and submit a pull request.


