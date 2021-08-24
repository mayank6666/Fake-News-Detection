from flask import Flask, abort, jsonify, request, render_template
import joblib
from feature import *
import json

Model = joblib.load('model.pkl')


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/api',methods=['POST'])
def get_delay():
    
    result=request.form
    query_title = result['title']
    query_text = result['maintext']
    print(query_text)
    query = get_all_query(query_title, query_text)
    user_input = {'query':query}
    pred = Model.predict(query)
    print(pred)
    dic = {1:'real',0:'fake'}
    return f'<html><body><h1>{dic[pred[0]]}</h1> <form action="/"> <button type="submit">back </button> </form></body></html>'


if __name__ == "__main__":
    # app.run(host = '0.0.0.0',port = '8080')
    app.run(debug = True)

