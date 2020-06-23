import os
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env 


app = Flask(__name__)

"""MongoDB - setting env variables"""
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = 'online_cookbook'


mongo = PyMongo(app)


@app.route('/')
@app.route('/index_recipe')
def index_recipe():
    return render_template('index.html')


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
