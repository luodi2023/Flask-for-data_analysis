from flask import render_template, request
from . import main
from data import generateDataFrameList, engine

frames = generateDataFrameList(engine)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/menu')
def menu():
    return render_template('menu_items_performance.html',
                           menu_frame=frames[1].loc[:10])


@main.route('/daily')
def daily():
    return render_template('daily_summary.html',
                           daily_frame=frames[0].loc[:10])


