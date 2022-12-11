fname = "input.txt"
import math
import re
import sys
from collections import defaultdict
monkey_dict = defaultdict(dict)
i= 0
# get monkey startings
with open(fname) as f:
    for line in f:
        # input starts with monkey get number
        if line.startswith('Monkey'):
            number = re.findall('[0-9]+', line)
            number = int(number[0])
        elif line.strip().startswith('Starting'):
            items = re.findall('[0-9]+', line)
            items = [int(item) for item in items]
            monkey_dict[number]['Worry'] = items
        elif line.strip().startswith('Operation'):
            if line.find('*') != -1: # is a multiply
                try: # if not multiplied by itself
                    op_num = re.findall('[0-9]+', line)
                    monkey_dict[number]['Operation'] = '*' + op_num[0]
                except: # else multiplied by itself
                    monkey_dict[number]['Operation'] = 'sq'
            else:
                try: # if not multiplied by itself
                    op_num = re.findall('[0-9]+', line)
                    monkey_dict[number]['Operation'] = '+' + op_num[0]
                except: # else multiplied by itself
                    monkey_dict[number]['Operation'] = 'add'

        elif line.strip().startswith('Test'):
            test_num = re.findall('[0-9]+', line)
            test_num = int(test_num[0])
            monkey_dict[number]['Test'] = test_num
        elif 'true' in line.strip():
            true_num = re.findall('[0-9]+', line)
            true_num = int(true_num[0])
            monkey_dict[number]['True'] = true_num
        elif 'false' in line.strip():
            false_num = re.findall('[0-9]+', line)
            false_num = int(false_num[0])
            monkey_dict[number]['False'] = false_num

                
for v in monkey_dict.keys():
    monkey_dict[v]['Inspections'] = 0

rounds = 20
for r in range(rounds):
    for monkey in monkey_dict.values():

        # monkey starts inspecting, increase worry levels
        if monkey['Operation'][0] == '*':
            op_num = int(monkey['Operation'][1:])
            monkey['Worry'] = [num*op_num for num in monkey['Worry']]
        elif monkey['Operation'] == 'sq':
            monkey['Worry'] = [num**2 for num in monkey['Worry']]
        else:
            op_num = int(monkey['Operation'][1:])
            monkey['Worry'] = [num+op_num for num in monkey['Worry']]
        # monkey finishes inspecting, decrease worry levels 
        monkey['Worry'] = [math.floor(num/3) for num in monkey['Worry']]
        
        monkey['Inspections'] += len(monkey['Worry'])

        # check if divisible by test
        for i in range(len(monkey['Worry'])):
            num = monkey['Worry'][i]
            if num % monkey['Test'] == 0:
                to_throw = monkey['True']
                monkey_dict[to_throw]['Worry'].append(num)
                
            else:
                to_throw = monkey['False']
                monkey_dict[to_throw]['Worry'].append(num)

        monkey['Worry'] = []
        
monkey_business = []
for monkey in monkey_dict.values():
    monkey_business.append(monkey['Inspections'])

monkey_business = sorted(monkey_business, reverse = True)[:2]
monkey_business = monkey_business[0] * monkey_business[1]
print(monkey_business)
            