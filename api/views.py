from api.serializers import PayablesSerializer, TransactionSerializer, UserSerializer
from api.models import Payables, Transaction
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status


'''
@swagger_auto_schema(method='post', request_body=UserSerializer)
@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    username = request.data['username']

    if serializer.is_valid():
        serializer.save()
        return Response(f'Usuario {username} criado com sucesso!!!')
    else:
        return Response(serializer.errors)   
'''
@swagger_auto_schema(method='post', request_body=TransactionSerializer)
@api_view(['POST'])
def register_transaction(request):
    """- Registra novas transações
       - Realiza operações para diferentes métodos de pagamento.
    """
    serializer = TransactionSerializer(data=request.data)
    
    
    
   
    
    if serializer.is_valid():
        card_number = request.data['card_number']
        if len(card_number)!=19:
            return Response({"error":"Cartão invalido"}, status=status.HTTP_400_BAD_REQUEST)
        last_four_digits = request.data['card_number'][-4:]
        masked_card_number = '*' * 15 + last_four_digits
        serializer.validated_data['card_number'] = masked_card_number
        value = request.data['payment_value']
        method = request.data['payment_method']
        

        Transaction.value_return(value=value, method=method)
        serializer.save()
        return Response('Transacao realizada com sucesso!!!', status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='get')
@api_view(['GET'])
def list_transaction(request):
    """ - Lista todas transações efetuadas"""
    transaction = Transaction.objects.all()
    serializer = TransactionSerializer(transaction, many=True)

    return Response(serializer.data)


@swagger_auto_schema(method='get')
@api_view(['GET'])
def funds(request):
    """ - Exibe o total na conta disponivel para usar (oque foi passado no débito), e oque foi passado no crédito a receber no futuro"""
    serializer =  PayablesSerializer(Payables.objects.all(), many=True)
    serializer = serializer.data
    list_debit = []
    list_credit= []
    for objeto in serializer:
        avaliable = (objeto['avaliable_founds'])
        if avaliable != None:
            list_debit.append(avaliable)
        
        waiting = (objeto['waiting_founds'])
        if waiting != None:
            list_credit.append(waiting)

    total_debit = sum(list_debit)
    total_credit = sum(list_credit)
    
    return Response(f'Saldo disponivel: R$:{total_debit} Saldo a receber: R$:{total_credit}')