import gdax, time
order_book = gdax.OrderBook(product_id='BTC-EUR')
order_book.start()
time.sleep(10)
order_book.close()
