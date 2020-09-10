from djongo import models
from django import forms
from datetime import datetime

# Instagram Classes
class InstagramUserStatus(models.Model):
  version = models.IntegerField()
  followers = models.IntegerField()
  following = models.IntegerField()
  posts = models.IntegerField()
  engagement = models.FloatField()
  date = models.DateTimeField()

  class Meta:
    abstract = True

class InstagramUserStatusForm(forms.ModelForm):
  class Meta:
    model = InstagramUserStatus
    fields = (
      'version', 'followers', 'following', 'posts', 'engagement', 'date'
    )

class InstagramUser(models.Model):
  id = models.CharField(max_length=256, primary_key=True)
  username = models.CharField(max_length=256)
  fullname = models.CharField(max_length=256)
  bio = models.CharField(max_length=514, blank=True)
  has_channel = models.BooleanField(null=True)
  is_business_account = models.BooleanField(null=True)
  business_category_name = models.CharField(max_length=256, null=True)
  is_verified = models.BooleanField(default=False)
  profile_pic_url = models.URLField(max_length=512, blank=True) 
  followers = models.IntegerField()
  following = models.IntegerField()
  posts = models.IntegerField()
  engagement = models.FloatField()

  CLASS_INFLUENCE = [
    ('simple-user', 'simple-user'),
    ('micro-influencer', 'micro-influencer'),
    ('influencer', 'influencer'),
  ]
  class_influence = models.CharField(
    max_length=48,
    choices=CLASS_INFLUENCE,
    null=True
  )

  user_status = models.ArrayField(
    model_container = InstagramUserStatus,
    model_form_class = InstagramUserStatusForm,
    null=True,
  )

class InstagramPost(models.Model):
  id = models.CharField(max_length=256, primary_key=True)
  type = models.CharField(max_length=256)
  shortcode = models.CharField(max_length=256)
  comment_count = models.IntegerField()
  likes_count = models.IntegerField()
  user_id = models.CharField(max_length=256)
  username = models.CharField(max_length=256)
  

# Twitter Classes
class TwitterUserStatus(models.Model):
  version = models.IntegerField()
  followers_count = models.IntegerField()
  friends_count = models.IntegerField()
  favourites_count = models.IntegerField()
  statuses_count = models.IntegerField()
  date = models.DateTimeField()

  class Meta:
    abstract = True

class TwitterUserStatusForm(forms.ModelForm):
  class Meta:
    model = TwitterUserStatus
    fields = (
      'version', 'followers_count', 'friends_count', 'favourites_count', 'statuses_count', 'date'
    )

class TwitterUser(models.Model):
  id_str = models.CharField(max_length=256, primary_key=True)
  name = models.CharField(max_length=256)
  screen_name = models.CharField(max_length=256)
  location = models.CharField(max_length=256, null=True)
  url = models.URLField(max_length=512, null=True)
  description = models.CharField(max_length=1024, null=True)
  verified = models.BooleanField(default=False)
  profile_image_url = models.URLField(max_length=512, null=True)
  lang = models.CharField(max_length=256, null=True)
  user_status = models.ArrayField(
    model_container = TwitterUserStatus,
    model_form_class = TwitterUserStatusForm,
    null=True
  )

class Tweet(models.Model):
  id_str = models.CharField(max_length=256, primary_key=True)
  created_at = models.DateTimeField()
  text = models.CharField(max_length=1024)
  user_id = models.CharField(max_length=256)
  in_reply_to_status_id_str = models.CharField(max_length=256, null=True)
  in_reply_to_user_id_str = models.CharField(max_length=256, null=True)
  in_reply_to_screen_name = models.CharField(max_length=256, null=True)
  type = models.CharField(max_length=256)

