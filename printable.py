from datetime import datetime
import json
# time_now = datetime.now()
# print(time_now.year, time_now.month, time_now.day)

# test = {"1": {"name": "Nothing", "age": 25, "phone": 43545},
#         "2": {"name": "Bdr", "age": 22, "phone": 432321}}

# x = json.dumps(test)
# with open('test.json', 'w') as filt:
#     filt.write(x)

with open('test.json', 'r') as filt:
    test = json.loads(filt.read())
print(test['2']['age'])
