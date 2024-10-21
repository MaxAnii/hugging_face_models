from django.urls import path
from .views import summerize_text
urlpatterns = [
    path("summerize_text/",summerize_text,name='summerize_text')
]
