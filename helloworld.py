from flask import Flask, render_template
import db_app
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)

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



if __name__ == '__main__':
    app.run(debug=True)