import pandas as pd  
from data_loaders.base_loader import DataLoader  # Import base abstract loader class
from utils import log  # Import logging function

# JSON loader class inheriting from the base DataLoader class
class JSONLoader(DataLoader):
    def load_data(self, filepath):
        log(f"Loading JSON file: {filepath}")  # Log the start of the operation
        try:
            data = pd.read_json(filepath)  # Read JSON file into a DataFrame
            log("JSON loaded successfully.")  # Log success
            return data  # Return the loaded DataFrame
        except Exception as e:
            log(f"Failed to load JSON: {e}")  # Log any error
            raise  # Re-raise the error
