
from classifier import classify_ticket

ticket = (
    "My laptop cannot connect to the office Wi-Fi. "
    "I have an important meeting soon."
)

try:
    result = classify_ticket(ticket)

    print("\nTicket classification successful!")
    print("-" * 40)

    for key, value in result.items():
        print(f"{key}: {value}")

except Exception as error:
    print(f"\nClassification failed: {error}")
