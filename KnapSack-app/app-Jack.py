# Rename this file to app.py if you want to see my solution working
# I used top-down DP while Vicky used bottom-up

from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///knapsack.db'
db = SQLAlchemy(app)
itemsArr = []
dp = []
ans = []

class Items(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200))
    weight = db.Column(db.Integer, nullable = False)
    value = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return '<Item %r' % self.id

# write knapsack function here
# item attributes: name, weight, value (you may want to cast values of weight and value to int)
# return list of items
def knapsack(currItem, currWeight):
    global itemsArr, dp

    #print("Checking " + str(currItem) + " " + str(currWeight))
    if(currItem == len(itemsArr)):
        return 0
    
    if(dp[currItem][currWeight] != -1):
        return dp[currItem][currWeight]
    
    if(currWeight - itemsArr[currItem]['weight'] < 0):
        dp[currItem][currWeight] = knapsack(currItem + 1, currWeight)
    else:
        dp[currItem][currWeight] = max(
            knapsack(currItem + 1, currWeight - itemsArr[currItem]['weight']) + itemsArr[currItem]['value'],
            knapsack(currItem + 1, currWeight))
    
    return dp[currItem][currWeight]

def trace(currItem, currWeight):
    global itemsArr, dp

    if(currItem == len(itemsArr)):
        return 0

    if(dp[currItem][currWeight] == knapsack(currItem + 1, currWeight)):     # skipped currItem
        trace(currItem + 1, currWeight)
    else:
        ans.append(itemsArr[currItem])
        trace(currItem + 1, currWeight - itemsArr[currItem]['weight'])

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        item_name, item_weight, item_value= request.form['name'], request.form['weight'], request.form['value']
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

@app.route('/output', methods=['POST', 'GET'])
def getouput():
    if request.method == 'POST':
        global itemsArr, dp, ans
        maxWeight = request.form['maxWeight']
        items = Items.query.all()

        dp = [ [-1 for i in range(int(maxWeight) + 1)] for j in range(len(items))] 
        itemsArr = [i.__dict__ for i in items]
        ans.clear()

        knapsack(0, int(maxWeight))
        trace(0, int(maxWeight))

        #for i in range(len(itemsArr)):
            #print(str(itemsArr[i]['value']) + " " + str(itemsArr[i]['weight']) + '\n')

        for i in range(len(items)):
            for j in range(int(maxWeight) + 1):
                print(str(dp[i][j]), end=" ")
            print("")
                #print(str(ans[i]['value']) + " " + str(ans[i]['weight']) + '\n')

        return render_template('output.html', items = ans, maxWeight = maxWeight)

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