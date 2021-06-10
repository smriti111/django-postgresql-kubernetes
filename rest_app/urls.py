from django.urls import path
from .views import ArticleAPIView,ArticleDetails,home,entry,get_score
 
urlpatterns = [path('article/', ArticleAPIView.as_view()),
              path('detail/<int:id>/', ArticleDetails.as_view()),
              path("", home,name="home page" ),
              path("entry/", entry,name="home page" ),
              path("get_score/", get_score,name="home page" ),
              ]
