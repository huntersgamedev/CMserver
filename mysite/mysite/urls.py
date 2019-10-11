"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from.import views
from.import settings
from django.conf.urls.static import static


urlpatterns = [

    
    #path('admin/', admin.site.urls),
    path('',views.redirecting, name='redirecting'),
    path('info/', views.retreiveUserToken,name='retreiveUserToken'),
    path('user/', views.GetUserData,name='GetUserData'),
    path('leaderboard/', views.GetLeaderBoard,name=' GetLeaderBoard'),
    path('addscore/<int:Score>/', views.UpdateScore,name=' UpdateScore'),
    
#.........Urls for saving the game..........................................
    path('loadplayerdata/', views.LoadPlayerData,name=' GetLeaderBoard'),
    #saving tutorialCompletion
    path('savedorm/',views.SaveDorm,name='SaveDorm'),

    #saving character creation Creation
    path ('savechar/<int:Head>/<int:Body>/',views.SaveCharacter,name='SaveCharacter'),

    #Saving for Cooks
    path('savecooksgame/<int:CooksScore>/',views.savecooksscore,name='Save Cooks Score'),
    path('savecooksquiz/<int:CooksQuiz>/',views.savecooksquiz,name='Save Cooks quiz'),

    #Saving for Homes
    path('savehomesgame/<int:HomesScore>/',views.savehomesscore,name='Save Homes Score'),
    path('savehomesquiz/<int:HomesQuiz>/',views.savehomesquiz,name='Save Homes quiz'),

    #saving for toys
    path('savetoysgame/<int:ToysScore>/',views.savetoysscore,name='Save Toys Score'),
    path('savetoyssquiz/<int:ToysQuiz>/',views.savetoysquiz,name='Save toys quiz'),

    #Reset All Values for User(Debug for developer use)
    path('wipestats/',views.WipeStats,name='wipe stats'),
    static(settings.STATIC_URL,document_root=settings.STATIC_ROOT),
] 
