#Author:Sourav Nanda
print(list(map(lambda num:'fizz' if num%3==0 else 'buzz' if num%5==0 else 'fizzbuzz' if num%5==0 and num%3==0 else num,range(1,101))))
