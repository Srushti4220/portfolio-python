from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Database credentials
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "srushti",
}

# Route to render the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    # Database connectivity code
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Process the form submission
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Insert data into the database
        sql = "INSERT INTO Contacts (name, email, message) VALUES (%s, %s, %s)"
        values = (name, email, message)

        try:
            cursor.execute(sql, values)
            conn.commit()
            return '<script>alert("Message sent successfully"); window.location.href = "/";</script>'
        except Exception as e:
            return f"Error: {str(e)}"
        finally:
            cursor.close()
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)
