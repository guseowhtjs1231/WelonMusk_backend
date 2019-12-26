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

class UserView(View):
    def post(self, request):

        data = json.loads(request.body)
        try:
            validate_email(data['email'])

            if len(data['password']) < 8:
                return JsonResponse({'errorMessage':'SHORT_PASSWORD'}, status = 400)
            elif not any(c.isupper() for c in data['password']):
                return JsonResponse({'errorMessage':'NO_CAPITAL_LETTER_PASSWORD'}, status = 400)

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
