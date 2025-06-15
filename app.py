from flask import Flask, render_template, request
from my_utils import is_unique_entry, save_to_firebase

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    description = request.form.get('description')

    if not name or not email or not description:
        return render_template('index.html', message="Please fill in all fields.")

    if not is_unique_entry(email, description):
        return render_template('index.html', message="Duplicate entry. Data not added.")

    save_to_firebase(name, email, description)
    return render_template('index.html', message="Submitted successfully!")

if __name__ == '__main__':
    app.run(debug=True)