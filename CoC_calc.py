import sys

#prompt user to select unit
print """pick a number that correspondes to a unit:
	1. Barbarian
	2. Archer
	3. Giant
	4. Goblin
	5. Wall Breaker
	6. Balloon
	7. Wizard
	8. Healer
	9. Dragon
	10. Pekka
	"""
unit = int(input())

#prompt user to select upgrade level
print "enter the upgrade level of the unit"
upgrade_level=int(input())

#prompt user to enter number of units
print "enter number of the units to be made"
number_units=int(input())


		
#math to calculate costs	
def cost(unit, upgrade_level, number_units):
	if unit==1:
		if upgrade_level==1:
			cost=number_units*25
		elif upgrade_level==2:
			cost=number_units * 40
		elif upgrade_level==3:
			cost=number_units * 60
		elif upgrade_level==4:
			cost=number_units * 80
		elif upgrade_level==5:
			cost=number_units * 100
		elif upgrade_level==6:
			cost=number_units * 150
		elif upgrade_level==7:
			cost=number_units * 200
		else:
			sys.exit("thats not a valid upgrade")
	
	elif unit==2:
	#if this is 'if' and not elif it returns not a valid unit. why?
		if upgrade_level==1:
			cost=number_units * 50
		elif upgrade_level==2:
			cost=number_units * 80
		elif upgrade_level==3:
			cost=number_units * 120
		elif upgrade_level==4:
			cost=number_units * 160
		elif upgrade_level==5:
			cost=number_units * 200
		elif upgrade_level==6:
			cost=number_units * 300
		elif upgrade_level==7:
			cost=number_units * 400
		else:
			sys.exit("thats not a valid upgrade")
			
	elif unit==3:
		if upgrade_level==1:
			cost=number_units * 250
		elif upgrade_level==2:
			cost=number_units * 750
		elif upgrade_level==3:
			cost=number_units * 1250
		elif upgrade_level==4:
			cost=number_units * 1750
		elif upgrade_level==5:
			cost=number_units * 2250
		elif upgrade_level==6:
			cost=number_units * 3000
		elif upgrade_level==7:
			cost=number_units * 3500
		else:
			sys.exit("thats not a valid upgrade")
	
	elif unit==4:
		if upgrade_level==1:
			cost=number_units * 25
		elif upgrade_level==2:
			cost=number_units * 40
		elif upgrade_level==3:
			cost=number_units * 60
		elif upgrade_level==4:
			cost=number_units * 80
		elif upgrade_level==5:
			cost=number_units * 100
		elif upgrade_level==6:
			cost=number_units * 150
		else:
			sys.exit("thats not a valid upgrade")
	
	elif unit==5:
		if upgrade_level==1:
			cost=number_units * 1000
		elif upgrade_level==2:
			cost=number_units * 1500
		elif upgrade_level==3:
			cost=number_units * 2000
		elif upgrade_level==4:
			cost=number_units * 2500
		elif upgrade_level==5:
			cost=number_units * 3000
		elif upgrade_level==6:
			cost=number_units * 3500
		else:
			sys.exit("thats not a valid upgrade")
		
	elif unit==6:
		if upgrade_level==1:
			cost=number_units * 2000
		elif upgrade_level==2:
			cost=number_units * 2500
		elif upgrade_level==3:
			cost=number_units * 3000
		elif upgrade_level==4:
			cost=number_units * 3500
		elif upgrade_level==5:
			cost=number_units * 4000
		elif upgrade_level==6:
			cost=number_units * 4500
		else:
			sys.exit("thats not a valid upgrade")
			
	elif unit==7:
		if upgrade_level==1:
			cost=number_units * 1500
		elif upgrade_level==2:
			cost=number_units * 2000
		elif upgrade_level==3:
			cost=number_units * 2500
		elif upgrade_level==4:
			cost=number_units * 3000
		elif upgrade_level==5:
			cost=number_units * 3500
		elif upgrade_level==6:
			cost=number_units * 4000
		else:
			sys.exit("thats not a valid upgrade")
	
	elif unit==8:
		if upgrade_level==1:
			cost=number_units * 5000
		elif upgrade_level==2:
			cost=number_units * 6000
		elif upgrade_level==3:
			cost=number_units * 8000
		elif upgrade_level==4:
			cost=number_units * 10000
		else:
			sys.exit("thats not a valid upgrade")
			
	elif unit==9:
		if upgrade_level==1:
			cost=number_units * 25000
		elif upgrade_level==2:
			cost=number_units * 30000
		elif upgrade_level==3:
			cost=number_units * 36000
		elif upgrade_level==4:
			cost=number_units * 42000
		else:
			sys.exit("thats not a valid upgrade")
			
	elif unit==10:
		if upgrade_level==1:
			cost=number_units * 30000
		elif upgrade_level==2:
			cost=number_units * 35000
		elif upgrade_level==3:
			cost=number_units * 40000
		elif upgrade_level==4:
			cost=number_units * 45000
		elif upgrade_level==5:
			cost=number_units * 50000
		else:
			sys.exit("thats not a valid upgrade")
	else:
		sys.exit('thats not a valid unit')
	return cost	
		

#adding costs of multiple unit styles together	

			
#unit(input)
#upgrade_level(input)
#number_units(input)

print cost(unit, upgrade_level, number_units)

#trying to make it so different unit types can be added to the total
def total():
	single_unit=cost(unit, upgrade_level, number_units)
	print "do you want to add more units?"
	response =raw_input()
	while response.lower() == "yes" or "y":
		single_unit += cost(unit, upgrade_level, number_units)
		break
		print single_unit
