#pfrom __future__ import unicode_literals
from django.db import models
import datetime
from django.template.defaultfilters import truncatewords


# Create your models here.

class Chobi(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'শিরোনাম')
    chobi = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg', verbose_name=u'ছবি')
    caption = models.CharField(max_length=500, verbose_name=u'ক্যাপশন', blank=True, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'ছবি'
        verbose_name_plural = u'ছবি'

class Gitikar(models.Model):
    title = models.CharField(max_length=100, verbose_name = u'নাম')
    biography = models.CharField(max_length=1000, blank=True, null=True, verbose_name = u'বিবরন')
    
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'গীতিকার'
        verbose_name_plural = u'গীতিকার'

class Prokashok(models.Model):
    title = models.CharField(max_length=150, verbose_name = u'নাম')
    short_description = models.CharField(max_length=1000, blank=True, null=True, verbose_name = u'বিবরন')
    class Meta:
        verbose_name = u'প্রকাশক'
        verbose_name_plural = u'প্রকাশকবৃন্দ'

    def __unicode__(self):
            return self.title

class Shilpi(models.Model):
    title = models.CharField(max_length=100, verbose_name = u'নাম')
    biography = models.CharField(max_length=1000, blank=True, null=True, verbose_name = u'বিবরন')
   
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'শিল্পী'
        verbose_name_plural = u'শিল্পীবৃন্দ'

class Bandname(models.Model):
    title = models.CharField(max_length=100, verbose_name = u'নাম')
    ph_title = models.CharField(max_length=100, blank=True, null=True, verbose_name = u'বাংলিশ নাম')
    short_history = models.CharField(max_length=1000, blank=True, null=True, verbose_name = u'বিবরন')
    shilpi = models.ManyToManyField(Shilpi, blank=True, null=True, verbose_name = u'শিল্পী')
    chobi = models.ManyToManyField(Chobi, blank=True, null=True, verbose_name = u'ছবি')
    class Meta:
        verbose_name = u'ব্যান্ড'
        verbose_name_plural = u'ব্যান্ডদল'

    def __unicode__(self):
        return self.title

class Albumname(models.Model):
    title = models.CharField(max_length=100, verbose_name = u'নাম')
    title_alt = models.CharField(max_length=100, blank=True, null=True, verbose_name = u'বাংলিশ নাম')
    album_text = models.CharField(max_length=10000, blank=True, null=True, verbose_name = u'বিবরন')
    album_no = models.CharField(max_length=1000, blank=True, null=True, verbose_name = u'এলবাম নাম্বার')
    lineup = models.ManyToManyField(Shilpi, blank=True, null=True, verbose_name = u'লাইন আপ')
    prokashok = models.ManyToManyField(Prokashok, blank=True, null=True, verbose_name = u'প্রকাশক')
    chobi = models.ManyToManyField(Chobi, blank=True, null=True, verbose_name = u'ছবি')
    release_year = models.IntegerField(default=datetime.datetime.now().year, blank=True, null=True, verbose_name = u'মুক্তির বছর')
    lead_guitar = models.ManyToManyField(Shilpi, blank=True, null=True, verbose_name = u'লিড গিটার', related_name='alb_lg')
    voice = models.ManyToManyField(Shilpi, blank=True, null=True, verbose_name = u'কন্ঠ', related_name='alb_voice')
    class Meta:
        verbose_name = u'এলবাম'
        verbose_name_plural = u'এলবামগুলো'

    def __unicode__(self):
        return self.title
    
    def first_letter(self):
        return self.title and self.tilte[0] or ''

class Catagory(models.Model):
    title = models.CharField(max_length=500, verbose_name = u'বিভাগ')
    short_description = models.CharField(max_length=1000, blank=True, null=True, verbose_name = u'বিবরন')
    class Meta:
        verbose_name = u'শ্রেণীবিভাগ'
        verbose_name_plural = u'বিভাগ সমূহ'
    
    def __unicode__(self):
        return self.title

class Gaan(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'শিরোনাম')
    title_alt = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'বাংলিশ')
    lyric = models.CharField(max_length=5000,verbose_name=u'গান')
    lyric_alt = models.CharField(max_length=5000, blank=True, null=True, verbose_name=u'বাংলিশ গান')
    gitikar = models.ManyToManyField(Shilpi, blank=True, null=True, verbose_name=u'গীতিকার', related_name ='ga_git')
    shilpi = models.ManyToManyField(Shilpi, blank=True, null=True, verbose_name=u'শিল্পী', related_name ='ga_voice')
    surokar = models.ManyToManyField(Shilpi, blank=True, null=True, verbose_name=u'সুর', related_name ='ga_tune')
    bandname = models.ManyToManyField(Bandname, blank=True, null=True, verbose_name=u'ব্যান্ড')
    albumname = models.ManyToManyField(Albumname, blank=True, null=True,verbose_name=u'এলবাম')
    catagory = models.ManyToManyField(Catagory, blank=True, null=True,verbose_name=u'শ্রেণিবিভাগ')
    video = models.CharField(max_length=1000, blank=True, null=True, verbose_name=u'ইউটিউব')
    sound = models.CharField(max_length=1000, blank=True, null=True, verbose_name=u'সাউন্ডক্লাউড')
    class Meta:
        verbose_name = u'গান'
        verbose_name_plural = u'গানগুলো'

    def __unicode__(self):
        return self.title

    def short_lyric(self):
        return truncatewords(self.lyric, 25)




