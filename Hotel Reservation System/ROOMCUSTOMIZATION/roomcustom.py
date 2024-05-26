from flask import Flask, render_template, request

app = Flask(__name__)

#make room function
class Room:
    def __init__(self, bed_type, view, decor_theme):
        self.bed_type = bed_type
        self.view = view
        self.decor_theme = decor_theme

    def __str__(self):
        return f"Bed Type: {self.bed_type}, View: {self.view}, Decor Theme: {self.decor_theme}"

#route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

#route for submission and customization
@app.route('/customize', methods=['POST'])
def customize():
    #retrieve form data from request
    bed_type = request.form['bed_type']
    view = request.form['view']
    decor_theme = request.form['decor_theme']

    # Create room with the customization options
    room = Room(bed_type, view, decor_theme)
    return render_template('customize.html', room=room)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)   
