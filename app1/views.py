from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import PrimeNumber
from .serializers import PrimeSerializer
from rest_framework import viewsets

# Create your views here.

# def prime_number():

#     in1 = int(input("Enter start range: "))  
    

#     output = []  
    
      
#     if in1 >= 0:
        
#         in2 = int(input("Enter end range: "))
#         for i in range(in1,in2 + 1):  
#             for j in range(2,i):  
#                 if (i % j) == 0:
#                     break  
#             else:
#                 output.append(i)
#         if output[0]==1 or output[1]==1 :
#             output.remove(1)
#             if output[0]==0:
#                 output.remove(0)
        
#         print(output)

class PrimeView(CreateAPIView):
    queryset = PrimeNumber.objects.all()
    serializer_class = PrimeSerializer

    # def post(self, request, *args, **kwargs):
    #     self.in1 = request.get('in1')
    #     print("=================================".self.in1)
    #     self.in2 = request.get('in2')
    #     if self.in1 >= 0:
    #         for i in range(self.in1,self.in2 + 1):  
    #             for j in range(2,i):  
    #                 if (i % j) == 0:
    #                     break  
    #             else:
    #                 self.out.append(i)
    #         if self.out[0]==1 or self.out[1]==1 :
    #             self.out.remove(1)
    #             if self.out[0]==0:
    #                self.out.remove(0)
            
    #     return super().post(request, *args, **kwargs)
