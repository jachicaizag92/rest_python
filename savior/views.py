from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import PromptSerializer
from .models import Prompt

class PromptViewSet(viewsets.ModelViewSet):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer

    def create(self, request, *args, **kwargs):
        print("Body de la solicitud POST:", request.data.get('prompt'))
        return super().create(request, *args, **kwargs)
    


