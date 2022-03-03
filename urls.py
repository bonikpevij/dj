from django.contrib import admin
from django.conf.urls import include,url
from django.urls import path
from blog import views
from blog.views import ContactUsView,SignupView
from tweet.views import Index,Profile,PostTweet, HashTagCloud,SearchInfo
admin.autodiscover()
url(r'^user/(\w+)/$', views.Profile)



urlpatterns = [
url(r'^$', Index.as_view()),
url(r'^user/(\w+)/$', Profile.as_view()),
url(r'^user/(\w+)/post/$', PostTweet.as_view()),
url(r'^user/(\w+)/contact/$', ContactUsView.as_view()),
url(r'^hashTag/(\w+)/$', HashTagCloud.as_view()),
url(r'^signup/$', SignupView.as_view()),
url(r'^search/$', SearchInfo.as_view()),
path('chat/', include('chat.urls')),
path('home/', views.home_view),
path('articles/', views.home_view),
path('admin/', admin.site.urls),
]
