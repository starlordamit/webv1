from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    with open('index.html','r') as f:
        html=f.read()
    print('@')
    return html
if __name__ == '__main__':
    app.run('127.0.0.1',8080)

