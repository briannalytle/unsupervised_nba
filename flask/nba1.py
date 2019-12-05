from flask import Flask, render_template, request, Response
import numpy as np
import pickle
import pandas as pd
import os

app = Flask(__name__)
app.debug = True


# define the route
@app.route('/')
# create the controller
def home():
   # return the view
   return render_template('index.html', result_Css = '', result_message = 'which is best?')


@app.route('/Offense')
# create the controller
def off_player_submit():
    #load in user import data
    raw_data = request.args
    user_input = raw_data['player_name']
    off_players = pickle.load(open(os.getcwd() + '/offensive.p', 'rb'))
    players = off_players[user_input].sort_values()[1:4].index

    salary = pickle.load(open(os.getcwd() + '/salaries.p', 'rb'))

    user_player_sal = salary.loc[user_input].to_string(index = False)

    related_salaries = []
    for i in players:
        printing = salary.loc[i].to_string(index =False)
        related_salaries.append({'player_name': i, 'salary' : printing})

    return render_template('player_return.html',  players=related_salaries, user_input = user_input, user_player_sal = user_player_sal)


@app.route('/defense')
# create the controller
def def_player_submit():
    #load in user import data
    raw_data = request.args
    user_input = raw_data['player_name']
    def_players = pickle.load(open(os.getcwd() + '/defensive.p', 'rb'))
    players = def_players[user_input].sort_values()[1:4].index

    salary = pickle.load(open(os.getcwd() + '/salaries.p', 'rb'))

    user_player_sal = salary.loc[user_input].to_string(index = False)

    related_salaries = []
    for i in players:
        printing = salary.loc[i].to_string(index =False)
        related_salaries.append({'player_name': i, 'salary' : printing})

    return render_template('player_return.html',  players=related_salaries, user_input = user_input, user_player_sal = user_player_sal)

@app.route('/shooting')
# create the controller
def shoot_player_submit():
    #load in user import data
    raw_data = request.args
    user_input = raw_data['player_name']
    def_players = pickle.load(open(os.getcwd() + '/shoot.p', 'rb'))
    players = def_players[user_input].sort_values()[1:4].index

    salary = pickle.load(open(os.getcwd() + '/salaries.p', 'rb'))

    user_player_sal = salary.loc[user_input].to_string(index = False)

    related_salaries = []
    for i in players:
        printing = salary.loc[i].to_string(index =False)
        related_salaries.append({'player_name': i, 'salary' : printing})

    return render_template('player_return.html',  players=related_salaries, user_input = user_input, user_player_sal = user_player_sal)

@app.route('/overall')
# create the controller
def overall_player_submit():
    raw_data = request.args
    user_input = raw_data['player_name']
    over_players = pickle.load(open(os.getcwd() + '/overall.p', 'rb'))
    players = over_players[user_input].sort_values()[1:4].index

    salary = pickle.load(open(os.getcwd() + '/salaries.p', 'rb'))

    user_player_sal = salary.loc[user_input].to_string(index = False)

    related_salaries = []
    for i in players:
        printing = salary.loc[i].to_string(index =False)
        related_salaries.append({'player_name': i, 'salary' : printing})

    return render_template('player_return.html',  players=related_salaries, user_input = user_input, user_player_sal = user_player_sal)


if __name__ == '__main__':
   app.run()
