L=[9,8,4,5,6,3,2,7,1]
# solution below
even_number=[]
odd_number=[]
for x in L:
    if x%2==0:
        even_number.append(x)
    else:
        odd_number.append(x)
        
sorted_even = sorted(even_number,reverse=True)
sorted_odd = sorted(odd_number,reverse=True)

result=sorted_odd+sorted_even
print(result)
        