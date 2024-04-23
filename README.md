# Cafe Billing System

## Overview

This project is a simple billing system developed using Python's Tkinter library and SQLite database. It is designed for a cafe shop named **_"The Urban Cafe and Krispy Chicken."_** The system allows users to select food and drink items, calculate the total bill, and save the order details to a database.

## Features

- **User-friendly GUI**: The graphical user interface (GUI) is built using Tkinter, making it easy to use.
  
- **Image Representation**: Food and drink items are visually represented using images to enhance user experience.
  
- **Database Integration**: The system uses SQLite to store order details, making it easy to retrieve and manage records.
  
- **Dynamic Billing**: The total bill is calculated dynamically based on the selected items, and a unique order ID is generated for each order.
  
- **Discount Option**: Although not fully implemented in the current version, there is provision to apply discounts to the total bill.

## Prerequisites

- Python 3.12.2
- Tkinter library
- PIL (Pillow) library
- SQLite3 library

## Usage

1. Launch the application by running `cafe.py`.
2. Select the desired quantity of each food and drink item using the dropdown menus.
3. Click the `Order` button to generate a unique order ID.
4. Click the `Calculate` button to view the total bill and order details.
5. Optionally, apply a discount to the total bill (not fully implemented).
6. Click the `Save` button to save the order details to the database.
7. Click the `Clear` button to reset the order form.
8. Click the `View` button to retrieve and view the saved records using `records.py`.

## Screenshots

![cafe](https://github.com/diwasbk/cafe-billing-system/assets/167800132/015281d9-1f15-4fc6-9de2-f91a798ca073)


