# MAI201 MLOps: Assignment 2 - Data Quality Report

## 1. Great Expectations Validation Results

<img width="2868" height="878" alt="Great Expectation_1" src="https://github.com/user-attachments/assets/03b9a368-cf57-4704-82e1-01ec41d49009" />

<img width="2815" height="1319" alt="image" src="https://github.com/user-attachments/assets/85452657-059b-4e4c-8275-7b99048d5bf8" />

### age
<img width="2257" height="1211" alt="image" src="https://github.com/user-attachments/assets/9c902c35-dd8b-4d0d-b353-eb850c344412" />

<br>

### country
<img width="2264" height="992" alt="image" src="https://github.com/user-attachments/assets/382e5940-4699-4ecc-a3a9-8ee3e7b96ecd" />

<br>

### customer_id
<img width="2098" height="1176" alt="image" src="https://github.com/user-attachments/assets/7b3fb183-016e-4cf7-8e0e-8bb2f2dc7960" />

<br>

### email
<img width="2227" height="1090" alt="image" src="https://github.com/user-attachments/assets/46834016-d3fd-4822-b89a-e3b92a7e71b9" />

<br>

### salary
<img width="2278" height="1214" alt="image" src="https://github.com/user-attachments/assets/97e71ecb-65cd-49ba-9af1-3e72425ce68e" />

<br>

### signup_date
<img width="2245" height="414" alt="image" src="https://github.com/user-attachments/assets/835da314-4f26-4e56-a787-a89b7770db5c" />


## 2. Identified Data Quality Issues
Based on the Great Expectations validation run on `customer_data.csv`, the following data quality issues were flagged:

* **Missing Values (Age/Email/Salary):** Several rows contained null or empty fields.
* **Duplicate Records:** `1` rows failed the customer_id uniqueness check.
* **Out-of-range Values (Age):** `1` rows showed ages outside the valid 0-120 range (e.g., age 999).
* **Out-of-range Values (Salary):** `1` rows showed negative salaries.
* **Invalid Email Formats:** `1` rows failed the regex validation (e.g., missing local parts or domains).
* **Invalid Geographies:** `1` rows contained countries outside the approved USA, Canada, UK, Australia list (e.g., India).

## 3. Pytest Execution Results

<img width="1926" height="623" alt="Pytest" src="https://github.com/user-attachments/assets/2ef0bd6a-2a53-45c8-99c0-abae0bced55b" />

## 4. Analytical Reflection
**Which data quality issue would most impact ML model performance and why?**

While all identified data quality issues degrade the fidelity of a dataset, the presence of **duplicate customer records** poses the most critical threat to Machine Learning model performance. 

In a production MLOps pipeline, duplicate rows create a severe risk of **data leakage** during the train-test split phase. If duplicate copies of the same customer profile end up in both the training set and the validation/test set, the model will inadvertently train on the exact data points it is meant to be evaluated against. 

This results in an artificial inflation of validation metrics (such as accuracy, precision, or F1-score). Data scientists relying on these metrics might unknowingly deploy an overfitted model that memorizes specific users rather than learning generalized patterns. Consequently, when deployed to production, the model will fail to generalize to unseen, real-world data, leading to severe performance degradation.
