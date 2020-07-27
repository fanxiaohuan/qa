# -*- coding: utf-8 -*-
import json

import requests


def getCoupon():
    cookies='BearereyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbjEyMyIsImNyZWF0ZWQiOjE1OTU0MDYyNzI2ODUsImV4cCI6MTU5NjAxMTA3Mn0.CIoxEKA7oqERAremd2ZcOc51SomYBmzDeWd0ba99EIaYS19flQnWvKPa12KXl_fVVzJ29AOSOj1FwtHy_-yQqQ'
    head = {'Authorization': cookies}
    coupon = requests.session()
    couponUrl='http://malladminapi.dev.yinongt.com/coupon/list?pageNum=1&pageSize=10'
    couponRequest=coupon.get(couponUrl,headers=head)
    couponResponse = couponRequest.text
    couponDate = json.loads(couponResponse)
    couponCodes = couponDate["data"]["list"]
    codes=[]
    for couponCode in couponCodes:
        if couponCode.get("code")!=None:
            codes.append(couponCode.get("code"))
    return codes
    

if __name__ == "__main__":
    couponValue = getCoupon()
    print(couponValue)
