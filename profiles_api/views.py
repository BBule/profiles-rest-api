from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from  profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializers

    def get(self, request, format=None):
        """"Returns a list of APIView features"""

        an_apiview = [
        'Uses HTTP Methods as function(get,post, patch, delete)',
        'Its similar to a traditional Django View',
        'Gives you the most control over your application logic',
        'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})


    def post(self, request):
        """Create a Hello Request with the name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_404_NOT_FOUND
            )

        return Response({'message':message})

    def put(self, request, pk=None):
        """Handles updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """"Handles a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Handles deleting an object"""
        return Response({'method':'DELETE'})
