# Condition Statements
# Indentation (4 spaces) is IMPORTANT in Python
# Atom automatically uses spaces for files with ".py" extention
# Python cares a LOT about how fat a line is indented.
# If you mix tabs and spaces,
# you may get "indentation errors" even everything looks fine

# ===One-way decision===#
for i in range(5) :
    print(i)
    if (i > 2) :
        print('Bigger than 2')
    print('Done with i', i)
print('All Done')

#===Two-way decision====#
x = 4

if x > 2 :
    print('Bigger')
else :
    print('Smaller')

print('All Done')

#===Multi-way decision===#
x= 20

if x < 2 :
    print('small')
elif x < 10 :
    print('medium')
else :
    print('large')
print('All Done')


#**********************#
if x < 2 :
    print('Below 2')
elif x < 20 :
    print('Below 20')
# This block will never be executed
elif x < 10 :
    print('Below 10')
else :
    print('Something else')
