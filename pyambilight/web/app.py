#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def root():
	return render_template('index.html', deviceConnected=False, stream=False)


@app.route('/connect', methods=['POST'])
def connect():
	data = request.form


@app.route('/set-color', methods=['POST'])
def set_color():
	data = request.form


@app.route('/set-brightness', methods=['POST'])
def set_brightness():
	data = request.form


@app.route('/set-color-mode', methods=['POST'])
def set_color_mode():
	data = request.form


def launch_app():
	app.run()
