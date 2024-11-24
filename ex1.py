''' Exercise #1 '''

#########################################
# Question 1 - do not delete this comment
#########################################
S = 100.0 # Replace ??? with a positive float of your choice.
AB = 30.0 # Replace ??? with a positive float of your choice.
BC = 15.0 # Replace ??? with a positive float of your choice.
AD = 15.0 # Replace ??? with a positive float of your choice.
DC = 10.0 # Replace ??? with a positive float of your choice.
# Write the rest of the code for question 1 below here.
Heikef=(AB+BC+AD+DC)
print("Perimeter is: {0}".format(Heikef))
emtza=(AB+DC)/2
print("Midsegment is: {0}".format(emtza))
height=(2*S)/(AB+DC)
print("Height is:{0}".format(height))




#########################################
# Question 2 - do not delete this comment
#########################################
my_name = 'liav' # Replace ??? with a string of your choice.
# Write the rest of the code for question 2 below here.
my_name=my_name.title()
print("Hello {0} :)".format(my_name))


#########################################
# Question 3 - do not delete this comment
#########################################
number  = 49 # Replace ??? with a string of your choice.
# Write the rest of the code for question 3 below here.
temp_num=number%7
if temp_num==0:
    print("i am {0} and i am divisibe by 7".format(number))
else:
    print("i am {0} and i am not divisible by 7".format(number))



#########################################
# Question 4 - do not delete this comment
#########################################
text = "tom" # Replace ??? with a string of your choice.
copies = 3  # Replace ??? with a positive int of your choice.
# Write the rest of the code for question 4 below here.

#making sub1+sub2
sub1=""
sub2=""
for i in range(len(text)):
    if i%2==0:
        sub2+=text[i]
    else:
        sub1+=text[i]
new_str=sub1+sub2

#printing format
for_print=""
for i in range(copies):
    for_print+=new_str
print (for_print)


#########################################
# Question 5 - do not delete this comment
#########################################
sub1=""
sub2=""
name ='droLtromedloV' # Replace ??? with a string of your choice.
q = -4 # Replace ??? with a int of your choice.
# Write the rest of the code for question 5 below here.

if q<0 or q>=len(name) or name=="":
     print("Error: illegal input!")
else:
    for i in range(q):
        sub1+=name[i]
    for j in range(q,len(name)):
        sub2+=name[j]

    temps1=""
    temps2=""
    for i in range(len(sub1)-1,-1,-1):
        temps1+=sub1[i]
    for i in range(len(sub2)-1,-1,-1):
        temps2+=sub2[i]
    sub2=temps2
    sub1=temps1

    
    print ("{0} {1}".format(sub1,sub2))



