event = {'amount': ['800.00'],
     'currency_code': ['KES'],
     'custom': ['custom'],
     'customer': [''],
     'fpn_id': ['147358'],
     'item_name': ['laptop'],
     'item_price': ['200'],
     'merchant': ['sky-swift@mobirr.com'],
     'order_id': ['”123456”'],
     'partner_message': [''],
     'payer_email': ['dukelester4@gmail.com'],
     'payment_channel': ['Mobile'],
     'quantity': ['4'],
     'request_date': ['2021-04-01T10:47:55'],
     'return_url': ['https://www.sky-swift.com'],
     'sender_acct': [''],
     'status': ['0004'],
     'status_msg': ['Payment is pending.'],
     'trace_number': ['T16642439539063'],
     'trans_id': ['0'],
     'txn_partner_ref': ['SBFLOEC2104017568042304']}

# {'amount': '800.00', 'currency_code': 'KES', 'custom': 'custom', 'customer': '', 'fpn_id': '147358', 'item_name': 'laptop', 'item_price': '200', 'merchant': 'sky-swift@mobirr.com', 'order_id': '”123456”', 'partner_message': '', 'payer_email': 'dukelester4@gmail.com', 'payment_channel': 'Mobile', 'quantity': '4', 'request_date': '2021-04-01T10:47:55', 'return_url': 'https://www.sky-swift.com', 'sender_acct': '', 'status': '0004', 'status_msg': 'Payment is pending.', 'trace_number': 'T16642439539063', 'trans_id': '0', 'txn_partner_ref': 'SBFLOEC2104017568042304'}
print(event['amount'])
merchant = event['merchant']
sender_acc = event['sender_acct']
order_id = event['order_id']
amount = event['amount']
item_name = event['item_name']
currency_code = event['currency_code']
quantity = event['quantity']
trans_id = event['trans_id']
fpn_id = event['fpn_id']
customer = event['customer']
status = event['status']
status_msg = event['status_msg']
payer_email = event['payer_email']
payment_channel = event['payment_channel']
txn_partner_ref = event['txn_partner_ref']

