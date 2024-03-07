from django.shortcuts import render

def index(req):
    return render(req, "home.html")

def news(req):
    return render(req, "news.html")
