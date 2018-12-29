# --------------
def palindrome(num):

 num = num+1
 num = str(num)
 if num[::-1] != num:
  return palindrome(int(num))

 return int(num)

palindrome(12)


# --------------
#Code starts here

def a_scramble(str_1,str_2):
 str_1 = str_1.lower()
 str_2 = str_2.lower()
 l1 = [x for x in str(str_1)]
 l2 = [x for x in str(str_2)]
 
 b = l2
 s = l1
 i = True
 if len(l1)>len(l2):
  b = l1
  s = l2
 print(s,'------',b)
 for each in range(0,len(s)):
  if s[each] in b:
   print(s[each])
   ind = b.index(s[each])
   del(b[ind])
  else :
   i = False
 return i

a_scramble("labratory","Bat")







# --------------
#Code starts here



def check_fib(num):
 a = 0
 b = 1
 fibo=[a, b]
 
 while b < num:
  a, b = b, a+b
  fibo.append(b)
 if num in fibo:
  return True
 else:
  return False
   

   
 
  

check_fib(987)


# --------------
#Code starts here

#Function to compress string
def compress(word):
    word=word.lower()
    mist=[]
    l=0
    while(l<len(word)):
        m=word[l]
        j=0
        while(l<len(word) and word[l]==m):
                 j=j+1
                 l=l+1    

        mist.append(m)
        mist.append(str(j))
    
    return ''.join(mist)






# --------------

#Function to check existence of k distinct characters in string
def k_distinct(string,k):
    s_list=(set(string.lower()))
    return len(s_list)>=k

#Code ends here


