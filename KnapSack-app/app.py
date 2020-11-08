from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///knapsack.db'
db = SQLAlchemy(app)

class Items(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200))
    weight = db.Column(db.Float, nullable = False)
    value = db.Column(db.Float, nullable = False)

    def __repr__(self):
        return '<Item %r' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        item_name, item_weight, item_value = request.form['name'], request.form['weight'], request.form['value']
        new_item = Items(name = item_name, weight = item_weight, value = item_value)

        try:
            db.session.add(new_item)
            db.session.commit()
            return redirect('/')
        except:
            return "there was a problem adding your item"

    else:
        items = Items.query.all()
        return render_template('index.html', items = items)

@app.route('/delete/<int:id>')
def delete(id):
    item_to_delete = Items.query.get_or_404(id)

    try:
        db.session.delete(item_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "there was a problem deleting your item"


if __name__ == "__main__":
    app.run(debug=True)