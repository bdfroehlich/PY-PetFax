from flask import ( Blueprint, render_template, request, redirect ) 
from . import models


bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/new')
def new(): 
    return render_template('facts/new.html')

@bp.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        submitter = request.form['submitter']
        fact = request.form['fact']

        #create new instance of fact model using submitter and fact as arguments
        new_fact = models.Fact(submitter=submitter,fact=fact)
        #add new_fact to database session
        models.db.session.add(new_fact)
        #commit the database session
        models.db.session.commit()
        return redirect('/facts')

    results = models.Fact.query.all()
    # for result in results:
    #     print(result)
    
    # returns a redirect to /facts/ - @bp.route('/') to leave the if statement then renders facts/index.html
    # if this was a GET request it would not enter the if statement logic
    return render_template('facts/index.html', facts=results)