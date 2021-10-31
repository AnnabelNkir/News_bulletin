from flask import render_template,request,redirect,url_for
from . import main
from ..request import getSource,getArticle
from ..models import Sources

#views
@main.route('/')
def index():
	'''
	view root page function that returns the index the page and its data
	'''
	sources = getSource('business')
	sports_sources = getSource('sports')
	technology_sources = getSource('technology')
	entertainment_sources = getSource('entertainment')
	title = "News Highlighter"

	return render_template('index.html',title = title, sources = sources,sports_sources = sports_sources,technology_sources = technology_sources,entertainment_sources = entertainment_sources)

@main.route('/sources/<id>')
def articles(id):
	'''
	view articles page
	'''
	articles = getArticle(id)
	title = f'NH | {id}'

	return render_template('articles.html',title= title,articles = articles)