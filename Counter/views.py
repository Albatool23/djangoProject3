
from django.shortcuts import render, redirect
def index(request):
    if 'time' in request.session:
        request.session["time"] += 1
    else:
        request.session["time"] = 0

    return render(request, "index.html")

    # return HttpResponse("this is the equivalent of @app.route('/')!")

def destroy(request):
    del request.session['time']
    return redirect('/')

