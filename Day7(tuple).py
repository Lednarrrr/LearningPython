'''
# Exercise Level 1
# 1. Create an empty tuple
empty_tpl=()
'''
# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers=('John', 'Albert', 'Chris')
sisters=('Rose', 'Daisy', 'Alex')
# 3. Join brothers and sisters tuples and assign it to siblings
siblings=brothers+sisters
# 4. How many siblings do you have?
print(f'I have {len(siblings)} siblings')
# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
temp=list(siblings)
temp.append('Steve')
temp.append('Ari')
family_members=tuple(temp)
print(family_members)
# A shortcut way
family_members=siblings+('Steve', 'Ari')
print(family_members)
# Exercise Level 2
# 1. Unpack siblings and parents from family_members
*unpackedSiblings, unpackedFather, unpackedMother=family_members
print(unpackedSiblings)
print(unpackedFather)
print(unpackedMother)
# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits=('Banana', 'Apple')
vegetables=('Lettuce', 'Cabbage')
animal_products=('Chicken', 'Pork')
food_stuff_tp=fruits+vegetables+animal_products
print(food_stuff_tp)
# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt=list(food_stuff_tp)
# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middleItem=food_stuff_tp[(len(food_stuff_tp)-1)//2:(len(food_stuff_tp)//2)+1]
print(middleItem)
# 5. Slice out the first three items and the last three items from food_stuff_lt list
firstThree=food_stuff_tp[:3]
lastThree=food_stuff_tp[-3:]
print(firstThree)
print(lastThree)
# 6. Delete the food_stuff_tp tuple completely
del food_stuff_tp
#print(food_stuff_tp)
# 7. Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country
# nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)