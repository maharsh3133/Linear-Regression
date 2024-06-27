# 🔢 Linear-Regression
Exploring and Learning Linear Regression Model by applying the model on an e-commerce dataset

# 📊 Linear Regression Examples

This repository contains two examples of linear regression applications. These examples demonstrate the basic concepts of linear regression, including data visualization, data preprocessing, and model building.

## Files 📄
- ***Ecom Expense.csv***: E-commerce expense data file
- ***Linear Regression EX1.py***: Python script to draft equation of line with and without noise
- ***Linear Regression EX2.py***: Python script for applying Linear Regression on E-commerce Data
- ***Report Linear Regression.docx***: Report to explain the graphs and plots in detail

## 🎥 Explanation Video: [Click to watch!](https://drive.google.com/file/d/16LCmEeC__JQRsyq_2lGyVeivVeF4NwPM/view?usp=sharing)

## Example 1️⃣: Linear Regression with and without Noise

In this example, we generate a simple linear dataset and visualize it with and without noise.

### Steps:

1. **📝 Data Generation**: Generate random `x` values uniformly distributed between -1 and 1. Compute `y` values as a linear function of `x` (y = 12x - 4).
2. **📈 Visualization**: Plot the `x` and `y` values using a scatter plot.
3. **🌟 Adding Noise**: Add normally distributed noise to the `y` values and visualize the noisy data.

### Visualization:

- **Scatter Plot (Without Noise)**:  
![Scatter Plot Without Noise](https://github.com/maharsh3133/Linear-Regression/assets/35959045/d49eecf2-a24d-420c-9956-d22166c74ee2)

- **Scatter Plot (With Noise)**:  
![Scatter Plot With Noise](https://github.com/maharsh3133/Linear-Regression/assets/35959045/7e660047-f878-41d7-9cfc-96265074f935)

## Example 2️⃣: Linear Regression on E-commerce Data

This example involves applying linear regression to an e-commerce expense dataset to predict total spend based on various features.

### Steps:

1. **📥 Data Loading**: Load the e-commerce expense data from a CSV file.
2. **🔍 Data Exploration**: Display the first few rows, dataset shape, column names, and summary information.
3. **🔧 Data Preprocessing**:
   - Convert categorical variables to numeric using one-hot encoding.
   - Drop unnecessary columns.
   - Normalize the data.
4. **📊 Data Visualization**:
   - Generate histograms for all features.
   - Generate a scatter matrix to visualize relationships between features.
5. **✨ Feature Selection**: Select relevant features for the regression model.
6. **🏗️ Model Building**:
   - Split the data into training and testing sets.
   - Train a linear regression model.
   - Evaluate the model using R-squared value.
7. **🔄 Extended Model**: Add an additional feature and rebuild the model to see the effect on performance.

### Dataset:

The dataset used for this example includes the following columns:
- Transaction ID
- Age
- Items
- Monthly Income
- Transaction Time
- Record
- Gender
- City Tier
- Total Spend

### Visualization:

- **Histograms**:  
  ![Histograms](https://github.com/maharsh3133/Linear-Regression/assets/35959045/44e55749-7db0-4b7e-9b22-db60288db756)

- **Scatter Matrix**:  
![Scatter Matrix](https://github.com/maharsh3133/Linear-Regression/assets/35959045/4e223f14-98bd-42f0-93a2-13564b8bb226)

### Feature Selection:

Selected features for the regression model:
- Monthly Income
- Transaction Time
- Gender (Female and Male)
- City Tier (Tier 1, Tier 2, Tier 3)

### Model Performance:

- **First Model R-squared**: 0.20892313489184833
- **Second Model R-squared**: 0.9194670977777539

## 👤 Author

- [Maharsh](https://www.linkedin.com/in/maharsh-patel-641777168/)
