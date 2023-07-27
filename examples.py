from cbc_api.cbc_api import CBCApi

#Create object with your api_key
cb = CBCApi("YOUR_COINBASE_COMMERCE_API_KEY")

#Create charge using fixed_price
#Parametr "description" optional. There is two parameters for pricing_type it's: 'no_price' and 'fixed_price'. 'no_price' is using to create charge with no specific order amount. Great for donation. 'fixed_price' allows you to specify a static order amount. 'amount' this is directly the amount of the order, used only with fixed_price.
charge = cb.create_charge(name='Test', description='Test description', pricing_type='fixed_price', amount=30)

print(charge)

#You will get json data payment url, address, price, payments, meta, etc..
#Response example:
#{'data': {'addresses': {'polygon': '0xf3426c20d3af59550f9c6ed1560d999e61fe473b', 'pusdc': '0xf3426c20d3af59550f9c6ed1560d999e61fe473b', 'ethereum': '0xf3426c20d3af59550f9c6ed1560d999e61fe473b', 'usdc': '0xf3426c20d3af59550f9c6ed1560d999e61fe473b', 'dai': '0xf3426c20d3af59550f9c6ed1560d999e61fe473b', 'apecoin': '0xf3426c20d3af59550f9c6ed1560d999e61fe473b', 'shibainu': '0xf3426c20d3af59550f9c6ed1560d999e61fe473b', 'tether': '0xf3426c20d3af59550f9c6ed1560d999e61fe473b', 'bitcoincash': 'qpmgkpnmalrjw73fzmgm6qnud8ghxlzm2uyj93d03l', 'litecoin': 'MTXjtdncXoaszvsYSQTY8qDF45E6R87xv8', 'bitcoin': '3Jjm7Sws7YPALwU9BRKWAsJA2iCUd5ymsM'}, 'brand_color': '#000000', 'brand_logo_url': 'https://res.cloudinary.com/commerce/image/upload/<Private>.jpg', 'code': '6DB6<Private>', 'coinbase_managed_merchant': False, 'created_at': '2023-06-03T13:30:30Z', 'exchange_rates': {'ETH-USD': '1902.955', 'BTC-USD': '27168.475', 'LTC-USD': '96.56', 'BCH-USD': '114.91', 'USDC-USD': '1.0', 'DAI-USD': '0.99995', 'APE-USD': '3.128', 'SHIB-USD': '0.000008635', 'USDT-USD': '1.000345', 'PMATIC-USD': '0.9027', 'PUSDC-USD': '1.0'}, 'expires_at': '2023-06-03T14:30:30Z', 'fee_rate': 0.01, 'fees_settled': True, 'hosted_url': 'https://commerce.coinbase.com/charges/6DB<Private>', 'id': '<Private>', 'local_exchange_rates': {'ETH-USD': '1902.955', 'BTC-USD': '27168.475', 'LTC-USD': '96.56', 'BCH-USD': '114.91', 'USDC-USD': '1.0', 'DAI-USD': '0.99995', 'APE-USD': '3.128', 'SHIB-USD': '0.000008635', 'USDT-USD': '1.000345', 'PMATIC-USD': '0.9027', 'PUSDC-USD': '1.0'}, 'logo_url': 'https://res.cloudinary.com/commerce/image/upload/v1650009132/<Private>.jpg', 'metadata': {}, 'name': 'Test', 'offchain_eligible': False, 'organization_name': '<Private>', 'payment_threshold': {'overpayment_absolute_threshold': {'amount': '5.00', 'currency': 'USD'}, 'overpayment_relative_threshold': '0.005', 'underpayment_absolute_threshold': {'amount': '5.00', 'currency': 'USD'}, 'underpayment_relative_threshold': '0.005'}, 'payments': [], 'pricing': {'local': {'amount': '30.00', 'currency': 'USD'}, 'polygon': {'amount': '33.233632000', 'currency': 'PMATIC'}, 'pusdc': {'amount': '30.000000', 'currency': 'PUSDC'}, 'ethereum': {'amount': '0.015765000', 'currency': 'ETH'}, 'usdc': {'amount': '30.000000', 'currency': 'USDC'}, 'dai': {'amount': '30.001500090000000000', 'currency': 'DAI'}, 'apecoin': {'amount': '9.590792838874680307', 'currency': 'APE'}, 'shibainu': {'amount': '3474232.773595830000000000', 'currency': 'SHIB'}, 'tether': {'amount': '29.989654', 'currency': 'USDT'}, 'bitcoincash': {'amount': '0.26107388', 'currency': 'BCH'}, 'litecoin': {'amount': '0.31068766', 'currency': 'LTC'}, 'bitcoin': {'amount': '0.00110422', 'currency': 'BTC'}}, 'pricing_type': 'fixed_price', 'pwcb_only': False, 'resource': 'charge', 'support_email': '<Private>@gmail.com', 'timeline': [{'status': 'NEW', 'time': '2023-06-03T13:30:30Z'}], 'utxo': False}}

#Get payment url
payment_url = charge['data']['hosted_url']

print(payment_url)

#You will get something like: https://commerce.coinbase.com/charges/BX2BDFG3


###########################################################################################################################################
#AIOGRAM + CBC_API EXAMPLE

import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from cbc_api.cbc_api import CBCApi

logging.basicConfig(level=logging.INFO)

# CoinBase Commerce
cb = CBCApi("YOUR_COINBASE_COMMERCE_API_KEY")

bot = Bot('YOUR_BOT_TOKEN')

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)


# Buttons
def buttons(var):
    # Create a reply keyboard markup with a button
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if var == 1:
        btn1 = '👛 Donate'
        markup.add(btn1)
    return markup


# Start command
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # Send a greeting message and display the button
    await bot.send_message(message.chat.id, "Hello!", reply_markup=buttons(1))


# Text handler
@dp.message_handler(content_types=['text'])
async def text(message: types.Message):
    if message.text == '👛 Donate':
        # Create a charge using CoinBase Commerce API
        async def charge():
            donate = cb.create_charge('Donate me', currency='EUR')
            url = donate['data']['hosted_url']
            return url

        # Await the charge function to get the donation URL
        url = await charge()
        await bot.send_message(message.chat.id, f'Donate URL: {url}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
