from django.conf.urls import url
from recycle_app import views
from rest_framework import routers
from .api import ViewSet

# SET THE NAMESPACE!
app_name = 'recycle_app'

urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^user_logout/$',views.user_logout,name='user_logout'),
    url(r'^sell/$',views.sell,name='sell'),
    url(r'^buy/$',views.buy,name='buy'),
    url(r'^about/$',views.about,name='about'),

]

router=routers.DefaultRouter()
router.register('api/user',ViewSet,'recycle_app')

urlpatterns1=router.urls
