from flask import Flask,render_template,request,redirect,session

app=Flask(
    __name__,
    static_folder='static',
    static_url_path='/static')

app.secret_key='asbs'

@app.route('/')
def index():
    session['isLogin'] = '!isLogin'
    return render_template('index.html')

@app.route('/signin',methods=['POST'])
def signin():
    id = request.form['id']
    pw = request.form['pw']
    if id == 'test' and pw == 'test':
        session['id'] = id
        session['pw'] = pw
        session['isLogin'] = 'isLogin'
        return redirect('/member')
    else:
        if id == '' or pw == '':
            errorMessage = '請輸入帳號、密碼'
            return redirect('/error/?message='+errorMessage)
        if id != 'test' or pw != 'test':
            errorMessage = '帳號、或密碼輸入錯誤'
            return redirect('/error/?message='+errorMessage)

@app.route('/signout')
def signout():
    session['isLogin'] = '!isLogin'
    return redirect('/')

@app.route('/member/')
def member():
    isLogin = session['isLogin']
    if isLogin != 'isLogin':
        return redirect('/')
    else:
        return render_template('member.html')

@app.route('/error/')
def error():
    errorMessage = request.args.get('message',None)
    return render_template('error.html',errorMessage=errorMessage)




    
    


    
        







# @app.route('/data')
# def handleData():
#     return 'My Data'

# @app.route('/user/<username>')
# def handleUser(username):
#     if username=="AK":
#         return 'SUP! ' + username
#     else:
#         return 'Hello ' + username

# @app.route('/hello')
# def hello():
#     name=request.args.get('name','')
#     session['username'] = name
#     return '你好 '+ name

# @app.route('/talk')
# def talk():
#     name=session['username']
#     return name + ' 很高興見到你'


app.run(port=3000)