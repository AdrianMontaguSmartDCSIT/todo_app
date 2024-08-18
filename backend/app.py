"""Module for basic CRUD for a todo app."""

from flask import Flask, jsonify, request, Response

from backend.types import TodoItem, NewTodoCategory, UpdateTodoItem

app = Flask(__name__)

TODO_LIST: dict[str, list[str]] = {}


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

        TODO_LIST[category].append(new_item)

        return jsonify({"message": f"{new_item} was added successfully."}), 200
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
        old_item = api_package.old_item.lower()
        new_item = api_package.new_item.lower()

        if check_empty_string(category, old_item, new_item):
            return (
                jsonify({"error": "Items must not be blank."}),
                400,
            )

        if not TODO_LIST.get(category):
            return (
                jsonify({"error": f"Category {category} does not exist."}),
                404,
            )

        for index, item in enumerate(TODO_LIST[category]):
            if item == old_item:
                TODO_LIST[category][index] = new_item

                return (
                    jsonify(
                        {
                            "message": f"{old_item} was updated to "
                            f"{new_item} successfully."
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


@app.route("/api/todos/item", methods=["DELETE"])
def delete_todo_item() -> tuple[Response, int]:
    """Deletes a todo item from a specified category.

    :return: A message indicating success or failure
    :rtype: `tuple`[`flask.Response`, `int`]
    """
    try:
        api_package = TodoItem(**request.get_json())

        category = api_package.category.lower()
        item_to_delete = api_package.item.lower()

        if check_empty_string(category, item_to_delete):
            return (
                jsonify({"error": "Items must not be blank."}),
                400,
            )

        if not TODO_LIST.get(category):
            return (
                jsonify({"error": f"Category {category} does not exist."}),
                404,
            )

        for index, item in enumerate(TODO_LIST[category]):
            if item == item_to_delete:
                TODO_LIST[category].pop(index)

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
            jsonify({"message": f"{category} was created successfully."}),
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
