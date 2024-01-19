# if we have two strings let's say u = fast and v = cats.The edit distance is nothing but the number of edits required to convert the first string to the other.

#Brute force
def edit_distance(str1,str2,m,n):

  #If the first string is empty we need to add n number of characters
    if m == 0:
       return n
  #if second string is empty we need to delete m characters 
    if n == 0:
       return m
   # if both strings last character is same then do nothing 
    if str1[m-1]==str2[n-1]:
        return edit_distance(str1,str2,m-1,n-1)
        
    else:
        result =  1 + min (
           edit_distance(str1,str2,m,n-1) # Adding a character
          ,edit_distance(str1,str2,m-1,n),#Removing a character
          edit_distance(str1,str2,m-1,n-1) #Replacing a character
                        )
        
    return result
        

str1 = "fast"
str2 = "cats"

print(edit_distance(str1,str2,len(str1),len(str2)))