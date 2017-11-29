#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 15:29:53 2017

@author: matpind
"""

musvit = {'name': 'Musvit','colour':'gul' ,'size':'lille' }
skovdue = {'name':'Skovdue' ,'colour':'grå' ,'size': 'stor'}
blåmejse = {'name':'Blåmejse' ,'colour':'blå' ,'size':'lille' }
solsort= {'name':'Solsort' ,'colour':'sort' ,'size':'mellem' }
rødhals = {'name':'Rødhals' ,'colour':'rød' ,'size':'lille' }


birds = [musvit,skovdue,blåmejse,solsort,rødhals]

#bird_attr = {'size':['lille','mellem','stor']}


q1 = input("Hej Anders. Har du set en fugl i haven? ")
if q1 == 'Ja' or q1 == 'ja':
    print ('')
    print ('Yay!')
    q2 = input("Ved du hvilken fugl det er? ")
    if q2 == 'Ja' or q2 == 'ja':
        q3 = input("Er det en musvit, en skovdue, en blåmejse, en rødhals eller en solsort? ")
        if q3 == 'musvit' or q3 == 'skovdue' or q3 == 'blåmejse' or q3 == 'rødhals' or q3 == 'solsort':
            print ('Godt klaret!')
        else:
            print('')
            print('Ingen af dem? Så er det måske en and?')
    else:
        print ('')
        print('Så lad os finde ud af det sammen!')
        q4 = input('Er fuglen stor eller lille? ')
        if q4 == 'stor':
            q5 = input('Er det en tyk skovdue? ')
            if q5 == 'ja':
                print('')
                print('Juhu, vi klarede det!')
            else:
                print('')
                print('Så er det måske en and?')
        else:
            q6 = input('Er den gul eller blå eller rød på brystet? ')
            if q6 == 'gul':
                print('')
                print ('Så er det en musvit!')
            elif q6 == 'blå':
                print('')
                print ('Så er det en blåmejse!')
            elif q6 == 'rød':
                print('')
                print ('Så er det en rødhals!')
            else:
                q7 = input('Hverken gul eller blå? Så er det måske en solsort? ')
                if q7 == 'ja':
                    print('')
                    print('Pyha! Så fandt vi ud af det alligevel!')
                else:
                    print('')
                    print('Så er det måske en and?')
else:
    print('')
    print ('Øv. Det var synd. Så vil du måske hellere flyve med dronen?')







#def hvilken_fugl(birds,x):
 #   q1 = input("Ved du hvilken fugl det var? ")
