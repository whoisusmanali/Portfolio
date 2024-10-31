from flask import Flask, render_template, request
from urllib.parse import quote as url_quot
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blog')
def blog():
    blog_posts = [
        {'title': 'Building Machine Learning Models', 'url': 'https://medium.com/@usman_blog_1'},
        {'title': 'Deploying Flask Apps on AWS', 'url': 'https://medium.com/@usman_blog_2'}
    ]
    return render_template('blog.html', blog_posts=blog_posts)




@app.route('/projects')
def projects():
    return render_template('projects.html')

if __name__ == '__main__':
    app.run(debug=True)
