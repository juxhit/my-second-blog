user = {'name': 'Jack', 'age': '20', 'work_hour': [2,4,6,8]}
print('Hello ', user['name'])
print('Your age:', user['age'])
print('Your work hours:', user['work_hour'])
open_hour = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Company work hours: ', open_hour)

# Test True
if 3 < 2:
    print('It works')
else:
    print('It does not work')

# Say Hi
if user['name'] == 'Jux':
    print('Hi Jux')
elif user['name'] == 'Jack':
    print('Hi Jack')
else:
    print('Who are you?')

def hello():
    print('function hello')

hello()

def hey(name):
    if name == 'Jux':
        print('Hi Jux')
    elif name == 'Jack':
        print('Hi Jack')
    else:
        print('Who are you?')

hey(user['name'])

def hi(name):
    print('Hi ' + name + '!')

girls = ['Monday', 'Tusday', 'Wensday', 'Thursday', 'Friday']

for name in girls:
    hi(name)
    print('Next girl')

for i in range(1,20):
    print(i)