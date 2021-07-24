import pandas as pd
import random
import nltk
from nltk import word_tokenize
nltk.download('punkt')
nltk.download('wordnet')
#from textaugment import Wordnet
#from textaugment import EDA
n=500
data1=[]
data2=[]#Problem
data3=[]#Answer
data4=[]#Score
for i in range(n):
    data1.append(i)
    data2.append(1)
    ans=random.randint(-5,5)
    data3.append(ans)
    if ans==-1:
        s=5
    else:
        s=0
    data4.append(s)



#t=Wordnet(v=False, n=True,p=0.5)
for i in range(n):
    data1.append(n+i)
    data2.append(2)
    list1=['i^6=-1','i^{16}=1','i^{26}=-1', '-1']
    ans=random.sample(list1, random.randint(1,4))

    data3.append(ans)
    if ans.__contains__('-1'):
        s=5
    else:
        s=len(ans)
    data4.append(s)

    for i in range(n):
        data1.append(2*n + i)
        data2.append(3)
        list1 = ['7+x+4+2x+1=36 ', '3x+12=36', '3x=24', 'x=8']
        list2=['', 'x+4=12, 2x+1=17']
        ans = random.sample(list1, random.randint(1, 1))
        ans1=random.sample(list2, random.randint(1, 1))
        ans=ans+ans1
        data3.append(ans)

        if ans.__contains__('x+4=12, 2x+1=17'):
            s = 5
        else:
            s = 3
        data4.append(s)
    for i in range(n):
        data1.append(3 * n + i)
        data2.append(4)
        list1 = ['f(-x)g(-x)=-f(x)g(x)',  'f(-x)g(-x)=f(x)g(x)']
        list2=['odd', 'even', 'either']
        ans = random.sample(list1, random.randint(1, 1))
        #data3.append(ans)
        ans1 = random.sample(list2, random.randint(1, 1))
        ans=ans+ans1
        data3.append(ans)
        if ans.__contains__('f(-x)g(-x)=-f(x)g(x)'):
             if ans.__contains__(ans.__contains__('odd')):
                 s=5
             else:
                 s=4
        elif ans.__contains__('odd'):
            s=1
        else:
            s=0
        data4.append(s)

print(data1)
print(data2)
print(data3)
print(data4)

dataFrame=pd.DataFrame({'ID':data1,'Problem':data2,'Answer':data3,'Score':data4})
dataFrame.to_csv('data_math.csv',index=False,sep=',')


