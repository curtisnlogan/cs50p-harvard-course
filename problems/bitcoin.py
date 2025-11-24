""" """

import requests
import sys


def main():
    """Entry point for the script.
    Calls the Bitcoin price calculator function."""
    bitcoin_price_calc()


def bitcoin_price_calc():
    """
    Prompts for the amount of Bitcoin and fetches the current price from
    CoinCap API.
    Calculates and prints the total value in USD.
    """
    try:
        # sys.argv[0] is the filename; sys.argv[1] should be the
        # amount of Bitcoin
        amount_float = float(sys.argv[1])
        # sys.argv[1] can't be == to 'none' as it doesn't exist so it 'is' None
        if sys.argv[1] is None:
            sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")
    try:
        # Send GET request to CoinCap API to fetch current Bitcoin price
        query = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey="
            "28a94c01269532eab2449c48a35e974a1d60ccda2e8edaa86539e32a93c9b818"
        )
    except requests.RequestException:
        print("error")
    # takes my query and returns it in a readable json format, ties to var
    query_json = query.json()
    # The price is returned as a string, so convert to float
    current_price = float(query_json["data"]["priceUsd"])
    # Calculate the total value in USD
    total_price = current_price * amount_float
    # Print the result formatted with commas and 4 decimal places
    print(f"${total_price:,.4f}")


if __name__ == "__main__":
    main()
