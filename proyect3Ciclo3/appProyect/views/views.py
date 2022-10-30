from django.shortcuts import render
from rest_framework import status, views
from rest_framework.response import Response

from appProyect.models import Paciente
from appProyect.models import Medico
from appProyect.models import Persona
from appProyect.models import Familiar

from appProyect.serializer.serializers import PacienteSerializer
from appProyect.serializer.serializers import MedicoSerializer
from appProyect.serializer.serializers import PersonaSerializer
from appProyect.serializer.serializers import FamiliarSerializer


# Create your views here.
class PacienteListView(views.APIView):
    def get(self, *args, **kwargs):
        queryset = Paciente.objects.all()
        serializer = PacienteSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PacienteCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = PacienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        try:
            user = Persona.objects.get(id=request.data["pa_persona"])
            user.rol = "paciente"
            user.save()
        except Persona.DoesNotExist:
            return Response({"detail": "No se pudo cambiar el rol a paciente"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PacienteDeleteView(views.APIView):
    def delete(self, request, *args, **kwargs):
        try:
            Paciente.objects.get(pa_persona=kwargs["pa_persona"]).delete()
            user = Persona.objects.get(id=kwargs["pa_persona"])
            user.rol = ""
            user.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Paciente.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class PacienteSearchView(views.APIView):
    def get(self, request, *args, **kwargs):
        try:
            user = Paciente.objects.get(pa_persona=kwargs["pa_persona"])
            serializer = PacienteSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Persona.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class MedicoListView(views.APIView):
    def get(self, *args, **kwargs):
        queryset = Medico.objects.all()
        serializer = MedicoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PersonaChangeRol(views.APIView):
    def put(self, request, *args, **kwargs):
        try:
            user = Persona.objects.get(id=kwargs["pk"])
            user.rol = request.data["rol"]
            user.save()
            return Response(status=status.HTTP_200_OK)
        except Persona.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class MedicoCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = MedicoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # cambiar rol de persona
        try:
            user = Persona.objects.get(id=request.data["me_persona"])
            user.rol = "medico"
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Persona.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class MedicoDeleteView(views.APIView):
    def delete(self, request, *args, **kwargs):
        try:
            Medico.objects.get(me_persona=kwargs["me_persona"]).delete()
            # quitar rol de persona
            try:
                user = Persona.objects.get(id=kwargs["me_persona"])
                user.rol = "paciente"
                user.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Persona.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except Medico.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class FamiliarListView(views.APIView):
    def get(self, *args, **kwargs):
        queryset = Familiar.objects.all()
        serializer = FamiliarSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PersonaListView(views.APIView):
    def get(self, *args, **kwargs):
        queryset = Persona.objects.all()
        serializer = PersonaSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PersonaSearchView(views.APIView):
    def get(self, request, *args, **kwargs):
        try:
            user = Persona.objects.get(id=kwargs["pk"])
            serializer = PersonaSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Persona.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class PersonaLoginAdminView(views.APIView):
    def post(self, request, *args, **kwargs):
        try:
            persona = Persona.objects.get(
                username=request.data['username'],
                password=request.data['password'],
            )
            serializer = PersonaSerializer(persona)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Persona.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
