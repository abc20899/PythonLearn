import re

line = 'XXXX出生于2001年7月21日'
line = 'XXXX出生于2001/7/21'
line = 'XXXX出生于2001-7-21'
line = 'XXXX出生于2001-07-21'
line = 'XXXX出生于2001-7'

# 提前年月日

rege_str = '.*出生于(\d{4}[年/-]\d{1,2}([月/-]\d{1,2}|[月/-]$|$))'
match_obj = re.match(rege_str, line)
print(match_obj.group(1))

'''
.*出生于(\d{4}[年/-]\d{1,2}([月/-]\d{1,2}|[月/-]$|$))
( 
  \d{4}    年/-
  \d{1,2}     月/- \d{1,2}   |   [月/-]$ | $

'''