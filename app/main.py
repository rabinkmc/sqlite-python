import sys

from dataclasses import dataclass

# import sqlparse - available if you need it!

database_file_path = sys.argv[1]
command = sys.argv[2]


def handle_dbinfo():
    with open(database_file_path, "rb") as database_file:
        database_file.seek(16)
        page_size = int.from_bytes(database_file.read(2), byteorder="big")
        print(f"database page size: {page_size}")


match command:
    case ".dbinfo":
        handle_dbinfo()
    case _:
        print(f"Invalid command: {command}")
