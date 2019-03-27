from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from .models import Account

class AccountView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [account.username for account in Account.objects.all()]
        return Response(usernames)


    def post(self, request):
        """
        Saves the user accounts.
        :param request:
        :return:
        """
        try:
            user_accounts = request.data
            print user_accounts
            for user_account in user_accounts:
                hostname = user_account.get('hostname')
                username = user_account.get('username')
                password = user_account.get('password')
                account = Account(host_name=hostname, username=username, password=password)
                account.save()
            return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
