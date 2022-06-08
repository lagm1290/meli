from rest_framework import routers
from django.urls import path
from apps.adn.api.views.check_secuence import CheckSequence
from apps.adn.api.views.get_statistics import Statistics


router_apirest = [
    path(r'mutant/', CheckSequence.as_view(), name='mutant'),
    path(r'stats/', Statistics.as_view(), name='stats'),
]


api_urls = router_apirest