## HOF

# HOF high order function (lo function!')
#
# myDecoratedNewFunction = myHOF(sayHello)
#
# myDecoratedNewFunction()
# myDecoratedNewFunction()
# myDecoratedNewFunction()
#
#
# функция высшего порядка)
# def myHOF(anyFunction):
#     print(f'function has benn runned at {datetime.now().time()}')
#
#     return anyFunction
#     # myDecoratedNewFunction == anyFunction
#
# def sayHello():
#     print('Hello from sayHel


### DECORATORS

# HOF high order function (функция высшего порядка)
# def myDecorator(anyFunction):
#     def newFunction(user):
#         print(f'function has benn runned by {user} at {datetime.now().time()}')
#         anyFunction()
#
#     return newFunction
#
# @myDecorator
# def sayHello():
#     print('Hello from sayHello function!')




# myDecoratedNewFunction = myDecorator(sayHello)
#
# myDecoratedNewFunction('Loik')
# myDecoratedNewFunction('Vasya')
# myDecoratedNewFunction('Natasha')