from django.conf.urls import url
import views

urlpatterns=[
    url(r'^add_(\d+)_(\d+)/$',views.cart),

]