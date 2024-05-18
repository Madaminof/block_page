from django.urls import path
from .views import *

urlpatterns = [
    path('', login_page, name='login_page'),
    path('logout_page/',logout_page, name='logout_page'),
    path('signup/',  SignUpView.as_view(), name='signup'),
    path('category/', CategoryView.as_view(), name='category'),
    path('detail/<int:pk>',DetailView.as_view(), name='detail')

]

