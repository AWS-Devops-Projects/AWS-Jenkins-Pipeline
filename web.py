# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


myapp = Flask(__name__)


@myapp.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


@myapp.route("/")
def hello():
    #    return name
    return render_template(
        'test.html', **locals())


if __name__ == "__main__":
    myapp.run(host='0.0.0.0', port=80)
