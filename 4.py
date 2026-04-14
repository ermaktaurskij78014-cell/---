from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def connect():
    conn = sqlite3.connect("books.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = connect()
    conn.execute("""CREATE TABLE IF NOT EXISTS authors (
        author_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )""")
    conn.execute("""CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author_id INTEGER NOT NULL,
        year INTEGER,
        genre TEXT,
        price REAL,
        FOREIGN KEY (author_id) REFERENCES authors(author_id)
    )""")
    conn.execute("INSERT OR IGNORE INTO authors (author_id, name) VALUES (1, 'Лев Толстой')")
    conn.execute("INSERT OR IGNORE INTO authors (author_id, name) VALUES (2, 'Достоевский')")
    conn.execute("INSERT OR IGNORE INTO authors (author_id, name) VALUES (3, 'Булгаков')")
    conn.execute("INSERT OR IGNORE INTO books VALUES (1,'Война и мир',1,1869,'Роман',850.0)")
    conn.execute("INSERT OR IGNORE INTO books VALUES (2,'Анна Каренина',1,1877,'Роман',650.0)")
    conn.execute("INSERT OR IGNORE INTO books VALUES (3,'Преступление и наказание',2,1866,'Роман',550.0)")
    conn.execute("INSERT OR IGNORE INTO books VALUES (4,'Мастер и Маргарита',3,1967,'Фэнтези',720.0)")
    conn.commit()
    conn.close()


@app.route("/")
def index():
    return jsonify({"message": "Books API"})


@app.route("/books", methods=["GET"])
def get_books():
    conn = connect()
    res = conn.execute("""
        SELECT b.book_id, b.title, a.name, b.year, b.genre, b.price
        FROM books b JOIN authors a ON b.author_id = a.author_id
    """).fetchall()
    conn.close()
    return jsonify([dict(r) for r in res])


@app.route("/books/<int:id>", methods=["GET"])
def get_book(id):
    conn = connect()
    res = conn.execute("""
        SELECT b.book_id, b.title, a.name, b.year, b.genre, b.price
        FROM books b JOIN authors a ON b.author_id = a.author_id
        WHERE b.book_id = ?
    """, (id,)).fetchone()
    conn.close()
    if res is None:
        return jsonify({"error": "not found"}), 404
    return jsonify(dict(res))


@app.route("/books", methods=["POST"])
def add_book():
    d = request.get_json()
    conn = connect()
    conn.execute(
        "INSERT INTO books (title, author_id, year, genre, price) VALUES (?,?,?,?,?)",
        (d["title"], d["author_id"], d.get("year"), d.get("genre"), d.get("price"))
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "added"}), 201


@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    conn = connect()
    conn.execute("DELETE FROM books WHERE book_id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "deleted"})


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
