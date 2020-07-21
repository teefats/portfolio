from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

#Write into the file
def write_to_file(data):
    with open('database.txt', mode = 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
   with open('database.csv',newline ='', mode='a') as database2:
       email = data['email']
       subject = data['subject']
       message = data['message']
       csv_writer = csv.writer(database2, delimiter = ',', quotechar = '"', quoting=csv.QUOTE_MINIMAL )
       csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods = ['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            print(data)
            return redirect("/thankyou.html")
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong on this occassion'



    # error = None
    # if request.method == 'POST':
    #     if valid_login(request.form['username'],
    #                    request.form['password']):
        #     return log_the_user_in(request.form['username'])
        # else:
        #     error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid


# @app.route('/about.html')
# def about():
#     return render_template("about.html")

# @app.route('/works.html')
# def works():
#     return render_template("works.html")

# @app.route('/work.html')
# def work():
#     return render_template("work.html")

# @app.route('/contact.html')
# def contact():
#     return render_template("contact.html")


# @app.route("/")
# def home():
#     return "Hello, Flaskssfffd!"



# @app.route('/<username>')
# def home(username= None):
#     # print(url_for('static', filename='favicon.ico'))
#     return render_template('index.html', name= username)

# @app.route('/<username>/<int:post_id>')
# def home(username= None,post_id = None):
#     # print(url_for('static', filename='favicon.ico'))
#     return render_template('index.html', name= username, post_id = post_id)


    
    

# @app.route("/blog")
# def blog():
#     return "These are my thoughts on blogs!"
# @app.route("/blogs")
# def blog():
#     return "This are my thoughts on blogs!"
    





