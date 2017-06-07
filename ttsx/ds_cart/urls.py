from django.conf.urls import url
import views

urlpatterns=[
    url(r'^add(\d+)_(\d+)/$',views.add),
    url(r'^list/$',views.list),
    url(r'^alter_count/$',views.alter_count),
    url(r'^delete/$',views.delete)

]