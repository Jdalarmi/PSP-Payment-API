from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
class AccountTests(APITestCase):
    def test_register_transaction(self):
        """
        Esse teste tenta registrar uma transação
        """
        url = reverse('register_transaction')
        data = {
                    "card_number": "2222-2222-2222-2222",
                    "payment_value": 1200,
                    "description_transaction": "academy",
                    "payment_method": "D",
                    "customer_name": "Alcione",
                    "expiration_date": "2023-11-26",
                    "cvv": 123
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_register_transaction_payment_value_null(self):
        """
        Esse teste tenta registrar uma transação
        """
        url = reverse('register_transaction')
        data = {
                    "card_number": "9122-2222-2222-2222",
                    "description_transaction": "academy",
                    "payment_method": "D",
                    "customer_name": "Alcione",
                    "expiration_date": "2023-11-26",
                    "cvv": 123
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_register_transaction_card_number_larger_than_max_length(self):
        """
        Esse teste tenta registrar uma transação
        """
        url = reverse('register_transaction')
        data = {
                    "card_number": "2222222-222222-222222-222222",
                    "description_transaction": "academy",
                    "payment_method": "D",
                    "customer_name": "Alcione",
                    "expiration_date": "2023-11-26",
                    "cvv": 123
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_register_transaction_card_number_not_exists(self):
        """
        Esse teste tenta registrar uma transação
        """
        url = reverse('register_transaction')
        data = {
                    "description_transaction": "academy",
                    "payment_method": "D",
                    "customer_name": "Alcione",
                    "expiration_date": "2023-11-26",
                    "cvv": 123
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_register_transaction_description_transaction_not_exists(self):
        """
        Esse teste tenta registrar uma transação
        """
        url = reverse('register_transaction')
        data = {
                    "description_transaction": "academy",
                    "payment_method": "D",
                    "customer_name": "Alcione",
                    "expiration_date": "2023-11-26",
                    "cvv": 123
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    
    def test_register_transaction_card_number_with_letters(self):
        """
        Esse teste tenta registrar uma transação
        """
        url = reverse('register_transaction')
        data = {
                    "card_number": "2222-2222-2222-aaaa",
                    "payment_value": 1200,
                    "description_transaction": "academy",
                    "payment_method": "D",
                    "customer_name": "Alcione",
                    "expiration_date": "2023-11-26",
                    "cvv": 123
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)    