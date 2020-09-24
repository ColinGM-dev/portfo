from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
# print(__name__)

@app.route('/templates/index.html')
def my_home():
    return render_template('/index.html')

# @app.route('/<string:page_name>')
# def html_page(page_name):
#     return render_template(page_name)

@app.route('/templates/about.html')
def about():
    return render_template('/about.html')

@app.route('/templates/contact.html')
def contact():
    return render_template('/contact.html')

@app.route('/templates/work.html')
def work():
    return render_template('/work.html')

@app.route('/templates/components.html')
def components():
    return render_template('/components.html')

# @app.route('/templates/thankyou.html')
# def about():
#     return render_template('/thankyou.html')

def write_to_file(data):
    with open('data_base.txt', mode='a') as database:
        email = data['email']
        phone = data['phone']
        name = data['name']
        file = database.write(f'\n {email}, {phone}, {name}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as dbase:
        email = data['email']
        phone = data['phone']
        name = data['name']
        message = data['message']
        csv_writer = csv.writer(dbase, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, phone, name, message])

@app.route('/templates/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return render_template('/thankyou.html')
        except:
            return 'Data not submitted'
    else:
        return render_template('/wrong.html')








