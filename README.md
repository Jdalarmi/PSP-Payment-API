# PSP-Payment-API
 Versão simplificada de um (PSP) - Payment Service Provider

# Resumo da API

Essa API consite em um versão simplificada de um (PSP).
1. Ela possui serviço de cadastrar uma transação com 
- Valor da transação
- Descrição da transação. Ex: 'Smartband XYZ 3.0'
- Método de pagamento (debit_card ou credit_card)
- Número do cartão
- Nome do portador do cartão
- Data de validade do cartão
- Código de verificação do cartão (CVV)

Aqui entra ponto importante numero de cartão é uma informação sensivel então séra armazenado apenas os 4 ultimos digitos e o restante como "*"

2. O proximo serviço lista todas transações já criadas.

3. O ultimo serviço faz consulta na base de dados das transações e analisa qual metodo de pagamento foi utilizado, debito ou credito e retorna:
Saldo disponivel e Saldo a receber de acordo com a conta que foi realizado em cima do valor de cada transação descontanto taxa de 3% para débito e 5% para crédito.

# Acessando deploy da API:

Caso queira acessar a API, abaixo você encontra endereço do deploy da API documentada com swagger:
[https://jefersondalarmi.pythonanywhere.com/swagger/]

