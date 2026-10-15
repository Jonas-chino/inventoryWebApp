# Overview

# Overview

As a software engineer, I am continually striving to deepen my understanding of server-side web development, Model-View-Template (MVT) architectures, and relational database management. To further these learning objectives, I developed **E-commerce store**, its a web application built using Python and the Django framework.

This application serves as an online digital storefront that allows users to browse available products, view detailed specifications, and complete simulated purchase orders. To run the web application locally on your computer, open your terminal in the project root directory and start the Django test server by executing:

```bash
python manage.py runserver
```

then use the link
http://127.0.0.1:8000/

# Web Pages

Product Catalog (/): This is the home page of the application. It dynamically queries the SQLite database using Django's ORM to retrieve all available products (Product.objects.all()). It then populates an HTML template, rendering each item with its name, description, price, and a link to view its specific details.

Product Detail Page (/product/<int:pk>/): When a user clicks on a product from the catalog, the application transitions to this dynamic detail view based on the product's unique primary key (pk). It displays the full item description, current price, and available stock. Additionally, it features an interactive form where the user can enter their name, email, and desired quantity to place an order. Submitting this form sends an HTTP POST request, which validates the input and saves a new Order record to the database.

Order Success Page (/order/success/<int:order_pk>/): Upon successfully completing a purchase, the app redirects the user to this confirmation page. It dynamically fetches the newly created order record from the database and displays a personalized success message along with a summary of the purchased item and customer details.

# Development Environment

IDE / Text Editor: Visual Studio Code (VS Code) for writing and managing Python and HTML code.

Programming Language: Python utilizing object-oriented programming principles and functional views.

Web Framework: Django (v6.0) for handling URL routing, HTTP requests/responses, and form processing.

Database: SQLite (integrated by default with Django) for persistent data storage of products and orders.

Version Control: Git for tracking code changes and source management.

# Useful Websites

- https://docs.djangoproject.com/en/6.1/
- https://developer.mozilla.org/es/docs/Learn_web_development/Extensions/Server-side/Django
- https://www.w3schools.com/django/django_intro.php

# Future Work

- Implement user authentication and accounts so customers can log in and view their personal order history.
- Add a multi-item shopping cart system to allow users to add multiple products before checking out.
- Item 3

```

```
