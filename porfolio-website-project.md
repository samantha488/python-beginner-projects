##this project contains html(frontend),css(for style) and little bit of python(backend using flash)
##VS code is necessary for this project

##python

```python
from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
if __name__== "__main__":
    app.run(debug=True)

## 2.HTML

```html
<!DOCTYPE html>
<html>
<head>
<title>My Porfolio</title>
 <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Hello!Im a Curious Mind Exploring Computer language</h1>
    <p>I curently know bout some cpp,html and python</p>
    <nav>
        
        <a href="/">home</a>
        <a href="#about">about</a>
        <a href="#projects">projects</a>
        <a href="#my skills">my skills</a>
        <a href="#contact me">contact me</a>

        <section id="about">
            <h2>about me</h2>
            <p>im goofy and funny ,and im an human:></p>
        </section>

        <section id="projects">
            <h2>My projects</h2>

            <div class="project-card">
                <h3>My First Project</h3>
                <p>a small project i do when im learning</p>
            </div>
            <div class="project-card">
                <h3>A Number Guessing Game</h3>
                <p>a game created using python</p>
            </div>
            
        </section>

        <section id="my skills">
            <h2>My Skills</h2>
            <p>python</p>```css
            <p>C++</p>
            <p>html</p>
        </section>

    </nav>

    <section id="contact me">
        <h2>Contact me</h2>
        <p>feel free to contact me anytime</p>
    </section>

</body>
</html>

## 2. CSS

```css
body{
    background-color: #121212;
    color:white;
    font-family:  Arial, sans-serif;
    
    h1{
        color:#ff8c42;
        font: size 40px;
        text-align:center;
    }
    margin:0;
    padding: 30px;

    nav{
        text-align: center;
        margin-top: 30px;
    }
    nav a{
        color:rgb(154, 88, 31);
        text-decoration:underline;
        margin-top: 15px;
        font-size: 18px;
    }
    section{
        padding: 20px;
        margin-top:60px;
        border-bottom:1px solid #333333;
        background-color: #1e1e1e;
        border-color: #333333;
        border-radius:12px;
        margin-top: 35px;
        max-width: 900px;
        margin: 40px auto;
    }
    h2{
       color:#ff8c42;
       padding:26px; 
    }
    p{
        font-size:18px;
        line-height: 1.8;
        color:gray;
    }
    nav a:hover{
        color:white;
    }
    .project-card{
        background-color: #252525;
        padding:20px;
        border-radius: 10px;
        margin-top: 20px;
    }
    .project-card:hover{
        background-color: #333333;
        transition: 0.3s;
    }
}
