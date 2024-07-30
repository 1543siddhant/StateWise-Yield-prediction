# State Wise Crop Yield Prediction

This repository contains the code and data for a machine learning project that predicts crop production and helps find districts and states that can collectively provide a specified amount of a crop. The model is trained using the `APY_Reduced2.csv` dataset.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Streamlit App](#streamlit-app)
- [Contributors](#contributors)
- [License](#license)

## Installation

To run the project, you need to have Python installed. Follow the steps below to set up the environment:

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/StateWiseCropYieldPrediction.git
    cd StateWiseCropYieldPrediction
    ```

2. Install the required packages:
    ```sh
    pip install pandas scikit-learn numpy joblib streamlit
    ```

## Usage

1. **Prepare the dataset:**

    Ensure the `APY_Reduced2.csv` file is in the root directory. This file should contain the following columns: `State`, `District`, `Crop`, `Crop_Year`, `Season`, `Area`, `Production`, and `Yield`.

2. **Run the training script:**

    ```sh
    python train_model.py
    ```

    This script performs the following tasks:
    - Loads the dataset
    - Cleans and preprocesses the data
    - Trains a RandomForestRegressor model
    - Saves the trained model, scaler, and label encoders using `joblib`

3. **Run the Streamlit app:**

    ```sh
    streamlit run app.py
    ```

    This will launch a web application where users can input the crop and the required amount, and the app will output the districts and states that can collectively provide the specified amount.

## Dataset

The dataset used for this project is `APY_Reduced2.csv`. Here are the first few rows:
State,District ,Crop,Crop_Year,Season,Area ,Production,Yield
Uttarakhand,ALMORA,Arhar/Tur,2020,Kharif,216,140,0.65
Uttarakhand,CHAMOLI,Arhar/Tur,2020,Kharif,227,178,0.78
Uttarakhand,CHAMPAWAT,Arhar/Tur,2020,Kharif,2,1,0.5
Uttarakhand,DEHRADUN,Arhar/Tur,2020,Kharif,387,516,1.33
Uttarakhand,NAINITAL,Arhar/Tur,2020,Kharif,5,3,0.6



