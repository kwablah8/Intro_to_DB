import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="Ek290401$", database="School"
    )

    print("Successfully connected to the database")

    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
    print("Database 'alx_book_store' created successfully!")

    mycursor.execute("USE alx_book_store")

    create_Books = """
CREATE TABLE Books (
    book_id PRIMARY KEY,
    title VARCHAR(130),
    author_id,
    price DOUBLE,
    publication_date DATE,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);
"""
    mycursor.execute(create_Books)
    print("Table 'Books' created successfully!")

    create_Authors = """
CREATE TABLE Authors (
    author_id PRIMARY KEY,
    author_name VARCHAR(215)
);
"""
    mycursor.execute(create_Authors)
    print("Table 'Authors' created successfully!")

    create_Customers = """
CREATE TABLE Customers (
    customer_id PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT
);
"""
    mycursor.execute(create_Customers)
    print("Table 'Customers' created successfully!")

    create_Orders = """
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);
"""
    mycursor.execute(create_Orders)
    print("Table 'Orders' created successfully!")

    create_Order_Details = """CREATE TABLE Order_Details (
    orderdetailid PRIMARY KEY,
    order_id,
    book_id INT,
    quantity DOUBLE,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);
"""
    mycursor.execute(create_Order_Details)
    print("Table 'Order_Details' created successfully!")

    if mydb.is_connected():
        print("✅ Connected to the database successfully.")

except Error as e:
    print("Error:", e)

if mycursor:
    mycursor.close()
if mydb.is_connected():
    mydb.close()
    print("Database connection closed.")
