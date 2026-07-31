# CIC IDS 2018 Dataset

Due to GitHub's file size limitations and best practices, the original CSV dataset is not included in this repository.

The data used in this project comes from the **CSE-CIC-IDS2018** dataset, focusing specifically on the network traffic data captured on **02-21-2018** (which contains DDoS attacks: LOIC and HOIC)[cite: 4].

## How to obtain the data

You only need the `02-21-2018.csv` file[cite: 1, 2, 3] to run the classification scripts in this repository. 

### Download via Kaggle (Recommended)
The required files are conveniently available on Kaggle. You can download the specific CSV file directly from this notebook environment:
👉 [Kaggle: CSE-CIC-IDS2018 (by SHAH TIHAM)](https://www.kaggle.com/code/shahtiham/cse-cic-ids2018)

**Manual Download Steps:**
1. Visit the link above.
2. Navigate to the **Input** tab, then look under **Data Sources** for **IDS 2018 Intrusion CSVs**.
3. Locate and download the `02-21-2018.csv` file.

**Download via Kaggle CLI:**
If you have the Kaggle API configured, you can pull the notebook and its associated data environment using:

```bash
kaggle kernels pull shahtiham/cse-cic-ids2018
```

**Setup Instructions**
1.Ensure the downloaded file is named exactly 02-21-2018.csv.
2.Place this file directly into this folder (data/).
3.Run the Python scripts from the src/ directory. The scripts are pre-configured to automatically load the data using a relative path.
