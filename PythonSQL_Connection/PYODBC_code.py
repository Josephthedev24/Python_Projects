import pyodbc
ConnectionString = (
    'Driver={ODBC Driver 17 for SQL SERVER};'  #You can find this part from the query 'from odbc data source'
    'Server={Servername};'     #You can find this part from the query 'from SQL SERVER 'SELECT @@SERVERNAME'
    'Database=master;'                         #Database that you will use. You can choose the master database to use all the databases you want in just one connection string
    'Trusted_Connection=yes;'
    'UID={Your_Username}'
    'PWD={Your_Password}'
)

connection = pyodbc.connect(ConnectionString)

cursor = connection.cursor()

command1 = 'SELECT * FROM database_name.dbo.table_name'
cursor.execute(command1) #cursor.execute('your_query') allows us to execute and use our query 
our_data = cursor.fetchall() # Here we get all the data line by line under our_data variable

for i in our_data:
    print(i)   #We get printed our database


command2 = """INSERT INTO database_name.dbo.table_name (col_1) VALUES ('new_data')"""
cursor.execute(command2) #In this query we added a new data to our database 
connection.commit() #connection.commit() makes this query possible because if we do not use this, there will be an error and failed to add new data to table

command3 = """DELETE FROM database_name.dbo.table_name WHERE col_1 = 'our_value'"""
cursor.execute(command3) #In this query we deleted a record from table 
connection.commit()

command4 = """UPDATE database_name.dbo.table_name SET col_1 = 'new_value' WHERE col_1 = 'old_value'"""
cursor.execute(command4)
connection.commit()






