from django.shortcuts import render

# Create your views here.
class Member:
    def __init__(self,userid,parentid):
        self.userid = userid
        self.parentid = parentid
        self.position = None
        self.level = None
        self.left = None
        self.right = None
        self.sponsor_bonus = None
        self.binary_bonus = None
        self.matching_bonus = None
        self.carry_forward = None
        