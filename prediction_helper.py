import pandas as pd
import joblib

model_young = joblib.load("artifacts/model_young.joblib")
model_rest = joblib.load("artifacts/rest_gr_model.joblib")
scale_young = joblib.load("artifacts/scaler_young.joblib")
scale_rest = joblib.load("artifacts/rest_scale.joblib")


def calculate_normalized_risk(medical_history):
    risk_score = {
        'diabetes': 6,
        'high blood pressure': 6,
        'heart disease': 8,
        'thyroid': 5,
        'no Disease': 0,
        'none': 0
    }

    # Split multiple diseases if present
    diseases = medical_history.lower().split('&')
    diseases = [d.strip() for d in diseases]  # Remove extra spaces
    diseases = [d if d in risk_score else 'none' for d in diseases]  # Ensure only valid diseases are considered

    # Calculate total risk score
    total_risk_score = sum(risk_score[d] for d in diseases)

    # Normalize the risk score using min-max normalization
    max_val = max(risk_score.values()) * 2  # Max possible score (assuming max 2 diseases)
    min_val = 0  # Min possible score

    normalized_risk_score = (total_risk_score - min_val) / (max_val - min_val) if max_val > min_val else 0
    return normalized_risk_score


def preprocess_input(user_inputs):
    expected_columns = [
        "age", "number_of_dependants", "income_lakhs", "insurance_plan", "genetical_risk","total_risk_score", "gender_Male",
        "region_Northwest", "region_Southeast", "region_Southwest", "marital_status_Unmarried", "bmi_category_Obesity",
        "bmi_category_Overweight", "bmi_category_Underweight", "smoking_status_Occasional", "smoking_status_Regular",
        "employment_status_Salaried", "employment_status_Self-Employed"
    ]
    insurance_plan_encoding = {'Bronze':1,'Silver': 2,'Gold':3}
    df = pd.DataFrame(0,columns = expected_columns,index = [0])

    # Fill in numerical and directly mapped values
    df.at[0, "age"] = user_inputs["Age"]
    df.at[0, "number_of_dependants"] = user_inputs["Number of Dependants"]
    df.at[0, "income_lakhs"] = user_inputs["Income (in Lakhs)"]
    df.at[0, "genetical_risk"] = user_inputs["Genetical Risk Score"]
    df.at[0, "insurance_plan"] = insurance_plan_encoding.get(user_inputs["Insurance Plan"],0)  # Default to 0 if not found

    # One-hot encoding for categorical values
    if user_inputs["Gender"] == "Male":
        df.at[0, "gender_Male"] = 1  # Gender is binary, so only "Male" is encoded

    region_col = f"region_{user_inputs['Region']}"
    if region_col in df.columns:
        df.at[0, region_col] = 1  # Set 1 for the specified region

    marital_status_col = f"marital_status_{user_inputs['Marital Status']}"
    if marital_status_col in df.columns:
        df.at[0, marital_status_col] = 1  # Set 1 for marital status

    bmi_col = f"bmi_category_{user_inputs['BMI Category']}"
    if bmi_col in df.columns:
        df.at[0, bmi_col] = 1  # Set 1 for BMI category

    smoking_col = f"smoking_status_{user_inputs['Smoking Status']}"
    if smoking_col in df.columns:
        df.at[0, smoking_col] = 1  # Set 1 for smoking status

    employment_col = f"employment_status_{user_inputs['Employment Status']}"
    if employment_col in df.columns:
        df.at[0, employment_col] = 1  # Set 1 for employment status

    df['total_risk_score'] = calculate_normalized_risk(user_inputs['Medical History'])
    df = handling_age(user_inputs['Age'],df)
    if user_inputs['Age'] > 25:
        model_features = model_rest.get_booster().feature_names
        df = df[[col for col in df.columns if col in model_features]]
    return df

def handling_age(age,df):
    if age <= 25:
        scaler_object = scale_young
    else:
        scaler_object = scale_rest

    cols_to_scale = scaler_object['cols_to_scale']
    scaler = scaler_object['scaler']

    df['income_level'] = None
    # df['genetical_risk'] = None
    df[cols_to_scale] = scaler.transform(df[cols_to_scale])
    df.drop('income_level',axis = 'columns',inplace = True)
    # df.drop('genetical_risk',axis='columns',inplace = True)
    return df


def predict(user_inputs):
    input_df = preprocess_input(user_inputs)
    if user_inputs['Age'] <= 25:
        prediction = model_young.predict(input_df)
    else:
        prediction = model_rest.predict(input_df)

    return int(prediction[0])