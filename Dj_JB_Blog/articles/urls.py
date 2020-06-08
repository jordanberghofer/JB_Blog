from django.urls import path

# By saying ".import" instead of something else, we are saying that the "." is where the current dir is e.g. %A_ScriptDir%
from.import views

urlpatterns = [
    # This is the syntax for writing the url for a home page e.g. www.google.com
    path(r'', views.article_list),
	path(r'about/', views.article_list)
]
