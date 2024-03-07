from django.shortcuts import render

def board(req):
    return render(req, "board.html")

