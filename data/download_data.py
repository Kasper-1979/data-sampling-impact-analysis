import os
import subprocess
import zipfile
import sys
import shutil

DATASET_NAME = "solarmainframe/ids-intrusion-csv" 
FILE_TO_EXTRACT = "02-21-2018.csv"
DATA_DIR = "data"

def main():
    print("[INFO] Starting Kaggle dataset download...")
    
    # Create data directory if it doesn't exist
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        
    target_path = os.path.join(DATA_DIR, FILE_TO_EXTRACT)
    
    # Check if file is already downloaded
    if os.path.exists(target_path):
        print(f"[INFO] File {FILE_TO_EXTRACT} already exists in '{DATA_DIR}'. Skipping download.")
        return

    # Download dataset using Kaggle CLI
    try:
        print(f"[INFO] Running Kaggle CLI to download '{DATASET_NAME}'...")
        subprocess.run([
            sys.executable, "-m", "kaggle", "datasets", "download", "-d", DATASET_NAME, "-p", DATA_DIR
        ], check=True)
    except FileNotFoundError:
        print("[ERROR] 'kaggle' command not found. Please install it via 'pip install kaggle' and configure your API key (kaggle.json).")
        sys.exit(1)
    except subprocess.CalledProcessError:
        print("[ERROR] Failed to download data. Please check your Kaggle API credentials.")
        sys.exit(1)

    # Extract the specific file
    zip_filename = DATASET_NAME.split('/')[-1] + ".zip"
    zip_path = os.path.join(DATA_DIR, zip_filename)
    
    print(f"[INFO] Extracting {FILE_TO_EXTRACT} from archive...")
    
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Find the file in the archive (it might be inside a subfolder)
            file_in_zip = next((f for f in zip_ref.namelist() if f.endswith(FILE_TO_EXTRACT)), None)
            
            if file_in_zip:
                zip_ref.extract(file_in_zip, DATA_DIR)
                extracted_path = os.path.join(DATA_DIR, file_in_zip)
                
                # Move to root of data/ if it was extracted to a subfolder
                if os.path.normpath(extracted_path) != os.path.normpath(target_path):
                    shutil.move(extracted_path, target_path)
                    # Remove empty subfolder if created
                    folder_path = os.path.dirname(extracted_path)
                    if not os.listdir(folder_path):
                        os.rmdir(folder_path)
                        
                print(f"[INFO] Success! File extracted to: {target_path}")
            else:
                print(f"[ERROR] File {FILE_TO_EXTRACT} not found in the downloaded archive.")
                
        # Clean up the large zip file to save space
        os.remove(zip_path)
        print("[INFO] Temporary ZIP archive removed to save space.")
        
    except Exception as e:
        print(f"[ERROR] An error occurred during extraction: {e}")

if __name__ == "__main__":
    main()
