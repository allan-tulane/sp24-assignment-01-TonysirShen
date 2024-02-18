"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
  if x <= 1:
    return x
  else:
    return foo(x-1) + foo(x-2);

def longest_run(mylist, key):
  temp = 0
  max = 0
  for i in mylist:
    if i == key:
      temp += 1;
      if temp > max:
        max = temp;
    else:
      temp = 0;
  return max



class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
      
result = Result(3,4,5,False)



def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        


def longest_run_recursive(mylist, key):
  # divding myarry and return Result Object to store information of the divided array
  def helper(list):
    # in case empty array
      if len (list) == 0:  
          return Result(0, 0, 0, True)
      elif len(list) == 1:
          if list[0] == key:
              return Result(1, 1, 1, True)# (left size of continuous sequence, right size continuous sequence,longest size of continuous sequence on record, is the entire range of the array belongs to the key) 
          else:
              return Result(0, 0, 0, False)

      mid = len(list) // 2
      left_result = helper(list[:mid])
      right_result = helper(list[mid:])

      # Combine data from left and right_result
      mix_longest_size = max(left_result.longest_size, right_result.longest_size) # find the longest size store in the subdivisions
      if list[mid-1] == key and list[mid] == key:# check if left and right should combined 
          mix_longest_size = max(mix_longest_size, left_result.right_size + right_result.left_size)
        
      # change the status of is entire range
      mix_is_entire_range = left_result.is_entire_range and right_result.is_entire_range
    
      mix_left_size = left_result.left_size
      if left_result.is_entire_range and list[mid] == key:# check if the next index of array belongs to the continous sequence
          mix_left_size += right_result.left_size# add the left data of the right result

      mix_right_size = right_result.right_size
      if right_result.is_entire_range and list[mid-1] == key:
          mix_right_size += left_result.right_size

     

    

      return Result(mix_left_size, mix_right_size, mix_longest_size, mix_is_entire_range)

  result = helper(mylist)
  return to_value(result) #return the longest size

# Example usage
myarray = [1, 2, 2, 3, 3, 3, 3, 3, 3 ,2 , 2, 1, 1, 1, 1]
key = 3


testarray =[1,1,2,3,4]

print(longest_run_recursive(myarray, key)) 
print(len(testarray)//2)
print(testarray[:2])
