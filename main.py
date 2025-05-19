from factory import DataLoaderFactory  # Import factory class
from utils import log  # Import logging function

def main():
    file_path = 'data/archive.zip'  # Filepath to the data file
    file_type = 'csv'  # Specify the file type: 'csv', 'json', 'zip'

    try:
        loader = DataLoaderFactory.get_loader(file_type)  # Get the appropriate loader using factory
        data = loader.load_data(file_path)  # Load the data using the loader
        log(f"Data shape: {data.shape}")  # Log the shape of the loaded data (rows x columns)
        print(data.head())  # Print first 5 rows of data to console

    except Exception as e:  # Catch any exception during the process
        log(f"Error in main: {e}")  # Log the error

if __name__ == "__main__":
    main()  # Run the main function if this is the main script
