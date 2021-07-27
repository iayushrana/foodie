from django.conf.urls import url
from . import views

app_name="food"

urlpatterns = [
    #/food/ homepage with no extra information
    url(r'^$', views.sfood,name="sfood"),


    url(r'^about_us$', views.about_us,name="about_us"),

    url(r'^contact_us$', views.contact_us,name="contact_us"),

    #url(r'^test$', views.test,name="test"),
    

    # /food/ homepage with no extra information
    url(r'^vegetable$', views.Vindex, name="vegetables"),

    url(r'^fruit$', views.Findex, name="fruits"),

    # /food/71(id)/ ^ represent the begning and $ ssign represent the end both at the same time
    url(r'^detail/(?P<album_id>[0-9]+)/$', views.detail, name="detail"),


    # /food/album/delete/
    #url(r'^album/(?P<pk>[0-9]+)/buy/$', views.Vindex, name='album-buy'),

    # /food/71(id)/ ^ represent the begning and $ ssign represent the end both at the same time

    # for registration


   # url(r'^carts/$', views.cart_home, name="cart"),
   # url(r'^carts/cart_update/$', views.cart_update, name="update"),

    url(r'^cart/$', views.cart_detail, name='cart_detail'),
    url(r'^cart/add/(?P<product_id>[0-9]+)/$', views.cart_add, name='cart_add'),
    url(r'^cart/remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),

]