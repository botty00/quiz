from django.urls import path
from . import views

urlpatterns = [  
   path('create_user',views.create_user,name='create_user'),
   path('loginview',views.loginview,name='loginview'),
   path('question',views.question,name='question'),
   path('answer/<int:correct>',views.answer,name='answer'),
   path('result',views.result,name='result'),
   path('start',views.start,name='start'),
   path('top',views.top,name='top'),
   path('complete',views.complete,name='complete')
]
