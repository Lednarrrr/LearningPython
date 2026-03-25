# Exercise
'''
age=0
height=0.0
complex=0j

# Area of Triangle
base=int(input('Enter base: '))
height=int(input('Enter height: '))
areaTriangle=(height*base)/2
print('Area of triangle: ', areaTriangle)

# Perimeter of Triangle
a=int(input('Enter side a: '))
b=int(input('Enter side b: '))
c=int(input('Enter side c: '))
print('Perimeter of triangle: ', a+b+c)

# Area and Perimeter of Rectangle
length=int(input('Enter length: '))
width=int(input('Enter width: '))
print('Area of rectangle: ', length*width)
print('Perimeter of rectangle: ', 2*(length+width))

# Area and Circumference of Circle
radius=int(input('Enter radius: '))
pi=3.14
print('Area of circle: ', pi*radius**2)
print('Circumference of circle: ', 2*pi*radius)

# Slope with a given
slope=2
y_intercept=-2
x_intercept=y_intercept/slope
print('Slope: ', slope)
print('Y-intercept: ', y_intercept)
print('X-intercept: ', x_intercept)

# Slope
point1=(2,2)
point2=(6,10)
print('Slope: ', point2[1]-point1[1]/point2[0]-point1[0])
print('Euclidean distance: ', (((point2[0]-point1[0])*2)+((point2[1]-point1[1])*2))**0.5)

# Compare two slopes
print('First Slope: ', slope)
print('Second Slope: ', point2[1]-point1[1]/point2[0]-point1[0])

# Calculate for the value of y by finding the value of x
x=0
while(True):
    y=x**2+6*x+9
    if y==0:
        break
    else:
        print('Value is not 0')
        x-=1

print('Value of y:', y)
print('Value of x:', x)

# Calculate length then make it false
lenPython=len('python')
lenDragon=len('dragon')
print('Output:', lenPython is not lenDragon)

# Check if 'on' is found
word1='python'
word2='dragon'
print('Output:', 'on' in word1 and 'on' in word2)

# Check if 'jargon' is found
sentence='I hope this course is not full of jargon.'
print('Output:', 'jargon' in sentence)

# Check if 'on' is not found
print('Output:', 'on' not in word1 and 'on' not in word2)

# Conversion of len output to float and string
print('Output:', str(float(len(word1))))

# Divisible by 2
number=int(input('Enter a number: '))
print('Divisible by 2?:', number%2==0)

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
floor=7//3
compared=int(2.7)
print('Output:', floor == compared) # The solution to this can be this or it can be this with no int conversion to compared print('Output:', floor == compared//1)

# Comparison of type
print('Output:', type('10')==type(10))

# Conversion comparison
print('Output:', int(float('9.8'))==10)

# Calculation of weekly earning
hours=int(input('Enter hours: '))
rate=int(input('Enter rate per hour: '))
print('Your weekly earning is', hours*rate)

# Calculation of number of seconds in years
lifespan=int(input('Enter your age: '))
print('You have lived for', int(lifespan*365*24*60*60)) # the formula can also be this for more precision: lifespan*365.25*24*60*60

# display table
n=[1,2,3,4,5]
# The solution to this is that every column the exponent increases by 1 except the first column
print(n[0], n[0]**0, n[0]**1, n[0]**2, n[0]**3)
print(n[1], n[1]**0, n[1]**1, n[1]**2, n[1]**3)
print(n[2], n[2]**0, n[2]**1, n[2]**2, n[2]**3)
print(n[3], n[3]**0, n[3]**1, n[3]**2, n[3]**3)
print(n[4], n[4]**0, n[4]**1, n[4]**2, n[4]**3)
'''