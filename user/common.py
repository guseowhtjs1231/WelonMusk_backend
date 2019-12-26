from django.views import View

class Common(View):
    
    def checkPassword(self, password):
        
        if len(password) < 8:
            return 'SHORT_PASSWORD'

        if not any(c.isupper() for c in password):
            return 'NO_CAPITAL_LETTER_PASSWORD'

        return None
