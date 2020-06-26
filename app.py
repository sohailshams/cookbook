import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt

if os.path.exists("env.py"):
    import env 


app = Flask(__name__)

"""MongoDB - setting env variables"""
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = 'online_cookbook'
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route('/')
@app.route('/index_recipe')
def index_recipe():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'username': request.form['username']})
        if login_user:
            if bcrypt.hashpw(request.form['pasword'].encode('utf-8'),
                             login_user['password']) == login_user['password']:
                session['username'] = request.form['username']
                return redirect(url_for('index_recipe'))
        flash("Invalid username / password. Please try again.")
    return render_template('login.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username': request.form.get('username')})
        if existing_user is None:
            hash_password = bcrypt.hashpw(
                request.form['pasword'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one({'username': request.form['username'],
                             'password': hash_password})
            session['username'] = request.form['username']

            flash('Welcome to Recipebook')
            return redirect(url_for('index_recipe'))

        flash('Username already exists')
    return render_template('register.html')


@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
   # flash('You have been logged out')
    return redirect(url_for('index_recipe'))


@app.route('/search_recipe', methods=['POST'])
def search_recipe():
    search_recipes = request.form.get("search_recipes")
    #  create the index
    mongo.db.recipe.create_index([("$**", 'text')])
    # search with the search word that came through the form
    cursor = mongo.db.recipe.find({"$text": {"$search": search_recipes}})
    print('cursor')
    recipe = [recipe for recipe in cursor]
    if recipe == []:
        # send recipes to page
        return render_template('recipes.html', recipe=recipe, query=search_recipes, search=True)
    else:
        # send recipes to page
        return render_template('recipes.html', recipe=recipe, query=search_recipes, search=True)


@app.route('/get_recipes')
def get_recipes():
    return render_template('recipes.html', recipe=mongo.db.recipe.find())


@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
                           cuisines=mongo.db.cuisines.find(),
                           cooktime=mongo.db.cooktime.find(),
                           recipetype=mongo.db.recipetype.find(),
                           serving=mongo.db.serving.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe = mongo.db.recipe
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))


@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    the_recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    return render_template('viewrecipe.html', recipe=the_recipe)


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    all_cuisines = mongo.db.cuisines.find()
    all_cooktime = mongo.db.cooktime.find()
    all_recipetype = mongo.db.recipetype.find()
    all_serving = mongo.db.serving.find()
    return render_template('editrecipe.html', recipe=the_recipe,
                           cuisines=all_cuisines,
                           cooktime=all_cooktime,
                           recipetype=all_recipetype,
                           serving=all_serving)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe = mongo.db.recipe
    recipe.update({'_id': ObjectId(recipe_id)},
    {
        'recipe_name': request.form.get('recipe_name'),
        'recipe_cuisine': request.form.get('recipe_cuisine'),
        'recipe_ingredients': request.form.get('recipe_ingredients'),
        'recipe_description': request.form.get('recipe_description'),
        'recipe_preparation': request.form.get('recipe_preparation'),
        'recipe_date': request.form.get('recipe_date'),
        'cooking_time': request.form.get('cooking_time'),
        'recipe_type': request.form.get('recipe_type'),
        'recipe_serving': request.form.get('recipe_serving')
    })
    return redirect(url_for('get_recipes'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipe.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
