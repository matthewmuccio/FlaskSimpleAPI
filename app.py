#!/usr/bin/env python3


from flask import Flask, jsonify, render_template
import requests


api = Flask(__name__)

@api.route("/phones/iphone-<version_number>", methods=["GET"])
def get_iphone(version_number):
	if version_number == "8":
		pass
	return render_template("iphone-{}.html".format(version_number))


if __name__ == "__main__":
	api.run(debug=True)
