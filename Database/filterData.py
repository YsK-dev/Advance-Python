import mysql.connector

# Establish a connection to the MySQL database
db = mysql.connector.connect(
    host="localhost",       # Database server address
    user="root",           # Database username
    password="Asd171307.", # Database password
    database="yskweb"      # Database name
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Example SQL queries (commented out for now)
# sql=("SELECT * FROM products WHERE id=1")                     # Select product with id=1
# sql=("SELECT * FROM products WHERE id>=1")                    # Select products with id >= 1
# sql=("SELECT * FROM products WHERE name='Iphone 17' or price='200'")  # Select products with name 'Iphone 17' or price '200'
# sql=("SELECT * FROM products WHERE name LIKE '%Iphone%'")     # Select products with 'Iphone' in the name
# sql=("SELECT * FROM products WHERE name LIKE 'Xiaomi%'")      # Select products with names starting with 'Xiaomi'
# sql=("SELECT * FROM products WHERE name LIKE '%Samsung' ")    # Select products with names ending with 'Samsung'
# sql=("SELECT * FROM products WHERE name LIKE '%Samsung' and description LIKE '%phone%' ")  # Select Samsung products with 'phone' in the description

# Define a function to fetch products by their ID
def getProductsbyId(id):
    # SQL query to select all columns from the 'products' table where the id matches the provided parameter
    sql = "SELECT * FROM products WHERE id=%s"
    
    # Parameters to pass into the SQL query (to prevent SQL injection)
    params = (id,)  # Note: The comma is required to make it a tuple
    
    # Execute the SQL query with the provided parameters
    cursor.execute(sql, params)
    
    # Fetch all rows returned by the query
    filteredResult = cursor.fetchall()
    
    # Print the fetched results
    print(filteredResult)

# Call the function to get products with id=7
getProductsbyId(7)

# Close the cursor and database connection to free up resources
cursor.close()
db.close()