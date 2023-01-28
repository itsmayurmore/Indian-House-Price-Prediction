
# Indian House Price Prediction

House price prediction with Random Forest Regressor is a machine learning model that is used to predict the price of a house in lakh rupees based on certain input variables such as city, location, area in sqft, and number of bedrooms (bhk). 

The model is trained on a large dataset of house prices from various cities including Bangalore, Chennai, Delhi, Hyderabad, Kolkata, and Mumbai.

The Random Forest Regressor uses an ensemble of decision trees to make predictions. It works by creating a large number of decision trees and aggregating the predictions made by each tree. This results in a more robust and accurate prediction compared to using a single decision tree.

In this model, the input variables are used to create a decision tree that predicts the price of a house based on the characteristics of the house. For example, if the input variables indicate that the house is located in Bangalore, has a large area in sqft, and has 3 bedrooms, the model will use this information to predict the price of the house.

The accuracy of the model is measured using the mean squared error (MSE) metric. The MSE is calculated by taking the difference between the predicted price and the actual price and squaring it. The lower the MSE, the more accurate the model is. In this case, the model has an accuracy of 89% which means that it is able to predict the price of a house with a high degree of accuracy.

Overall, the Random Forest Regressor is a useful tool for predicting the price of a house based on various input variables such as city, location, area in sqft, and number of bedrooms. It is able to achieve a high level of accuracy and is widely used in the real estate industry for predicting house prices.




## Demo

https://indianhouseprice.pythonanywhere.com


## Run Locally

Clone the project

```bash
  git clone https://github.com/itsmayurmore/Indian-House-Price-Prediction.git
```


Install dependencies
```bash
  Install Python 3.x
```

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python app.py
```

