from django.urls import path,include
from django.contrib.auth.models import User
from rest_framework import routers,serializers,viewsets



#serlizers define api represention

class UserSerilizers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =User
        fields=['url','username','first_name','last_name', 'email','is_staff']

#viewsets define the view behavirous

class UserViewsets(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerilizers


#routers provide an easy way of auto determining of url config

router=routers.DefaultRouter()
router.register(r'users',UserViewsets)



urlpatterns=[
    path('',include(router.urls)),
    path('api/auth/',include('rest_framework.urls',namespace='rest_framework')),

]