
#bitwise operation works only on integers 
n1, n2 = 20, 50

# Bitwise XOR is used in some encryption techniques.
# Networking protocols often involve bitwise operations for tasks such as setting or extracting specific fields in packet headers.
# Example: IP address manipulation, subnetting.
# Bitwise operations are common in embedded systems programming where memory and processing resources are limited
# Bitwise operations can be used to optimize certain algorithms for performance, particularly in scenarios where
# bitwise operations are more efficient than arithmetic operations.

#printing bitwise OR operations
print('bitwise OR of',+n1,'and',+n2,'is :', n1 | n2)  

#printing bitwise AND operations
print('bitwise AND of',+n1,'and',+n2,'is :', n1 & n2)  

#printing bitwise XOR operations
print('bitwise XOR of',+n1,'and',+n2,'is :', n1 ^ n2)  

#printing bitwise NOT operations
print('bitwise NOT ~ of',+n2,'is :', ~n2)

#printing bitwise leftshift operations
n3 = n2 << 2 
print('bitwise leftshift ~ of',+n2,'is :',n3 )

#printing bitwise right shift operations
print('bitwise right shift ~ of',+n3,'is :', n3 >> 2 )
