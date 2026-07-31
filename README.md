# Decision Tree Performance: Impact of Data Sampling Methods

This repository contains an academic project analyzing how different data preprocessing and sampling techniques affect the performance of a Decision Tree classifier[cite: 4]. The primary focus is on detecting Network/DDoS attacks using the highly imbalanced **CIC-IDS-2018** dataset[cite: 4].

## 📊 Project Overview
Real-world cybersecurity datasets are often heavily imbalanced, where normal traffic vastly outnumbers attack instances[cite: 4]. This project evaluates three sampling approaches to address this issue:
1. **Random Sampling (Baseline)** - Original imbalanced distribution[cite: 3, 4].
2. **Undersampling (RandomUnderSampler)** - Reducing the majority class[cite: 2, 4].
3. **Oversampling (SMOTE)** - Synthetically generating minority class instances[cite: 1, 4].

*A detailed Polish report is available in the `docs/` folder.*

## 🚀 Key Findings
Based on the experiments, **SMOTE oversampling** proved to be the most effective method[cite: 4]:
* Achieved **99.93% overall accuracy**[cite: 4].
* Perfectly classified (100% Precision, Recall, and F1-score) the severely underrepresented minority class (`DDOS attack-LOIC-UDP`), which originally had only 15 instances in the raw dataset[cite: 4].
* Produced the most balanced and representative logical rules for the Decision Tree[cite: 4].

## 📁 Repository Structure
```text
├── data/                        # Directory for dataset (downloaded via script)
├── docs/                        
│   └── sprawozdanie_projektowe.pdf  # Comprehensive project report (PL)
├── src/                         # Source code for experiments
│   ├── oversampling_smote.py    # SMOTE implementation
│   ├── undersampling.py         # Random Undersampling implementation
│   └── random_sampling.py       # Baseline classification
├── download_data.py             # Automated Kaggle dataset downloader
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore file
└── README.md                    # Project documentation
