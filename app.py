
from flask import Flask, render_template, request
from classifier import classify_ticket
from database import (
    init_db,
    save_ticket,
    get_all_tickets,
    get_dashboard_stats,
)
from flask import Flask, render_template, request
app = Flask(__name__)

# Limit submitted form data to 10 KB.
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None
    description = ""

    if request.method == "POST":
        description = request.form.get("description", "").strip()

        if not description:
            error = "Please enter a ticket description."

        elif len(description) > 3000:
            error = "Ticket description must be 3000 characters or fewer."

        else:
            try:
                result = classify_ticket(description)
                ticket_id = save_ticket(description, result)
                result["ticket_id"] = ticket_id

            except Exception:
                app.logger.exception("Ticket classification failed.")
                error = (
                    "Unable to classify this ticket right now. "
                    "Please try again later."
                )

    return render_template(
        "index.html",
        result=result,
        error=error,
        description=description,
    )



@app.route("/tickets")
def tickets():
    all_tickets = get_all_tickets()

    categories = ["Hardware", "Software", "Network", "Access", "Other"]
    priorities = ["Critical", "High", "Medium", "Low"]

    selected_category = request.args.get("category", "")
    selected_priority = request.args.get("priority", "")

    # Ignore unsupported filter values.
    if selected_category not in categories:
        selected_category = ""

    if selected_priority not in priorities:
        selected_priority = ""

    # Apply the selected filters.
    if selected_category:
        all_tickets = [
            ticket for ticket in all_tickets
            if ticket["category"] == selected_category
        ]

    if selected_priority:
        all_tickets = [
            ticket for ticket in all_tickets
            if ticket["priority"] == selected_priority
        ]

    return render_template(
        "tickets.html",
        tickets=all_tickets,
        categories=categories,
        priorities=priorities,
        selected_category=selected_category,
        selected_priority=selected_priority,
    )



@app.errorhandler(413)
def request_too_large(error):
    return "Request too large. Please submit a shorter ticket.", 413


@app.route("/dashboard")
def dashboard():
    stats = get_dashboard_stats()
    return render_template("dashboard.html", stats=stats)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
