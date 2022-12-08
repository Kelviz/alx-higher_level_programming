#!/usr/bin/python3

def common_elements(set_1, set_2):
    c = []
    for a in set_1:
        for b in set_2:
            if b == a:
                c.append(b)
    return c
            
