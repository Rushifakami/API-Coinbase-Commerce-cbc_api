import requests

API_URL = 'https://api.commerce.coinbase.com'


class CBCApi:
    def __init__(self, token: str):
        self.token = token
        self.headers = {
            'X-CC-Version': '2018-03-22',
            'Accept': 'application/json',
            'X-CC-Api-Key': self.token
        }

    def charge_list(self):
        response = requests.get(f'{API_URL}/charges', headers=self.headers).json()
        return response

    def create_charge(
            self,
            name: str,
            description: str = None,
            pricing_type: str = 'no_price',
            amount: float = None,
            currency: str = 'USD',
            customer_id: str = None,
            customer_name: str = None
    ):
        data = {
            'name': name,
            'pricing_type': pricing_type
        }

        if description is not None:
            data['description'] = description

        if pricing_type == 'fixed_price':
            if amount is None:
                raise ValueError("Amount is required for fixed pricing")
            data['local_price'] = {
                'amount': amount,
                'currency': currency
            }

        if customer_id is not None:
            data['metadata'] = {
                'customer_id': customer_id
            }

        if customer_name is not None:
            if customer_id is not None:
                data['metadata'] = {
                    'customer_id': customer_id,
                    'customer_name': customer_name
                }
            else:
                data['metadata'] = {
                    'customer_name': customer_name
                }

        response = requests.post(f'{API_URL}/charges', headers=self.headers, json=data).json()
        return response

    def charge_show(self, charge_code: str):
        response = requests.get(f'{API_URL}/charges/{charge_code}', headers=self.headers).json()
        return response

    def charge_cancel(self, charge_code: str):
        response = requests.post(f'{API_URL}/charges/{charge_code}/cancel', headers=self.headers).json()
        return response

    def charge_resolve(self, charge_code: str):
        response = requests.post(f'{API_URL}/charges/{charge_code}/resolve', headers=self.headers).json()
        return response

    def checkouts_list(self):
        response = requests.get(f'{API_URL}/checkouts', headers=self.headers).json()
        return response

    def checkouts_create(
            self,
            name: str,
            description: str,
            requested_info: list,
            pricing_type: str = 'no_price',
            amount: float = None,
            currency: str = 'USD'
    ):
        data = {
            'name': name,
            'description': description,
            'requested_info': requested_info,
            'pricing_type': pricing_type
        }

        if pricing_type == 'fixed_price':
            if amount is None:
                raise ValueError("Amount is required for fixed pricing")

            data['local_price'] = {
                'amount': amount,
                'currency': currency
            }

        response = requests.post(f'{API_URL}/checkouts', headers=self.headers, json=data).json()
        return response

    def checkouts_show(self, checkout_id: str):
        response = requests.get(f'{API_URL}/checkouts/{checkout_id}', headers=self.headers).json()
        return response

    def checkouts_update(
            self,
            checkout_id: str,
            name: str = None,
            description: str = None,
            requested_info: list = None,
            amount: float = None,
            currency: str = 'USD'
    ):
        data = {}

        if name:
            data['name'] = name

        if description:
            data['description'] = description

        if requested_info:
            data['requested_info'] = requested_info

        if amount:
            data['local_price'] = {
                'amount': amount,
                'currency': currency
            }

        response = requests.put(f'{API_URL}/checkouts/{checkout_id}', headers=self.headers, json=data).json()
        return response

    def checkouts_delete(self, checkout_id: str):
        response = requests.delete(f'{API_URL}/checkouts/{checkout_id}', headers=self.headers).json()
        return response

    def invoice_list(self):
        response = requests.get(f'{API_URL}/invoices', headers=self.headers).json()
        return response

    def invoice_create(
            self,
            business_name: str,
            customer_email: str,
            customer_name: str,
            memo: str,
            amount: float,
            currency: str = 'USD'
    ):
        invoice_data = {
            'business_name': business_name,
            'customer_email': customer_email,
            'customer_name': customer_name,
            'memo': memo,
            'local_price':
                {
                    'amount': amount,
                    'currency': currency
                }
        }
        response = requests.post(f'{API_URL}/invoices', headers=self.headers, json=invoice_data).json()
        return response

    def invoice_show(self, invoice_id: str):
        response = requests.get(f'{API_URL}/invoices/{invoice_id}', headers=self.headers).json()
        return response

    def invoice_void(self, invoice_id: str):
        response = requests.put(f'{API_URL}/invoices/{invoice_id}/void', headers=self.headers).json()
        return response

    def invoice_resolve(self, invoice_id: str):
        response = requests.put(f'{API_URL}/invoices/{invoice_id}/resolve', headers=self.headers).json()
        return response

    def events_list(self):
        response = requests.get(F'{API_URL}/events', headers=self.headers).json()
        return response

    def event_show(self, event_id: str):
        response = requests.get(f'{API_URL}/events/{event_id}', headers=self.headers).json()
        return response
