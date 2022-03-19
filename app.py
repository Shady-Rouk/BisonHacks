from flask import Flask, render_template, request, redirect, url_for
from model import *
import json

app = Flask('app')

@app.route('/')
@app.route('/sign-in', methods=['GET', 'POST'])
def sign_in(): 
  return render_template('sign-in.html')


@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
  return render_template('sign-up.html')

events = open('opportunity_data.txt', 'r')
events_dict = json.loads(events.read())
events.close()


@app.route('/create-to-main', methods=['GET', 'POST'])
def create_to_main():
  create_user(request.form["email"], request.form["password"], str(request.form["dob"]))
  return redirect(url_for('sign_in'), 200)


@app.route('/main', methods=['GET', 'POST'])
def main():
  user_data = {"email": request.form["email"], "password": request.form["password"]}
  if authenticate(user_data["email"], user_data["password"]):
    user_hours = get_service_hours(user_data["email"])
    return render_template('main.html', ev_dict=events_dict, user=user_data, user_email=user_data["email"], user_hours=user_hours)
  print('Failed')
  return "<h1>Invalid Login Details</h1>"


@app.route('/opportunity', methods=['GET', 'POST'])
def opportunity():
  user_data = get_user(request.form['email'])
  opp_data = events_dict[request.form['decision']]
  return render_template('opportunity-page.html', oppId=request.form['decision'], opp=opp_data, user_email=user_data["email"])


@app.route('/update', methods=['GET', 'POST'])
def update():
  user = get_user(request.form['email'])
  opp = events_dict[request.form['oppId']]
  update_service_hours(user["email"], opp['length'])
  return redirect(url_for('sign_in'), 200)

app.run(host='0.0.0.0', port=8080)
