from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from gwent_api import views

urlpatterns = [
    url(r'^gwent/$', views.api_root),
    url(r'^gwent/cards/$', views.CardList.as_view(), name='card-list'),
    url(r'^gwent/categories/$', views.CategoryList.as_view(), name='category-list'),
    url(r'^gwent/factions/$', views.FactionList.as_view(), name='faction-list'),
    url(r'^gwent/groups/$', views.GroupList.as_view(), name='group-list'),
    url(r'^gwent/rarities/$', views.RarityList.as_view(), name='rarity-list'),
    url(r'^gwent/cards/(?P<pk>[^\/]+)/$', views.CardDetail.as_view(), name='card-detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns) 