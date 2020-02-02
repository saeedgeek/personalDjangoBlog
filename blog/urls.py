from django.urls import path
from .views import blog,blogDetail
urlpatterns = [
    path('', blog,name="allblog"),
    path('<int:postId>/',blogDetail),
    
]