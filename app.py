from flask import Flask, render_template, request
import pickle
import numpy as np
import sqlite3
import datetime

app = Flask(__name__)

pickled_model = pickle.load(open(f'Model/House.pkl', 'rb'))
conn = sqlite3.connect('Database/UserSavedData.db', check_same_thread=False)
cur = conn.cursor()

location_list = ['area','bhk','Alaknanda', 'Anna Nagar', 'BTM Layout', 'Banjara Hills', 'Bellandur', 'Borivali East', 'Chembur', 'Chittaranjan Park', 'Choolaimedu', 'Dattapada', 'Egmore', 'Gachibowli', 'Goregaon West', 'Hebbal', 'Hitech City', 'JP Nagar Phase 4', 'Jasola', 'Jubilee Hills', 'Kalkaji', 'Kalwa', 'Kandivali East', 'Kandivali West', 'Kharghar', 'Konanakunte', 'Kondapur', 'Koramangala', 'Madhapur', 'Magathane', 'Malad East', 'Malad West', 'Mira Road East', 'Nungambakkam', 'Paschim Vihar', 'Pitampura', 'Raja Annamalai Puram', 'Sahakar Nagar', 'Saket', 'Sarita Vihar', 'Sector 10 Dwarka', 'Sector 11 Dwarka', 'Sector 12 Dwarka', 'Sector 13 Dwarka', 'Sector 13 Rohini', 'Sector 17 Ulwe', 'Sector 19 Dwarka', 'Sector 2 Dwarka', 'Sector 20 Kharghar', 'Sector 22 Dwarka', 'Sector 23 Dwarka', 'Sector 24 Rohini', 'Sector 3 Dwarka', 'Sector 4 Dwarka', 'Sector 5 Dwarka', 'Sector 6 Dwarka', 'Sector 7 Dwarka', 'Sector 9 Dwarka', 'Sector-18 Dwarka', 'Shastri Nagar', 'T Nagar', 'Thane', 'Thane West', 'Thiruvanmiyur', 'Thoraipakkam OMR', 'Vadapalani', 'Vasant Kunj']
def predict_price(location , area , bhk , city):
    c =-1
    x = np.zeros(len(location_list))
    for i in location_list:
        c = c+1
        if(i == location):
            x[c] = 1
    
    x[0] = area
    x[1] = bhk
    if city == 'Bangalore':
        a = [0 ,0 ,0 ,0 ,0]
        X = np.concatenate((x, a))
    elif city == 'Chennai':
        a = [1 ,0 ,0 ,0 ,0]
        X = np.concatenate((x, a))
    elif city == 'Delhi':
        a = [0 ,1 ,0 ,0 ,0]
        X = np.concatenate((x, a))
    elif city == 'Hyderabad':
        a = [0 ,0 ,1 ,0 ,0]
        X = np.concatenate((x, a))
    elif city == 'Kolkata':
        a = [0 ,0 ,0 ,1 ,0]
        X = np.concatenate((x, a))
    elif city == 'Mumbai':
        a = [0 ,0 ,0 ,0 ,1]
        X = np.concatenate((x, a))
    return pickled_model.predict([X])[0]


@app.route('/')
def home():
    city_list = ['Mumbai' , 'Delhi' , 'Bangalore','Chennai','Hyderabad','Kolkata']
    return render_template('index.html',city = city_list)

@app.route('/city/Bangalore')
def bangalore():
    loc_list = ['BTM Layout','Bellandur','Hebbal','JP Nagar Phase 4','Konanakunte','Koramangala','Sahakar Nagar','Other']
    return render_template('form.html' , locations = loc_list , city = 'Bangalore')

@app.route('/city/Chennai')
def chennai():
    loc_list = ['Anna Nagar','Choolaimedu','Egmore','Nungambakkam','Raja Annamalai Puram','T Nagar','Thiruvanmiyur','Thoraipakkam OMR','Vadapalani','Other']
    return render_template('form.html', locations = loc_list, city = 'Chennai')

@app.route('/city/Mumbai')
def mumbai():
    loc_list = ['Borivali East' ,'Chembur','Dattapada','Goregaon West','Kalwa','Kandivali East','Kandivali West','Kharghar','Magathane','Malad East','Malad West','Mira Road East','Sector 17 Ulwe','Sector 20 Kharghar','Thane','Thane West','Other']
    return render_template('form.html', locations = loc_list, city = 'Mumbai')

@app.route('/city/Delhi')
def delhi():
    loc_list = ['Alaknanda','Chittaranjan Park','Jasola','Kalkaji','Paschim Vihar','Pitampura','Saket','Sarita Vihar','Sector 2 Dwarka','Sector 3 Dwarka','Sector 4 Dwarka','Sector 5 Dwarka','Sector 6 Dwarka','Sector 7 Dwarka','Sector 9 Dwarka','Sector 10 Dwarka','Sector 11 Dwarka','Sector 12 Dwarka','Sector 13 Dwarka','Sector-18 Dwarka','Sector 19 Dwarka','Sector 22 Dwarka','Sector 23 Dwarka','Sector 13 Rohini','Sector 24 Rohini','Shastri Nagar','Vasant Kunj','Other']
    return render_template('form.html', locations = loc_list, city = 'Delhi')

@app.route('/city/Hyderabad')
def hyderabad():
    loc_list = ['Banjara Hills','Gachibowli','Hitech City','Jubilee Hills','Kondapur','Madhapur','Other']
    return render_template('form.html', locations = loc_list, city = 'Hyderabad')

@app.route('/city/Kolkata')
def kolkata():
    loc_list = ['Other']
    return render_template('form.html', locations = loc_list, city = 'Kolkata')

@app.route('/result',methods =["GET", "POST"])
def result():
    if request.method == 'POST':
        city = request.form.get("city")
        area = request.form.get("area")
        location = request.form.get("loc")[:][:]
        bhk = request.form.get("bhk")
        result = predict_price(location,area,bhk,city)
        
        query = '''INSERT INTO saved_house_data (City,Location,Area,BHK,Predicted_Price,Saved_time) VALUES (?,?,?,?,?,?)'''
        cur.execute(query,(city,location,area,bhk,round(float(result),5),datetime.datetime.now()))
        conn.commit()

    return render_template('result.html', price = round(float(result),3) , city = city , area = area , location = location , bhk =bhk)

@app.route('/records')
def records():
    statement = '''SELECT * FROM saved_house_data'''

    cur.execute(statement)

    output = cur.fetchall()

    conn.commit()
    return render_template('show_records.html',Records = output)


if __name__ == '__main__':
   app.run()