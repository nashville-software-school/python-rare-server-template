import sqlite3
import json
from models import Category

CATEGORIES = [
    {
        "id": 1,
        "label": "News"
    }
]

# # Function with a single parameter
# def get_single_animal(id):
#     with sqlite3.connect("./kennel.sqlite3") as conn:
#         conn.row_factory = sqlite3.Row
#         db_cursor = conn.cursor()

#         # Use a ? parameter to inject a variable's value
#         # into the SQL statement.
#         db_cursor.execute("""
#         SELECT
#             a.id,
#             a.name,
#             a.breed,
#             a.status,
#             a.location_id,
#             a.customer_id
#         FROM animal a
#         WHERE a.id = ?
#         """, (id, ))

#         # Load the single result into memory
#         data = db_cursor.fetchone()

#         # Create an animal instance from the current row
#         animal = Animal(data['id'], data['name'], data['breed'],
#                         data['status'], data['location_id'],
#                         data['customer_id'])

#         return json.dumps(animal.__dict__)


def create_category(category):
    # Get the id value of the last animal in the list
    max_id = CATEGORIES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    category["id"] = new_id

    # Add the animal dictionary to the list
    CATEGORIES.append(category)

    # Return the dictionary with `id` property added
    return category


def delete_category(_id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM category
        WHERE id = ?
        """, (id, ))


# def update_animal(id, new_animal):
#     # Iterate the ANIMALS list, but use enumerate() so that
#     # you can access the index value of each item.
#     for index, animal in enumerate(ANIMALS):
#         if animal["id"] == id:
#             # Found the animal. Update the value.
#             ANIMALS[index] = new_animal
#             break


def get_all_categories():
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.label
        FROM Categories c
        """)

        # Initialize an empty list to hold all animal representations
        categories = []

        # Convert rows of data into c Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            category = Category(row['id'], row['label'])

            categories.append(category.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(categories)


# def get_animals_by_location(location):

#     with sqlite3.connect("./kennel.sqlite3") as conn:
#         conn.row_factory = sqlite3.Row
#         db_cursor = conn.cursor()

#         # Write the SQL query to get the information you want
#         db_cursor.execute("""
#         select
#             a.id,
#             a.name,
#             a.species,
#             a.breed,
#             a.location_id,
#             a.customer_id
#         from Animal a
#         WHERE a.location = ?
#         """, (location, ))

#         animals = []
#         dataset = db_cursor.fetchall()

#         for row in dataset:
#             animal = Animal(
#                 row['id'], row['name'], row['address'], row['location'], row['password'])
#             animals.append(animal.__dict__)

#     return json.dumps(animals)


# def delete_animal(id):
#     with sqlite3.connect("./kennel.sqlite3") as conn:
#         db_cursor = conn.cursor()

#         db_cursor.execute("""
#         DELETE FROM animal
#         WHERE id = ?
#         """, (id, ))


# def update_animal(id, new_animal):
#     with sqlite3.connect("./kennel.sqlite3") as conn:
#         db_cursor = conn.cursor()

#         db_cursor.execute("""
#         UPDATE Animal
#             SET
#                 name = ?,
#                 breed = ?,
#                 status = ?,
#                 location_id = ?,
#                 customer_id = ?
#         WHERE id = ?
#         """, (new_animal['name'], new_animal['breed'],
#               new_animal['status'], new_animal['location_id'],
#               new_animal['customer_id'], id, ))

#         # Were any rows affected?
#         # Did the client send an `id` that exists?
#         rows_affected = db_cursor.rowcount

#     if rows_affected == 0:
#         # Forces 404 response by main module
#         return False
#     else:
#         # Forces 204 response by main module
#         return True
