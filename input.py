# import re

# while True:
#     user = input('search for characters?')
#     text = 'wale'
#     if(re.search(user, text)):
#          print('found')
#     else:
#          print('not found')
# valid = re.search(user, text)

# print(valid)

person = {
    "firstName":"john",
    "age":27,
    "rank":[
        {
            "position":'junior Dev',
            "salary":'#20,000'
        },
        {
            "position":'senior Dev',
            "salary":'#30,000'
        }
    ]
}
print(person['firstName'] + ' is having a role of ' + person["rank"][0]['position'])
# # 
