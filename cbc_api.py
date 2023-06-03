import requests


class CBCApi:
    def __init__(self, token):
        self.token = token
        self.headers = {
            'X-CC-Version': '2018-03-22',
            'Accept': 'application/json',
            'X-CC-Api-Key': token
        }

    def charge_list(self):
        response = requests.get('https://api.commerce.coinbase.com/charges', headers=self.headers).json()
        return response

    def create_charge(self, name, description=None, pricing_type='no_price', amount=None, currency='USD'):
        data = {'name': name, 'pricing_type': pricing_type}
        if description is not None:
            data['description'] = {'description': description}
        if pricing_type == 'fixed_price':
            if amount is None:
                raise ValueError("Amount is required for fixed pricing")
            data['local_price'] = {
                'amount': str(amount),
                'currency': currency
            }
        response = requests.post('https://api.commerce.coinbase.com/charges', headers=self.headers, json=data).json()
        return response

    def charge_show(self, charge_code):
        response = requests.get(f'https://api.commerce.coinbase.com/charges/{charge_code}', headers=self.headers).json()
        return response

    def charge_cancel(self, charge_code):
        response = requests.post(f'https://api.commerce.coinbase.com/charges/{charge_code}/cancel', headers=self.headers).json()
        return response

    def charge_resolve(self, charge_code):
        response = requests.get(f'https://api.commerce.coinbase.com/charges/{charge_code}/resolve', headers=self.headers).json()
        return response

    def checkouts_list(self):
        response = requests.get('https://api.commerce.coinbase.com/checkouts', headers=self.headers).json()
        return response

    def checkouts_create(self, name, description, requested_info, pricing_type='no_price', amount=None, currency='USD'):
        data = {'name': name,
                'description': description,
                'requested_info': requested_info,
                'pricing_type': pricing_type}
        if pricing_type == 'fixed_price':
            if amount is None:
                raise ValueError("Amount is required for fixed pricing")
            data['local_price'] = {
                'amount': str(amount),
                'currency': currency
            }
        response = requests.post('https://api.commerce.coinbase.com/checkouts', headers=self.headers, json=data).json()
        return response

    def checkouts_show(self, checkout_id):
        response = requests.get(f'https://api.commerce.coinbase.com/checkouts/{checkout_id}', headers=self.headers).json()
        return response

    def checkouts_update(self, checkout_id, name, description, requested_info, pricing_type='no_price', amount=None, currency='USD'):
        data = {'name': name, 'description': description, 'requested_info': requested_info, 'pricing_type': pricing_type}
        if pricing_type == 'fixed_price':
            if amount is None:
                raise ValueError("Amount is required for fixed pricing")
            data['local_price'] = {
                'amount': str(amount),
                'currency': currency
            }
        response = requests.put(f'https://api.commerce.coinbase.com/checkouts/{checkout_id}', headers=self.headers, json=data).json()
        return response

    def checkouts_delete(self, checkout_id):
        response = requests.delete(f'https://api.commerce.coinbase.com/checkouts/{checkout_id}', headers=self.headers).json()
        return response

    def invoice_list(self):
        response = requests.get('https://api.commerce.coinbase.com/invoices', headers=self.headers).json()
        return response

    def invoice_create(self, business_name, customer_email, customer_name, memo, amount, currency='USD'):
        invoice_data = {'business_name': business_name,
                        'customer_email': customer_email,
                        'customer_name': customer_name,
                        'memo': memo,
                        'local_price': {'amount': str(amount), 'currency': str(currency)}}
        response = requests.post('https://api.commerce.coinbase.com/invoices', headers=self.headers, json=invoice_data).json()
        return response

    def invoice_show(self, invoice_id):
        response = requests.get(f'https://api.commerce.coinbase.com/invoices/{invoice_id}', headers=self.headers).json()
        return response

    def invoice_void(self, invoice_id):
        response = requests.put(f'https://api.commerce.coinbase.com/invoices/{invoice_id}/void', headers=self.headers).json()
        return response

    def invoice_resolve(self, invoice_id):
        response = requests.put(f'https://api.commerce.coinbase.com/invoices/{invoice_id}/resolve', headers=self.headers).json()
        return response

    def events_list(self):
        response = requests.get('https://api.commerce.coinbase.com/events', headers=self.headers).json()
        return response

    def event_show(self, event_id):
        response = requests.get(f'https://api.commerce.coinbase.com/events/{event_id}', headers=self.headers).json()
        return response
