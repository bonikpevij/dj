from django.http import HttpResponseRedirect,HttpResponse
from django.template import Context
from django.template.loader import render_to_string
from django.views.generic import View, ListView
from django.shortcuts import render, redirect
from user_profile.models import User
from tweet.models import Tweet, HashTag
from tweet.forms import TweetForm, SearchForm
from django.core import serializers
import json
class Index(View):
    def get(self, request):
        params = {}
        params["name"] = "Django"
        return render(request, 'base.html', params)
class SearchInfo(ListView):
    model = Tweet
    template_name = 'main.html'
    def get_context_data(self, **kwargs):
        context= super(SearchInfo, self).get_context_data(**kwargs)
        tweets = list(Tweet.objects.order_by('text'))
        tweets=serializers.serialize("json",tweets)
        context["qs_json"]=json.dumps(tweets)
        return context

class HashTagCloud(View):
    """Hash Tag page reachable from /hastag/<hashtag> URL"""
    def get(self, request, hashtag):
        params = dict()
        hashtag = HashTag.objects.get(name=hashtag)
        params["tweets"] = hashtag.tweet
        return render(request, 'hashtag.html', params)
class Profile(View):
    """User Profile page reachable from /user/<username> URL"""
    def get(self, request, username):
        params = dict()
        form = TweetForm()
        user = User.objects.get(username=username)
        tweets = Tweet.objects.filter(user=user)
        params["tweets"] = tweets
        params["user"] = user
        params["form"] = form
        return render(request,'profile.html', params)

class PostTweet(View):
    """Tweet Post form available on page /user/<username> URL"""
    def post(self, request, username):
        form = TweetForm(self.request.POST)
        if form.is_valid():
            user = User.objects.get(username=username)
            tweet = Tweet(text=form.cleaned_data['text'],user=user,country=form.cleaned_data['country'])
            tweet.save()
            words = form.cleaned_data['text'].split(" ")
            for word in words:
                if word[0] == "#":
                    hashtag, created =HashTag.objects.get_or_create(name=word[1:]), hashtag.tweet.add(tweet)
        return HttpResponseRedirect('/user/'+username)

