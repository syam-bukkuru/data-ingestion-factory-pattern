from data_loaders.csv_loader import CSVLoader  # Import CSV loader class
from data_loaders.json_loader import JSONLoader  # Import JSON loader class
from data_loaders.zip_loader import ZIPLoader  # Import ZIP loader class
from utils import log  # Import logging function

# Factory class to select the appropriate loader
class DataLoaderFactory:
    @staticmethod  # No need to instantiate this class; can call this method directly via class
    def get_loader(filetype):
        log(f"Requesting loader for filetype: {filetype}")  # Log request

        if filetype == 'csv':
            return CSVLoader()  # Return a CSVLoader object
        elif filetype == 'json':
            return JSONLoader()  # Return a JSONLoader object
        elif filetype == 'zip':
            return ZIPLoader()  # Return a ZIPLoader object
        else:
            raise ValueError(f"Unsupported file type: {filetype}")  # If unsupported, raise error
