
from database import init_db, save_ticket, get_all_tickets

init_db()

sample_ticket = (
    "My laptop cannot connect to the office Wi-Fi."
)

sample_result = {
    "category": "Network",
    "priority": "High",
    "sentiment": "Urgent",
    "suggested_response": "Please check your Wi-Fi connection.",
}

ticket_id = save_ticket(sample_ticket, sample_result)

print(f"Saved ticket ID: {ticket_id}")

tickets = get_all_tickets()

print(f"Total saved tickets: {len(tickets)}")
print("Latest ticket:", tickets[0]["description"])
