from django.shortcuts import render
from django.http import HttpResponse
from album.models import Gaan
from album.models import Albumname
from album.models import Bandname
from album.models import Gitikar
from album.models import Prokashok
from album.models import Shilpi
from album.models import Catagory
from itertools import chain
from operator import attrgetter

# Create your views here.

class Alphabet_list(object):
    
    def alph_list(self):
       gaa_all = [i[0] for i in Gaan.objects.values_list('title', flat=True)]
       git_all = [i[0] for i in Gitikar.objects.values_list('title', flat=True)]
       pro_all = [i[0] for i in Prokashok.objects.values_list('title', flat=True)]
       alb_all = [i[0] for i in Albumname.objects.values_list('title', flat=True)]
       ban_all = [i[0] for i in Bandname.objects.values_list('title', flat=True)]
       shi_all = [i[0] for i in Shilpi.objects.values_list('title', flat=True)]
       cat_all = [i[0] for i in Catagory.objects.values_list('title', flat=True)]
       com_list = sorted(set(list(chain(git_all, alb_all, ban_all, gaa_all, pro_all, shi_all, cat_all))))
       return com_list


def search_page(request):
    
    wa = request.get_host()
    combined_list = Alphabet_list().alph_list()

    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        gaan = Gaan.objects.filter(title__contains=q)
        gaan_alt = Gaan.objects.filter(title_alt__contains=q)
        lyric = Gaan.objects.filter(lyric__contains=q)
        lyric_alt = Gaan.objects.filter(lyric_alt__contains = q)
        ga = set(list(chain(gaan, gaan_alt, lyric)))

        alb_s = Albumname.objects.filter(title__contains=q)
        alb_s_alt = Albumname.objects.filter(title_alt__contains=q)
        album_result = set(list(chain(alb_s, alb_s_alt)))

        wa = request.get_host()
        return render (request,'search_result_page.html', {'gaan':ga, 'web_adress': wa, 'combined_list':combined_list, 'album':album_result})
    else:
        return render(request, 'search_form_page.html',{'error': True, 'combined_list':combined_list},)

def alphabet_list(request):
    wa = request.get_host()
    combined_list = Alphabet_list().alph_list()
    return render(request, 'alphabet_list.html', {'web_adress': wa, 'combined_list':combined_list})

def alphabet_list_iso(request):
    wa = request.get_host()
    combined_list = Alphabet_list().alph_list()
    return render(request, 'alphabet_list_iso.html', {'web_adress': wa, 'combined_list':combined_list})

def list_results (request, alf):
    wa = request.get_host()
    combined_list = Alphabet_list().alph_list()

    alb_alf = Albumname.objects.filter(title__startswith=alf)
    gaa_alf = Gaan.objects.filter(title__startswith=alf)
    git_alf = Gitikar.objects.filter(title__startswith=alf)
    pro_alf = Prokashok.objects.filter(title__startswith=alf)
    ban_alf = Bandname.objects.filter(title__startswith=alf)
    shi_alf = Shilpi.objects.filter(title__startswith=alf)
    cat_alf = Catagory.objects.filter(title__startswith=alf)
   
    return render(request, 'list_results.html', {'web_adress': wa, 'a_album':alb_alf, 'a_gaan':gaa_alf, 'a_gitikar':git_alf, 'a_prokashok':pro_alf, 'a_band':ban_alf, 'a_shilpi':shi_alf, 'a_catagory':cat_alf, 'combined_list':combined_list})


def gaa_go(request, username):
    wa = request.get_host()
    combined_list = Alphabet_list().alph_list()
  
    ga = Gaan.objects.filter(id=username)
    return render (request,'result.html', {'web_adress': wa, 'gaan':ga,'combined_list':combined_list})

def album_go(request, username):
    wa = request.get_host()
    combined_list = Alphabet_list().alph_list()

    alb = Albumname.objects.get(id=username)
    ga = Gaan.objects.filter(albumname=alb)
    return render (request,'result.html', {'web_adress': wa, 'gaan':ga, 'album':alb, 'combined_list':combined_list})

def git_go(request, username):
    wa = request.get_host()
    combined_list = Alphabet_list().alph_list()

    git = Gitikar.objects.get(id=username)
    ga = Gaan.objects.filter(gitikar=git)
    return render (request,'result.html', {'web_adress': wa,'gaan':ga, 'album':git, 'combined_list':combined_list})


def pro_go(request, username):
    wa = request.get_host()
    combined_list = Alphabet_list().alph_list()

    pro = Prokashok.objects.get(id=username)
    alb = Albumname.objects.filter(prokashok=pro)
    ga = Gaan.objects.filter(albumname=alb)
    return render (request,'result.html', {'web_adress': wa,'gaan':ga, 'album':pro, 'combined_list':combined_list})

def shi_go(request, username):
    wa = request.get_host()
    combined_list = Alphabet_list().alph_list()

    shi = Shilpi.objects.get(id=username)
    ga = Gaan.objects.filter(shilpi=shi)
    return render (request,'result.html', {'web_adress': wa, 'gaan':ga, 'album':shi, 'combined_list':combined_list})


def ban_go(request, username):
    wa = request.get_host()
    combined_list = Alphabet_list().alph_list()

    ban = Bandname.objects.get(id=username)
    ga = Gaan.objects.filter(bandname=ban)
    return render (request,'result.html', {'web_adress': wa, 'gaan':ga, 'album':ban, 'combined_list':combined_list})


def cat_go(request, username):
    wa = request.get_host()
    combined_list = Alphabet_list().alph_list()

    cat = Catagory.objects.get(id=username)
    ga = Gaan.objects.filter(catagory=cat)
    return render (request,'result.html', {'web_adress': wa, 'gaan':ga, 'album':cat, 'combined_list':combined_list})


def album_details(request, username):
    wa = request.get_host()
    combined_list = Alphabet_list().alph_list()

    alb = Albumname.objects.get(id=username)

    return render (request,'album_details.html', {'web_adress': wa, 'album':alb, 'combined_list':combined_list})

def publisher_album_list(request, username):
    wa = request.get_host()
    combined_list = Alphabet_list().alph_list()
    
    publisher= Prokashok.objects.get(id=username)
    album_list = publisher.albumname_set.all()
    return render (request,'album_list.html', {'web_adress': wa, 'album':album_list, 'combined_list':combined_list})

def publisher_album_list(request, username):
    wa = request.get_host()
    combined_list = Alphabet_list().alph_list()
    
    album_list= Albumname.objects.filter(release_year=username)
    return render (request,'album_list.html', {'web_adress': wa, 'album':album_list, 'combined_list':combined_list})


def artist_activity(request, username):
    wa = request.get_host()
    combined_list = Alphabet_list().alph_list()
    
    shilpi= Shilpi.objects.get(id=username)
    gitikar = shilpi.ga_git.all()
    voice = shilpi.alb_voice.all()
    lead = shilpi.alb_lg.all()
    return render (request,'artist_activity.html', {'web_adress': wa, 'gitikar':gitikar, 'combined_list':combined_list, 'shilpi':shilpi, 'voice':voice, 'lead':lead})

def band_details(request, username):
    wa = request.get_host()
    combined_list = Alphabet_list().alph_list()

    ban = Bandname.objects.get(id=username)
    ga = Gaan.objects.filter(bandname=ban)
    alb = Albumname.objects.filter(gaan__in = ga).distinct()
        
    return render (request,'band_details.html', {'web_adress': wa, 'band':ban, 'combined_list':combined_list, 'album':alb})



















