import os
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

# We still define a path for logic, but we will use /tmp for saving
UPLOAD_FOLDER = '/tmp'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            # 1. Save to /tmp
            file_location = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_location)

            # 2. Predict
            result, confidence = predict_tumor(file_location)

            # 3. Return the display route
            # Note: We point to '/serve-image/' so we can fetch from /tmp
            return render_template('index.html', result=result, 
                                   confidence=f"{confidence*100:.2f}%", 
                                   file_path=f'/serve-image/{file.filename}')

    return render_template('index.html', result=None)

# 4. New route to serve files from /tmp
@app.route('/serve-image/<filename>')
def serve_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)