import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    amount = float(sys.argv[1])

except ValueError:
    sys.exit("command-line argument is not a number")


API_KEY = "c25cc059e4f1b11e28414b3dda30a61e5314e3ea32ca5dc20f0dc0ce872c9049"

url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"

try:
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    price = float(data["data"]["priceUsd"])

except requests.RequestException:
    sys.exit("API request failed")

total = amount * price

print(f"${total:,.4f}")


