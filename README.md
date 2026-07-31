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
```

## ⚙️ Setup & Installation
###1. Install Dependencies
Clone this repository and install the required Python packages:

```bash
pip install -r requirements.txt
```

### 2. Configure Kaggle API (For Dataset)
This project uses an automated script to download the specific ~300MB CSV file (02-21-2018.csv) from the 7GB CSE-CIC-IDS2018 Kaggle dataset.

1.Create a Kaggle account.
2.Go to your Account Settings -> API -> Create New Token.
3.Place the downloaded kaggle.json file in your system's Kaggle folder (e.g., ~/.kaggle/kaggle.json on Linux/Mac or C:\Users\<User>\.kaggle\kaggle.json on Windows).

### 3. Download the Data
Run the automated downloader script from the root directory:

```bash
python download_data.py
```

The script will automatically download the archive, extract the required CSV file into the data/ folder, and clean up the temporary files.

## 💻 Running the Experiments
Once the data is downloaded, you can run any of the models from the root directory.

To test the SMOTE oversampling method:

```bash
python src/oversampling_smote.py
```

To test the random undersampling method:

```bash
python src/undersampling.py
```

To test the baseline random sampling:

```bash
python src/random_sampling.py
```
