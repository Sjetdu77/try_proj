from flask import Flask, request, render_template, jsonify, redirect, url_for, jsonify
import json

app = Flask(__name__)
infos = json.load(open('data/infos.json'))

@app.route('/')
def index():
	return render_template("index.html", infos=infos)

@app.route('/stats/')
def statsGen():
	return render_template("allStats.html", infos=infos)

@app.route('/stats/<character>')
def statsChar(character):
	return render_template("stat.html", name=character, infos=infos[character])

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=5100)