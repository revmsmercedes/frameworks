"""
ROI Calculator

Calculate the annual ROI value from time savings and error reduction.

Formula:
Annual Value = (Weekly Hours Saved × 50 × $75) + (Error Rate Reduction × Transaction Volume)
"""

def calculate_annual_value(weekly_hours_saved, error_rate_reduction, transaction_volume, hourly_value=75, work_weeks=50):
    time_savings_value = weekly_hours_saved * work_weeks * hourly_value
    error_reduction_value = error_rate_reduction * transaction_volume
    annual_value = time_savings_value + error_reduction_value
    return annual_value

def main():
    print("ROI Calculator")
    weekly_hours = float(input("Enter weekly hours saved: "))
    error_reduction = float(input("Enter error rate reduction (as decimal, e.g. 0.05): "))
    transactions = int(input("Enter annual transaction volume: "))

    roi = calculate_annual_value(weekly_hours, error_reduction, transactions)
    print(f"\nEstimated Annual Value: ${roi:,.2f}")

if __name__ == "__main__":
    main()
