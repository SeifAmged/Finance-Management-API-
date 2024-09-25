from django.urls import path
from .views import (
    TransactionListCreateView,
    TransactionRetrieveUpdateDestroyView,
    CategoryListView,
    UserListView,
    UserTransactionsView,
    ReportView,
    TransactionsByCategoryView,
)

urlpatterns = [
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionRetrieveUpdateDestroyView.as_view(), name='transaction-detail'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<str:category_name>/transactions/', TransactionsByCategoryView.as_view(), name='transactions-by-category'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:user_id>/transactions/', UserTransactionsView.as_view(), name='user-transactions'),
    path('reports/', ReportView.as_view(), name='report'),
]