# 🏥 Health Insurance Premium Prediction  

## 📌 Overview  
This project develops a predictive model for an insurance company to estimate health insurance premiums based on various demographic, health, and lifestyle factors. Using machine learning, the model helps:  

- Optimize pricing strategies  
- Reduce underwriting risks  
- Offer fair and personalized premiums to customers  

## 🎯 Objective  
Insurance companies face challenges in accurately pricing policies due to varying risk factors. This project provides a data-driven solution to:  

✔ Improve premium accuracy  
✔ Reduce financial risk  
✔ Enable personalized insurance plans  
✔ Enhance data-driven decision-making  

## 🔍 Key Features  
✅ **Prediction Model**: Uses advanced ML algorithms to estimate insurance premiums.  
✅ **Model Segmentation**: Dataset split based on age groups (≤25 & >25) for better accuracy.  
✅ **Error Reduction**: Error analysis-driven improvements reduced large deviations in predictions.  
✅ **Deployment on Streamlit**: A web-based interface for real-time predictions.  
✅ **Multicollinearity Handling**: Variance Inflation Factor (VIF) used to remove highly correlated features.  

## 🏗 Project Workflow  

### 🔹 Phase 1: Data Preprocessing & Exploration  
- **Data Cleaning**: Handling missing values and outliers.  
- **Feature Encoding**:  
  - One-hot encoding & label encoding for categorical variables.  
  - Normalization to scale numerical features.  
- **Multicollinearity Reduction**:  
  - Used Variance Inflation Factor (VIF) to remove highly correlated features.  
- **Exploratory Data Analysis (EDA)**: Identifying correlations and feature importance.  

### 🔹 Phase 2: Model Segmentation & Optimization  

#### 1️⃣ Initial Model Performance & Error Analysis  
- Initially, **XGBoost** was applied to the entire dataset, achieving an impressive **98% R² score**.  
- However, **error analysis** revealed:  
  - **29%** of records had prediction errors exceeding **10%**.  
  - **3%** of records had errors exceeding **50%**.  
  - Most high-error cases belonged to individuals aged **25 and below**.  
- Despite high accuracy, the model struggled with generalization, leading to large premium variations for certain age groups.  

#### 2️⃣ Model Segmentation Based on Age  
To address this issue, the dataset was split into two groups:  

- **Age ≤ 25** → Introduced a new feature: **Genetical Risk Score**  
- **Age > 25** → Used original features without modification  

🔹 This segmentation improved model accuracy and significantly reduced prediction errors:  
✅ **Only 2% of records now have errors >10%**  
✅ **0% of records have errors >50%**  

#### 3️⃣ Model Training & Evaluation  
- **Feature Engineering**: Transforming raw data for better predictions.  
- **Model Selection**: Experimented with **Linear Regression, XGBoost**.  
- **Hyperparameter Tuning**: Optimized model performance.  
- **Evaluation Metric**: Used **R² score** for model assessment.  

### 🔹 Phase 3: Deployment & Integration  
✔ Built an **Interactive Web Interface** using **Streamlit**  
✔ Deployed the **Model for Real-time Predictions**  

---

## 📊 Factors Affecting Premiums  
The model predicts premiums based on:  

### 🔹 Demographics  
- Age, Gender, Marital Status, Region  

### 🔹 Health Indicators  
- BMI Category, Medical History (e.g., Diabetes), Genetical Risk Score (for Age ≤ 25)  

### 🔹 Lifestyle & Habits  
- Smoking Status, Employment Status, Income  

### 🔹 Policy Details  
- Insurance Plan (Bronze, Silver, etc.), Number of Dependents  

---

## 🛠 Tech Stack  

| **Category**   | **Tools Used**  |  
|---------------|---------------|  
| **Programming** | Python  |  
| **Libraries** | NumPy, Pandas, Scikit-Learn, Matplotlib, Seaborn, XGBoost  |  
| **Modeling** | Linear Regression, XGBoost  |  
| **Deployment** | Streamlit  |  

---


## 📈 Future Improvements
### ✅ Incorporate Deep Learning models for even better accuracy
### ✅ Add more demographic and health-related features

---

## 🚀 Running the Project Locally  

```sh
# Clone the repository
git clone https://github.com/your-repo/Health_Insurance_Prediction.git

# Navigate to the project directory
cd Health_Insurance_Prediction

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py



