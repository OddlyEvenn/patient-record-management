def get_summary(df):
    total_patients = len(df)

    # Clean 'Fees' column before converting to float
    df['Fees'] = df['Fees'].replace('', '0').astype(float)

    total_revenue = df['Fees'].sum()
    recent_registrations = df.sort_values('Date of registration', ascending=False).head(5)

    return {
        "total_patients": total_patients,
        "total_revenue": total_revenue,
        "recent": recent_registrations
    }
