import logging  

logging.basicConfig(
    level=logging.INFO,  # Set logging level (INFO and above will be logged).
    filename='app.log',  # Log messages will be saved to 'app.log' file.
    filemode='a',  # 'a' means append to the file, don't overwrite it.
    format='%(asctime)s - %(levelname)s - %(message)s'  # Define log message format.
)

def log(message):
    logging.info(message)  