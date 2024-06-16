from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open(r'E:\Portfolio\database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print("Form Data Received:", data)  # Debugging line
            write_to_csv(data)
            return redirect('/thankyou.html')
        except Exception as e:
            print(f"An error occurred: {e}")  # Detailed error message
            return 'did not save to database'
    else:
        return 'something went wrong'

if __name__ == '__main__':
    app.run(debug=True)
