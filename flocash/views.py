# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#
import json
from math import e

from django.http import HttpResponse, request
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

# Create your views here.
from flask import jsonify
from rest_framework.decorators import api_view

from flocash.models import Payments


@require_http_methods(["GET", "POST"])
def flocashView(request):
    if request.method == 'POST' and request.method == 'GET':
        user_id = request.GET.get('id', None)
        # Save the payment status
        payment = Payments.objects.get(user_id=user_id)
        payment.payment_successful = True
        if payment.hasUserPaid(user_id):  # This is where we are verifying the payment
            # Save the payment status
            payment = Payments.objects.get(user_id=user_id)
            payment.payment_successful = True
            payment.save()

    return render(request, 'flocashform.html')
    # return HttpResponse('success')


@require_http_methods(["GET", "POST"])
@csrf_exempt
@api_view(["POST", "GET"])
def webhook(request):
    event = None

    payload = request.data
    print(payload)

    try:
        data = payload
        data = json.dumps(data)

        event = json.loads(data)
        print(event)

    except:

        print('⚠️  Webhook error while parsing basic request.' + str(e))

        return jsonify(success=False)

    # Handle the event

    if event and event['status_msg'] == 'Payment is pending.':

        print('Payment of {} pending for {}'.format(event['amount'], event['item_name']))

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

        print('Transaction details ::', merchant, sender_acc, order_id, amount, item_name, currency_code,
              quantity, trans_id, fpn_id, customer, status, status_msg, payer_email, payment_channel, txn_partner_ref)

        context = {
            'merchant': event['merchant'],
            'sender_acc': event['sender_acct'],
            'order_id': event['order_id'],
            'amount': event['amount'],
            'item_name': event['item_name'],
            'currency_code': event['currency_code'],
            'quantity': event['quantity'],
            'trans_id': event['trans_id'],
            'fpn_id': event['fpn_id'],
            'customer': event['customer'],
            'status': event['status'],
            'status_msg': event['status_msg'],
            'payer_email': event['payer_email'],
            'payment_channel': event['payment_channel'],
            'txn_partner_ref': event['txn_partner_ref'],

        }
        return render(request, 'success.html', context)

    elif event and event['status_msg'] == 'Payment is successiful.':

        print('Payment of {} successful for {}'.format(event['amount'], event['item_name']))

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

        print('Transaction details ::', merchant, sender_acc, order_id, amount, item_name, currency_code,
              quantity, trans_id, fpn_id, customer, status, status_msg, payer_email, payment_channel, txn_partner_ref)

        context = {
            'merchant': event['merchant'],
            'sender_acc': event['sender_acct'],
            'order_id': event['order_id'],
            'amount': event['amount'],
            'item_name': event['item_name'],
            'currency_code': event['currency_code'],
            'quantity': event['quantity'],
            'trans_id': event['trans_id'],
            'fpn_id': event['fpn_id'],
            'customer': event['customer'],
            'status': event['status'],
            'status_msg': event['status_msg'],
            'payer_email': event['payer_email'],
            'payment_channel': event['payment_channel'],
            'txn_partner_ref': event['txn_partner_ref'],

        }
        return render(request, 'success.html', context)


    elif event and event['status_msg'] == 'Payment is cancelled.':

        print('Payment of {} cancelled  for {}'.format(event['amount'], event['item_name']))

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

        print('Transaction details ::', merchant, sender_acc, order_id, amount, item_name, currency_code,
              quantity, trans_id, fpn_id, customer, status, status_msg, payer_email, payment_channel, txn_partner_ref)

        context = {
            'merchant': event['merchant'],
            'sender_acc': event['sender_acct'],
            'order_id': event['order_id'],
            'amount': event['amount'],
            'item_name': event['item_name'],
            'currency_code': event['currency_code'],
            'quantity': event['quantity'],
            'trans_id': event['trans_id'],
            'fpn_id': event['fpn_id'],
            'customer': event['customer'],
            'status': event['status'],
            'status_msg': event['status_msg'],
            'payer_email': event['payer_email'],
            'payment_channel': event['payment_channel'],
            'txn_partner_ref': event['txn_partner_ref'],

        }
        return render(request, 'success.html', context)

    else:

        # Unexpected event type

        print('Unhandled event type {}'.format(event['type']))

    return HttpResponse('success')
