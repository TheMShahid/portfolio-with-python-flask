from flask import Flask, render_template, request, url_for, redirect
import csv

app = Flask(__name__)

# @app.route('/<username>/<int:post_id>')
# def hello_world(username=None, post_id = None):
#   return render_template('server.html', name=username, post_id=post_id)



@app.route('/')
def root():
  return render_template('index.html')

@app.route('/<string:page_name>')
def HtmlPage(page_name):
  return render_template(page_name)

def write_to_file(data):
  with open('../database.txt', mode='a') as database:
    email = data['email']
    subject = data['subject']
    message = data['message']
    file = database.write(f'\n {email}, {subject}, {message}')

def write_to_csv(data):
  with open('database.csv', mode='a') as database2:
    email = data['email']
    subject = data['subject']
    message = data['message']
    csv_writer = csv.writer(database2, delimiter=',', quotechar=',', quoting=1)
    csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
  if request.method == 'POST':
    try:
      data = request.form.to_dict()
      write_to_csv(data)
      return redirect('/Thanks.html')
    except:
      return 'did not save to database'
  else:
    return 'somethings went wrong. Try again!'

# @app.route('/works.html')
# def works():
#   return render_template('works.html')
#
# @app.route('/about.html')
# def about():
#   return render_template('about.html')
#
# @app.route('/contact.html')
# def contact():
#   return render_template('contact.html')
#
# @app.route('/components.html')
# def components():
#   return render_template('components.html')