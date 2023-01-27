
from django.http import HttpResponse
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.response import Response

import requests
import base64

class OktaErrorView(APIView):
    def get(self,request):
        

        access_token = request.session.get('oidc_access_token')

        ## revoke access_token  - i dnot know if this works, i think works
        # url = "https://dev-45133078.okta.com/oauth2/default/v1/revoke"

        # headers = {
        #     "Accept": "application/json",
        #     "Content-Type": "application/x-www-form-urlencoded",
        #     "Authorization": "Basic" + base64.b64encode(("0oa7ljf5rfqcDlqBO5d7:Rk9BB0QNj-ulHi6nobxIzvjt2rMV3N77LWN7yKyk").encode()).decode()
        # }
        # data = {
        #     "token": access_token,
        #     "token_type_hint": "refresh_token"
        # }
        # res = requests.post(url,data=data,headers=headers)

        ## get user info -- works
        # headers2 = {
        #     "Authorization": "Bearer " + access_token
        # }
        # res2 = requests.get("https://dev-45133078.okta.com/oauth2/default/v1/userinfo",headers=headers2)

        id_token =  str(request.session.get('oidc_id_token'))
        # id_token = str(request.COOKIES['csrftoken'])
        post_logout_redirect_uri = 'http://localhost:8000'
        url = f"https://dev-45133078.okta.com/oauth2/default/v1/logout?id_token_hint=${id_token}&client_id=0oa7ljf5rfqcDlqBO5d7"
        res3 = requests.get(url)
       
        # logout(request)
        # return redirect(res3.text)
        return Response({"res3":res3.text,"session":request.session})



#     headers = {
#     "Accept": "application/json",
#     "Content-Type": "application/json",
#     # "Authorization": f"SSWS {api_token}"
# }
