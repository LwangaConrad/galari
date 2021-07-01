from django.shortcuts import render
from django.http import HttpResponse
from .models import Piece
from .forms import PieceForm
from django.db.models import Q
from django.views.generic import ListView

class SearchResultsView(ListView):
    model = Piece
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Piece.objects.filter(
            Q(artist__icontains=query) | Q(title__icontains=query)
        )
        return object_list

# Create your views here.
def home(request) :
    return render(request, 'home.html')
def about(request) :
    return render(request, 'about.html', {})
def galler(request, kin):
    # queryset = Piece.objects.all()
    # context = {
    #     "object_list": queryset
    # }
    pce = Piece.objects.filter(kind = kin)
    content = {
        'pr': pce
    }
    return render(request, 'artworks.html', content)
def exhib(request, person):
    rep = Piece.objects.filter(artist = person)
    content = {
        'rep': rep
    }
    return render(request, 'exhibition.html', content)
def addpiece(request):
    form = PieceForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = PieceForm()
    cont = {
        'form': form
    }
    return render(request, 'addpiece.html', cont)