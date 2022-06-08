from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count,Q
from rest_framework import status
from apps.adn.models import DnaVerified


class Statistics(APIView):
    def get(self, request):
        queryset = DnaVerified.objects.all().aggregate(
            count_mutant_dna = Count('is_mutant', filter=Q(is_mutant=True)),
            count_human_dna = Count('is_mutant', filter=Q(is_mutant=False)),
            ratio=(1 / Count('is_mutant', filter=Q(is_mutant=True))/Count('is_mutant', filter=Q(is_mutant=False)))
        )
        return Response(queryset,status.HTTP_200_OK)


