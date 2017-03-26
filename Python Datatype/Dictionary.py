
#****************   Python Dictionary ***********************

# Each key is separated from its value by a colon (:)

# How many to declear dict in python

# dict = { } # this is not a set
# d = dict()
# d[' '] = ''

# Now Example of Dictionary

'''

d = {}  # this is a dist not set
d = dict()
d['Name'] = 'Jibon'
d['Name'] = 'Python'
d[1] = 'Number one'

print(d)
print(type(d))
print('\n')

'''

# **********************Now Example of dict *********************************

# About you using Dictionary

'''

d = dict(Name = 'jibon',
         phone = '01987132107',
         gethub= 'jibon69',
        email = 'jayed.swe@gamil.com',
        )
print('About Jibon :' ,d)

print('Phone Number : ',d['phone'])

'''

#*********   About you using Dictionary ****************

'''

d = {'name' : 'Jibon',
     'phone' : '01987132107',
     'email' : 'jayed.swe@gamil.com',
     'location' : 'DIU',}
d[19] = 'Python'

print('About me = ',d)

print('Jibon  : ',d['name']) # Print only Jibon

print('python : ',d[19]) # print only 19

print('\n')

'''

#**************** Example of dict ***************************

'''

d = dict(Name = 'jibon',
         phone = '01987132107',
         gethub= 'jibon69',
         email = 'jayed.swe@gamil.com',
        )

print('Key of  dict  : ',d.keys()) # key of dict

print('Value of dict : ',d.values()) # Value of dict

print('Email  : ', d.get('email')) # d['email']

print('Gethub : ', d['gethub'])

print('All item:', d.items())

'''

#*********** Multiple dict in Dictionary



d = dict(Name = 'jibon',
         phone = '01987132107',
         gethub= 'jibon69',
         email = 'jayed.swe@gamil.com',
        )

d1 = {'new Dict': 'Ahmed', 'New Email': 'a@gmail.com'}
d.update(d1)
print(d)

d['new Dict'] = {'n' : 'Name',
                 'E' : 'jibon@gmail.com',
                 "phone" : '029394',
                 'list' : [1, 2, 44, 44, 5],
                 'set' : {1, 2, 3, 3 ,3, 3,100},
                 'tuple' : (1, 2, 2, 4, 2, 3)
                 }


print(d)

print('E : ', d['new Dict']['E'])

print('Print 44 :',d['new Dict']['list'][3])

print('Print 1 : ', d['new Dict']['tuple'].index(2))



# *************** using this loop print all dist ******************

'''

for key, value in d.items():
    print(key, ' = ', value)

'''
