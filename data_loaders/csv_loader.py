import pandas as pd  
from data_loaders.base_loader import DataLoader  # Import base abstract loader class
from utils import log  # Import logging function

# CSV loader class inheriting from the base DataLoader class
class CSVLoader(DataLoader):
    def load_data(self, filepath):
        log(f"Loading CSV file: {filepath}")  # Log the start of the operation
        try:
            data = pd.read_csv(filepath)  
            log("CSV loaded successfully.")  # Log success
            return data  # Return the loaded DataFrame
        except Exception as e:  
            log(f"Failed to load CSV: {e}")  # Log the error
            raise  # Re-raise the error so it can be handled later
