from flask import Flask, render_template, request

app = Flask(__name__)

#make room function
class Room:
    def __init__(self, bed_type, view, decor_theme):
        self.bed_type = bed_type
        self.view = view
        self.decor_theme = decor_theme

    
