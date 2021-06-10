from .models import Article
from .serializers import ArticleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render,HttpResponse
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated



def home(request):
    #return HttpResponse("This is a home page")
    articles = Article.objects.all()
    #print(articles)
    serializer = ArticleSerializer(articles, many=True)
    #return Response(serializer.data)
    data=serializer.data
    return render(request, 'welcome.html', {'d': data})
    #return render(request,"welcome.html")

def entry(request):
        if request.method=='POST':
            title=request.POST.get('title_book')
            author=request.POST.get('author_book')
            rating=request.POST.get('rating_book')
            book=Article(title=title, author=author,rating=rating)
            book.save()
        return render(request,"entry.html")


def get_score(request):
    Rating=5
    if request.method=='POST':
        title=request.POST.get('book_name')
        print(title)
        obj=Article.objects.all().filter(title=title)
        print(obj)
        for query in obj:
            Rating =query.rating
            #print('inside for loop')
        print(Rating)
            

    return render(request,"get_score.html",{'rating': Rating})
 
class ArticleAPIView(APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    #authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticated]

 
    def get(self, request):
        articles = Article.objects.all()
        print(articles)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
 
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 
 
class ArticleDetails(APIView):
 
    def get_object(self, id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
 
 
    def get(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
 
 
 
    def put(self, request,id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)