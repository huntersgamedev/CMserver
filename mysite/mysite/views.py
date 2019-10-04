from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.db.models import IntegerField
from django.db.models.functions import Cast
from scorsite.models import PostUserScore
from scorsite.models import UserSaveFile
#from scorsite.models.functions import Cast
from django.core.serializers import serialize
import requests
import json
import webbrowser
import urllib
import operator



#global multi use variables
global target_url
target_url = 'https://bbgbctest.blackboard.com'

global redirect_url
redirect_url='http://startgbc.georgebrown.ca/info/'

global SECRET
SECRET = "ANuwg76VOV7aIA0KYqfv6KWIGOWEw0FX"  

global KEY
KEY = "ce2cbd52-60e4-4e94-bb23-66099afe6d16"  






#TEMP STEP 1 of three legged OAuth opens a browser with working URL to get authorization code
def redirecting(word):
    #webbrowser.open('https://bbgbctest.blackboard.com/learn/api/public/v1/oauth2/authorizationcode?redirect_uri=http://startgbc.georgebrown.ca/info/&response_type=code&client_id=ce2cbd52-60e4-4e94-bb23-66099afe6d16&scope=read&state=DC1067EE-63B9-40FE-A0AD-B9AC069BF4B0/',new=0,autoraise=False)
    #webbrowser.open('https://www.google.ca/')
    RedirectURI='https://bbgbctest.blackboard.com/learn/api/public/v1/oauth2/authorizationcode?redirect_uri=http://startgbc.georgebrown.ca/info/&response_type=code&client_id=ce2cbd52-60e4-4e94-bb23-66099afe6d16&scope=read&state=DC1067EE-63B9-40FE-A0AD-B9AC069BF4B0/'
    
    return HttpResponseRedirect (RedirectURI)


# STEP 2 of three legged OAuth gets the users authorization code then gets a oauth token
def retreiveUserToken(request):
    woo={'code=':'value'
    }
    r= request.GET.get('code')
    UserOAuthToken(request,r)
    return HttpResponse(r)







# Step 3 of three legged oauth. Retreive the users token using there authorizion code
def UserOAuthToken(request,userCode):  
        CLIENT_ID= 'gstudent1'
        CLIENT_SECRET='Gbc123'
        
  
  
        CREDENTIALS = 'client_credentials'  
        PAYLOAD = {  
            'grant_type':'authorization_code',  
            'code':userCode,
            'redirect_uri':redirect_url,     
            }

        global TOKEN
        TOKEN = None  
        target_url = 'https://bbgbctest.blackboard.com'
        session = request.session  
        oauth_path = '/learn/api/public/v1/oauth2/token'  
        OAUTH_URL = target_url + oauth_path  
        
        
        # session.mount('https://', Tls1Adapter()) # remove for production  
        # Authenticate
        print('auth code is',userCode)
        r = requests.post(OAUTH_URL, data=PAYLOAD, auth=(KEY, SECRET),verify=True) 
        #r = requests.post(OAUTH_URL, data=PAYLOAD, auth=(KEY, SECRET),verify=True)  
        print("[auth:setToken()] STATUS CODE: " + str(r.status_code) )
        #print()
        print("[auth:setToken()] RESPONSE: " + r.text)  
  
        if r.status_code == 200:  
            parsed_json = json.loads(r.text)  
            TOKEN = parsed_json['access_token']  
            session['TOKEN']=r.text
            GetUserData(request)

            return HttpResponse(r)
        
      



#retreive users Data for the game leaderboard 
#NEXT NEEDED STEP FIRE OFF REQUIRED DATA TO DATABASE
def GetUserData(request):
    print('the session varaible is'+request.session['TOKEN'])
    target_url = 'https://bbgbctest.blackboard.com'
    oauth_path ='/learn/api/public/v1/users'
    TOKEN=request.session['TOKEN']
    r=requests.get(target_url+oauth_path,headers={'Authorization':'Bearer '+TOKEN}, verify=True)

    print("[auth:setToken()] STATUS CODE:"+ str(r.status_code))
    print("[auth:setToken()] RESPONSE: " + r.text)
   
    
    if r.status_code== 200:
        rt=r.json()
        #example of how to parse the requests data properly Look at https://developer.blackboard.com/portal/displayApi to find info names
        UN=rt['results'][0]['userName']
        request.session['UserName']=UN
        FN=rt['results'][0]['name']['given']
        LN=rt['results'][0]['name']['family']


        print('this is the'+UN+FN+LN)
        print('The session key is'+request.session['UserName'])
        

        if PostUserScore.objects.filter(UserName=UN).exists():
           #SaveInst=UserSaveFile.objects.create(UserName=UN)
            print("USER ALREADY EXSITS DON'T DO ANYTHING")
            
            
        else:
            ScoreInst=PostUserScore.objects.create(FirstName=FN,LastName=LN,UserName=UN)
            SaveInst=UserSaveFile.objects.create(UserName=UN)
           
            

            #parsed_json = json.loads(r.text)  
            #student = parsed_json.GET.get()  
            #print("STUDENTINFO: "+ student)
            print("[auth:setToken()] RESPONSE: "+ r)
          
        return HttpResponse(r.text)


    

