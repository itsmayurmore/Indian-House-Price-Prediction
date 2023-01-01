import sqlite3

conn = sqlite3.connect('Database/UserSavedData.db')


conn.execute('''CREATE TABLE saved_house_data
         (City Varchar(20) ,
         Location       Varchar(20),
        Area Real,
         BHK   INT,
         Predicted_Price Real,
         Saved_time timestamp);''')

conn.close()