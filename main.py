import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load the dataset
file_path = 'APY_Reduced2.csv'
data = pd.read_csv(file_path)

# Trim spaces in column names
data.columns = data.columns.str.strip()

# Data Cleaning and Preprocessing
data.dropna(inplace=True)  # Handle missing values

# Encode categorical variables
label_encoders = {}
for column in ['State', 'District', 'Crop', 'Season']:
    label_encoders[column] = LabelEncoder()
    data[column] = label_encoders[column].fit_transform(data[column])

# Feature and Target variables
X = data[['State', 'District', 'Crop', 'Crop_Year', 'Season', 'Area']]
y = data['Production']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model Training
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model and scaler
joblib.dump(model, 'crop_production_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(label_encoders, 'label_encoders.pkl')

# Function to find districts and states for buying X amount of crop
def find_districts_for_crop(crop, amount_required, data, label_encoders):
    # Filter data for the specified crop
    crop_encoded = label_encoders['Crop'].transform([crop])[0]
    crop_data = data[data['Crop'] == crop_encoded]
    
    # Sort data by production in descending order
    crop_data = crop_data.sort_values(by='Production', ascending=False)
    
    districts = []
    total_amount = 0
    
    for _, row in crop_data.iterrows():
        districts.append((row['State'], row['District'], row['Production']))
        total_amount += row['Production']
        if total_amount >= amount_required:
            break
    
    # Decode the State and District labels back to their original form
    result = [(label_encoders['State'].inverse_transform([int(state)])[0],
               label_encoders['District'].inverse_transform([int(district)])[0],
               production) for state, district, production in districts]
    
    return result

# Streamlit app
st.title("Crop Production Finder")

# Section for finding districts for crop
st.header("Find Districts for Crop")

crop = st.selectbox("Select crop:", label_encoders['Crop'].classes_)
amount_required = st.number_input("Enter the required amount of crop:", min_value=0.0, step=1.0)

if st.button("Find Districts"):
    districts = find_districts_for_crop(crop, amount_required, data, label_encoders)
    st.write(f'Districts and states that can collectively provide {amount_required} units of {crop}:')
    for state, district, production in districts:
        st.write(f'State: {state}, District: {district}, Production: {production}')
