from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from applications.testing.models import Testing
from applications.testing.serializers import TestingSerializer


class TestingViewSet(viewsets.ModelViewSet):
    queryset = Testing.objects.all()
    serializer_class = TestingSerializer
    permission_classes = [IsAuthenticated, ]


    # def get_permissions(self):
    #     if self.action in ['list', 'retrieve']:
    #         permissions = ''
    #     elif self.action == 'like':
    #         permissions = [IsAuthenticated, ]
    #     else:
    #         permissions = [IsReviewAuthor, ]
    #     return [permission() for permission in permissions]
    #
    # @action(detail=True, methods=['POST'])
    # def like(self, request, *args, **kwargs):
    #     flag = self.get_object()
    #     like_obj, _ = Like.objects.get_or_create(flag=flag, user = request.user)
    #     like_obj.like = not like_obj.like
    #     like_obj.save()
    #     status = 'liked'
    #     if not like_obj.like:
    #         status = 'unliked'
    #     return Response({'status': status})