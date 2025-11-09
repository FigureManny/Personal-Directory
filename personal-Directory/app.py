from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    projects = [
    {
        'title': 
        'green-glass-door',
        'repo_link': 'https://github.com/FigureManny/green-glass-door-',
        'description': 'This green glass door game was made using python, html and css and prioritized having a series of words enter the green glass door depending on a rule amongst all words.',
        'image': 'img/greenglassdoor.png', 
    },
    {
        'title': 'Object-Detection',
        'repo_link': 'https://github.com/FigureManny/Object-detection',
        'description': 'This project is a object detection website where any image is imported, processed and exported with a confidence rate that the computer conducts and the user can search for the processed image in the database',
        'image': 'img/objectdetection.png', 
    },
    {
        'title': 'Flask-TODO',
        'repo_link': 'https://github.com/FigureManny/flask-todo',
        'description': "This Flask-TODO site uses python and flask aspects to help the user, create, eliminate and add more to a TODO list to their preference.",
        'image': 'img/todo.png', 
    },
    {
        'title': 'Madlib-FLask',
        'repo_link': 'https://github.com/FigureManny/flask-todo',
        'description': "This Madlib FLask site uses python and flask aspects to help the user create a sentence using random Verbs, Nouns, Adjectives, Adbverbs, etc:",
        'image': 'img/MadLib.png', 
    },
    {
        'title': 'Sentiment-Analysis',
        'repo_link': 'https://github.com/FigureManny/Sentiment-Analysis',
        'description': "This Sentiment Analysis app is operated in the terminal and analyzes a sentence to discover its behavior throughout a series of words relating if the sentence is positive, neutral or negative.",
        'image': 'img/Sentiment.png',
    },
    {
        'title': 'Link to all projects ',
        'repo_link': 'https://github.com/FigureManny?tab=repositories',
        'description': "Here are all of my uploaded repositories/projects from GitHub",
        'image': 'img/github.png',
    }
]
    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)

