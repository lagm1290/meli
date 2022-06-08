import numpy as np
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from apps.adn.api.services.find_secuence import FindSequence
from apps.adn.api.services.manage_array import ManageArray
from apps.adn.models import DnaVerified


class CheckSequence(APIView):
    def post(self, request, *args, **kwargs):
        get_dna = self.request.data.get('dna', None)
        is_mutante = False

        """ is validated if the criteria are met  """
        if self.validate(get_dna):
            new_array = ManageArray.create(get_dna)
            rows, columns = new_array.shape

            count = 0

            for i in range(rows - 1):
                for x in range(columns - 1):
                    find_sequence = FindSequence(array=new_array,
                                                 rows=rows,
                                                 columns=columns,
                                                 row=i,
                                                 column=x)
                    if find_sequence.vertical():
                        count += 1
                    if find_sequence.horizontal():
                        count += 1
                    if find_sequence.obliquo():
                        count += 1

                    if count > 1:
                        is_mutante = True
                        break

        DnaVerified.objects.create(
            dna=get_dna,
            is_mutant=is_mutante
        )

        status_response = status.HTTP_200_OK if is_mutante else status.HTTP_403_FORBIDDEN
        response = 'Es Mutante' if is_mutante else 'No Es Mutante'

        return Response(response, status_response)

    @staticmethod
    def validate(dna):
        reference = {'A', 'T', 'C', 'G'}

        """ check exist dna"""
        if not dna:
            raise ValidationError(
                detail={
                    "error": "DNA is required"
                }
            )
        """ check if a list"""
        if not isinstance(dna, list):
            raise ValidationError(
                detail={
                    "error": "DNA should be an array"
                }
            )

        """ check if the list size is greater than 1 """
        if len(dna) < 2:
            raise ValidationError(
                detail={
                    "error": "DNA the list must have a minimum size of 2"
                }
            )

        """ check dna if it complies with the reference """
        for row in dna:
            new_set = set(map(str, row.upper()))
            if new_set.difference(reference):
                raise ValidationError(
                    detail={
                        "error": "DNA does not comply with the reference A,T,C,G"
                    }
                )

        return True
