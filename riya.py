from flask import Flask, request,render_template
app=Flask(__name__)
@app.route('/')
def hello():
    return render_template("login.html")
database={'shri':'shri@123','shre':'shre@123','Priya':'Priya@123'}
@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['Username']
    pwd=request.form['Password']
    if name1 not in database:
        return render_template('login.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
            return render_template('home.html')
if __name__=='__main__':
    app.run(debug=True)