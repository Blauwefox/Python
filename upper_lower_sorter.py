print'please type a string of stuff'
s = raw_input()

def up_low(s):
    splitter = s.split()
    lowercase_no = 0
    uppercase_no = 0
    
    for elem in splitter: 
        first_elem = elem[0] 
        lowercase = [c for c in first_elem if c.islower()]
        
        if lowercase != []:
            lowercase_no += 1 
        else: 
            uppercase_no +=1
        
    print 'No of lowercase characters :',lowercase_no
    print 'No of uppercase characters :',uppercase_no   
    
up_low(s)