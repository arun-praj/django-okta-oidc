from mozilla_django_oidc.auth import OIDCAuthenticationBackend
from django.contrib.auth.models import User

def provider_logout(request): 
    token = str(request.session.get('oidc_id_token'))
    redirect_url = f'https://dev-45133078.okta.com/oauth2/default/v1/logout?id_token_hint={token}&client_id=0oa7ljf5rfqcDlqBO5d7'
    return redirect_url

class MyOIDCAB(OIDCAuthenticationBackend):

 
    def filter_users_by_claims(self, claims):
        username = claims.get('preferred_username')
        if not username:
            return self.UserModel.objects.none()

        try:
            profile = User.objects.get(username=username)
            return [profile]

        except User.DoesNotExist:
            return self.UserModel.objects.none()
