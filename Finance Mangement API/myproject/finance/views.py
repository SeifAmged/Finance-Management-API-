from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Transaction, Category
from .serializers import UserSerializer, CategorySerializer, TransactionSerializer
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Sum
from rest_framework import status
from rest_framework.exceptions import NotFound  
from rest_framework.permissions import IsAuthenticated

class TransactionListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['transaction_date', 'category', 'user']
    ordering_fields = ['transaction_date', 'amount']

class TransactionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class CategoryListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class UserListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserTransactionsView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Transaction.objects.filter(user__id=user_id)

class ReportView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user_id = request.query_params.get('user_id')
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if not user_id:
            return Response({'error': 'User ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        transactions = Transaction.objects.filter(user__id=user_id)

        if start_date and end_date:
            transactions = transactions.filter(transaction_date__range=[start_date, end_date])
        elif start_date:
            transactions = transactions.filter(transaction_date__gte=start_date)
        elif end_date:
            transactions = transactions.filter(transaction_date__lte=end_date)

        total_amount = transactions.aggregate(Sum('amount'))['amount__sum'] or 0

        serializer = TransactionSerializer(transactions, many=True)

        report_data = {
            'user_id': user_id,
            'total_amount': total_amount,
            'transactions': serializer.data,
        }

        return Response(report_data)

# تعديل TransactionsByCategoryView
class TransactionsByCategoryView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionSerializer

    def get_queryset(self):
        category_name = self.kwargs['category_name'].lower()  
        category_choices = dict(Transaction.TRANSACTION_CATEGORIES).keys()
        if category_name not in category_choices:
            raise NotFound(detail="Category not found.")  
        return Transaction.objects.filter(category__iexact=category_name)