def GetLeaderBoard(request):    
    #LB= PostUserScore.objects.all()
    results=PostUserScore.objects.order_by(-Cast('Score',IntegerField()),)[:10]
    jResults=serialize('json',results)
   
   # context={'SortedScores':results}

    return HttpResponse(jResults)


def UpdateScore(request,Score):
    #print('IM LOOKING FOR THIS GUY'  +request.session['UserName'])
    #PostUserScore.objects.filter(UserName=request.session['UserName']).update(Score=Score)
    PostUserScore.objects.filter(UserName='gstudent1').update(Score=Score)
   
    #UD.Score=Score
    #UD.Save()

    print("the score is{}".format(Score))
    word=''
    return HttpResponse('')




#------------------------------------For loading and saving player data--------------------------

def LoadPlayerData(request):

    #CurrentUser=request.session['UserName']

    Test=UserSaveFile.objects.filter(UserName='gstudent1')
    JTest=serialize('json',Test)

    return HttpResponse(JTest)
    #search the table for a user

#Saves tutorial data
def SaveDorm(request):
    
    #UserSaveFile.objects.filter(UserName=request.session['UserName']).update(Tutorial=1)
    UserSaveFile.objects.filter(UserName='gstudent1').update(Tutorial=1)

    return HttpResponse('')

#---------------saves character creator data---------------------
def SaveCharacter(request,Head,Body):

     #UserSaveFile.objects.filter(UserName=request.session['UserName']).update(CharHead=Head)
     #UserSaveFile.objects.filter(UserName=request.session['UserName']).update(CharBody=Body)
     UserSaveFile.objects.filter(UserName='gstudent1').update(CharHead=Head)
     UserSaveFile.objects.filter(UserName='gstudent1').update(CharBody=Body)

     return HttpResponse('')

#-----------------saves cooks scores------------------------
def savecooksscore(request,CooksScore):
    
    #UserSaveFile.objects.filter(UserName=request.session['UserName']).update(CooksScore=CooksScore)
    UserSaveFile.objects.filter(UserName='gstudent1').update(CooksScore=CooksScore)

    return HttpResponse('')

def savecooksquiz(request,CooksQuiz):
    
    #UserSaveFile.objects.filter(UserName=request.session['UserName']).update(CooksQuiz=CooksQuiz)
    UserSaveFile.objects.filter(UserName='gstudent1').update(CooksQuiz=CooksQuiz)

    return HttpResponse('')


#----------------------Save homesScore--------------------

def savehomesscore(request,HomesScore):
    
    #UserSaveFile.objects.filter(UserName=request.session['UserName']).update(HomesScore=HomesScore)
    UserSaveFile.objects.filter(UserName='gstudent1').update(HomesScore=HomesScore)

    return HttpResponse('')

def savehomesquiz(request,HomesQuiz):
    
    #UserSaveFile.objects.filter(UserName=request.session['UserName']).update(HomesQuiz=HomesQuiz)
    UserSaveFile.objects.filter(UserName='gstudent1').update(HomesQuiz=HomesQuiz)

    return HttpResponse('')


#-----------Save ToysScore----------------------------

def savetoysscore(request,ToysScore):
    
    #UserSaveFile.objects.filter(UserName=request.session['UserName']).update(ToysScore=ToysScore)
    UserSaveFile.objects.filter(UserName='gstudent1').update(ToysScore=ToysScore)

    return HttpResponse('')

def savetoysquiz(request,ToysQuiz):

    #UserSaveFile.objects.filter(UserName=request.session['UserName']).update(ToysQuiz=ToysQuiz)
    UserSaveFile.objects.filter(UserName='gstudent1').update(ToysQuiz=ToysQuiz)

    return HttpResponse('')

#--------------------------Debug to wipe all the player stats--------------------------
def WipeStats(request):
    UserSaveFile.objects.filter(UserName='gstudent1').update(ToysQuiz=0)
    UserSaveFile.objects.filter(UserName='gstudent1').update(ToysScore=0)
    UserSaveFile.objects.filter(UserName='gstudent1').update(HomesQuiz=0)
    UserSaveFile.objects.filter(UserName='gstudent1').update(HomesScore=0)
    UserSaveFile.objects.filter(UserName='gstudent1').update(CooksQuiz=0)
    UserSaveFile.objects.filter(UserName='gstudent1').update(CooksScore=0)
    UserSaveFile.objects.filter(UserName='gstudent1').update(CharBody=0)
    UserSaveFile.objects.filter(UserName='gstudent1').update(CharHead=0)
    UserSaveFile.objects.filter(UserName='gstudent1').update(Tutorial=0)
    PostUserScore.objects.filter(UserName='gstudent1').update(Score=0)

    return HttpResponse('')
    