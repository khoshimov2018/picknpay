from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from .models import Buyer, Seller, TermsAndCondition, ItemPurchased
from .serializers import BuyerSerializer, SellerSerialiazer, TermsAndConditionSerializer, ItemPurchasedSerializer

# Create your views here

# Authentication password
admin_password = "9054f7aa9305e012b3c2300408c3dfdf390fcddf"

@api_view(['POST', 'GET', 'PUT'])
def buyer(request):
    params = request.query_params 
    if request.method == 'GET':
        if len(params) >= 1:
            phone = params['phone']
            buyer = Buyer.objects.filter(phone=phone)
            if len(buyer) == 0:
                content = { "message": 'User Not Found'}
                return Response(content, status=status.HTTP_404_NOT_FOUND)
            else:
                responseResult = BuyerSerializer(buyer, many=True)
                admin= params['admin']
                password = params['password']
                if admin == admin_password and password == buyer[0].password:
                    return Response({ "buyer" : responseResult.data }, status=status.HTTP_200_OK)
                else:
                    content = { "message": "Unauthorized Access"}
                    Response(content, status=status.HTTP_401_UNAUTHORIZED)
        else:
            content = { "message": 'Missing access parameters'}
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
    elif request.method == 'POST':
        # Adding user to the data base
        if len(params) > 0:
            admin = params['admin']
            if admin == admin_password:
                data = request.data
                Buyer.objects.create(username=data['username'],phone=data['phone'], 
                 password=data['password'], 
                 profilePhoto=data['profilePhoto'],
                 eventAndMarketing=data['eventAndMarketing'],
                 service=data['service'],
                 personDetails=data['personDetails']
                 )
                return Response({ "message" : "Added a buyer", "data": request.data}, status=status.HTTP_200_OK)
            else:
                content = { "message": "UnAuthorized Access"}
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            content = { "message": 'Missing access parameters'}
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
            

@api_view(['POST', 'GET', 'PUT'])
def seller(request):
    params = request.query_params 
    if request.method == 'GET':
        if len(params) >= 1:
            phone = params['phone']
            seller = Seller.objects.filter(phone=phone)
            if len(seller) == 0:
                content = { "message": 'User Not Found'}
                return Response(content, status=status.HTTP_404_NOT_FOUND)
            else:
                responseResult = SellerSerialiazer(seller, many=True)
                admin= params['admin']
                password = params['password']
                if admin == admin_password and password == seller[0].password:
                    return Response({ "seller" : responseResult.data }, status=status.HTTP_200_OK)
                else:
                    content = { "message": "UnAuthorized Access"}
                    Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            content = { "message": 'Missing access parameters'}
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
    elif request.method == 'POST':
        # Adding user to the data base
        if len(params) > 0:
            admin = params['admin']
            if admin == admin_password:
                data = request.data
                Seller.objects.create(username=data['username'],phone=data['phone'], 
                 password=data['password'], 
                 profilePhoto=data['profilePhoto'],
                 eventAndMarketing=data['eventAndMarketing'],
                 service=data['service'],
                 personDetails=data['personDetails']
                 )
                return Response({ "message" : "Added a seller", "data": request.data}, status=status.HTTP_200_OK)
            else:
                content = { "message": "UnAuthorized Access"}
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            content = { "message": 'Missing access parameters'}
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def getTermsAndConditions(request):
    params = request.query_params 
    try: 
        admin = params['admin']
        if admin == admin_password:    
            conditions = TermsAndCondition.objects.all()
            serializer = TermsAndConditionSerializer(conditions, many=True)
            return Response(serializer.data)
        else:
            content = { "message": "UnAuthorized Access"}
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    except:
        content = { "message": 'Missing access parameters'}
        return Response(content, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST', 'GET'])
def getItems(request):
    params = request.query_params 
    if request.method == 'GET':
        try:
            admin = params['admin']
            if admin == admin_password:
                items =   ItemPurchased.objects.all()
                data = []
                for item in items:
                    data.append({ "name": item.name, "price": item.price, "purchasedAt": item.purchasedAt, "seller": item.seller.id, 
                    "buyer": item.buyer.id})
                return Response({ "items": data})
            else:
                content = { "message": "UnAuthorized Access"}
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        except: 
            content = { "message": 'Missing access parameters'}
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
    elif request.method == 'POST': 
        try:
            admin = params['admin']
            data = request.data
            if admin == admin_password:
                buyer = Buyer.objects.get(pk=data['buyer_id'])
                seller = Seller.object.get(pk=data)
                return Response({ "message" : "Added a seller", "data": request.data}, status=status.HTTP_200_OK)
            else:
                content = { "message": "UnAuthorized Access"}
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        except:
            content = { "message": 'Missing access parameters'}
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

