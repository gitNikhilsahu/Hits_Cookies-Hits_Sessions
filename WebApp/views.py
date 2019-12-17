from django.shortcuts import render

def Home(request):
    return render(request, 'Home.html')

def Hits_View_Cookie(request):
    hit = request.COOKIES.get('hit', 0)
    newhit = int(hit)+1
    response = render(request, 'HitCookie.html', {'hit':newhit})
    response.set_cookie('hit', newhit)
    return response

def Hits_View_Session(request):
    hit1 = request.session.get('hit1', 0)
    newhit1 = int(hit1)+1
    request.session['hit1'] = newhit1
    return render(request, 'HitSession.html', {'hit1':newhit1})
