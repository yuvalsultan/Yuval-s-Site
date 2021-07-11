from flask import Blueprint, render_template, request,flash
import flask
from flask_login import login_required, current_user
import flask_login
from website.models import MovieList, MyMovies, Users,db
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq


views = Blueprint('views', __name__)



#When home url is on:
#login_required makes sure we must be logged in to access home page 



@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method=='POST':               #When add to wish list is on: searches for the movie in MovieList and adds it to the list and update in the db as a strign
        for movie in MovieList:
            if request.form['MovieName']==movie.name:
                if movie.name in MyMovies:
                    flash('Movie is already in wish list')
                else:
                    MyMovies.append(movie.name)
                    str=','.join(MyMovies)
                    curr=flask_login.current_user
                    curr.Movies=str
                    db.session.commit()

    return render_template("home.html",user=current_user, MovieList=MovieList, MyMovies=MyMovies)


#When wishlist in pressed: convert back from str in db to a list and present it 
@views.route('/wishList')
def wishList():
    ForRealWish=[]
    str=flask_login.current_user.Movies
    print(str)
    wishwish=str.split(',')
    for i in wishwish:
        for movie in MovieList:
            if i==movie.name:
                ForRealWish.append(movie)
        print(i)
    return render_template("WishList.html",user=current_user, ForRealWish=ForRealWish )
