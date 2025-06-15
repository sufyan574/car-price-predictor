import streamlit as st
import pickle
import numpy as np


class CarPricePredictor:
    def __init__(self, model_path, scaler_path=None):
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)
        if scaler_path:
            with open(scaler_path, 'rb') as f:
                self.scaler = pickle.load(f)
        else:
            self.scaler = None

    def preprocess_input(self, inputs):
        data = np.array([inputs])
        if self.scaler:
            data = self.scaler.transform(data)
        return data

    def predict(self, inputs):
        processed = self.preprocess_input(inputs)
        return self.model.predict(processed)[0]


# Streamlit App UI
def main():
    st.title("Car Price Prediction App (PKR)")
    st.markdown("### Enter the car details to predict price")

    year = st.number_input("Year", min_value=2000, max_value=2025, value=2015)
    kms_driven = st.number_input("Kilometers Driven", min_value=1000, max_value=300000, value=50000)
    
    fuel_type = st.selectbox("Fuel Type", options=["Petrol", "Diesel", "CNG", "LPG", "Electric"])
    fuel_map = {"Petrol": 3, "Diesel": 0, "CNG": 1, "LPG": 2, "Electric": 4}

    company = st.selectbox("Company", options=["Maruti", "Hyundai", "Honda", "Toyota", "Ford", "Mahindra",])
    company_map = {"Maruti": 4, "Hyundai": 2, "Honda": 1, "Toyota": 5, "Ford": 0, "Mahindra": 3}

    if st.button("Predict Price"):
        self.model = pickle.load(open("models/svm_model.pkl", "rb"))
        input_data = [year, kms_driven, fuel_map[fuel_type]]
        price = model.predict(input_data)
        st.success(f"Estimated Price: {round(price, 2)} PKR")

if __name__ == "__main__":
    main()
