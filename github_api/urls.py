from django.urls import path

from github_api.views import get_user_accounts

urlpatterns = [
    path('accounts/', get_user_accounts, name='accounts'),
]