#### FUNCTION #######
#%% User Defined Function
def my_first_function(var1, var2):
    """
    parametre:var1, var2
    return:output
  
    """
    output= (var1+var2)*50
    return output
print(my_first_function(4,6))

def add(a):
    b=a+1
    print(a, b)
    return b
add(1)

def Mult(a, b):
    c = a * b
    return(c)

result = Mult(12,2)
print(result) #24
Mult(2, "Michael Jackson ") # 'Michael Jackson Michael Jackson '

# Make a Function for the calculation above
def Equation(a,b):
    c = a + b + 2 * a * b - 1
    if(c < 0):
        c = 0 
    else:
        c = 5
    return(c)

#%% Built-in function
str1 = "denmem"
str2= "1005"
print(str1)

float(10) # int to float 10.0
int(10.0) # float to int 10
round(10.7) # 11
int(str2) # 1005
    
# Build-in function print()
album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5] 
print(album_ratings)

# Use sum() to add every element in a list or tuple together
sum(album_ratings) # 70.0

# Show the length of the list or tuple
len(album_ratings) # 8

# Example for setting param with default value
def isGoodRating(rating=4): 
    if(rating < 7):
        print("this album sucks it's rating is",rating)
        
    else:
        print("this album is good its rating is",rating)

isGoodRating() # this album sucks it's rating is 4
isGoodRating(10) # this album is good its rating is 10


#%% default and flexible function
def cember_cevresi_hesapla(r,pi =3.14):
    output = 2*pi*r
    return output

# When the number of arguments are unknown for a function, They can all be packed into a tuple as shown:
def printAll(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args)) 
    for argument in args:
        print(argument)

#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')

# Similarly, The arguments can also be packed into a dictionary as shown:
def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')

def hesapla(kilo,boy,*args):
    output = boy+kilo+args[0]
    return output
hesapla(1,2,3,4,5)

#%%Lamda Function
sonuc2 = lambda x : x*x 
print(sonuc2(2)) ##4
