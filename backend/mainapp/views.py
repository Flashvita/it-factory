from rest_framework.response import Response
from rest_framework import generics, views, status

from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import (
    OpenApiResponse,
    OpenApiParameter,
    OpenApiTypes
)

from .models import Shop
from .serializers import ShopSerializer, VisitSerializer


@extend_schema(
        tags=['Shops'],
        summary='Список торговых точек пользователя',
        parameters=[
            OpenApiParameter(
                'phone_number',
                OpenApiTypes.STR,
                OpenApiParameter.QUERY,
                description="Номер телефона",
                required=True
            )
        ],
        responses={"200": ShopSerializer}
    )
class ShopListApiView(generics.ListAPIView):
    serializer_class = ShopSerializer

    def get_queryset(self):
        return Shop.objects.select_related("worker").filter(
            worker__phone_number=self.request.query_params.get("phone_number")
        )


@extend_schema(
        tags=['Visits'],
        summary='Посетить торговую точку',
        request=VisitSerializer,
        parameters=[
            OpenApiParameter(
                'phone_number',
                OpenApiTypes.STR,
                OpenApiParameter.QUERY,
                description="Номер телефона",
                required=True
            )
        ],
        responses={
            "201": VisitSerializer,
            "400": OpenApiResponse(
                description="Error message"
            ),
        }
    )
class VisitCreateApiView(views.APIView):
    serializer_class = VisitSerializer

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)

            phone_number = self.request.query_params.get("phone_number")
            if serializer.validated_data["shop"].worker.phone_number != phone_number:
                raise Exception("Worker must be working in shop")

            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                {"message": f"{e}"},
                status=status.HTTP_403_FORBIDDEN
            )
