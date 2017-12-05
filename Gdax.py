import gdax
import time

public_client = gdax.PublicClient();

print('\tList of products: \n')
print(public_client.get_products())

print('\n\tProduct BTC-EUR \n')
print(public_client.get_product_order_book('BTC-EUR'))

print('\n\tProduct ticket BTC-EUR\n')
print(public_client.get_product_ticker(product_id='BTC-EUR'))

print('\n\tProduct trades BTC-EUR\n')
public_client.get_product_trades(product_id='ETH-USD')

print('\n\tProduct historic rats BTC-EUR\n')
public_client.get_product_historic_rates('ETH-USD')

print('\n\tProduct historic rates with granu BTC-EUR\n')
public_client.get_product_historic_rates('ETH-USD', granularity=3000)

print('\n\tProduct 24hr stats BTC-EUR\n')
public_client.get_product_24hr_stats('ETH-USD')

print('\n\tCurrencies\n')
public_client.get_currencies()

print('\n\tTime\n')
public_client.get_time()
