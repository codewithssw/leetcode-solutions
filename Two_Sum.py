#LeetCode 1:Two Sum
#Approach: Nested For Loop
#Time Complexity: O(n^2) - We iterate through the list twice using nested Loops 

nums = [2, 7, 11, 15]
target = 13

def twoSum(nums, target):
    #Outer Loop selects the first number
    for i in range(len(nums)):
        #Inner Loop checks every subsequent number in the list
        for j in range(i + 1, len(nums)):
            #If the two numbers add up to our target, return their indices
            if (nums[i] + nums[j] == target):
                return [i, j]
            

result = twoSum(nums, target)
print("Result: ", result)



#--------Test Case Example--------------------------------------
'''
i = range(0, 4) -- 0,1,2,3              j = range(i + 1, 4)


i = 0 = 2

            j = range(1, 4) ---- 1,2,3
            j = 1 = 7
            j = 2 = 11
            j = 3 = 15

i = 1 = 7
etc....


Result: [0,2] (because nums[0] + nums[2] == 13)
                          2    +    11   == 13

'''

        
            
            

            
                
            
    
            
            
    
                
        
        
        
        
            
        
    



                
            
        
        


        
        
               
            
            
            
            
            
          
            


    

   
                
            
             
        


    