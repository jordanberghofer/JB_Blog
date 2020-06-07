# """Dj_JB_Blog URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/3.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
from django.contrib import admin
from django.urls import path

# By saying ".import" instead of something else, we are saying that the "." is where the current dir is e.g. %A_ScriptDir%
from.import views

urlpatterns = [
    path(r'admin/', admin.site.urls),

    # This is the syntax for writing the url for an about page e.g. www.google.com/about
    path(r'about/', views.about),

    # This is the syntax for writing the url for a home page e.g. www.google.com
    path(r'', views.homepage),
]
