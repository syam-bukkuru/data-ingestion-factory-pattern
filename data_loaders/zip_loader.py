import pandas as pd  
import zipfile  # Built-in module to work with ZIP files
from data_loaders.base_loader import DataLoader  # Base class for data loaders
from utils import log  # For logging messages

# ZIP loader class inheriting from DataLoader
class ZIPLoader(DataLoader):
    def load_data(self, filepath):
        log(f"Loading ZIP file: {filepath}")  # Log start of ZIP file loading
        try:
            with zipfile.ZipFile(filepath, 'r') as zip_ref:  # Open the ZIP file for reading
                file_list = zip_ref.namelist()  # List files inside the ZIP
                log(f"Files in ZIP: {file_list}")  # Log list of files found

                csv_files = [f for f in file_list if f.endswith('.csv')]  # Filter CSV files

                if not csv_files:
                    raise ValueError("No CSV file found in the ZIP.")  # If no CSV file, raise error

                log(f"Reading first CSV file: {csv_files[0]}")  # Log which file is being read

                with zip_ref.open(csv_files[0]) as file:  # Open first CSV file inside ZIP
                    data = pd.read_csv(file)  # Read CSV file into DataFrame

                log("CSV inside ZIP loaded successfully.")  # Log success
                return data  # Return the loaded DataFrame

        except Exception as e:
            log(f"Failed to load ZIP file: {e}")  # Log any error
            raise  # Re-raise error
