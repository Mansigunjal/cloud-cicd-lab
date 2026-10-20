
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

tasks = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Task Tracker</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f1f5f9;
            margin: 0;
            padding: 40px 15px;
        }
        .container {
            max-width: 700px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 15px #0001;
        }
        h1 { color: #234e70; }
        input, button {
            box-sizing: border-box;
            padding: 12px;
            margin: 6px 0;
            width: 100%;
        }
        button {
            background: #2563eb;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }
        li {
            background: #eff6ff;
            margin: 10px 0;
            padding: 14px;
            border-radius: 6px;
        }
        .subtitle { color: #64748b; }
    </style>
</head>
<body>
<div class="container">
    <h1>Student Task Tracker</h1>
    <p class="subtitle">Organize your assignments and deadlines.</p>

    <h2>Add a New Task</h2>
    <form action="/add" method="POST">
        <input name="title" placeholder="Task title" required>
        <input name="subject" placeholder="Subject" required>
        <label>Due date</label>
        <input type="date" name="due_date" required>
        <button type="submit">Add Task</button>
    </form>

    <h2>My Tasks ({{ tasks|length }})</h2>
    {% if tasks %}
        <ul>
        {% for task in tasks %}
            <li>
                <strong>{{ task.title }}</strong><br>
                Subject: {{ task.subject }}<br>
                Due date: {{ task.due_date }}
            </li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No tasks added yet. Add your first task above!</p>
    {% endif %}
</div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()
    subject = request.form.get("subject", "").strip()
    due_date = request.form.get("due_date", "")

    if title and subject and due_date:
        tasks.append({
            "title": title,
            "subject": subject,
            "due_date": due_date
        })

    return redirect("/")

@app.route("/student")
def student():
    return {
        "name": "Student",
        "course": "Cloud Computing and DevOps"
    }

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
