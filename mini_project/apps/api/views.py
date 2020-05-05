from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import (
ValidationError, PermissionDenied
)
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.api.models import (
Word, Definition
)

from .serializer import (
    WordSerializer, DefinitionSerializer
)


##################################################################################################
#
##################################################################################################

class WordViewSet(viewsets.ModelViewSet):
    #permissions comes into play here
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Word.objects.all().filter(owner = self.request.user)
        # take this request and filter objects only in user
        #we are getting all this way bc of authntification
        #list categories per current logedin in user
        return queryset
    #now serialize it
    serializer_class = WordSerializer

    def create(self, request, *args, **kwargs):
        word = Word.objects.filter(
            name = request.data.get('name'),
            owner = request.user
        )
        # if word exists says this message
        if word:
            msg = 'Category with that name already exists'
            raise ValidationError(msg)
        return super().create(request)

    def destroy(self, request, *args, **kwargs):
        word = Word.objects.get(pk= self.kwargs["pk"])
        #if this user isnt the owner you cant delte it
        if not request.user == word.owner:
            raise PermissionDenied("you cannot delete this word")
        return super().destroy(request, *args, **kwargs)


    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)
##################################################################################################
#
##################################################################################################

class WordsDefinitions(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated)
    #this is to check if you are authenticted
    #if you are create a word and
    def get_queryset(self):
        if self.kwargs.get("word_pk"):
            word = Word.objects.get(pk=self.kwargs["word_pk"])
            queryset = Definition.objects.filter(
                owner=self.request.user,
                word = word
            )
        return queryset

    serializer_class = DefinitionSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

###################################################################################################
#
##################################################################################################

class SingleWordDef(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        if self.kwargs.get("word") and self.kwargs.get("pk"):
            word = Word.objects.get(pk=self.kwargs["word_pk"])
            queryset = Definition.objects.filter(
                pk=self.kwargs["pk"],
                owner=self.request.user,
                word=word
            )
        return queryset
    serializer_class = DefinitionSerializer

##################################################################################################
#
##################################################################################################
class DefinitionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        queryset = Definition.objects.all().filter(owner=self.request.user)
        return queryset
    serializer_class =  DefinitionSerializer

    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            raise PermissionDenied(
                "only logged in users with accounts can create recipes"
            )
        return super().create(request, *args, **kwargs)

    def destory(self, request, *args, **kwargs):
        #in defnintion get me all the objects where the pk = what you looking for
            definition = Definition.objects.get(pk=self.kwargs["pk"])
        #if you ar not the user you cant do this. you do not own this
            if not request.user == definition.owner:
                raise PermissionDenied("You cannot delete this recipe")
        #return the parent function destroy with the request the argumetn and the kword argument
            return super().destroy(request, *args, *kwargs)

    def update(self, request, *args, **kwargs):

        # still not too sure what this line is doing
        # call this recipe in the objects has this primarary key that was passed in
        definition = Definition.objects.get(pk=self.kwargs["pk"])

        #if the user does not match the definition owner
        if not request.user == definition.owner:

        #tell them this
            raise PermissionDenied("You cannot change this Recipe")

        #otherwise call the parents function update and the arguments
        # will be the request, args? and karg? are kwargs the authentification token?
        return super().update(request, *args, **kwargs)

    def perform_create(self, serializer):
        # save what youve done... are you saving the users acount or the serilizer category
        serializer.save(owner=self.request.user)
