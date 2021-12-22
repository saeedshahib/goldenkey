from django.urls import path , include

from .views import CreditCharge

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('account/', include('allauth.urls')),

    #Login url : http://127.0.0.1:8000/users/rest-auth/login/
    #Sign Up url : http://127.0.0.1:8000/users/rest-auth/registration/
    #Logout url : http://127.0.0.1:8000/users/rest-auth/logout/
    #User detail url : http://127.0.0.1:8000/users/rest-auth/user/


    #url for charging credit
    #url = http://127.0.0.1:8000/users/creditcharge/
    path('creditcharge/', CreditCharge.as_view())

]