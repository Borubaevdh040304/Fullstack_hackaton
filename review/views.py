from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action, api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotAcceptable, NotAuthenticated
from drf_yasg.utils import swagger_auto_schema


from .serializers import PostCommentsSerializer, RestourantCommentSerializer, RatingRestourantSerializer
from .models import PostComments, RestourantComments, RatingRestourant #, RestourantFavorites, PostFavorites
# from main.models import Post, Restaurant

from main.permissions import IsAuthorOrReadOnly


User = get_user_model()


class PostCommentsViewSet(ModelViewSet):
    queryset = PostComments.objects.all()
    serializer_class = PostCommentsSerializer
    permission_classes = [IsAuthorOrReadOnly]
    

class RestourantCommentsViewSet(ModelViewSet):
    queryset = RestourantComments.objects.all()
    serializer_class = RestourantCommentSerializer
    permission_classes = [IsAuthorOrReadOnly]


class CreateRatingAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=RatingRestourantSerializer())
    def post(self, request):
        user = request.user
        ser = RatingRestourantSerializer(data=request.data, context={"request":request})
        ser.is_valid(raise_exception=True)
        rest_id = request.data.get("restourant")
        if RatingRestourant.objects.filter(author=user, lesson__id=rest_id).exists():
            raiting = RatingRestourant.objects.get(author=user, lesson__id=rest_id) 
            raiting.value = request.data.get("value")
            raiting.save()
        else:
            ser.save()
        return Response(status=201)



 
# @api_view(['POST'])
# def favourite_rest(request):
#     user_id = request.data.get('user')
#     rest_id =request.data.get('rest')
#     user = get_object_or_404(User, id = user_id)
#     rest = get_object_or_404(Restaurant, id = rest_id)

#     if RestourantFavorites.objects.filter(rest=rest, user=user).exists():
#         RestourantFavorites.objects.filter(rest=rest,user=user).delete()
#     else:
#         RestourantFavorites.objects.create(rest=rest,user=user)
#     return Response(status=201)


# @api_view(['POST'])
# def favourite_post(request):
#     user_id = request.data.get('user')
#     post_id =request.data.get('post')
#     user = get_object_or_404(User, id = user_id)
#     post = get_object_or_404(Post, id = post_id)

#     if PostFavorites.objects.filter(post=post, user=user).exists():
#         PostFavorites.objects.filter(post=post,user=user).delete()
#     else:
#         PostFavorites.objects.create(post=post,user=user)
#     return Response(status=201)