# src/file_handler.py
"""
File Handler Module
-------------------
Responsible for reading sales data files safely and returning
structured records for further processing.

Handles:
- UTF-8 encoding
- Pipe (|) delimited files
- Header-based parsing
"""

def read_sales_file(file_path):
    """
    Reads the sales data file and returns records as a list of dictionaries.

    Args:
        file_path (str): Path to sales_data.txt

    Returns:
        list: List of sales records (dict)
    """

    records = []

    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            headers = file.readline().strip().split("|")

            for line_no, line in enumerate(file, start=2):
                if not line.strip():
                    continue

                values = line.strip().split("|")

                # Ensure column count consistency
                if len(values) != len(headers):
                    print(f"Skipping invalid row at line {line_no}")
                    continue

                record = dict(zip(headers, values))
                records.append(record)

    except FileNotFoundError:
        print(f"ERROR: File not found -> {file_path}")
    except UnicodeDecodeError:
        print("ERROR: Encoding issue. Please ensure UTF-8 encoding.")
    except Exception as e:
        print(f"Unexpected error while reading file: {e}")

    return records
