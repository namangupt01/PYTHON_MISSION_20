# Hardcoded exchange rates as of a certain date
print("ABBREVIATIONS FOR CURRENCIES : EUR  USD  JPY  INR   GBP")
exchange_rates = {#https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=EUR HERE I HAVE USED THIS
    "USD": {"EUR": 0.92066, "JPY": 156.89623, "GBP": 0.782910, "INR": 83.119288},
    "EUR": {"USD": 1.0861094, "JPY": 170.40145, "GBP": 0.085034493, "INR": 90.276889},
    "JPY": {"USD": 0.00637326635, "EUR": 0.0058676727, "GBP": 0.0049895136 , "INR": 0.52971831},
    "GBP": {"USD": 1.2772708, "EUR": 1.1759773, "JPY": 200.41837, "INR": 106.17033},
    "INR": {"USD": 0.012030902, "EUR": 0.01107676, "JPY": 1.8875942, "GBP": 0.0094189474}
}
# HERE I HAVE  CREATED THE DICTIONARY WHICH IS A COLLECTION OF KEY - VALUE PAIR
# HERE IT CONTAINED THE NESTED DICTIONARY TO REPRESENT EXCHANGE RATES FOR DIFFERENT CURRENCIES

# THIS IS THE SIMPLE METHOD PASSINF TWO ARGUMENTS AS BASE CURRENCY AND THE TARGET CURRENCY 
# HERE I HAVE USED THE TRY AND CATCH TO HANDLE THE ERROR EXCEPTIION ALREADY EXPLAINED IN THE CODE 
def get_exchange_rate(base_currency, target_currency):
    try:
        rate = exchange_rates[base_currency][target_currency]
        return rate
    except KeyError:
        raise ValueError(f"Exchange rate not available for {base_currency} to {target_currency}")

def convert_currency(amount, base_currency, target_currency):
    try:
        exchange_rate = get_exchange_rate(base_currency, target_currency)
        converted_amount = amount * exchange_rate
        return converted_amount
    except ValueError as e:
        print(f"Error: {e}")
        return None
# NOW THIS METHOD IS FOR CONVERTING THE CURRENCY WITH AMOUNT, BASE CURRENCY, TARGET CURRENCY AS THE ARGUMENTS AND AGAIN 
# USED THE TRY AND CATCH TO CONVERT SIMPLY APPLY THE FORMULA 
# HERE Exhange rate = the particular dictionary part 

def main():
    base_currency = input("Enter base currency (e.g., USD): ").upper()
    target_currency = input("Enter target currency (e.g., EUR): ").upper()
    amount = float(input(f"Enter amount in {base_currency}: "))

    converted_amount = convert_currency(amount, base_currency, target_currency)
    if converted_amount is not None:
        print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")

if __name__ == "__main__":
    main()
