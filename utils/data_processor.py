# src/data_processor.py
"""
Data Processor Module
---------------------
Responsible for validating, cleaning, and transforming
raw sales records into analytics-ready data.

Implements assignment rules:
- Removes invalid records
- Cleans numeric fields with commas
- Calculates revenue
- Produces validation summary
"""

def process_sales_data(records):
    """
    Cleans and validates raw sales records.

    Rules Applied:
    - TransactionID must start with 'T'
    - CustomerID and Region must not be empty
    - Quantity must be > 0
    - UnitPrice must be > 0
    - UnitPrice may contain commas

    Args:
        records (list): Raw sales records

    Returns:
        tuple:
            valid_records (list)
            summary (dict)
    """

    valid_records = []
    invalid_records = 0

    for record in records:
        try:
            # TransactionID validation
            if not record["TransactionID"].startswith("T"):
                raise ValueError("Invalid TransactionID")

            # Mandatory fields
            if not record["CustomerID"] or not record["Region"]:
                raise ValueError("Missing CustomerID or Region")

            # Quantity validation
            quantity = int(record["Quantity"])
            if quantity <= 0:
                raise ValueError("Invalid Quantity")

            # UnitPrice validation & cleaning
            unit_price = int(record["UnitPrice"].replace(",", ""))
            if unit_price <= 0:
                raise ValueError("Invalid UnitPrice")

            # Data enrichment
            record["Quantity"] = quantity
            record["UnitPrice"] = unit_price
            record["Revenue"] = quantity * unit_price

            valid_records.append(record)

        except Exception:
            invalid_records += 1

    summary = {
        "total_records": len(records),
        "invalid_records": invalid_records,
        "valid_records": len(valid_records)
    }

    return valid_records, summary
