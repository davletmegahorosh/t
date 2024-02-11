import sqlite3
from pathlib import Path
from datetime import datetime, timedelta

def check_db(send_text):
    if get_text() == []:
        return True
    for text in get_text():
        if send_text != list(text)[1]:
            return True
    return False

def init_db():
    try:
        global db, cursor
        with sqlite3.connect(Path(__file__).parent.parent / "db.sqlite3") as connection:
            db = connection
            cursor = db.cursor()
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")


def create_tables():
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS existed_texts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            time DATETIME
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS gpt_request (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS chats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chat_id INTEGER
        )
        """
    )
    db.commit()

def get_text():
    cursor.execute(
        """
        SELECT * FROM existed_texts
        """
    )
    return [i for i in cursor.fetchall()]

def get_request():
    cursor.execute(
        """
        SELECT * FROM gpt_request
        """
    )
    return cursor.fetchone()[1]

def get_chats():
    cursor.execute(
        """
        SELECT * FROM chats
        """
    )
    return [i[1] for i in cursor.fetchall()]


def change_request(text):
    cursor.execute(
        """
        DELETE FROM gpt_request
    """
    )
    cursor.execute(
        """
        INSERT OR IGNORE INTO gpt_request(text)
         VALUES(:text)
        """,
        {'text':text}
    )
    db.commit()

def add_chat(chat_id):
    cursor.execute(
        """
        INSERT OR IGNORE INTO chats(chat_id)
         VALUES(:text)
        """,
        {'chat_id':chat_id}
    )
    db.commit()


def save_text(text):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        """
        INSERT INTO existed_texts (text, time)
        VALUES (:t, :time)
        """,
        {
            "t": text,
            "time": current_time,
        }
    )
    db.commit()

def drop_db():
    one_hour_ago = (datetime.now() - timedelta(minutes=10)).strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        """
        DELETE FROM existed_texts
        WHERE time <= :time_threshold
        """,
        {
            "time_threshold": one_hour_ago,
        }
    )
    db.commit()

