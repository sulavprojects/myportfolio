from django.shortcuts import render

from home.models import Update, Services, Expreance, Education, Myskills, Funfact

# Create your views here.


def home(request):
    # allservices = Services.objects.all()
    allexpreance = Expreance.objects.all()
    alleducation = Education.objects.all()
    allmyskill  = Myskills.objects.all()
    allFunfact = Funfact.objects.all()
    latestupdate = Update.objects.latest('title', 'first_name', 'last_name', 'first_auto', 'second_auto', 'my_short_discription', 'my_cv', 'profilepic', 'About_me_description', 'DOB', 'freelancer', 'adderss', 'language', 'nationality', 'phone_number', 'email_address')
    latestservices = Services.objects.latest('first_service_title', 'first_service_Discription', 'second_service_title', 'second_service_Discription', 'third_service_title', 'third_service_Discription', 'fourth_service_title', 'fourth_service_Discription', 'fifth_service_title', 'ffith_service_Discription', 'sixth_service_title', 'sixth_service_Discription')
    # latestexpreance = Expreance.objects.latest()
    # latesteducation = Education.objects.latest()



      
   
    
    
    

    context = {#'fontsfinal': fontsfinal,
                # 'allservices': allservices,
                'allexpreance': allexpreance,
                'alleducation': alleducation,
                'allmyskill': allmyskill,
                'allfunfact': allFunfact,
                'latestupdate': latestupdate,
                'latestservices': latestservices,


                
    
    }
    return render(request , 'index.html',context)  