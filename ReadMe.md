# 📊 Data Ingestion using Factory Design Pattern (Python)

A clean, scalable, and beginner-friendly implementation of the **Factory Design Pattern** for data ingestion in Python.  
It can handle multiple file formats (CSV, JSON, ZIP, Excel) and convert them into a common **pandas DataFrame** — perfect for any Machine Learning or Data Science pipeline.

---

## 📌 Features
- Factory Pattern to select the appropriate data loader dynamically
- Individual loaders for each file format
- Error handling and logging
- Scalable structure for adding new formats (Parquet, SQL, APIs, etc.)
- Clean and modular code

---

## 📂 Project Structure

data-ingestion-factory-pattern/
├── data/
│ └── (sample files)
├── data_loaders/
│ ├── base_loader.py
│ ├── csv_loader.py
│ ├── json_loader.py
│ ├── zip_loader.py
│ └── excel_loader.py
├── utils.py
├── factory.py
├── main.py
├── requirements.txt
└── README.md

---

## 🚀 How It Works

1️⃣ The **Factory** selects a loader based on file type  
2️⃣ The **Loader** reads the file and converts it to a pandas DataFrame  
3️⃣ The main program interacts only with the factory, keeping the ingestion logic decoupled and clean  

---

## 📦 Supported File Formats

- CSV (.csv)
- JSON (.json)
- ZIP (.zip containing CSV files)
- Excel (.xlsx)

---

## 📝 Example Usage

```python
from factory import DataLoaderFactory

file_path = 'data/sample.csv'
file_type = 'csv'

loader = DataLoaderFactory.get_loader(file_type)
data = loader.load_data(file_path)

print(data.head())

🔧 Installation
1️⃣ Clone this repository
git clone https://github.com/yourusername/data-ingestion-factory-pattern.git
cd data-ingestion-factory-pattern


2️⃣ Install dependencies
pip install -r requirements.txt