from django.shortcuts import render


# Create your views here.
def index(request):
    if request.method == "POST":
        toname = request.POST["toname"]
        fromname = request.POST["fromname"]
        print(toname, fromname)
        return render(request, 'index.html', {'to': toname, 'from': fromname})

    return render(request, 'index.html', {'to': "Shyam", 'from': "Naynesh Rathod"})
