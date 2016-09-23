from flask import render_template, redirect, g, url_for, jsonify, request
from sqlalchemy import Table
from alumni import app, db
from alumni.models import Alum
from alumni.database import session, create_session, metadata
from config import MAX_SEARCH_RESULTS

@app.route('/')
@app.route('/index')
def index():
    return render_template('alumni.html')

@app.route('/_search', methods=['GET'])
def search():
	zip = request.args.get('zip', 0, type=str)
	results = Alum.query.filter(Alum.zipcode == zip).all()
	return jsonify(result=[a.serialize() for a in results])
