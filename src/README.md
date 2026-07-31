# 💻 Source Code

This directory contains the Python scripts used to train and evaluate the Decision Tree classifier under different data sampling conditions. 

## 📂 Scripts Overview

* **`oversampling_smote.py`** 
  Implements the Synthetic Minority Over-sampling Technique (SMOTE) using the `imblearn` library[cite: 1]. It balances the training data by generating synthetic examples for the minority classes before training the model[cite: 1].
* **`undersampling.py`** 
  Utilizes `RandomUnderSampler` from the `imblearn` library to reduce the number of instances in the majority class, forcing a balanced distribution in the training set[cite: 2].
* **`random_sampling.py`** 
  Serves as the baseline for the experiment[cite: 3]. It trains the model on the naturally imbalanced data without any external class-balancing interventions[cite: 3].

## 🛠️ Implementation Details

Each script in this directory follows a consistent analytical pipeline:
* **Data Loading & Preprocessing:** The scripts automatically load the `02-21-2018.csv` dataset and select five critical network traffic features (e.g., Flow Duration, Tot Fwd Pkts)[cite: 1, 2, 3]. The data is then standardized using `StandardScaler`[cite: 1, 2, 3].
* **Custom Decision Tree:** Instead of using pre-built models, the scripts feature a custom, from-scratch implementation of a Decision Tree classifier (`MyDecisionTree` class)[cite: 1, 2, 3]. It utilizes entropy calculations to determine the best node splits[cite: 1, 2, 3]. The maximum tree depth is restricted to 7, and the minimum samples required to split an internal node is set to 10[cite: 1, 2, 3].
* **Evaluation:** After training, each script automatically outputs a comprehensive classification report (Precision, Recall, F1-score), the overall accuracy score, and a confusion matrix to the terminal[cite: 1, 2, 3].

## 🚀 Execution
Ensure you have downloaded the dataset into the `data/` directory and installed the required dependencies. Run the scripts from the root directory of the repository:
```bash
python src/oversampling_smote.py
