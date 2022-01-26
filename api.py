import subprocess
import os
from subprocess import Popen, PIPE
from flask_cors import CORS, cross_origin
from subprocess import check_output
from flask import Flask
from flask import request
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
app = Flask(__name__)
cors = CORS(app)
UPLOAD_FOLDER = './stolenData'
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'log'}



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        #if 'file' not in request.files:
        #    flash('No file part')
        #    return redirect(request.url)
        print("file: ", request.files)
        file = request.files['upload_file']
        
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file', name=filename))
    return 'ok'





@app.route('/submit/<submit_data>', methods = ['POST','GET'])
@cross_origin()
def submit(submit_data):
    if (request.method == 'POST'):
            f = open("trainee_data.txt", "a")
            f.write(submit_data)
            f.close()
            return submit_data; # a multidict containing POST data
               
@app.route('/deactivate_directives',methods=['GET'])
@cross_origin()
def deactivate():
    result_success = subprocess.check_output("bash deactivate_directives.sh", shell=True);
    return "deactivated directives";
   
@app.route('/restart_dt',methods=['GET'])
@cross_origin()
def restart():
    result_success = subprocess.check_output("bash restart_dt.sh", shell=True);
    return "restarted dt";

@app.route('/stop_cr',methods=['GET'])
@cross_origin()
def compose():
    result_success = subprocess.check_output("bash stop.sh &>/dev/null", shell=True);
    return "successfully shut down cyber range infrastructure";

@app.route('/start_cr',methods=['GET'])
@cross_origin()
def docker():
    result_success = subprocess.check_output("bash restart.sh &>/dev/null", shell=True)
    return "successfully started cyber range infrastructure";

@app.route('/attacker',methods=['GET'])
@cross_origin()
def attacker():
    result_success = subprocess.check_output("bash activate_directive.sh attacker", shell=True)
    return "ok";

@app.route('/mitm',methods=['GET'])
@cross_origin()
def mitm():
    result_success = subprocess.check_output("bash activate_directive.sh mitm", shell=True)
    return "ok";

@app.route('/dos',methods=['GET'])
@cross_origin()
def dos():
    result_success = subprocess.check_output("bash activate_directive.sh dos", shell=True)
    return "ok";

@app.route('/log_manipulation',methods=['GET'])
@cross_origin()
def log_manipulation():
    result_success = subprocess.check_output("bash activate_directive.sh log_manipulation", shell=True)
    return "ok";

@app.route('/arp',methods=['GET'])
@cross_origin()
def arp():
    result_success = subprocess.check_output("bash activate_directive.sh arp", shell=True)
    return "ok";

@app.route('/pull_frontend',methods=['GET'])
@cross_origin()
def pull_frontend():
    result_success = subprocess.check_output("bash git_pull_frontend.sh", shell=True)
    return "pulled frontendend from git"

@app.route('/pull_backend',methods=['GET'])
@cross_origin()
def pull_backend():
    result_success = subprocess.check_output("bash git_pull_backend.sh", shell=True)
    return "pulled backend from git"



app.run(port=9090, host="0.0.0.0")
