from django.contrib import admin
from django.urls import path, include

# By saying ".import" instead of something else, we are saying that the "." is where the current dir is e.g. %A_ScriptDir%
from.import views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'articles/', include('articles.urls')),
    # This is the syntax for writing the url for an about page e.g. www.google.com/about
    path(r'about/', views.about),
    # This is the syntax for writing the url for a home page e.g. www.google.com
    path(r'', views.homepage),
]
