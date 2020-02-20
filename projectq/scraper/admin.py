from django.contrib import admin
from .models import Page
from .models import Image
from lxml import html
import requests
from cssselect import HTMLTranslator

"""
import scrapy

class ImageScraper(scrapy.Spider):
    name = "imagescraper"
    def __init__(self, url):
        self.start_urls = list(url)

    def parse(self, response):
        breakpoint()
        pass
"""

class PageAdmin(admin.ModelAdmin):
    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or dict()
        extra_context['test'] = 'abc'
        page = Page.objects.get(id=object_id)
        url = page.url
        html_page = requests.get(url)
        tree = html.fromstring(html_page.content)
        selector = HTMLTranslator().css_to_xpath('img')
        images = [i.get('src') for i in tree.xpath(selector)]
        extra_context['images'] = images
        return super().change_view(request, object_id, form_url, extra_context)

admin.site.register(Page, PageAdmin)
admin.site.register(Image)
