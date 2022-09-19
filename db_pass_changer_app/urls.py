from db_pass_changer_app import views
from django.urls import path

urlpatterns = [
    path('',views.transper_password.as_view()),
    


]