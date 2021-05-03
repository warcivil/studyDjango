from django.urls import path
from news.views import index, test, get_category

urlpatterns = [
    path('', index, name="home"),
    path('test/', test),
    path('category/<int:index_category>/', get_category, name="category"),
]