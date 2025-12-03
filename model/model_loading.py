import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "logistic_regression_model.pkl")
with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)
    
def predict(input_df):
    # Ensure correct column order
    print("\n========== DEBUG ==========")
    print("EXPECTED:", model.feature_names_in_)
    print("RECEIVED:", input_df.columns.tolist())
    print("===========================\n")
    input_df = input_df[model.feature_names_in_]


    # Convert to numpy array


    # Predict
    return model.predict(input_df)
