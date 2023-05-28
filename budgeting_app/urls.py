from django.urls import path
from .views import BudgetLogin, BudgetRegister, BudgetList
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('login/', BudgetLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', BudgetRegister.as_view(), name='register'),
    path('', BudgetList.as_view(), name='budget')
]