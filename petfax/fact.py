from flask import ( Blueprint, render_template, request, redirect ) 


bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/new')
def new(): 
    return render_template('facts/new.html')

@bp.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        return redirect('/facts')
    
    # returns a redirect to /facts/ - @bp.route('/') to leave the if statement then renders facts/index.html
    # if this was a GET request it would not enter the if statement logic
    return render_template('facts/index.html')