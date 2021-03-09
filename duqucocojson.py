import json,os,time

test_dict='annotations/instances_val2017.json'


with open(test_dict,'r') as load_f:
    load_dict = json.load(load_f)
    print(type(load_dict))
    print(load_dict.keys())

print(load_dict['annotations'][0])
#print(load_dict['annotations'])
#print(load_dict['categories'])
#print(load_dict['images'])
#print(load_dict['licenses'])
    #time.sleep(20)
'''
json_str = json.loads(test_dict)
print(json_str)

print(type(json_str))
'''
#   dict_keys(['info', 'licenses', 'images', 'annotations', 'categories'])

