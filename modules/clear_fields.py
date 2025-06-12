# modules/clear_fields.py

def clear_entry_fields(entry_dict):
    for field in entry_dict.values():
        field.delete(0, 'end')
