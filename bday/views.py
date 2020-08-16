from django.shortcuts import render

from .models import *


# Create your views here.
def index(request):
    if request.method == "POST":
        toname = request.POST["toname"]
        fromname = request.POST["fromname"]
        w = wish.objects.create(toname=toname, fromname=fromname)
        print(w)
        ws = w.save()

        wid = wish.objects.get(id=w.id)
        # wid = wish.objects.get(wishurl=w.wishurl)
        # wishurl = wid.wishurl
        print(ws)
        if w:
            wid = wish.objects.get(id=w.id)
            # wish.objects.filter(pk=wid.pk).update(wishurl="http://127.0.0.1:8000/%s" % (wid.slug))
            print("object", wid)
            print("Slug   ", wid.slug)
            print("To name", wid.toname)
            print("From name", wid.fromname)
            print("Wish Url", wid.wishurl)
            return render(request, 'index.html', {"data": wid})
    else:
        wid = wish.objects.get(id=1)
        return render(request, 'index.html', {"data": wid})


def index_id(request, id):
    if not id:
        wid = wish.objects.get(id=1)
        return render(request, 'index.html', {"data": wid})
    else:
        wid = wish.objects.get(id=id)
        return render(request, 'index.html', {"data": wid})

#
#     if request.method == "POST":
#         toname = request.POST["toname"]
#         fromname = request.POST["fromname"]
#         w = wish.objects.create(toname=toname, fromname=fromname)
#         print(w)
#         ws = w.save()
#         wid = wish.objects.get(id=w.id)
#         wishurl = wid.wishurl
#
#         print(ws)
#         if w:
#             wid = wish.objects.get(id=w.id)
#             # wish.objects.filter(pk=wid.pk).update(wishurl="http://127.0.0.1:8000/%s" % (wid.slug))
#
#             print("object", wid)
#             print("Slug   ", wid.slug)
#             print("To name", wid.toname)
#             print("From name", wid.fromname)
#             print("Wish Url", wid.wishurl)
#
#         return render(request, 'index.html', {'to': toname, 'from': fromname, 'urlshare': wishurl})
#     else:
#         wid = wish.objects.get(id=id)
#         toname = wid.toname
#         fromname = wid.fromname
#         wishurl = wid.wishurl
#
#         return render(request, 'index.html', {'to': toname, 'from': fromname, 'urlshare': wishurl})
#
#     # return render(request, 'index.html', {'to': "toname", 'from': "fromname"})
#
#
# def index_slug(request, slug):
#     if request.method == "POST":
#         toname = request.POST["toname"]
#         fromname = request.POST["fromname"]
#         w = wish.objects.create(toname=toname, fromname=fromname)
#         print(w)
#         ws = w.save()
#         wid = wish.objects.get(id=w.id)
#         wishurl = wid.wishurl
#         print(ws)
#         if w:
#             wid = wish.objects.get(id=w.id)
#             # wish.objects.filter(pk=wid.pk).update(wishurl="http://127.0.0.1:8000/%s" % (wid.slug))
#
#             print("object", wid)
#             print("Slug   ", wid.slug)
#             print("To name", wid.toname)
#             print("From name", wid.fromname)
#             print("Wish Url", wid.wishurl)
#
#         return render(request, 'index.html', {'to': toname, 'from': fromname, 'urlshare': wishurl})
#     else:
#         wid = wish.objects.get(slug=slug)
#         toname = wid.toname
#         fromname = wid.fromname
#         wishurl = wid.wishurl
#         return render(request, 'index.html', {'to': toname, 'from': fromname, 'urlshare': wishurl})
