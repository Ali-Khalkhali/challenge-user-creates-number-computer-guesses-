import random
a,b =1,99
while True:
    guess=random.randint(a,b)
    print('a:',a)
    print('b:',b)
    answer= input(f'guess is{guess}. Was my answer correct? Bigger or smaller?')
    if answer=='b':
        a=guess
    elif answer=='s':
        b=guess
    elif answer=='y':
        print("Yes!!!You rock!")
        break
    else:
        print('i Can\'t understand!...')
        

        
