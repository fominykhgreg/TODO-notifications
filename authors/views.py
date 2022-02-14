from django.http import response
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer
from .models import Author, Article, Book, Biography
from rest_framework.views import APIView
from .serializers import AuthorSerializer,BiographySerializer,ArticleSerializer,BookSerializer





class AuthorModelViewSet(ModelViewSet):
   renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
   queryset = Author.objects.all()
   serializer_class = AuthorSerializer



class BiographyViewSet(ModelViewSet):
   
   queryset = Biography.objects.all()
   serializer_class = BiographySerializer


class ArticleViewSet(ModelViewSet):
   
   queryset = Article.objects.all()
   serializer_class = ArticleSerializer


class BookViewSet(ModelViewSet):
  
   queryset = Book.objects.all()
   serializer_class = BookSerializer

class ArticleAPIVIew(APIView):
   renderer_classes = [JSONRenderer]

   def get(self, request, format=None):
       articles = Article.objects.all()
       serializer = ArticleSerializer(articles, many=True)
       return Response(serializer.data)
