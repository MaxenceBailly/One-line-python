(lambda a:print('\n'.join([f'{i}-'+('FizzBuzz' if i%3==0 and i%5==0 else 'Fizz' if i%3==0 else 'Buzz' if i%5==0 else '') for i in range(1, a+1)])))(eval(input("What's range ?:")))