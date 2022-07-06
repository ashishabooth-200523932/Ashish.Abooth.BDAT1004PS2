#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a=0

def b():
    global a
    a=c(a)
    
def c(a):
    return a+2
print (a)


# /*HERE IN THIS QUESTION, WHEN EXUCUTING b(), it shows no value, because it is only declared but not given any value. so funtion b() is an empty function */
# 
# my_module - file is also there where the output is given. (see screenshot attached in the word file).

# In[ ]:


*(Ending, of, Solution, No., 1, above, */)


# SOLUTION NO. 2 :-

# In[ ]:


import os

def file_length("F:\myFile.txt.txt"):
        
file = os.path.getsize("F:\myFile.txt.txt")

    contents = file.read()
    
    file.close()
    
    print(len(contents))


# SOLUTION NO. 3 :-

# In[ ]:


class Marsupial:
    
    def __init__(m, put_in_pouch):
        m.put = pouch_contents(['doll', 'firetruck', 'kitten'])
        m.put = name
    def query(self):
        return('m=Marsupial'
              m.put_in_pouch('doll')
              m.put_in_pouch('firetruck')
              m.put_in_pouch('kitten')
    
class kangaroo():
    
    def __init__(x,y):
        x.y = random.choice()
        jump().__str__(name)
    # Call the parent's query method and add new behavior
    def query(self):
        return jump().query() + ("I am a kangaroo located at coordinates (x,y)")

print(jump().query())


# SOLUTION NO. 4 :-

# In[ ]:


def Collatz(n):
     
    while x != 1:
        print(x, end = ' ')
 
        # If x is odd
        if x & 1:
            x = 3 * x + 1
 
        # If even
        else:
            x = x // 2
 
    # Print 1 at the end
    print(x)
 
print Collatz(n)


# SOLUTION NO. 5 :-

# In[ ]:


def binary(n):

    if n==0:
return (0)
elif n == 1:
return (1)
else:
return 
binary(n//2)+binary(n%2) #recursive call

print(binary(0))
print(binary(1))
print(binary(14))


# SOLUTION NO. 7 :-

# In[ ]:


from bs4 
import BeautifulSoup
import requests

urls=[]            # to get urls in here...

def getsite(site):
    r = requests.get(site)   # getting the request from url..
    
    s = BeautifulSoup(r.text, "html.parser")    #In order to convert..
    
    for i in s.find_all("a"):   
        href = i.attrs['href']
           
        if href.startswith("/"):  # to check wheather the website is selected..
            site = site+href
               
            if site not in  urls:
                urls.append(site) 
                print(site)
                                         # calling it self  
                getsite(site)            #recursive funtion
                onclick()                # function to execute on click
   
if __name__ =="__main__":
   
    # website as input
    site="http://example.recursivewebsite.com//"
   
    # calling function
    scrape(site)


# SOLUTION NO. 8 :-

# In[ ]:


(a.) Select Temperature(C) 
     From Table_name;                #Table Name is not given
    
(b.) Select Distinct City 
     From Table_name;
    
(c.) Select * From Table_name 
     WHERE Country='India';
        
(d.) Select * From table_name
     WHERE Season='FALL';

(e.) SELECT City, Country, Season
     FROM table_name
     WHERE Rainfall BETWEEN 200 AND 400;

(e.) Select City, Country

     WHERE Rainfall BETWEEN 200 AND 400;
    
(f.) Select City, Country
     From table_Name
     WHERE AVG(Temperature) > 20
     ORDER BY Temperature ASC;
    
(e.) Select SUM(Rainfall)
     From Table_name
     WHERE City='Cairo';
        
(f.) Select SUM(Rainfall)
     From Table_name
     GROUP BY Season;

