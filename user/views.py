import json
import jwt
import bcrypt

from django.views import View
from django.http  import JsonResponse
from django.db    import IntegrityError
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from .models      import Users
from welonmusk.settings import SECRET_KEY

class SignUpView(View):
    def post(self, request):

        data = json.loads(request.body)
        try:
            validate_email(data['email'])
            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt() )

            Users(
                first_name = data['first_name'],
                last_name = data['last_name'],
                email    = data['email'],
                password = hashed_password.decode('utf-8')
            ).save()

            return JsonResponse({'message':'SUCCESS'}, status = 200)
        except KeyError as e:
            return JsonResponse({'errorMessage':'MISSING_KEY'}, status = 400)

        except IntegrityError as e:
            return JsonResponse({'errorMessage': 'DUPLICATED_EMAIL'}, status = 400)

        except ValidationError as e:
            return JsonResponse({'errorMessage': 'INVALID_EMAIL'}, status = 400)

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            validate_email(data['email'])
            user = Users.objects.get(email = data['email'])
            if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                access_token = jwt.encode({'id': user.id}, SECRET_KEY, algorithm='HS256')
                return JsonResponse({'access_token': access_token.decode('utf-8')}, status=200)
            else:
                return JsonResponse({'message':'WRONG_PASSWORD'}, status = 400)

        except KeyError:
            return JsonResponse({'errorMessage':'MISSING_KEY'}, status = 400)

        except JWTError:
            return JsonResponse({'errorMessage':'JWT_ERROR'}, status = 400)

        except ValidationError:
            return JsonResponse({'errorMessage': 'INVALID_EMAIL'}, status = 400)
