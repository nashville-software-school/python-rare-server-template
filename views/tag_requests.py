import sqlite3
import json
from models import Tag

TAGS = [
    {
        "id": 1,
        "label": "Blue",
        "user_id":1
    },
    {
        "id": 2,
        "label": "Purple",
        "user_id":3
    },
    {
        "id": 3,
        "label": "Red",
        "user_id":2
    }
]

def get_all_tags():
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            t.id,
            t.label
            t.user_id
        FROM Tags t
        """)
        
        tags = []
        
        data = db_cursor.fetchall()
        
        for row in data:
            tag = Tag(row["id"], row["label"], row["user_id"])
            tags.append(tag.__dict__)
                  
            return json.dumps(tags)
    
def get_single_tag(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            t.id,
            t.label
            t.user_id
        FROM Tags t
        WHERE t.id = ?
        """, (id, ))
        
        data = db_cursor.fetchone()
        
        tag = Tag(data["id"], data["label"], data["user_id"])
        
        return json.dumps(tag.__dict__)
    
def create_tag(new_tag):
    # max_id = TAGS[-1]["id"]
    # new_id = max_id + 1
    # tag["id"] = new_id
    # TAGS.append(tag)
    # return tag
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        INSERT INTO Tags (label)
        VALUES (?)
        """, (new_tag["label"], ))
        
        id = db_cursor.lastrowid
        
        new_tag["id"] = id
        
    return json.dumps(new_tag)
# # def get_all_tags():
# #     return TAGS

# # # Function with a single parameter
# # def get_single_tag(id):
# # # Variable to hold the found tag, if it exists
# #     requested_tag = None

# #     # Iterate the TAGS list above. Very similar to the
# #     # for..of loops you used in JavaScript.
# #     for tag in TAGS:
# #         # Dictionaries in Python use [] notation to find a key
# #         # instead of the dot notation that JavaScript used.
# #         if tag["id"] == id:
# #             requested_tag = tag

# #     return requested_tag

# def create_tag(tag):
#     # Get the id value of the last tag in the list
#     max_id = TAGS[-1]["id"]

#     # Add 1 to whatever that number is
#     new_id = max_id + 1

#     # Add an `id` property to the tag dictionary
#     tag["id"] = new_id

#     # Add the tag dictionary to the list
#     TAGS.append(tag)

#     # Return the dictionary with `id` property added
#     return tag

# # def delete_tag(id):
# #     # Initial -1 value for tag index, in case one isn't found
# #     tag_index = -1

# #     # Iterate the TAGS list, but use enumerate() so that you
# #     # can access the index value of each item
# #     for index, tag in enumerate(TAGS):
# #         if tag["id"] == id:
# #             # Found the tag. Store the current index.
# #             tag_index = index

# #     # If the tag was found, use pop(int) to remove it from list
# #     if tag_index >= 0:
# #         TAGS.pop(tag_index)

# def update_tag(id, new_tag):
#     # Iterate the TAGS list, but use enumerate() so that
#     # you can access the index value of each item.
#     for index, tag in enumerate(TAGS):
#         if tag["id"] == id:
#             # Found the tag. Update the value.
#             TAGS[index] = new_tag
#             break
        
# def get_all_tags():
#     # Open a connection to the database
#     with sqlite3.connect("./kennel.sqlite3") as conn:

#         # Just use these. It's a Black Box.
#         conn.row_factory = sqlite3.Row
#         db_cursor = conn.cursor()

#         # Write the SQL query to get the information you want
#         db_cursor.execute("""
#         SELECT
#             a.id,
#             a.name
#             a.user_id
#         FROM tag a
#         """)

#         # Initialize an empty list to hold all tag representations
#         tags = []

#         # Convert rows of data into a Python list
#         dataset = db_cursor.fetchall()

#         # Iterate list of data returned from database
#         for row in dataset:

#             # Create an tag instance from the current row.
#             # Note that the database fields are specified in
#             # exact order of the parameters defined in the
#             # Animal class above.
#             tag = Tag(row['id'], row['name'], row['user_id'])

#             tags.append(tag.__dict__)

#     # Use `json` package to properly serialize list as JSON
#     return json.dumps(tags)

# def get_single_tag(id):
#     with sqlite3.connect("./kennel.sqlite3") as conn:
#         conn.row_factory = sqlite3.Row
#         db_cursor = conn.cursor()

#         # Use a ? parameter to inject a variable's value
#         # into the SQL statement.
#         db_cursor.execute("""
#         SELECT
#             a.id,
#             a.name
#             a.user_id
#         FROM Tag a
#         WHERE a.id = ?
#         """, ( id, ))

#         # Load the single result into memory
#         data = db_cursor.fetchone()

#         # Create an tag instance from the current row
#         tag = Tag(data['id'], data['name'], data['user_id'])

#         return json.dumps(tag.__dict__)
    
# def get_tags_by_user_id(user_id):

#         with sqlite3.connect("./kennel.sqlite3") as conn:
#             conn.row_factory = sqlite3.Row
#             db_cursor = conn.cursor()

#             # Write the SQL query to get the information you want
#             db_cursor.execute("""
#             select
#                 a.id,
#                 a.name
#                 a.user_id
#             from Tag a
#             WHERE a.user_id = ?
#             """, ( user_id, ))

#             tags = []
#             dataset = db_cursor.fetchall()

#             for row in dataset:
#                 tag = Tag(row['id'], row['name'],row['user_id'])
#                 tags.append(tag.__dict__)

#         return json.dumps(tags)
    
# def get_tags_by_name(name):

#         with sqlite3.connect("./kennel.sqlite3") as conn:
#             conn.row_factory = sqlite3.Row
#             db_cursor = conn.cursor()

#             # Write the SQL query to get the information you want
#             db_cursor.execute("""
#             select
#                 s.id,
#                 s.name
#                 s.user_id
#             from Tag s
#             WHERE s.name = ?
#             """, ( name, ))

#             tags = []
#             dataset = db_cursor.fetchall()

#             for row in dataset:
#                 tag = Tag(row['id'], row['name'], row['user_id'])
#                 tags.append(tag.__dict__)

#         return json.dumps(tags)

# def delete_tag(id):
#     with sqlite3.connect("./kennel.sqlite3") as conn:
#         db_cursor = conn.cursor()

#         db_cursor.execute("""
#         DELETE FROM tag
#         WHERE id = ?
#         """, (id, ))
