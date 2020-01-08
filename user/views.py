import json
import jwt
import bcrypt

from django.views           import View
from django.http            import JsonResponse
from django.http            import HttpResponse
from django.db              import IntegrityError
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from .models                import Users
from welonmusk.settings     import SECRET_KEY

def checkPassword(password):
    if len(password) < 8:
        return 'SHORT_PASSWORD'

    if not any(c.isupper() for c in password):
        return 'NO_CAPITAL_LETTER_PASSWORD'

    return None

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            validate_email(data['email'])
            password_error = checkPassword(data['password'])

            if password_error != None:
                return JsonResponse({'message': password_error}, status = 400)

            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

            Users(
                first_name = data['first_name'],
                last_name = data['last_name'],
                email    = data['email'],
                password = hashed_password.decode('utf-8')
            ).save()

            return HttpResponse(status = 200)

        except KeyError:
            return JsonResponse({'message':'INVALID_KEY'}, status = 400)

        except IntegrityError:
            return JsonResponse({'message': 'DUPLICATED_EMAIL'}, status = 400)

        except ValidationError:
            return JsonResponse({'message': 'INVALID_EMAIL'}, status = 400)

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            user = Users.objects.get(email = data['email'])
            if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                access_token = jwt.encode({'id': user.id}, SECRET_KEY, algorithm='HS256')
                return JsonResponse({'access_token': access_token.decode('utf-8')}, status=200)
            
            return JsonResponse({'message':'WRONG_PASSWORD'}, status = 400)

        except Users.DoesNotExist:
            return JsonResponse({'message':'INVALID_USER'}, status = 400)
        except KeyError:
            return JsonResponse({'message':'INVALID_KEY'}, status = 400)
