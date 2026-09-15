from flask import Flask, jsonify, request

app = Flask(__name__)


# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}


# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]


@app.route("/", methods=["GET"])
def home():
    """Return a welcome message."""
    return jsonify({"message": "Welcome to the Events API"}), 200


@app.route("/events", methods=["GET"])
def get_events():
    """Return all events."""
    return jsonify([event.to_dict() for event in events]), 200


@app.route("/events", methods=["POST"])
def create_event():
    """Create a new event from JSON input."""
    data = request.get_json(silent=True)

    # Validate that JSON data and the title are provided.
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    # Generate a new ID.
    new_id = max([event.id for event in events], default=0) + 1

    # Create and store the new event.
    new_event = Event(new_id, data["title"])
    events.append(new_event)

    return jsonify(new_event.to_dict()), 201


@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    """Update the title of an existing event."""
    data = request.get_json(silent=True)

    # Find the event by ID.
    event = next((event for event in events if event.id == event_id), None)

    if event is None:
        return jsonify({"error": "Event not found"}), 404

    # Validate the title.
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    # Update the event title.
    event.title = data["title"]

    return jsonify(event.to_dict()), 200


@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    """Remove an event from the list."""
    # Find the event by ID.
    event = next((event for event in events if event.id == event_id), None)

    if event is None:
        return jsonify({"error": "Event not found"}), 404

    # Remove the event from the in-memory database.
    events.remove(event)

    return "", 204


if __name__ == "__main__":
    app.run(debug=True)