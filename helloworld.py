from flask import Flask, render_template, url_for, redirect, request
import db_app
from flask_bootstrap import Bootstrap
import datetime
import random


app = Flask(__name__)
bootstrap = Bootstrap(app)

def setting_time():
    date = datetime.datetime.now()
    m = date.month
    d = date.day
    h = date.hour
    min_ = date.minute
    sec = date.second

    if m <= 9:
        month = "0" + str(m)
    else:
        month = str(m)
    if d <= 9:
        day = "0" + str(d)
    else:
        day = str(d)
    if h <= 9:
        hour = "0" + str(h)
    else:
        hour = str(h)
    if min_ <= 9:
        minute = "0" + str(min_)
    else:
        minute = str(min_)
    if sec <= 9:
        second = "0" + str(sec)
    else:
        second = str(sec)
    todays_date = str(date.year) + "-" + month + "-" + day
    current_time = hour + ":" + minute + ":" + second
    time = [todays_date, current_time]
    return time

@app.route('/')
def index():
    user = "Peter"
    some = "i"
    thing = "u"
    todo_list = []
    added_list = []
    f1 = db_app.db_interaction_class(user,some,thing)
    shoppinglist = f1.view_document()
    for item in shoppinglist:
        if item["added_to_basket"] == True:
            added_list.append(item)
        else:
            todo_list.append(item)
    return render_template('index.html', user=user, todo_list=todo_list, added_list=added_list)


@app.route('/second/<item_name>')
def change_basket_status(item_name):
    #TO_DO add username
    user = "Peter"
    dicta ="s"
    f2 = db_app.db_interaction_class(dicta, item_name, user)
    f2.change_inbasket_status()
    return redirect(url_for('index'))

@app.route('/delete_in_basket')
def remove_inbasket():
    user = "Peter"
    some = "i"
    thing = "u"
    not_inbasket = []
    f1 = db_app.db_interaction_class(user,some,thing)
    shoppinglist = f1.view_document()
    for item in shoppinglist:
        if item["added_to_basket"] == True:
            f2 =db_app.db_interaction_class(user, item['item'], thing)
            f2.delete_document()
            print(item)
        else:
            not_inbasket.append(item)
    return redirect(url_for('index'))

@app.route('/add_item')
def adding_item():
    #TO_DO add username
    username = "Peter"
    return render_template('add_item.html', user = username)

@app.route('/send', methods=['GET','POST'])
def send():
    #TO_DO add username
    if request.method == 'POST':
        record = {
            "user_name": "Peter",
            "item": "Stadium",
            "quantity": 1,
            "date": "2018-01-01",
            "time": "10:43",
            "_id": "1212",
            "added_to_basket":False
        }
        record['item'] = request.form['item_name'].upper()
        record['quantity'] = int(request.form['quantity'])
        current_date = setting_time()
        record['date'] = current_date[0]
        record['time'] = current_date[1]
        random_num = random.randint(1,1000000000)
        record['_id'] = str(random_num)
        db_class = db_app.db_interaction_class(record, record['item'], record['item'])
        db_class.create_document()
        return redirect(url_for('adding_item'))
        

if __name__ == '__main__':
    app.run(debug=True)
