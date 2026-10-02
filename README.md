# Django E-Commerce Web Application

A full-stack e-commerce web application developed using Django and Python.

## Features

- User Registration and Login
- User Logout
- Product Listing
- Product Details
- Product Search
- Product Category Filtering
- Shopping Cart
- Increase/Decrease Cart Quantity
- Remove Products from Cart
- Checkout System
- Cash on Delivery Payment
- Order Creation
- My Orders
- Order Status Tracking
- Product Stock Management
- Django Admin Panel
- Form Validation
- Automated Unit Tests
- Responsive Web Interface

## Technologies Used

- Python
- Django
- HTML5
- CSS3
- SQLite
- Django Templates
- Git
- GitHub

## Project Structure

```text
ecommerce/
│
├── ecommerce/
├── store/
├── users/
├── product/
├── templates/
├── venv/
├── manage.py
└── README.md
How to Run the Project
1. Clone the repository
git clone <repository-url>

2. Open the project folder
cd ecommerce

3. Create and activate virtual environment
python -m venv venv

Windows PowerShell:
venv\Scripts\Activate.ps1

4. Install Django
pip install django

5. Apply migrations
python manage.py migrate

6. Run the development server
python manage.py runserver

Open:
http://127.0.0.1:8000/

Testing
Run the automated tests using:
python manage.py test

The project includes tests for:
- Product creation
- Cart item creation
- Order creation
Admin Panel
Django Admin is used to manage:
- Products
- Cart Items
- Orders
- Order Status
- Product Stock
Admin URL:
http://127.0.0.1:8000/admin/

Application Flow
User Registration/Login
        ↓
Browse Products
        ↓
Search / Filter Products
        ↓
View Product Details
        ↓
Add Product to Cart
        ↓
Manage Cart
        ↓
Checkout
        ↓
Cash on Delivery
        ↓
Order Created
        ↓
Stock Updated
        ↓
View My Orders

Future Enhancements
- Online Payment Gateway
- Wishlist
- Product Reviews and Ratings
- Email Order Notifications
- User Profile Management
- Advanced Product Filtering
- Order Cancellation
- Deployment to Cloud
Developer
R Prudvi Paul
B.Tech Computer Science Engineering
GitHub: Prudvi1432

