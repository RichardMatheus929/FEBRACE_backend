from django.shortcuts import render

from rest_framework.views import Response,APIView

from .models import Projeto

# Create your views here.

class InfoProject(APIView):
    def get(self,request,id_project):

        escola = Projeto.objects.filter(id=id_project).first().escola
        name = Projeto.objects.filter(id=id_project).first().nome

        quantidade_projetos = Projeto.objects.filter(nome__icontains=name).count()
        categorias_premiacoes = Projeto.objects.filter(nome__icontains=name).values_list('categoria_premiacao', flat=True)
        categorias_premiacoes = list(categorias_premiacoes)

        info = {
            'escola':escola,
            'premios':quantidade_projetos,
            'categorias':categorias_premiacoes
            }

        return Response ({'info':str(info)})
