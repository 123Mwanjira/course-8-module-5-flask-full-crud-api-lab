# Module Lab: Building Full CRUD RESTful APIs with Flask

## Learning Goals

* Implement RESTful API endpoints using Flask.
* Handle HTTP GET, POST, PATCH, and DELETE methods.
* Accept and process JSON input using `request.get_json()`.
* Simulate persistent data using in-memory Python objects.
* Return structured JSON responses with appropriate HTTP status codes.
* Handle validation errors and missing resources.

## Introduction

This project implements a RESTful Flask API for managing events.

The API supports:

* Viewing a welcome message
* Viewing all events
* Creating new events
* Updating event titles
* Deleting events

The application uses an in-memory Python list instead of a database.

## Setup Instructions

### Install Dependencies

Ensure Python is installed:

```bash
python --version
```

Install the project dependencies using Pipenv:

```bash
pipenv install
```

Run the application with:

```bash
pipenv run python app.py
```

The API will be available at:

```text
http://localhost:5000
```

## API Endpoints

| Method | Endpoint       | Description              | Success Status |
| ------ | -------------- | ------------------------ | -------------- |
| GET    | `/`            | Return a welcome message | 200            |
| GET    | `/events`      | Return all events        | 200            |
| POST   | `/events`      | Create a new event       | 201            |
| PATCH  | `/events/<id>` | Update an event title    | 200            |
| DELETE | `/events/<id>` | Delete an event          | 204            |

## Example Requests

### Get Welcome Message

```bash
curl http://localhost:5000/
```

### Get All Events

```bash
curl http://localhost:5000/events
```

### Create an Event

```bash
curl -X POST http://localhost:5000/events \
  -H "Content-Type: application/json" \
  -d '{"title": "Hackathon"}'
```

Example response:

```json
{
  "id": 3,
  "title": "Hackathon"
}
```

### Update an Event

```bash
curl -X PATCH http://localhost:5000/events/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Hackathon 2025"}'
```

### Delete an Event

```bash
curl -X DELETE http://localhost:5000/events/2
```

A successful delete returns:

```text
204 No Content
```

## Input Validation and Error Handling

The API validates incoming requests.

### Missing Title

A POST or PATCH request without a `title` returns:

```text
400 Bad Request
```

with a JSON error message:

```json
{
  "error": "Title is required"
}
```

### Event Not Found

Updating or deleting an event that does not exist returns:

```text
404 Not Found
```

with:

```json
{
  "error": "Event not found"
}
```

## Testing

The project includes automated tests using pytest.

Run the tests with:

```bash
pipenv run pytest
```

The test suite verifies:

* Event creation
* Event updating
* Updating a missing event
* Event deletion
* Deleting a missing event

## Implementation Details

The API uses:

* Flask for the web application
* `request.get_json()` for JSON request data
* `jsonify()` for JSON responses
* An `Event` class to represent events
* An in-memory list as the data store

The event IDs are generated automatically when new events are created.

## Best Practices Demonstrated

* RESTful route naming
* Appropriate HTTP methods
* Appropriate HTTP status codes
* JSON responses
* Input validation
* 404 handling for missing resources
* Inline comments explaining important logic
* Automated testing with pytest

## Conclusion

This lab demonstrates how to build a complete CRUD-style REST API using Flask and an in-memory data store. It provides a foundation for building APIs that can later be extended to use a persistent database.
 Author
  Maurine Wanjira