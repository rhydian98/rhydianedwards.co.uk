from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')
@app.route('/post_id')
def post():
    postName
    return render_template('post.html', postName=postName)

@app.route('make_post')



@app.route('/create_post')
def create_post():
    return render_template('makePost.html')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
    
if __name__ == '__main__':
    app.run(debug=True)