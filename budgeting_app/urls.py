from django.urls import path
from .views import BudgetLogin, BudgetRegister, TransactionList, TransactionDetail, TransactionCreate, TransactionDelete, TransactionUpdate
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('login/', BudgetLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', BudgetRegister.as_view(), name='register'),
    path('', TransactionList.as_view(), name='budget'),
    path('transaction/<int:pk>/', TransactionDetail.as_view(), name='transaction'),
    path('transaction-create/', TransactionCreate.as_view(), name='transaction-create'),
    path('transaction-update/<int:pk>/', TransactionUpdate.as_view(), name='transaction-update'),
    path('transaction-delete/<int:pk>/', TransactionDelete.as_view(), name='transaction-delete'),
]