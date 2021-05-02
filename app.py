import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


# HOME / INDEX


@app.route("/")
def get_index():
    top9recipes = mongo.db.recipes.find().sort("views", -1).limit(9)
    return render_template("index.html", recipes=top9recipes)


# ALL RECIPES


@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("/recipes/recipes.html", recipes=recipes)

# SEARCH RECIPES


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    if len(recipes) == 0:
        flash(f"We're sorry but no recipes with {query} were found!")
    else:
        flash(f"Your search for {query} returned {len(recipes)} result(s)!")
    return render_template("/recipes/recipes.html", recipes=recipes)    

# FILTER RECIPES (CATEGORY & SPICE)


@app.route("/category_filter/<id>")
def category_filter(id):
    recipes = list(mongo.db.recipes.find({"category_name": id}))
    return render_template("/recipes/recipes.html", recipes=recipes)


@app.route("/spice_filter/<id>")
def spice_filter(id):
    recipes = list(mongo.db.recipes.find({"spiciness": id}))
    return render_template("recipes/recipes.html", recipes=recipes)


# SINGLE RECIPE


@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    recipe_db = mongo.db.recipes.find_one_or_404({'_id': ObjectId(recipe_id)})
    mongo.db.recipes.update(
        {'_id': ObjectId(recipe_id)}, {'$inc': {'views': int(1)}})
    return render_template("recipes/recipe.html", recipe=recipe_db)


# REGISTER


@ app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("/user/register.html")

# LOGIN


@ app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(
                    url_for("profile", username=session["user"])
                    )

            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password ")
            return redirect(url_for("login"))

    return render_template("/user/login.html")


# PROFILE PAGE


@ app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    user = session.get("user").lower()
    user_recipes = list(
        mongo.db.recipes.find({"added_by": session["user"]}))
    if user is not None:
        return render_template(
            "user/profile.html", username=username, recipes=user_recipes)
    else:
        return render_template("/user/login.html")


# LOGOUT


@ app.route("/logout")
def logout():
    flash("You have been logged out")
    session.clear()
    return redirect(url_for("login"))


# ADD RECIPE


@ app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if not session.get("user"):
        render_template("templates/error_handlers/404.html")

    if request.method == "POST":
        is_vegetarian = "on" if request.form.get("is_vegetarian") else "off"
        is_vegan = "on" if request.form.get("is_vegan") else "off"
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "spiciness": request.form.get("spiciness"),
            "category_name": request.form.get("category_name"),
            "img_url": request.form.get("img_url"),
            "recipe_serves": request.form.get("recipe_serves"),
            "prep_time": request.form.get("prep_time"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_method": request.form.get("recipe_method"),
            "recipe_inventor": request.form.get("recipe_inventor"),
            "is_vegetarian": is_vegetarian,
            "is_vegan": is_vegan,
            "added_by": session["user"]
        }

        mongo.db.recipes.insert_one(recipe)
        flash("Recipe successfully added")
        return redirect(url_for("profile", username=session['user']))

    spicelevel = mongo.db.spicelevel.find()
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "recipes/add_recipe.html", spicelevel=spicelevel, categories=categories
        )


# EDIT RECIPE


@ app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):

    if not session.get("user"):
        return render_template("error_handlers/404.html")

    if request.method == "POST":
        is_vegetarian = "on" if request.form.get("is_vegetarian") else "off"
        is_vegan = "on" if request.form.get("is_vegan") else "off"
        submit = {
            "recipe_name": request.form.get("recipe_name"),
            "spiciness": request.form.get("spiciness"),
            "category_name": request.form.get("category_name"),
            "img_url": request.form.get("img_url"),
            "recipe_serves": request.form.get("recipe_serves"),
            "prep_time": request.form.get("prep_time"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_method": request.form.get("recipe_method"),
            "recipe_inventor": request.form.get("recipe_inventor"),
            "is_vegetarian": is_vegetarian,
            "is_vegan": is_vegan,
            "added_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe successfully edited")
        return redirect(url_for("profile", username=session['user']))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    spicelevel = mongo.db.spicelevel.find()
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "/recipes/edit_recipe.html", recipe=recipe, spicelevel=spicelevel,
        categories=categories)


# DELETE RECIPE

@ app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe successfully deleted")
    return redirect(url_for("profile", username=session['user']))


# SUBSCRIBE TO NEWSLETTER


@app.route("/subscribe", methods=["GET", "POST"])
def subscribe():
    if request.method == "POST":
        existing_email = mongo.db.subscribers.find_one(
            {"email_address": request.form.get("email_address")})

        if existing_email:
            flash("You have already signed up to the newsletter")
            return redirect(url_for('get_index'))
        subscribe = {
            "email_address": request.form.get("email_address")
        }
        mongo.db.subscribers.insert_one(subscribe)

    flash("You have succesfully subscribed")
    return redirect(url_for("get_index"))


# ERROR HANDLERS

@app.errorhandler(403)
def forbidden(e):
    return render_template("/error_handlers/403.html"), 403


@app.errorhandler(404)
def not_found(e):
    return render_template("/error_handlers/404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("/error_handlers/500.html"), 500


# THE APP ITSELF


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
