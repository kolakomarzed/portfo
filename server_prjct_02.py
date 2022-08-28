from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
import os


@app.route("/")
def home_page():
    return render_template('./index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name) 



def prep_csv(file):
    if not os.path.exists(file):
        headers = ['email','subject','message']
        csv_file = open(file, 'w') 
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(headers)


def write_to_csv(data):
    with open (file, mode ='a',newline= '') as database2: 
                email = data['email']
                subject = data['subject']
                message = data ['message']
                fieldnames = ['email','subject','message']
                csv_writer = csv.DictWriter(database2,fieldnames=fieldnames)  
                csv_writer.writerow({'email':email,'subject':subject,'message':message}) 


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
 
    if request.method == 'POST':
        
        global file
        file = 'database.csv'
        data = request.form.to_dict()
        prep_csv(file)
        write_to_csv(data)
        return redirect ('/thank_you.html')



