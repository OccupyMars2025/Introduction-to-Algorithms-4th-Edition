def count_long_subarray_v001(A):
    '''
    use a dictionary to store the length of the longest increasing subarray and the number of such subarrays,
    not efficient !!!
    
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count = 0
    ##################
    # YOUR CODE HERE #
    start = 0
    end = start + 1
    len_and_count_dict = {}
    while start < len(A) and end < len(A):
        if A[end - 1] < A[end]:
            end += 1
        else:
            len_and_count_dict.setdefault(end - start, 0)
            len_and_count_dict[end - start] += 1
            start = end
            end = start + 1
    len_and_count_dict.setdefault(end - start, 0)
    len_and_count_dict[end - start] += 1
    
    count = len_and_count_dict[max(len_and_count_dict.keys())]
    ##################
    return count 




def count_long_subarray_v002(A):
    '''
    Do not use a dictionary !!!
    
    This function is buggy !!!
    Can you find the bug ?
    
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    # length of the longest increasing subarray in A[:i]
    longest_length = 1  
    # number of longest increasing subarrays in A[:i]
    count = 1  
    # length of the longest increasing subarray that ends at A[i-1]
    current_length = 1
    for i in range(1, len(A)):
        if A[i-1] < A[i]:
            current_length += 1
        else:
            if current_length > longest_length:
                longest_length = current_length
                count = 1
            elif current_length == longest_length:
                count += 1
            current_length = 1
    return count




"""  
2024/12/10: Yes, the above function is buggy !!! 
I found the bug by "maintaining the loop invariant" !!!
The 3 lines of comments below construct the loop invariant.
Before the start of each iteration, you must make sure that the invariant holds.
But in the above function, the loop invariant is clearly not maintained !!!

Amazing !!! This is the first time I find a bug by "maintaining the loop invariant" !!!
"maintaining the loop invariant" is a very powerful technique !!!
"maintaining the loop invariant" is not just the only correct way to prove your 
algorithm is correct !!! But it is also the most powerful technique to help you debug your code !!!
It is not just some boring math, but is also a very useful tool !!!

VERY USEFUL TOOL !!! I LOVE MATH !!!

"""
def count_long_subarray_v003(A):
    '''
    Do not use a dictionary !!!
    
    This function is buggy !!!
    Can you find the bug ?
    
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    # length of the longest increasing subarray in A[:i]
    longest_length = 1  
    # number of longest increasing subarrays in A[:i]
    count = 1  
    # length of the longest increasing subarray that ends at A[i-1]
    current_length = 1
    for i in range(1, len(A)):
        if A[i-1] < A[i]:
            current_length += 1
            if current_length > longest_length:
                longest_length = current_length
                count = 1
            elif current_length == longest_length:
                count += 1
        else:
            current_length = 1
    return count




def count_long_subarray(A):
    '''
    Actually, count_long_subarray_v003() is still buggy !!!
    count_long_subarray_v003() still don't maintain the loop invariant !!!
    
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    # length of the longest increasing subarray in A[:i]
    longest_length = 1  
    # number of longest increasing subarrays in A[:i]
    count = 1  
    # length of the longest increasing subarray that ends at A[i-1]
    current_length = 1
    for i in range(1, len(A)):
        if A[i-1] < A[i]:
            current_length += 1
        else:
            current_length = 1
        if current_length > longest_length:
            longest_length = current_length
            count = 1
        elif current_length == longest_length:
            count += 1
    return count