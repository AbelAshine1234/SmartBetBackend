"""
URL configuration for smartbetbackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from users.views import UserList as UserListViews,UserCreatedView,GetUser
from users.update import ChangeRole,ChangeEmail,ChangeName,ChangePassword
from analysis.views import GetAnalysisView,AnalysisView,AnalysisViewChangeTitle,AnalysisViewChangeContent
from articles.views import GetArticlesView,ArticlesView,ArticlesViewChangeTitle,ArticlesViewChangeContent
from tips.views import GetTipsView,TipsView,TipsViewChangeTitle,TipsViewChangeContent

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/userlist/",UserListViews.as_view()),
    path("api/user/",UserCreatedView.as_view()),
    path("api/user/<int:pk>/",GetUser.as_view()),
    path("api/user/role/<int:pk>/",ChangeRole.as_view()),
    path("api/user/email/<int:pk>/",ChangeEmail.as_view()),
    path("api/user/name/<int:pk>/",ChangeName.as_view()),
    path("api/user/password/<int:pk>/",ChangePassword.as_view()),
    # analysis
    path("api/analysis/<int:pk>/",GetAnalysisView.as_view()),
    path("api/analysis/",AnalysisView.as_view()),
    path("api/analysis/title/<int:pk>/",AnalysisViewChangeTitle.as_view()),
    path("api/analysis/content/<int:pk>/",AnalysisViewChangeContent.as_view()),
    # analysis
    path("api/articles/<int:pk>/",GetArticlesView.as_view()),
    path("api/articles/",ArticlesView.as_view()),
    path("api/articles/title/<int:pk>/",ArticlesViewChangeTitle.as_view()),
    path("api/articles/content/<int:pk>/",ArticlesViewChangeContent.as_view()),

    # tips
    path("api/tips/<int:pk>/",GetTipsView.as_view()),
    path("api/tips/",TipsView.as_view()),
    path("api/tips/title/<int:pk>/",TipsViewChangeTitle.as_view()),
    path("api/tips/content/<int:pk>/",TipsViewChangeContent.as_view()),
    ]
