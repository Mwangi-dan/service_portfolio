from flask import Blueprint, request, jsonify, flash, redirect, render_template, url_for
from app.models import User, Message
import os

portfolio = Blueprint('portfolio', __name__)


@portfolio.route('/', methods=['GET'])
def index():
    return render_template('index.html',active_page='home')


@portfolio.route('/about', methods=['GET'])
def about():
    return render_template('about.html', active_page='about')


@portfolio.route('/services', methods=["GET"])
def services():
    return render_template('services.html', active_page='services')


@portfolio.route('/portfolio', methods=["GET"])
def personal_portfolio():
    return render_template('portfolio.html', active_page='portfolio')

@portfolio.route('/contact', methods=["GET"])
def contact():
    return render_template('contact.html', active_page='contact')

