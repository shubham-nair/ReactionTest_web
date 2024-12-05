from flask import Flask, render_template, request, redirect, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId  # Import ObjectId
import time

app = Flask(__name__)
app.secret_key = 'session1'

# MongoDB configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/reaction_game"
mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve user data from the form
        name = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        level = request.form.get('level')
        game_time = int(request.form.get('game_time'))  # Game time setting

        # Store data in session
        session['name'] = name
        session['age'] = age
        session['gender'] = gender
        session['level'] = level
        session['game_time'] = game_time  # Store game time in session

        # Save user data to MongoDB
        user_data = {
            'name': name,
            'age': age,
            'gender': gender,
            'level': level,
            'game_time': game_time,
            'timestamp': time.time()
        }
        # Convert ObjectId to string before storing in session
        session['user_id'] = str(mongo.db.users.insert_one(user_data).inserted_id)

        return redirect(url_for('game'))
    return render_template('index.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    level = session.get('level')
    game_time = session.get('game_time')
    if not level:
        return redirect(url_for('index'))
    return render_template('game.html', level=level, game_time=game_time)

@app.route('/result', methods=['POST'])
def result():
    # Retrieve reaction times and correctness from the form
    data = request.get_json()
    reaction_times = data.get('reaction_times', [])
    correct_responses = data.get('correct_responses', 0)
    total_responses = data.get('total_responses', 0)

    # Calculate average reaction time and accuracy
    if reaction_times:
        average_reaction_time = sum(reaction_times) / len(reaction_times)
        average_reaction_time = round(average_reaction_time, 2)
    else:
        average_reaction_time = 0

    accuracy = (correct_responses / total_responses) * 100 if total_responses > 0 else 0
    accuracy = round(accuracy, 2)

    # Update user data in MongoDB with results
    mongo.db.users.update_one(
        {'_id': ObjectId(session['user_id'])},  # Convert back to ObjectId
        {'$set': {
            'reaction_times': reaction_times,
            'average_reaction_time': average_reaction_time,
            'correct_responses': correct_responses,
            'total_responses': total_responses,
            'accuracy': accuracy
            }
        }
    )

    return render_template('result.html', average_reaction_time=average_reaction_time, accuracy=accuracy)

if __name__ == '__main__':
    app.run(debug=True)
