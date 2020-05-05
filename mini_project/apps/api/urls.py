from django.conf.urls import url
from rest_framework.routers import DefaultRouter
#i need to go over views again

#import all the classes from views
from .views import (
    WordViewSet,WordsDefinitions, SingleWordDef, DefinitionViewSet
)

router = DefaultRouter()
router.register('words', WordViewSet, basename= 'words')
router.register('definitions', DefinitionViewSet, basename= 'definitions')

custom_urlpatterns=[
    url(r'words/(?P<category_pk>\d+)definitions', WordsDefinitions.as_view(), name='word_definitions'),
    url(r'words/(?P<category_pk>\d+)definitions(?P<pk>\d+)$', SingleWordDef.as_view(), name='single_word_definition')
]
#now need to tell comp how to use url patterns
urlpatterns = router.urls
urlpatterns += custom_urlpatterns

##python manage.py makemigrations
#python manage.py migrate
#python manage.py runserver