# if we have two strings let's say u = fast and v = cats.The edit distance is nothing but the number of edits required to convert the first string to the other.

#Brute force Time Complexity --> 3 ^ (m+n) = exponential time complexity
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


#Using Dynamic programming --> O(m * n) -->quadratic time complexity

def edit_distance(str1,str2,m,n,mem = None):
    
    if mem is None:
        mem = {}
    
    if (m,n) in mem:
        return mem[(m,n)]
    
    if m == 0:
       return n
    
    if n == 0:
       return m
    
    if str1[m-1] == str2[n-1]:
        result =  edit_distance(str1,str2,m-1,n-1,mem)
        
    else:
        result =  1+ min(edit_distance(str1,str2,m,n-1,mem),
        edit_distance(str1,str2,m-1,n,mem),
        edit_distance(str1,str2,m-1,n-1,mem))
        
    mem[(m,n)] = result  
   
    return result
        

str1 = "fast"
str2 = "cats"

print(edit_distance(str1,str2,len(str1),len(str2)))



#Using matrix -->Time complexity - O(m*n) and Space Complexity - O(m*n) 
def edit_distance(str1, str2):
    m, n = len(str1), len(str2)

    # Initialize a matrix to store edit distances
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the matrix with base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Build the matrix in a bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],       # Deletion
                                  dp[i][j - 1],       # Insertion
                                  dp[i - 1][j - 1])   # Replacement

    return dp[m][n]

# Example usage:
str1 = "kitten"
str2 = "sitting"
result = edit_distance(str1, str2)
print(f"The edit distance between '{str1}' and '{str2}' is: {result}")

