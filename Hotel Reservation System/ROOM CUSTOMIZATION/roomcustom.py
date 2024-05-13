from flask import Flask, render_template, request

app = Flask(__name__)

class Room:
    def __init__(self, bed_type, view, decor_theme):
        self.bed_type = bed_type
        self.view = view
        self.decor_theme = decor_theme

    def __str__(self):
        return f"Bed Type: {self.bed_type}, View: {self.view}, Decor Theme: {self.decor_theme}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customize', methods=['POST'])
def customize():
    bed_type = request.form['bed_type']
    view = request.form['view']
    decor_theme = request.form['decor_theme']

    room = Room(bed_type, view, decor_theme)
    return render_template('customize.html', room=room)

if __name__ == '__main__':
    app.run(debug=True)
