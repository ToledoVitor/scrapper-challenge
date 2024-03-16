import logging
import sqlite3
from contextlib import closing
from typing import List, Tuple


class ScrapperStorage:
    def save_images(self, images: List[Tuple[str]]) -> None:

        with closing(sqlite3.connect("database.db")) as connection:
            with closing(connection.cursor()) as cursor:

                try:
                    cursor.execute(
                        """CREATE TABLE dogs (
                                    id INTEGER PRIMARY KEY,
                                    url varchar(255) NOT NULL,
                                    created_at text DEFAULT CURRENT_TIMESTAMP
                                )"""
                    )
                except sqlite3.OperationalError:
                    ...

                cursor.executemany("INSERT INTO dogs (url) VALUES (?)", images)
                logging.info(f"Database updated: {len(images)} new images saved")
