# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import forms

# Create your views here.
def test():
    return render('test.html')

def index(request):
    form=forms.search_form()
    if request.method=='POST':
        form=forms.search_form(request.POST)
        if form.is_valid():
            search=form.cleaned_data['search']#input form index page
            duration=form.cleaned_data['duration']#input from index page
            object = forms.scraper() # passing output string to object of scraper class in forms.py
            if search=='datascience':

                # scraper code starts here
                from urllib.request import urlopen
                from urllib.error import HTTPError
                from bs4 import BeautifulSoup
                import re
                def get_site_file(url):
                    """
                    url - base url to access desired web file
                    """
                    try:
                        html = urlopen(url)
                        bs = BeautifulSoup(html, 'html.parser')
                        return bs

                    except HTTPError as e:
                        print(e)

                page_content = get_site_file('https://www.coursera.org/search?query=data%20science&')
                try:
                    discovery_course = page_content.find("ul", \
                                                    {'class': 'ais-InfiniteHits-list'})
                except AttributeError as e:
                    print('Something seems to be missing with the tag')
                if page_content == None:
                    print('The file could not be found')
                else:
                    courses = page_content.find_all('li', {'class': 'ais-InfiniteHits-item'})
                    for course in courses:
                        try:
                            course_title = course.h2.get_text()
                            course_rating = course.find('span', {'class': 'ratings-text'}). \
                                get_text()
                            #assigning output strings to array of class object of show_result class in forms.py

                            object.Title.append(f"Course Title: \t {course_title}")
                            object.Rating.append(f"Course Rating: \t {course_rating}")
                            object.display.append('\n' + ('|') + ('<' * 3) + ('-' * 7) + ' New Course ' + ('-' * 7) + ('>' * 3) + (
                                '|') + '\n')
                        except AttributeError as e:
                            print(e)
                 #craper code ends here

            return  render(request,'googleproject/search.html',{'test_result':object})#object returned to page

    return render(request,'googleproject/index.html',{'forms':form})#if no input is there empty website than form is generated returned to page

def searchshow(request):
    result=forms.show_result()
    return render (request,'googleproject/search.html',{'search_result':result})
    #serach result page  for future use after prototype
    # if run throught changing url by adding 'searchshow/' to url as seen in urls.py
