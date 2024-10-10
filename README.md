# Part 1: System Design

## E-Commerce System

**File Name:** `part_1_system_design.py`

## Description
This project implements a simple E-Commerce system in Python. It enables users to create accounts, log in, manage orders, add or remove products from their cart, and process payments. The system effectively tracks users, products, and orders, providing a foundational experience for online shopping.

### Features
- **User Account Management**: Allows for user account creation and login.
- **Product Management**: Supports adding, removing, and updating product stock.
- **Order Management**: Facilitates order creation, completion, and updates.
- **Payment Processing**: Handles payment transactions for orders.

## Class Diagram
**File Name:** part_1_system_design(Class_Diagram).md

## Getting Started

### Prerequisites
- **Python 3.x**: Ensure Python is installed on your machine.
- **Visual Studio Code (VS Code)**: Recommended IDE for running the code.

### Running the Code in Visual Studio Code

#### For Windows

1. **Launch Visual Studio Code**: Open the application on your computer.

2. **Open the File**: Navigate to and open `Part_1_System_Design.py` in VS Code.

3. **Open the Terminal**: Access the terminal within VS Code by selecting `View > Terminal` from the menu.

4. **Run the Code**: In the terminal, execute the following command:

   For Window
   ```bash
   python Part_1_System_Design.py
   ```

   For MAC
   ```bash
   python3 Part_1_System_Design.py
   ```




# Part 2: Business Logic Implementation

## Inventory Management System

**File Name:** `part_2_business_logic_implementation.py`

### Description

This inventory management system tracks stock levels and manages restocking for a warehouse. It allows for processing sales orders and updating stock levels while providing alerts for items that need restocking.

## Features

- **Load Inventory**: Load initial products with their stock levels.
- **Process Orders**: Reduce stock levels based on incoming sales orders. Triggers restock alerts if stock levels fall below a specified threshold.
- **Restock Items**: Update stock levels for items that need restocking.

## Getting Started

### Prerequisites

- **Python 3.x**: Ensure Python is installed on your machine.
- **Visual Studio Code (VS Code)**: Recommended IDE for running the code.

### Running the Code in Visual Studio Code

#### For Windows

1. **Launch Visual Studio Code**: Open the application on your computer.

2. **Open the File**: Navigate to and open `part_2_business_logic_implementation.py` in VS Code.

3. **Open the Terminal**: Access the terminal within VS Code by selecting `View > Terminal` from the menu.

4. **Run the Code**: In the terminal, execute the following command:

   ```bash
   python part_2_business_logic_implementation.py

   ```

   For MAC
   ```bash
   python3 Part_1_System_Design.py
   ```


# Part 3: Database Query Handling

## Online Bookstore Database Queries

**File Name:** `part_3_database_query_handling.sql`

## Description
This repository contains SQL queries designed for managing and analyzing data within an online bookstore's relational database. The schema comprises four main tables: **Customers**, **Books**, **Orders**, and **OrderDetails**. The provided queries address specific business requirements, such as identifying top customers, calculating author revenue, and finding popular books based on order quantities.

### Database Schema
- **Customers**: Contains customer information (ID, name, email).
- **Books**: Contains book details (ID, title, author, price).
- **Orders**: Contains order information (ID, customer ID, order date).
- **OrderDetails**: Connects orders to books and tracks quantities.

### Queries Included
1. **Top 5 Customers**: Retrieves the top 5 customers who have purchased the most books (by total quantity) over the last year.
2. **Total Revenue by Author**: Calculates total revenue generated from book sales by each author.
3. **Books Ordered More Than 10 Times**: Lists all books that have been ordered more than 10 times, along with the total quantity ordered for each book.

## How to Run in MySQL Workbench

### Prerequisites
- MySQL Server installed.
- MySQL Workbench installed.
- Appropriate permissions to create databases and tables.

### Steps to Execute the Queries

1. **Create the Database and Use It**:
   - Open MySQL Workbench.
   - Execute the command to create and select the database:
     ```sql
     CREATE DATABASE OnlineBookstore;
     USE OnlineBookstore;
     ```

2. **Create Tables**:
   - The necessary table structures are defined in the `part_3_database_query_handling.sql` file. Execute this file to create the tables.

3. **Insert Sample Data**:
   - Sample data insertion commands are also included in the same SQL file. Execute it to populate the tables.

4. **Run the Queries**:
   - The queries to retrieve the desired information are included in the `part_3_database_query_handling.sql` file. Execute these queries to get insights.

## How to Run in an Online SQL Editor

1. Copy the SQL code from the `part_3_database_query_handling.sql` file.
2. Open any online SQL editor that supports MySQL.
3. Paste the code into the editor.
4. Execute the code to create the database, tables, insert data, and run the queries.

