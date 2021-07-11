from . import db
from flask_login import UserMixin
import requests
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq




class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    Movies=db.Column(db.String())
    


class Movie:
    name=''
    img=''
    summ=''
    genre=''
    link=''
    rate=''

    def __init__(self,name,img,summ,genre,link,rate):
        self.name=name
        self.img=img
        self.summ=summ
        self.genre=genre
        self.link=link
        self.rate=rate

r=requests.get('https://itunes.apple.com/us/rss/topmovies/limit=25/json')
info=r.json()
Movies=info['feed']['entry']
MovieList=[]
MyMovies=[]

#reads from the json file and making a list of movies
for s in Movies:
    name=s['im:name']['label']
    img=s['im:image'][2]['label']
    summ=s['summary']['label']
    genre=s['category']['attributes']['term']
    link=s['link'][0]['attributes']['href']
    new_movie=Movie( name=name,img=img, summ=summ,genre=genre,link=link,rate='')
    MovieList.append(new_movie)

for movie in MovieList:
     my_Url=movie.link
     url_read=ureq(my_Url) #downloads the page
     page_html=url_read.read()
     url_read.close()
     page_soup= soup(page_html, "html.parser") 
     movie.rate=page_soup.figure['aria-label']


