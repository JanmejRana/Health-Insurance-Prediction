import streamlit as st
from prediction_helper import predict

def main():
    st.title("Health Insurance Prediction")

    # Dropdown options
    gender_options = ['Male', 'Female']
    region_options = ['Northwest', 'Southeast', 'Northeast', 'Southwest']
    marital_status_options = ['Unmarried', 'Married']
    bmi_category_options = ['Normal', 'Obesity', 'Overweight', 'Underweight']
    smoking_status_options = ['No Smoking', 'Regular', 'Occasional']
    employment_status_options = ['Salaried', 'Self-Employed', 'Freelancer']
    medical_history_options = ['Diabetes', 'High blood pressure', 'No Disease', 'Diabetes & High blood pressure',
                               'Thyroid', 'Heart disease', 'High blood pressure & Heart disease',
                               'Diabetes & Thyroid', 'Diabetes & Heart disease']
    insurance_plan_options = ['Bronze', 'Silver', 'Gold']

    # Streamlit UI with multiple columns per row
    col1, col2, col3 = st.columns(3)
    with col1:
        gender = st.selectbox("Gender", gender_options)
        marital_status = st.selectbox("Marital Status", marital_status_options)
        smoking_status = st.selectbox("Smoking Status", smoking_status_options)
        genetical_risk = st.number_input("Genetical Risk Score", min_value=0, max_value=100, value=50, step=1)

    with col2:
        region = st.selectbox("Region", region_options)
        bmi_category = st.selectbox("BMI Category", bmi_category_options)
        employment_status = st.selectbox("Employment Status", employment_status_options)
        medical_history = st.selectbox("Medical History", medical_history_options)

    with col3:
        insurance_plan = st.selectbox("Insurance Plan", insurance_plan_options)
        age = st.number_input("Age", min_value=18, max_value=100, value=18, step=1)
        number_of_dependants = st.number_input("Number of Dependants", min_value=0, max_value=10, value=0, step=1)
        income_lakhs = st.number_input("Income (in Lakhs)", min_value=0.0, max_value=100.0, value=5.0, step=0.1)


    user_inputs = {
        "Gender": gender,
        "Region": region,
        "Marital Status": marital_status,
        "BMI Category": bmi_category,
        "Smoking Status": smoking_status,
        "Employment Status": employment_status,
        "Medical History": medical_history,
        "Insurance Plan": insurance_plan,
        "Age": age,
        "Number of Dependants": number_of_dependants,
        "Income (in Lakhs)": income_lakhs,
        "Genetical Risk Score": genetical_risk
    }
    if st.button("Submit"):
        prediction = predict(user_inputs)
        st.success(f"Predicted Premium : {prediction}")


if __name__ == "__main__":
    main()
