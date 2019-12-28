from django import  forms

SEARCH=[('null','Type Of Course'),
    ('datascience','Data Science'),
('artificial intelligence','Artificial Intelligence'),
('programming','Programming'),
('autonomous system','Autonomous System'),
('cloud computing','Cloud Computing'),
        ]
DURATION=[ ('0','Select Duration'),
          ('1',' 1 month'),
          ('2','2-3 month'),
          ('3', '3-6 month'),
          ('6', 'more than 6 month'),
]
class search_form(forms.Form):
    search=forms.CharField(widget=forms.Select(choices=SEARCH))
    duration=forms.CharField(widget=forms.Select(choices=DURATION))
  #  return render(request,'googleproject/index.html',{'forms':search})

class show_result(forms.Form):

    title=['akash','aba','a']
    duration="1"
    description="hello world"
    link="hi link"
    level="level"

class scraper:
    Title=[]
    Rating=[]
    display=[]

