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

        print('start')
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
            return JsonResponse({'errorMessage':'there is no ' + str(e) + ' key'}, status = 400)

        except IntegrityError as e:
            return JsonResponse({'errorMessage': str(e)}, status = 400)

        except ValidationError as e:
            return JsonResponse({'errorMessage': str(e)}, status = 400)

        except Exception as exception:
            return JsonResponse({'errorMessage': str(exception)}, status = 500)
