from django import forms
from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from album.models import Gitikar, Shilpi, Prokashok, Bandname, Albumname, Gaan, Catagory, Chobi

# কাস্টোমাইজেশন

class GaanForm(forms.ModelForm):
    lyric = forms.CharField(label = u'গান', widget=forms.Textarea(attrs={'rows': 20, 'cols': 100}))
    lyric_alt = forms.CharField(label = u'বাংলিশ গান', widget=forms.Textarea(attrs={'rows': 20, 'cols': 100}))
    sound = forms.CharField(label = u'অডিও লিংক', widget=forms.Textarea(attrs={'rows': 2, 'cols': 100}), required=False)
    video = forms.CharField(label = u'ভিডিও লিংক', widget=forms.Textarea(attrs={'rows': 2, 'cols': 100}), required=False)
    class Meta:
        model = Gaan
        fields = ['title', 'title_alt', 'lyric', 'lyric_alt', 'gitikar', 'shilpi', 'surokar', 'bandname','albumname', 'catagory', 'video', 'sound']

class AlbumForm(forms.ModelForm):
    album_text=forms.CharField(label=u'সংক্ষিপ্ত বিবরণ', widget=forms.Textarea(attrs={'rows': 20, 'cols': 100}), required=False)
    class Meta:
        model = Albumname
        fields = ['title', 'title_alt','album_text', 'album_no', 'prokashok', 'release_year', 'voice', 'lead_guitar', 'chobi']
        verbose_name = u'এলবাম'
        verbose_name_plural = u'এলবাম'

class BandForm(forms.ModelForm):
    short_history=forms.CharField(label=u'সংক্ষিপ্ত বিবরণ', widget=forms.Textarea(attrs={'rows': 20, 'cols': 100}), required=False)
    class Meta:
        model = Bandname
        fields = ['title', 'ph_title','short_history', 'shilpi', 'chobi']
        verbose_name = u'এলবাম'
        verbose_name_plural = u'এলবাম'


class CatagoryForm(forms.ModelForm):
    short_description=forms.CharField(label=u'সংক্ষিপ্ত বিবরণ', widget=forms.Textarea(attrs={'rows': 20, 'cols': 100}), required=False)
    class Meta:
        model = Catagory
        fields = ['title','short_description']
        verbose_name = u'বিভাগ'
        verbose_name_plural = u'বিভাগ'

class GaanAdmin(admin.ModelAdmin):
    list_display =('title','short_lyric',) # এডমিনের এডিট পেইজে কোন কোন ফিল্ড যাবে সেটা দেখায়
    search_fields = ('title','lyric',) # চেইঞ্জ লিস্টে সার্চ বার যোগ করে
    #list_filter = ('gitikar','shilpi','bandname','albumname','catagory', 'surokar') # বামপাশে ফিল্টার যোগ করে
    filter_horizontal = ('gitikar','shilpi','bandname','albumname', 'catagory', 'surokar')
    form =GaanForm

class CatagoryAdmin(admin.ModelAdmin):
    form = CatagoryForm


class AlbumAdmin(admin.ModelAdmin):
    list_display =('title','album_text',) # এডমিনের এডিট পেইজে কোন কোন ফিল্ড যাবে সেটা দেখায়
    search_fields = ('title', 'album_text') # চেইঞ্জ লিস্টে সার্চ বার যোগ করে
    #list_filter = ('gitikar','shilpi','bandname','albumname','catagory', 'surokar') # বামপাশে ফিল্টার যোগ করে
    filter_horizontal = ('prokashok', 'voice', 'lead_guitar', 'chobi')
    form =AlbumForm

class BandAdmin(admin.ModelAdmin):
    search_fields = ('title', 'shilpi') # চেইঞ্জ লিস্টে সার্চ বার যোগ করে
    #list_filter = ('gitikar','shilpi','bandname','albumname','catagory', 'surokar') # বামপাশে ফিল্টার যোগ করে
    filter_horizontal = ('chobi', 'shilpi')
    form =BandForm

class CatagoryAdmin(admin.ModelAdmin):
    form = CatagoryForm


# মডেল রেজিস্টার

admin.site.register(Gitikar)
admin.site.register(Shilpi)
admin.site.register(Bandname, BandAdmin)
admin.site.register(Prokashok)
admin.site.register(Albumname, AlbumAdmin)
admin.site.register(Catagory, CatagoryAdmin)
admin.site.register(Gaan, GaanAdmin)
admin.site.register(Chobi)
