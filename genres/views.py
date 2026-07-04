#from django.shortcuts import render
#from django.http import JsonResponse
#from django.shortcuts import get_object_or_404
#from django.views.decorators.csrf import csrf_exempt
#import json


from rest_framework import generics
from genres.models import Genre
from genres.serializers import GenreSerializer


'''
# Function based view 
@csrf_exempt
def genre_create_list_view(request):
     if request.method == 'GET':
        genres = Genre.objects.all()
        data = [{'id': genre.id, "name": genre.name} for genre in genres]
        return JsonResponse(data, safe=False)
             
    #List comprehention que faz o mesmo que o código acima
    #data = []
    #for genre in genres:
    #    data.append(
    #        {'id':genre.id, 'name': genre.name}
    #    )

     elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        new_genre = Genre(name = data['name'])
        new_genre.save()
        return JsonResponse(
            {'id': new_genre.id, 'name': new_genre.name},
            status = 201,
        )
'''        


#Reescrevendo a view acima
#Class Based View
class GenreCreateListView(generics.ListCreateAPIView):
    #Queryset com um filtro, direto
    #queryset = Genre.objects.filter(name='Terror')
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

'''
# Function based view
@csrf_exempt     
def genre_detail_view(request, pk):
    #Comentando para usar o get or 404
    # genre = Genre.objects.get(pk = pk)
    genre = get_object_or_404(Genre, pk = pk)
    if request.method == 'GET':
        data = {'id': genre.id, 'name': genre.name}
        return JsonResponse(data)
    
    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data['name']
        genre.save()
        return JsonResponse(
            {'id': genre.id, 'name': genre.name},
            status = 202
        )
    elif request.method == 'DELETE':
        genre.delete()
        return JsonResponse(
            {'message': 'Gênero excluido com sucesso'},
            status = 204,
        )
'''


#Reescrevendo a view acima
#Class Based View
class GenreRetrieveUpdadeDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

   
