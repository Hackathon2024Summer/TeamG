from flask import Flask, render_template, request, flash, redirect, session, abort
from datetime import timedelta
import uuid
import hashlib
import re

from models import dbConnect

#render_template
# アプリケーションのpythonファイルと同じ階層のtempatesフォルダ内に配置しておく
# テンプレートを表示するには、このモジュールを用い、templatesフォルダ内のhtmlファイルを指定する→$1

#request　ー＞ユーザ登録処理のところで使用
#requestオブジェクトが参照できる。POSTリクエストのパラメーターは、request.form.get(key)<-keyは、htmlで設定された名称？のはず

app = Flask(__name__) #Webアプリの作成
app.secret_key = uuid.uuid4().hex
app.permanent_session_lifetime = timedelta(days = 30)

@app.route('/signup')
def signup():
    return render_template('signup.html')

# サインアップ処理
@app.route('/signup', methods=['POST'])
def userSignup():
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    email = request.form.get('email')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if firstname == '' or lastname == '' or email == '' or password1 == '' or password2 == '':
        flash('空のフォームがあるようです')
    elif password1 != password2:
        flash('二つのパスワードの値が違っています')
    elif re.match(pattern, email) is None:
        flash('正しいメールアドレスの形式ではありません')
    else:
        uid = uuid.uuid4()
        password = hashlib.sha256(password1.encode('utf-8')).hexdigest()
        DBuser = dbConnect.getUser(email)

        if DBuser != None:
            flash('既に登録されているようです')
        else:
            dbConnect.createUser(uid, firstname, lastname, email, password)
            UserId = str(uid)
            session['uid'] = UserId
            return redirect('/')
    return redirect('/signup')

# ログインページの表示
@app.route('/login')
def login():
    return render_template('login.html')

# ログイン処理
@app.route('/login', methods=['POST'])
def userLogin():
    email = request.form.get('email')
    password = request.form.get('password')

    if email == '' or password == '':
        flash('空のフォームがあるようです')

    else:
        user = dbConnect.getUser(email)
        if user is None:
            flash('このユーザーは存在しません')
        else:
            hashPassword = hashlib.sha256(password.encode('utf-8')).hexdigest()
            if hashPassword != user["password"]:
                flash('パスワードが間違っています!')
            else:
                session['uid'] = user["id"]
                return redirect('/')
    return redirect('/login')

# ログアウト
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


##############せきど担当##################
# login後に表示される最初のホーム画面でチャネル一覧と掲示板を表示する
# userIDからUserが所属するグループのみを表示する。
@app.route('/')   #ログインしてたら:最初に入るホームディレクトリ
def index():
    uid = session.get("uid")    #sessionがあるかどうかを確認
    if uid is None:
        return redirect('/login')   #sesshonがなければログインページへ
    else:
        channels = dbConnect.getChannel()   #Userが所属しているチャネルの一覧のみを表示する
        #print(channels)
        # groups.reverse()  →ここはなくてもいいはず？
    return render_template('index.html', channels=channels, uid=uid)

@app.route('/group/delete/<cid>') 
def deleteChannel(cid):
    uid = session.get('uid')
    if uid is None:
        return redirect('/login')
    else:
        channel = dbConnect.getChannelById(cid)
        if channel['uid'] != uid:
            return redirect('/')
        else:
            dbConnect.deleteChannel(cid)
            return redirect('/')

@app.route('/group/new', methods=['GET'])
def show_add_group():
    uid = session.get('uid')
    if uid is None:
        return redirect('/login')
    return render_template('add-channel.html')

# チャンネル（グループ）を追加する処理
@app.route('/group/new', methods=['POST'])      #どこのURL、ディレクトリで指定しているか？→Frontチームに確認
def add_group():
    uid = session.get('uid')
    if uid is None:
        return redirect('/login')
    newGroupName = request.form.get('groupName')   #グループ名のnameが何かを確認
    group = dbConnect.getGroupByName(newGroupName)  #既に登録されたグループ名が存在しないか確認
    if group == None: 
        dbConnect.addGroup(newGroupName, uid)
        return redirect('/')
    else:
        error = '既に同じ名前のチャンネルが存在しています'
        return render_template('error.html', error_message=error)

@app.route('/detail/<cid>')
def detail_channel(cid):
    id = session.get('uid')
    if id is None:
        return redirect('/login')
    messages = dbConnect.getMessagesByChannel(cid)
    channel = dbConnect.getChannelById(cid)
    #print("messages=", messages)
    return render_template('chatroom.html', messages=messages, uid=id, channel=channel)

@app.route('/message/create', methods=['POST'])
def add_message():
    id = session.get('uid')
    if id is None:
        return redirect('/login')
    message = request.form.get('message')
    cid = request.form.get('cid')
    print("cid=", cid)
    if message:
        dbConnect.createMessage(id, cid, message)
    return redirect('/detail/{cid}'.format(cid=cid))

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
    #app.run(debug=True)

