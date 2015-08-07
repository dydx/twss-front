from flask import Flask, render_template, request, url_for
import urllib2, urllib

twss_url = 'http://45.55.79.204:32768/api'

app = Flask(__name__)

# present user with form
# accept POST requests from form
# query external API for data
# respond with results of API request

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/submit/', methods=['POST'])
def submitted():
    phrase = request.form['phrase']
    twss_data = urllib2.Request(twss_url, phrase)
    data_handler = urllib2.urlopen(twss_data)
    return render_template('submitted.html', data = data_handler.read())

if __name__ == "__main__":
    print('**** Flask Service Started ****')
    app.debug = True
    app.run()
