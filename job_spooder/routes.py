from flask import jsonify
from job_spooder import app
from job_spooder.models import JobArticle


@app.route('/stepstone')
def stepstone():
    return jsonify([i.as_dict() for i in JobArticle.query.filter_by(site='StepStone').limit(50).all()])


@app.route('/monster')
def monster():
    return jsonify([i.as_dict() for i in JobArticle.query.filter_by(site='Monster').limit(50).all()])
