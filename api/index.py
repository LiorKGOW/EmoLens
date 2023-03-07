from flask import Flask, flash, request, redirect, url_for,render_template,send_from_directory,jsonify
from werkzeug.utils import secure_filename
from deepface import DeepFace
import os



# if on windows, use this
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

# function to check if the file has an allowed extension (ex: .jpg, .png, etc.)
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# this is an example of route that renders a template
# to let you upload a file and then analyze it
# it will show the result of the analysis in the same page
@app.route('/', methods=['GET', 'POST'])
def upload_file():

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            analysis = DeepFace.analyze(img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename), actions = ['emotion'])
            print(analysis)
            return render_template('index.html', analysis=analysis['dominant_emotion'], filename=filename)
    return render_template('index.html')

# this endpoint returns the result of the analysis in json format
@app.route('/analyze', methods=[ 'POST'])
def analyze():

    file = request.files['file']
    if file.filename == '':
        print('No selected file')
        return 'No selected file'
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        saved_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        analysis = {}
        try:
            analysis = DeepFace.analyze(img_path = saved_path)
        except ValueError:
            analysis = {'error': 'could not detect face'}
        except:
            analysis = {'error': 'something went wrong'}
        print(analysis)
        return jsonify(analysis)
    else:
        return 'Something went wrong'


# this endpoint returns the image that was uploaded to let 
# the browser display it
@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


if __name__ == '__main__':
    app.run(debug=True)
    