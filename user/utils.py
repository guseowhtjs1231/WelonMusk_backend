import jwt

from django.http        import JsonResponse,HttpResponse

from welonmusk.settings import SECRET_KEY
from user.models        import Users

def login_required(func):
    secret = SECRET_KEY
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = jwt.decode(request.headers['Authorization'], secret, algorithm = 'HS256')
            print("access_token=",end=""),print(access_token)

            user_id = access_token['id']
            request.user = Users.objects.get(id = user_id)
            return func(self, request, *args, **kwargs)
        except jwt.DecodeError:
            return JsonResponse({'Message' : 'INVALID_TOKEN'}, status = 400)
        except Users.DoesNotExit:
            return JsonResponse({'Message' : 'INVALID_USER'}, status = 400)
    return wrapper

