from datetime import date

from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import filters, generics, status
from rest_framework.decorators import api_view
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from .models import Case
from .serializers import CaseSerializer


@api_view(["GET", "POST", "DELETE"])
def case_list(request):
    if request.method == "GET":
        cases = Case.objects.all()

        start = request.query_params.get("from")
        if start is None:
            start = date(1, 1, 1)
        end = request.query_params.get("to")
        if end is None:
            end = date(9999, 12, 31)
        cases = Casse.objects.filter(date__gte=start, date__lte=end)

        cases_serializer = CaseSerializer(cases, many=True)
        return JsonResponse(cases_serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        case_serializer = CaseSerializer(data=data)
        if case_serializer.is_valid():
            case_serializer.save()
            return JsonResponse(case_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(case_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        count = Case.objects.all().delete()
        return JsonResponse(
            {"message": "{} Cases were deleted successfully!".format(count[0])},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def case_detail(request, pk):
    case = get_object_or_404(Case, pk=pk)
    if request.method == "PUT" or request.method == "PATCH":
        data = JSONParser().parse(request)
        serializer = CaseSerializer(case, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        case.delete()
        return JsonResponse(
            {"message": "Case was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )
    serializer = CaseSerializer(case)
    return JsonResponse(serializer.data)


class APICase(APIView):
    def get(self, request):
        cases = Case.objects.all()
        start = request.query_params.get("from")
        if start is None:
            start = date(1, 1, 1)
        end = request.query_params.get("to")
        if end is None:
            end = date(9999, 12, 31)
        cases = Case.objects.filter(date__gte=start, date__lte=end)
        cases_serializer = CaseSerializer(cases, many=True)
        return JsonResponse(cases_serializer.data, safe=False)

    def post(self, request):
        data = JSONParser().parse(request)
        case_serializer = CaseSerializer(data=data)
        if case_serializer.is_valid():
            case_serializer.save()
            return JsonResponse(case_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(case_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        count = Case.objects.all().delete()
        return JsonResponse(
            {"message": "{} Cases were deleted successfully!".format(count[0])},
            status=status.HTTP_204_NO_CONTENT,
        )


class APICaseDetail(APIView):
    def get(self, request, pk):
        case = get_object_or_404(Case, pk=pk)
        serializer = CaseSerializer(case)
        return JsonResponse(serializer.data)

    def delete(self, request, pk):
        case = get_object_or_404(Case, pk=pk)
        case.delete()
        return JsonResponse(
            {"message": "Case was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )

    def put(self, request, pk):
        case = get_object_or_404(Case, pk=pk)
        data = JSONParser().parse(request)
        serializer = CaseSerializer(case, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        case = get_object_or_404(Case, pk=pk)
        data = JSONParser().parse(request)
        serializer = CaseSerializer(case, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CaseList(generics.ListCreateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ("date", "views", "clics", "cost", "cpc", "cpm")

    def delete(self, request):
        count = Case.objects.all().delete()
        return JsonResponse(
            {"message": "{} Cases were deleted successfully!".format(count[0])},
            status=status.HTTP_204_NO_CONTENT,
        )


class CaseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer