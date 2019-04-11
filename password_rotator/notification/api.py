from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from .models import NotificationModel

class NotificationView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAdminUser,)

    def __init__(self):
        self.shouldChange = False

    def get(self, request, format=None):
        """
        Returns the url or None for which the password needs to be changed.
        """
        # shouldChange = request.session.get('shouldChange')
        shouldChangeObj = (NotificationModel.objects.all())[0]
        shouldChange = shouldChangeObj.shouldChange
        if shouldChange:
            shouldChangeObj.shouldChange = False
            shouldChangeObj.save()
        print shouldChange
        return Response("www.amazon.in" if shouldChange else "None")
        # return Response("www.amazon.in")

    def post(self, request):
        """
        Saves the user accounts.
        :param request:
        :return:
        """
        try:
            # self.shouldChange = True
            # request.session['shouldChange'] = True
            # print request.session['shouldChange']
            shouldChangeObj = (NotificationModel.objects.all())[0]
            shouldChangeObj.shouldChange = True
            shouldChangeObj.save()

            return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
