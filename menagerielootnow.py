from os import system, name
import time

# SO FAR, WHOLE COMPLETED SEGMENTS ARE: SUB MGs, SNIPERS, ROCKET LAUNCHERS AND HEAVY MGs.

# DEFINED EXTRAS - CLEARING OUTPUT AND ERROR MESSAGE

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

def invalidAnswer():
	print('Invalid answer. Please try again.')
	time.sleep(1)
	clear()

# HEAVY MACHINE GUNS

def heavyMGs():
	heavyCAT01 = input("Heavy Machine Guns:\n1 - Fixed Odds\n99 - Return to Weapon Menu\nPlease pick a number from 1 / 99: ")
	if heavyCAT01 == '1':
		clear()
		fixedOdds()
	elif heavyCAT01 == '99':
		clear()
		lootWeapons()
	else:
		clear()
		invalidAnswer()
		heavyMGs()

def fixedOdds():
	returnToMenu = input("Rune combination...\nSlot 1 (Red): Ambition\nSlot 2 (Blue): Any\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		heavyMGs()
	else:
		clear()
		invalidAnswer()
		fixedOdds()

# ROCKET LAUNCHERS

def rocketLaunchers():
	rocketCAT01 = input("Rocket Launchers:\n1 - Bad Omens\n2 - Zenobia-D\n3 - Sleepless\n99 - Return to Weapon Menu\nPlease pick a number from 1-3 / 99: ")
	if rocketCAT01 == '1':
		clear()
		badOmens()
	elif rocketCAT01 == '2':
		clear()
		zenobiaD()
	elif rocketCAT01 == '3':
		clear()
		Sleepless()
	elif rocketCAT01 == '99':
		clear()
		lootWeapons()
	else:
		clear()
		invalidAnswer()
		rocketLaunchers()

def badOmens():
	returnToMenu = input("Rune combination...\nSlot 1 (Red): Ambition\nSlot 2 (Purple): Any\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		rocketLaunchers()
	else:
		clear()
		invalidAnswer()
		badOmens()

def zenobiaD():
	returnToMenu = input("Rune combination...\nSlot 1 (Red): Ambition\nSlot 2 (Red): Any\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		rocketLaunchers()
	else:
		clear()
		invalidAnswer()
		zenobiaD()

def Sleepless():
	returnToMenu = input("Rune combination...\nSlot 1 (Red): Ambition\nSlot 2 (Green): Any\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		rocketLaunchers()
	else:
		clear()
		invalidAnswer()
		Sleepless()

# SNIPERS

def snipers():
	snipersCAT01 = input("Snipers:\n1 - Twilight Oath\n2 - Beloved\n3 - Fate Cries Fowl\n4 - Dreaded Venture\n99 - Return to Weapon Menu\nPlease pick a number from 1-4 / 99: ")
	if snipersCAT01 == '1':
		clear()
		twilightOath()
	elif snipersCAT01 == '2':
		clear()
		beloved()
	elif snipersCAT01 == '3':
		clear()
		fateCriesFowl()
	elif snipersCAT01 == '4':
		clear()
		dreadedVenture()
	elif snipersCAT01 == '99':
		clear()
		lootWeapons()
	else:
		clear()
		invalidAnswer()
		snipers()

def twilightOath():
	returnToMenu = input("Rune combination...\nSlot 1 (Purple): Jubilation\nSlot 2 (Purple): Any\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		snipers()
	else:
		clear()
		invalidAnswer()
		twilightOath()

def beloved():
	returnToMenu = input("Rune combination...\nSlot 1 (Purple): Jubilation\nSlot 2 (Red): Any\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		snipers()
	else:
		clear()
		invalidAnswer()
		beloved()

def fateCriesFowl():
	returnToMenu = input("Rune combination...\nSlot 1 (Purple): Jubilation\nSlot 2 (Green): Any\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		snipers()
	else:
		clear()
		invalidAnswer()
		fateCriesFowl()

def dreadedVenture():
	returnToMenu = input("Rune combination...\nSlot 1 (Purple): Jubilation\nSlot 2 (Purple): Any\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		snipers()
	else:
		clear()
		invalidAnswer()
		dreadedVenture()

# SUB MACHINE GUNS

def subMGs():
	smgCAT01 = input("Sub Machine Guns:\n1 - CalusMiniTool\n2 - TracklessWaste\n3 - HardTruths\n4 - BadReputation\n99 - Return to Weapon Menu\nPlease pick a number from 1-4 / 99: ")
	if smgCAT01 == '1':
		clear()
		calusMiniTool()
	elif smgCAT01 == '2':
		clear()
		tracklessWaste()
	elif smgCAT01 == '3':
		clear()
		hardTruths()
	elif smgCAT01 == '4':
		clear()
		badReputation()
	elif smgCAT01 == '99':
		clear()
		lootWeapons()
	else:
		clear()
		invalidAnswer()
		subMGs()

def calusMiniTool():
	returnToMenu = input("Rune combination...\nSlot 1 (Purple): Beast\nSlot 2 (Purple): Any\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		subMGs()
	else:
		clear()
		invalidAnswer()
		calusMiniTool()

def tracklessWaste():
	returnToMenu = input("Rune combination...\nSlot 1 (Purple): Beast\nSlot 2 (Red): Any\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		subMGs()
	else:
		clear()
		invalidAnswer()
		tracklessWaste()

def hardTruths():
	returnToMenu = input("Rune combination...\nSlot 1 (Purple): Beast\nSlot 2 (Green): Any\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		subMGs()
	else:
		clear()
		invalidAnswer()
		hardTruths()

def badReputation():
	returnToMenu = input("Rune combination...\nSlot 1 (Purple): Beast\nSlot 2 (Purple): Any\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		subMGs()
	else:
		clear()
		invalidAnswer()
		badReputation()

# HAND CANNONS

def handCannons():
	handCannonCAT01 = input("Hand Cannons:\n1 - Trust\n2 - Austringer\n3 - Waking Vigil\n99 - Return to Weapon Menu\nPlease pick a number from 1-3 / 99: ")
	if handCannonCAT01 == '1':
		clear()
		trust()
	elif handCannonCAT01 == '2':
		clear()
		austringer()
	elif handCannonCAT01 == '3':
		clear()
		wakingVigil()
	elif handCannonCAT01 == '99':
		clear()
		lootWeapons()
	else:
		clear()
		invalidAnswer()
		handCannons()

def trust():
	returnToMenu = input("Rune combination...\nSlot 1 (Green): Desire\nSlot 2 (Purple): Beast\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		handCannons()
	else:
		clear()
		invalidAnswer()
		trust()

def austringer():
	returnToMenu = input("Rune combination...\nSlot 1 (Green): Desire\nSlot 2 (Purple): Jubilation\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		handCannons()
	else:
		clear()
		invalidAnswer()
		austringer()

def wakingVigil():
	returnToMenu = input("Rune combination...\nSlot 1 (Green): Desire\nSlot 2 (Red): Ambition\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		handCannons()
	else:
		clear()
		invalidAnswer()
		wakingVigil()

# SIDEARMS

def sidearms():
	sidearmCAT01 = input("Sidearms:\n1 - Pribina-D\n2 - Drang (Baroque)\n3 - The Last Dance\n4 - Anonymous Autumn\n5 - Smuggler's Word\n99 - Return to Weapon Menu\nPlease pick a number from 1-5 / 99: ")
	if sidearmCAT01 == '1':
		clear()
		pribinaD()
	elif sidearmCAT01 == '2':
		clear()
		drangBaroque()
	elif sidearmCAT01 == '3':
		clear()
		theLastDance()
	elif sidearmCAT01 == '4':
		clear()
		anonymousAutumn()
	elif sidearmCAT01 == '5':
		clear()
		smugglersWord()
	elif sidearmCAT01 == '99':
		clear()
		lootWeapons()
	else:
		clear()
		invalidAnswer()
		sidearms()

def pribinaD():
	returnToMenu = input("Rune combination...\nSlot 1 (Green): Desire\nSlot 2 (Green): Desire\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		sidearms()
	else:
		clear()
		invalidAnswer()
		pribinaD()

def drangBaroque():
	returnToMenu = input("Rune combination...\nSlot 1 (Green): Pride\nSlot 2 (Purple): Beast\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		sidearms()
	else:
		clear()
		invalidAnswer()
		drangBaroque()

def theLastDance():
	returnToMenu = input("Rune combination...\nSlot 1 (Green): Pride\nSlot 2 (Purple): Jubilation\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		sidearms()
	else:
		clear()
		invalidAnswer()
		theLastDance()

def anonymousAutumn():
	returnToMenu = input("Rune combination...\nSlot 1 (Green): Pride\nSlot 2 (Red): Ambition\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		sidearms()
	else:
		clear()
		invalidAnswer()
		anonymousAutumn()

def smugglersWord():
	returnToMenu = input("Rune combination...\nSlot 1 (Green): Pride\nSlot 2 (Green): Desire\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		sidearms()
	else:
		clear()
		invalidAnswer()
		smugglersWord()

# FUSION RIFLES

def fusionRifles():
	fusionCAT01 = input("Fusion Rifles:\n1 - Proelium FR3\n2 - Main Ingredient\n3 - The Epicurean\n4 - Erentil FR4\n99 - Return to Weapon Menu\nPlease pick a number from 1-4 / 99: ")
	if fusionCAT01 == '1':
		clear()
		proeliumFR3()
	elif fusionCAT01 == '2':
		clear()
		mainIngredient()
	elif fusionCAT01 == '3':
		clear()
		theEpicurean()
	elif fusionCAT01 == '4':
		clear()
		erentilFR4()
	elif fusionCAT01 == '99':
		clear()
		lootWeapons()
	else:
		clear()
		invalidAnswer()
		fusionRifles()

def proeliumFR3():
	returnToMenu = input("Rune combination...\nSlot 1 (Blue): Excess\nSlot 2 (Purple): Beast\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		fusionRifles()
	else:
		clear()
		invalidAnswer()
		proeliumFR3()

def mainIngredient():
	returnToMenu = input("Rune combination...\nSlot 1 (Blue): Excess\nSlot 2 (Purple): Jubilation\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		fusionRifles()
	else:
		clear()
		invalidAnswer()
		mainIngredient()

def theEpicurean():
	returnToMenu = input("Rune combination...\nSlot 1 (Blue): Excess\nSlot 2 (Red): Ambition\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		fusionRifles()
	else:
		clear()
		invalidAnswer()
		theEpicurean()

def erentilFR4():
	returnToMenu = input("Rune combination...\nSlot 1 (Blue): Excess\nSlot 2 (Green): Desire\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		fusionRifles()
	else:
		clear()
		invalidAnswer()
		erentilFR4()

# SHOTGUNS

def shotguns():
	shotgunCAT01 = input("Shotguns:\n1 - Badlander\n2 - Parcel of Stardust\n3 - Imperial Decree\n4 - Dust Rock Blues\n99 - Return to Weapon Menu\nPlease pick a number from 1-4 / 99: ")
	if shotgunCAT01 == '1':
		clear()
		badlander()
	elif shotgunCAT01 == '2':
		clear()
		parcelOfStardust()
	elif shotgunCAT01 == '3':
		clear()
		imperialDecree()
	elif shotgunCAT01 == '4':
		clear()
		dustRockBlues()
	elif shotgunCAT01 == '99':
		clear()
		lootWeapons()
	else:
		clear()
		invalidAnswer()
		shotguns()

def badlander():
	returnToMenu = input("Rune combination...\nSlot 1 (Blue): Wealth\nSlot 2 (Purple): Beast\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		shotguns()
	else:
		clear()
		invalidAnswer()
		badlander()

def parcelOfStardust():
	returnToMenu = input("Rune combination...\nSlot 1 (Blue): Wealth\nSlot 2 (Purple): Jubilation\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		shotguns()
	else:
		clear()
		invalidAnswer()
		parcelOfStardust()

def imperialDecree():
	returnToMenu = input("Rune combination...\nSlot 1 (Blue): Wealth\nSlot 2 (Red): Ambition\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		shotguns()
	else:
		clear()
		invalidAnswer()
		imperialDecree()

def dustRockBlues():
	returnToMenu = input("Rune combination...\nSlot 1 (Blue): Wealth\nSlot 2 (Green): Desire\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		shotguns()
	else:
		clear()
		invalidAnswer()
		dustRockBlues()

# THE MAIN MENUS

def lootWeapons():
	clear()
	cat01 = input("Chalice of Opulence weapon loot pool:\n1 - Sub MGs\n2 - Snipers\n3 - Rocket Launchers\n3.1 - Heavy MGs\n4 - Hand Cannons\n5 - Sidearms\n6 - Fusion Rifles\n7 - Shotguns\n99 - Return to Menu\nPlease pick a number from 1-7 / 99: ")
	if cat01 == '1':
		clear()
		subMGs()
	elif cat01 == '2':
		clear()
		snipers()
	elif cat01 == '3':
		clear()
		rocketLaunchers()
	elif cat01 == '3.1':
		clear()
		heavyMGs()
	elif cat01 == '4':
		clear()
		handCannons()
	elif cat01 == '5':
		clear()
		sidearms()
	elif cat01 == '6':
		clear()
		fusionRifles()
	elif cat01 == '7':
		clear()
		shotguns()
	elif cat01 == '99':
		clear()
		mainMenu()
	else:
		clear()
		invalidAnswer()
		lootWeapons()

def mainMenu():
	clear()
	cat01 = input("Hi User. Welcome to MenagerieLootNow. Please select one of the following.\n1 - Weapons\n2 - Armour\nChoice: ")
	if cat01 == '1':
		clear()
		lootWeapons()
	elif cat01 == '2':
		clear()
		lootArmour()
	else:
		clear()
		invalidAnswer()
		mainMenu()

# ARMOR SYSTEM

def lootArmour():
	clear()
	armourCat01 = input("Chalice of Opulence armor loot pool:\n1 - Class Items (Mobility/Recovery/Resilience)\n2 - Helmets\n3 - Gauntlets\n4 - Chest Armor\n5 - Leg Armor\n99 - Return to Menu\nPlease pick a number from 1-5 / 99: ")
	if armourCat01 == '1':
		clear()
		classItems()
	elif armourCat01 == '2':
		clear()
		helmets()
	elif armourCat01 == '3':
		clear()
		gauntlets()
	elif armourCat01 == '4':
		clear()
		chestArmor()
	elif armourCat01 == '5':
		clear()
		legArmor()
	elif armourCat01 == '99':
		clear()
		mainMenu()
	else:
		clear()
		invalidAnswer()
		lootArmour()

# CLASS ITEMS

def classItems():
	classCAT01 = input("Class Items:\n1 - Mobility Focus\n2 - Recovery Focus\n3 - Resilience Focus\n99 - Return to Armor Menu\nPlease pick a number from 1-3 / 99: ")
	if classCAT01 == '1':
		clear()
		mobilityClass()
	elif classCAT01 == '2':
		clear()
		recoveryClass()
	elif classCAT01 == '3':
		clear()
		resilienceClass()
	elif classCAT01 == '99':
		clear()
		lootArmour()
	else:
		clear()
		invalidAnswer()
		classItems()

def mobilityClass():
	returnToMenu = input("Rune combination...\nSlot 1 (Purple): Joy\nSlot 2 (Purple): Any\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		classItems()
	else:
		clear()
		invalidAnswer()
		mobilityClass()

def recoveryClass():
	returnToMenu = input("Rune combination...\nSlot 1 (Red): Cunning\nSlot 2 (Purple): Any\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		classItems()
	else:
		clear()
		invalidAnswer()
		recoveryClass()

def resilienceClass():
	returnToMenu = input("Rune combination...\nSlot 1 (Red): Gluttony\nSlot 2 (Purple): Any\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		classItems()
	else:
		clear()
		invalidAnswer()
		resilienceClass()

# HELMETS

def helmets():
	helmetCAT01 = input("Helmets:\n1 - Mobility Focus\n2 - Recovery Focus\n3 - Resilience Focus\n99 - Return to Armor Menu\nPlease pick a number from 1-3 / 99: ")
	if helmetCAT01 == '1':
		clear()
		mobilityHelmet()
	elif helmetCAT01 == '2':
		clear()
		recoveryHelmet()
	elif helmetCAT01 == '3':
		clear()
		resilienceHelmet()
	elif helmetCAT01 == '99':
		clear()
		lootArmour()
	else:
		clear()
		invalidAnswer()
		helmets()

def mobilityHelmet():
	returnToMenu = input("Rune combination...\nSlot 1 (Green): War\nSlot 2 (Purple): Joy\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		helmets()
	else:
		clear()
		invalidAnswer()
		mobilityHelmet()

def recoveryHelmet():
	returnToMenu = input("Rune combination...\nSlot 1 (Green): War\nSlot 2 (Red): Cunning\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		helmets()
	else:
		clear()
		invalidAnswer()
		recoveryHelmet()

def resilienceHelmet():
	returnToMenu = input("Rune combination...\nSlot 1 (Green): War\nSlot 2 (Red): Gluttony\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		helmets()
	else:
		clear()
		invalidAnswer()
		resilienceHelmet()

# GAUNTLETS

def gauntlets():
	gauntletCAT01 = input("Gauntlets:\n1 - Mobility Focus\n2 - Recovery Focus\n3 - Resilience Focus\n99 - Return to Armor Menu\nPlease pick a number from 1-3 / 99: ")
	if gauntletCAT01 == '1':
		clear()
		mobilityGauntlets()
	elif gauntletCAT01 == '2':
		clear()
		recoveryGauntlets()
	elif gauntletCAT01 == '3':
		clear()
		resilienceGauntlets()
	elif gauntletCAT01 == '99':
		clear()
		lootArmour()
	else:
		clear()
		invalidAnswer()
		gauntlets()

def mobilityGauntlets():
	returnToMenu = input("Rune combination...\nSlot 1 (Red): Cunning\nSlot 2 (Purple): Joy\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		gauntlets()
	else:
		clear()
		invalidAnswer()
		mobilityGauntlets()

def recoveryGauntlets():
	returnToMenu = input("Rune combination...\nSlot 1 (Red): Cunning\nSlot 2 (Red): Cunning\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		gauntlets()
	else:
		clear()
		invalidAnswer()
		recoveryGauntlets()

def resilienceGauntlets():
	returnToMenu = input("Rune combination...\nSlot 1 (Red): Cunning\nSlot 2 (Red): Gluttony\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		gauntlets()
	else:
		clear()
		invalidAnswer()
		resilienceGauntlets()

# CHEST ARMOR

def chestArmor():
	chestCAT01 = input("Chest Armor:\n1 - Mobility Focus\n2 - Recovery Focus\n3 - Resilience Focus\n99 - Return to Armor Menu\nPlease pick a number from 1-3 / 99: ")
	if chestCAT01 == '1':
		clear()
		mobilityChest()
	elif chestCAT01 == '2':
		clear()
		recoveryChest()
	elif chestCAT01 == '3':
		clear()
		resilienceChest()
	elif chestCAT01 == '99':
		clear()
		lootArmour()
	else:
		clear()
		invalidAnswer()
		chestArmor()

def mobilityChest():
	returnToMenu = input("Rune combination...\nSlot 1 (Blue): Pleasure\nSlot 2 (Purple): Joy\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		chestArmor()
	else:
		clear()
		invalidAnswer()
		mobilityChest()

def recoveryChest():
	returnToMenu = input("Rune combination...\nSlot 1 (Blue): Pleasure\nSlot 2 (Red): Cunning\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		chestArmor()
	else:
		clear()
		invalidAnswer()
		recoveryChest()

def resilienceChest():
	returnToMenu = input("Rune combination...\nSlot 1 (Blue): Pleasure\nSlot 2 (Red): Gluttony\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		chestArmor()
	else:
		clear()
		invalidAnswer()
		resilienceChest()

# LEG ARMOR

def legArmor():
	legCAT01 = input("Leg Armor:\n1 - Mobility Focus\n2 - Recovery Focus\n3 - Resilience Focus\n99 - Return to Armor Menu\nPlease pick a number from 1-3 / 99: ")
	if legCAT01 == '1':
		clear()
		mobilityLegs()
	elif legCAT01 == '2':
		clear()
		recoveryLegs()
	elif legCAT01 == '3':
		clear()
		resilienceLegs()
	elif legCAT01 == '99':
		clear()
		lootArmour()
	else:
		clear()
		invalidAnswer()
		legArmor()

def mobilityLegs():
	returnToMenu = input("Rune combination...\nSlot 1 (Red): Gluttony\nSlot 2 (Purple): Joy\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		legArmor()
	else:
		clear()
		invalidAnswer()
		mobilityLegs()

def recoveryLegs():
	returnToMenu = input("Rune combination...\nSlot 1 (Red): Gluttony\nSlot 2 (Red): Cunning\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		legArmor()
	else:
		clear()
		invalidAnswer()
		recoveryLegs()

def resilienceLegs():
	returnToMenu = input("Rune combination...\nSlot 1 (Red): Gluttony\nSlot 2 (Red): Gluttony\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		legArmor()
	else:
		clear()
		invalidAnswer()
		resilienceLegs()

mainMenu()