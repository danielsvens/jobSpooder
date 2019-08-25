from flask import jsonify
from job_spooder import app
from job_spooder.models import StepStone, Monster


@app.route('/stepstone')
def stepstone():
    return jsonify([i.as_dict() for i in StepStone.query.limit(50).all()])


@app.route('/monster')
def monster():
    return jsonify([i.as_dict() for i in Monster.query.limit(50).all()])
