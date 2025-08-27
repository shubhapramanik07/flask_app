
# from flask import Flask, request, jsonify
# app = Flask(__name__)


# @app.get('/')
# def root():
#    return {"msg": "Welcome, Shubha!"}


# @app.get('/greet/<name>')
# def greet(name):
#     excited = request.args.get('x', 'no') == 'yes'
#     text = f"Hello {name}{'!!!' if excited else '.'}"
#     return {"greeting": text}


# @app.post('/calc/add')
# def add():
#     body = request.get_json() or {}
#     a, b = body.get('a', 0), body.get('b', 0)
#     try:
#         return {"sum": float(a) + float(b)}, 201, {"X-Server": "Flask"}
#     except Exception:
#         return {"error": "send a & b numbers"}, 400


# @app.errorhandler(404)
# def notfound(e):
#     return {"error": "No such route, amigo"}, 404

# if __name__ == "__main__":
#     app.run(debug=True)






# x = "hii my name is shubha n it's my first app using flask"
# print(x)
# print("hey i am doing debug!!")


#--------------------:lec-04:-----------------

# 1. building Url dynamically ,,, 2. variable rules and url building
### Building Url Dynamically 
####Variable Rules And URL Building

# from flask import Flask,redirect,url_for

# app=Flask(__name__)

# @app.route('/')
# def welcome():
#     return 'Welcome to my Youtube Channel'

# @app.route('/success/<int:score>')
# def success(score):
#     return "<html><body><h1 style='color:green;'>The Result is passed</h1></body></html>"


# @app.route('/fail/<int:score>')
# def fail(score):
#     return "The Person has failed and the marks is "+ str(score)

# ### Result checker
# @app.route('/results/<int:marks>')
# def results(marks):
#     result=""
#     if marks<50:
#         result='fail'
#     else:
#         result='success'
#     return redirect(url_for(result,score=marks))


# if __name__=='__main__':
#     app.run(debug=True)



#another example

# from flask import Flask, url_for

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return f'<a href="{url_for("show_user", username="Shubha")}">Go to Shubha’s page</a>'

# @app.route('/user/<username>')
# def show_user(username):
#     return f"Profile page of {username}"



###how to integrate html with flask ...
#### http verb GET and POST....


###next we have-     Jinja2 template engine
'''
{%...%} condition , for loop we can use it.
{{   }} expressions to print output
{#  Comment  # } this is  for comments
'''

#.............................................

from flask import Flask, redirect, url_for,render_template,request


app = Flask(__name__)

# @app.route('/')
# def welcome():
# 	return 'Welcome to my Youtube Channel'
#instead of the upper func we can or should use the following method which is the actual method for rendering html templates

@app.route('/')
def welcome():
    return render_template('index.html')

#that much............................

@app.route('/success/<int:score>')
# def success(score):
#     return "<html><body><h1 style='color:green;'>The Result is passed</h1></body></html>"


def success(score):

    # res = ""
    # if score >= 50:
    #     res = "PASS"
    # else:
    #     res = "FAIL"


    return render_template('result.html', result=score)




@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has failed and the marks is " + str(score)



# Result checker
@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks < 50:
        result = 'fail'
    else:
        result = 'success'
    return redirect(url_for(result, score=marks))


#this will come after the submit...

@app.route('/submit', methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method =="POST":
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['data_science'])
        total_score = (science+maths+c+data_science)/4


    # res = ""
    # if total_score >= 50:
    #     res = "success"
    # else:
    #     res = "fail"
    return redirect(url_for('success',score=total_score))




if __name__ == '__main__':
    app.run(debug=True)


