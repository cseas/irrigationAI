from sklearn.cross_decomposition import PLSRegression
# from sklearn.ensemble import RandomForestRegressor

import pandas as pd

# Used weather_data_copy.csv as weather_data.csv lacks the 'date' column, used in line 12
X = pd.read_csv("weather_data_copy.csv")

# removed the last value = 239.5, due to mismatch in no. of examples
y = pd.read_csv("water_required.csv")

X = X.drop('date', axis = 1)

# print(X.isnull().any())
# fill empty values in the dataset
X = X.fillna(method='ffill')
# print("..........................")
# print(X.isnull().any())

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

X_train = X_train.values
X_test = X_test.values
y_train = y_train.values
y_test = y_test.values

plsr = PLSRegression(
    n_components=2, 
    scale=True, 
    max_iter=500, 
    tol=1e-06, 
    copy=True)

# plsr = RandomForestRegressor(n_estimators = 1000, random_state = 42)

# plsr
# model = plsr.fit(X_train, y_train)
# forest
model = plsr.fit(X_train, y_train.ravel())

pred = model.predict(X_test)

# accuracy
# print(model.score(X_test, y_test))

# for i in range(136):
#     print(model.predict([X_test[i]]))

# this is water required by crop in mm
water_requirement = model.predict([X_test[0]])
# convert to cm
water_requirement = water_requirement/10

def run_motor(soil_moisture):
    global water_requirement
    water_requirement = ((100 - soil_moisture) * 0.01) * (water_requirement)

    # area of field
    area = 12.5 * 8.5
    # speed of motor in cm cube per sec
    speed = 6.25
    # water required scaled down by factor of 10 for demo
    water_requirement = water_requirement/10

    seconds = (water_requirement * area)/speed

    # convert to int
    seconds = int(seconds[0])

    return seconds
