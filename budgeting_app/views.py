from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.db.models import Sum

from .models import BudgetInfo



class BudgetLogin(LoginView):
    template_name = 'budgeting_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('budget')
    

class BudgetRegister(FormView):
    template_name = 'budgeting_app/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('budget')

    def form_valid(self, form):
        user = form.save()

        if user is not None:
            login(self.request, user)

        return super(BudgetRegister, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return reverse_lazy('budget')
        
        return super(BudgetRegister, self).get(*args, **kwargs)


class TransactionList(LoginRequiredMixin, ListView):
    model = BudgetInfo
    context_object_name = 'budget'

    # Formats dollar sign based on whether or not balance is negative
    def format_negative(self, balance):
        if balance >= 0:
            return f"${balance}"

        return f"-${abs(balance)}"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['budget'] = context['budget'].filter(user=self.request.user)

        balance = context['budget'].aggregate(Sum('amount'))['amount__sum']
        # If balance is a whole number, round to whole number, else round to the nearest hundredth
        if balance:
            if balance.is_integer():
                context['balance'] = self.format_negative(round(balance))
            
            else:
                context['balance'] = self.format_negative(round(balance), 2)
            
        else:
            context['balance'] = "$0"

        # Search function
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['budget'] = context['budget'].filter(title__icontains=search_input).union(context['budget'].filter(category__icontains=search_input))
        
        context['search_input'] = search_input

        return context
    

class TransactionDetail(LoginRequiredMixin, DetailView):
    model = BudgetInfo
    context_object_name = 'budget'


class TransactionCreate(LoginRequiredMixin, CreateView):
    model = BudgetInfo
    fields = ['title', 'description', 'category', 'amount', 'date']
    success_url = reverse_lazy('budget')

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super(TransactionCreate, self).form_valid(form)
    

class TransactionUpdate(LoginRequiredMixin, UpdateView):
    model = BudgetInfo
    fields = ['title', 'description', 'category', 'amount', 'date']
    success_url = reverse_lazy('budget')


class TransactionDelete(LoginRequiredMixin, DeleteView):
    model = BudgetInfo
    context_object_name = 'budget'
    success_url = reverse_lazy('budget')