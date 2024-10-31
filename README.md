### Flask-PostgreSQL Unique Fruits API

##Team Members: Madison Lenz, Destani Ford

This project demonstrates how to integrate Flask with PostgreSQL and display unique items from two database tables in an HTML table. It includes two endpoints:



/api/update_basket_a: Inserts a new fruit entry into basket_a and displays a success or error message.


/api/unique: Displays unique fruits from basket_a and basket_b in an HTML table, or an error message if applicable.



---


#Quick Start Prerequisites
Ensure you have PostgreSQL installed and running, with two tables (basket_a and basket_b) copied this code:

```sql
CREATE TABLE basket_a (
    a INT PRIMARY KEY,
    fruit_a VARCHAR (100) NOT NULL
);



CREATE TABLE basket_b (
    b INT PRIMARY KEY,
    fruit_b VARCHAR (100) NOT NULL
);

```
---


```sql
INSERT INTO basket_a (a, fruit_a)
VALUES
    (1, 'Apple'),
    (2, 'Orange'),
    (3, 'Banana'),
    (4, 'Cucumber');
    

INSERT INTO basket_b (b, fruit_b)
VALUES
    (1, 'Orange'),
    (2, 'Apple'),
    (3, 'Watermelon'),
    (4, 'Pear');
```
    
### Local Test Setup


#Install a Python 3 Virtual Environment:
```
sudo apt-get install python3-venv
```
#Create and Activate the Virtual Environment.
```
python3 -m venv python_venv
```
```
source python_venv/bin/activate
```

#Install Project Requirements.
```
pip install wheel
```
```
pip install -r requirements.txt
```

#Run the Server.

```
python main.py
```
View unique fruits by typing this into the browser's httml bar:


127.0.0.1:5000/api/unique
