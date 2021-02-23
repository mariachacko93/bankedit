"""MyBank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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


from django.urls import path

from Profiles.views import CreateProfile, AccountView, success, UpdateprofileView, Deleteprofile, ViewProfile, \
    generateaccnoView,profilesuccess,TransferView,withdrawView,DepositView,transfersuccess,depositsuccess,withdrawsuccess

urlpatterns = [
    path("createprofile/",CreateProfile.as_view(),name="createprofile"),
    path("updateprofile/<int:pk>/", UpdateprofileView.as_view(), name="updateprofile"),
    path("success/",success,name="success"),
    path("delete/<int:pk>/",Deleteprofile.as_view(),name="delete"),
    path("viewprofile/<int:pk>/", ViewProfile.as_view(), name="viewprofile"),
    path("generate/", generateaccnoView, name="generate"),
    path("profilesuccess/", profilesuccess, name="profilesuccess"),
    path("accview/<int:pk>",AccountView.as_view(),name="accview"),
    path("transfer", TransferView.as_view(), name="transfer"),
    path("withdraw", withdrawView.as_view(), name="withdraw"),

    path("deposit", DepositView.as_view(), name="deposit"),
    path("transfersuccess", transfersuccess, name="transfers"),
    path("withdrawsuccess", withdrawsuccess, name="withdraws"),
    path("depositsuccess", depositsuccess, name="deposits"),

]
