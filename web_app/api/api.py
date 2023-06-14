from django.conf import settings
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from googletrans import Translator
import os

# ViewSets define the view behavior.
class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        content_type = file_uploaded.content_type
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)

class html_trasnlator(views.APIView):
    def post(self, request):
        for entry in request.data:
            model_name = entry.pop('model_name')
            path = os.path.join(settings.MODEL_ROOT, model_name)
            try:
                translator = Translator()
                result = os.system("translate -h " + path_file)
                files.append(result[0])

            except Exception as err:
                return Response(str(err), status=status.HTTP_400_BAD_REQUEST)

        return Response(file, status=status.HTTP_200_OK)

class subtitle_video(views.APIView):
    def post(self, request):
        for entry in request.data:
            model_name = entry.pop('model_name')
            path_file = os.path.join(settings.MODEL_ROOT, model_name)
            try:
                result = os.system("autosub " + path_file)
            except Exception as err:
                return Response(str(err), status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_200_OK)

  class subtitle_audio(views.APIView):
    def post(self, request):
        for entry in request.data:
            model_name = entry.pop('model_name')
            path_file = os.path.join(settings.MODEL_ROOT, model_name)
            try:
                result = os.system("autosub " + path_file)
            except Exception as err:
                return Response(str(err), status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_200_OK)
