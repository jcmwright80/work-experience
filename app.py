from flask import Flask, request, render_template_string
from db import get_connection

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form["task"]
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO todos (task, due_date, complete) VALUES (%s,2025-06-10,0)", (task))
        conn.commit()
        conn.close()

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, task FROM todos")
    todos = cur.fetchall()
    conn.close()

    return render_template_string("""
        <form method="post">
            <input name="task"/>
            <button>Add</button>
        </form>
        <ul>
        {% for id, task in todos %}
            <li>{{ task }}</li>
        {% endfor %}
        </ul>
    """, todos=todos)

if __name__ == "__main__":
    app.run(debug=True)
