from api.serializers import TransactionSerializer, PayablesSerializer
from api.models import Transaction, Payables
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status


funds_value  = 150

@swagger_auto_schema(method='post', request_body=TransactionSerializer)
@api_view(['POST'])
def register_transaction(request):
    '''
        CADA COMPRA LEVA EM CONSIDERAÇÃO QUE VOCÊ TEM R$:150,00 DISPONIVEL DE SALDO.
        SE VOCÊ PASSAR DESSE VALOR A API BLOQUEIA AS TRANSAÇÕES!
    '''
    serializer = TransactionSerializer(data=request.data)
    value = request.data['payment_value']
    method = request.data['payment_method']
    card_number = request.data['card_number']
    
    global funds_value

    if not sufficient_balance(value):
        return Response({'error': 'Saldo insuficiente'}, status=status.HTTP_400_BAD_REQUEST)

    last_four_digits = card_number[-4:]
    masked_card_number = '*' * 15 + last_four_digits
    request.data['card_number'] = masked_card_number

    if serializer.is_valid():
        funds_value -= value
        Transaction.value_return(value=value, method=method)
        serializer.save()
        return Response(f'Transação realizada com sucesso!!!OBS:SEU SALDO É DE SOMENTE R$:{funds_value}')
    else:
        return Response(serializer.errors)

def sufficient_balance(payment_value):
    global funds_value
    return funds_value >= payment_value



@swagger_auto_schema(method='get')
@api_view(['GET'])
def list_transaction(request):
    transaction = Transaction.objects.all()
    serializer = TransactionSerializer(transaction, many=True)

    return Response(serializer.data)


@swagger_auto_schema(method='get')
@api_view(['GET'])
def funds(request):
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
