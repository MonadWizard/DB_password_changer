from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import config
import os


from . change_pass import password_change_config, password_change_db, password_change_config2

class transper_password(APIView):

    def get(self,request):
        data = "you have to change password"
        print("get request data")
        return Response(data, status=status.HTTP_200_OK)

    def post(self,request):
        new_password = str(request.data["password"])
        password_change_config(new_password)
        try:
            password_change_db(new_password)
        except Exception as e:
            return Response(new_password,status=status.HTTP_401_UNAUTHORIZED)

        # password_change_config2(os.environ.get('DB_PASSWORD2'))

        return Response(new_password,status=status.HTTP_201_CREATED)
        