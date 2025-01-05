import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('final.csv')

one_hot_encoder = OneHotEncoder(sparse_output=False)
encoded_data = one_hot_encoder.fit_transform(df[['Brand']]) # Get the encoded data

# Get feature names from the encoder
feature_names = one_hot_encoder.get_feature_names_out(['Brand'])
# Create a DataFrame from the encoded data
encoded_df = pd.DataFrame(encoded_data, columns=feature_names, index=df.index)
# Concatenate the encoded DataFrame with the original DataFrame
df = pd.concat([df, encoded_df], axis=1)

X = df.drop(['Brand', 'Touchscreen', 'Bluetooth', 'Current Price'], axis=1)
y = df['Current Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
def predict(brand,battery_life):
    new_brand_encoded = one_hot_encoder.transform([[brand]])
    input_data = [battery_life]
    arr = np.array(input_data).reshape(1,-1)
    merged_array = np.concatenate((arr, new_brand_encoded), axis=1)
    result = model.predict(merged_array)
    return result
