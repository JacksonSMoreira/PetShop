from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from reserva.models import Reserva, Petshop
from rest_api.serializers import AgendamentoModelSerializer, PetshopNestedModelSerializer

class AgendamentoModelViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = AgendamentoModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({'message':f'Hello, {request.data.get("name")}'})
    
    return Response({'hello': 'World API'})

class PetshopModelViewSet(ReadOnlyModelViewSet):
    queryset = Petshop.objects.all()
    serializer_class = PetshopNestedModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


'''class AgendamentoFilterSet(FilterSet):

    class Meta:
        model = AgendamentoModelViewSet
        fields = {
            'TURNO_OPCOES': ['iexact'],
            'TAMANHO_OPCOES': ['icontens']
                  
                  }

'''