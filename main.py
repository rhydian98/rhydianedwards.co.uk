from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQL_ALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/E/Programming/PythonProjects/Flask Tutorial/rhydianedwards.co.uk/app.db'
db = SQLAlchemy(app)
class post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    datePosted = db.Column(db.DateTime)
    content = db.Column(db.Text) 

@app.route('/')
def index():
    return render_template('home.html')
@app.route('/post_id')
def post(): 
    return render_template('post.html')

@app.route('/makePost', methods=['POST'])
def make_post():
    return render_template('makePost.html')

@app.route('/create_post',methods= ['POST'])
def create_post():
    title = request.form['postTitle']
    tags = request.form['tags']
    content = request.form['postContent']
    return '<h1>Title: {} tags: {} Content: {}'.format(title, tags, content)
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
    
if __name__ == '__main__':
    app.run(debug=True)