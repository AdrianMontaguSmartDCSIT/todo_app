"""Module for basic CRUD for a todo app."""

import uuid

from flask import Flask, jsonify, request, Response
from flask_cors import CORS

from backend.types import (
    TodoItem,
    NewTodoCategory,
    UpdateTodoItem,
    DeleteTodoItem,
)

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

TODO_LIST: dict[str, list[dict[str, str]]] = {}


@app.route("/")
@app.route("/index")
def home() -> str:
    return "Hello World!"


@app.route("/api/todos")
def get_todos() -> tuple[Response, int]:
    """Returns all todo categorues and items.

    :return: A dictionary of todo list items
    :rtype: `tuple`[`flask.Response`, `int`]
    """
    try:
        return jsonify(TODO_LIST), 200
    except Exception:
        return (
            jsonify(
                {"error": "An error occurred while processing your request."}
            ),
            500,
        )


def check_empty_string(*args):
    for item in args:
        if item == "":
            return True
    return False


@app.route("/api/todos/item", methods=["POST"])
def create_todo_item() -> tuple[Response, int]:
    """Creates a new todo item in a specified category.

    :return: A message indicating success or failure
    :rtype: `tuple`[`flask.Response`, `int`]
    """
    try:
        api_package = TodoItem(**request.get_json())

        category = api_package.category.lower()
        new_item = api_package.item.lower()

        if check_empty_string(category, new_item):
            return (
                jsonify({"error": "Items must not be blank."}),
                400,
            )

        if not TODO_LIST.get(category):
            return (
                jsonify({"error": f"Category {category} does not exist."}),
                404,
            )

        if new_item in TODO_LIST[category]:
            return (
                jsonify({"error": f"Item {new_item} already exists."}),
                409,
            )

        item = dict(id=uuid.uuid4(), name=new_item)

        TODO_LIST[category].append(item)

        return (
            jsonify(
                {
                    "item": item,
                    "message": f"{new_item} was added successfully.",
                }
            ),
            200,
        )
    except ValueError as e:
        print(f"A valuerror occured - {e}")
        return (
            jsonify(
                {"error": "Invalid data format. Please check your input."}
            ),
            400,
        )
    except KeyError as e:
        print(f"A keyerror occured - {e}")
        return (
            jsonify(
                {"error": "Invalid request format. Please check your input."}
            ),
            400,
        )
    except Exception as e:
        print(f"An error occured - {e}")
        return (
            jsonify(
                {"error": "An error occurred while processing your request."}
            ),
            500,
        )


@app.route("/api/todos/item", methods=["PUT"])
def update_todo_item() -> tuple[Response, int]:
    """Updates an existing todo item in a specified category.

    :return: A message indicating success or failure
    :rtype: `tuple`[`flask.Response`, `int`]
    """
    try:
        api_package = UpdateTodoItem(**request.get_json())

        category = api_package.category.lower()
        id = api_package.id
        new_item = api_package.new_item.lower()

        if check_empty_string(category, id, new_item):
            return (
                jsonify({"error": "Items must not be blank."}),
                400,
            )

        if not TODO_LIST.get(category):
            return (
                jsonify({"error": f"Category {category} does not exist."}),
                404,
            )

        for item in TODO_LIST[category]:
            if item.id == id:
                old_item = item.name
                item.name = new_item

                return (
                    jsonify(
                        {
                            "id": id,
                            "category": category,
                            "item": new_item,
                            "message": f"{old_item} was updated to "
                            f"{new_item} successfully.",
                        }
                    ),
                    200,
                )

        return jsonify({"error": f"{old_item} was not found."}), 404
    except ValueError as e:
        print(f"A valuerror occured - {e}")
        return (
            jsonify(
                {"error": "Invalid data format. Please check your input."}
            ),
            400,
        )
    except KeyError as e:
        print(f"A keyerror occured - {e}")
        return (
            jsonify(
                {"error": "Invalid request format. Please check your input."}
            ),
            400,
        )
    except Exception as e:
        print(f"An error occured - {e}")
        return (
            jsonify(
                {"error": "An error occurred while processing your request."}
            ),
            500,
        )


def remove_entry(category: str, id_to_remove: str):
    list_to_return = []
    for item in TODO_LIST[category]:
        if item["id"] == id_to_remove:
            item_to_remove = item["name"]
        else:
            list_to_return.append(item)
    return list_to_return, item_to_remove


@app.route("/api/todos/item", methods=["DELETE"])
def delete_todo_item() -> tuple[Response, int]:
    """Deletes a todo item from a specified category.

    :return: A message indicating success or failure
    :rtype: `tuple`[`flask.Response`, `int`]
    """
    try:
        api_package = DeleteTodoItem(**request.get_json())

        category = api_package.category.lower()
        id = api_package.id

        if check_empty_string(category, id):
            return (
                jsonify({"error": "Items must not be blank."}),
                400,
            )

        if not TODO_LIST.get(category):
            return (
                jsonify({"error": f"Category {category} does not exist."}),
                404,
            )
        original_length = len(TODO_LIST[category])

        TODO_LIST[category], item_to_delete = remove_entry(category, id)

        if len(TODO_LIST[category]) != original_length:
            return (
                jsonify(
                    {
                        "message": f"{item_to_delete} was deleted "
                        "successfully."
                    }
                ),
                200,
            )

        return jsonify({"error": f"{item_to_delete} was not found."}), 404
    except ValueError as e:
        print(f"A valuerror occured - {e}")
        return (
            jsonify(
                {"error": "Invalid data format. Please check your input."}
            ),
            400,
        )
    except KeyError as e:
        print(f"A keyerror occured - {e}")
        return (
            jsonify(
                {"error": "Invalid request format. Please check your input."}
            ),
            400,
        )
    except Exception as e:
        print(f"An error occured - {e}")
        return (
            jsonify(
                {"error": "An error occurred while processing your request."}
            ),
            500,
        )


@app.route("/api/todos/category", methods=["POST"])
def create_todo_category() -> tuple[Response, int]:
    """Creates a new todo category.

    :return: A message indicating success or failure
    :rtype: `tuple`[`flask.Response`, `int`]
    """
    try:
        api_package = NewTodoCategory(**request.get_json())

        category = api_package.category.lower()

        if check_empty_string(category):
            return (
                jsonify({"error": "Category must not be blank."}),
                400,
            )

        if TODO_LIST.get(category):
            return (
                jsonify({"error": f"Category {category} already exists."}),
                409,
            )

        TODO_LIST[category] = []

        return (
            jsonify(
                {
                    "category": category,
                    "message": f"{category} was created successfully.",
                }
            ),
            200,
        )
    except ValueError as e:
        print(f"A valuerror occured - {e}")
        return (
            jsonify(
                {"error": "Invalid data format. Please check your input."}
            ),
            400,
        )
    except KeyError as e:
        print(f"A keyerror occured - {e}")
        return (
            jsonify(
                {"error": "Invalid request format. Please check your input."}
            ),
            400,
        )
    except Exception as e:
        print(f"An error occured - {e}")
        return (
            jsonify(
                {"error": "An error occurred while processing your request."}
            ),
            500,
        )


if __name__ == "__main__":
    app.run(debug=True)
