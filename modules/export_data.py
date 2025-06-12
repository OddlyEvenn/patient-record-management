# modules/export_data.py

def export_to_csv(df, filename="patient_data_export.csv"):
    try:
        df.to_csv(filename, index=False)
        return True, f"Data exported successfully to {filename}"
    except Exception as e:
        return False, str(e)
     