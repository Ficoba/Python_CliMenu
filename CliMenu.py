import sys

class CliMenu:
	def __init__(self, title = "", noConfirmation = False, uniqueChoice = False, width = 50):
		self.noConfirmation = noConfirmation
		self.quit = False
		self.options = []
		self.previousMenu = False
		self.title = title
		self.uniqueChoice = uniqueChoice
		self.width = width
		self.header = ("{:=^" + str(self.width) + "s}").format(" " + self.title + " ")
		self.footer = "=" * self.width
	
	def getHeader(self):
		return self.header
	
	def setHeader(self, header):
		self.header = header
		
		return self
	
	def printHeader(self):
		print(self.header)
	
	def getFooter(self):
		return self.footer
	
	def setFooter(self, footer):
		self.footer = footer
		
		return self
	
	def printFooter(self):
		print(self.footer)
	
	def printChooices(self, isSubMenu = False):
		exitChoice = False
		
		# 1st loop to manage go to previous menu
		while not exitChoice:
			# 2nd loop to manage current menu displayed
			while not exitChoice:
				print("[ ] represents 'not selected'")
				print("[*] represents 'selected'\n")
				print("Choose:")
				
				if isSubMenu:
					print("\tp - Previous menu")
				
				print("\tq - Quit without execute action")
				
				if not self.noConfirmation:
					print("\tc to execute actions")
				
				if self.uniqueChoice:
					print("\t<number> - To Select item (other choice will be unselected)")
				else:
					print("\t<number> - To Select/Unselect item")
				
				if not self.uniqueChoice:
					print("\ta - Select all")
					print("\tu - Unselect all")
				
				print("")
				
				for optionKey, option in enumerate(self.options):
					selected = " "
					
					if option['selected']:
						selected = "*"
					
					print("[" + selected + "] " + str(optionKey) + " - " + option['label'])
					
				try:
					choice = str(input("\nEnter your choice: ").lower()).strip()
				except KeyboardInterrupt:
					sys.exit(0)
				
				if choice == "c" and not self.noConfirmation:
					exitChoice = True
				elif choice == "p" and isSubMenu:
					exitChoice = True
					self.unselectAllOptions()
					self.setPreviousMenu(True)
				elif choice == "q":
					exitChoice = True
					self.unselectAllOptions()
					self.setQuit(True)
				elif choice == "a" and not self.uniqueChoice:
					self.selectAllOptions()
					
					if self.noConfirmation:
						exitChoice = True
				elif choice == "u" and not self.uniqueChoice:
					self.unselectAllOptions()
					
					if self.noConfirmation:
						exitChoice = True
				else:
					choiceNr = -1
					
					try:
						choiceNr = int(choice)
						
						if choiceNr >= 0 and choiceNr < len(self.options):
							if self.uniqueChoice:
								self.unselectAllOptions()
								self.selectOption(choiceNr)
							else:
								self.switchSelectOption(choiceNr)
							
							if self.noConfirmation:
								exitChoice = True
						else:
							print("Please select a number between 0 and " + str(len(self.options) - 1))
					except Exception:
						print("Please enter a valid entry")
						pass
				
				print("")
			
			for optionSelected in self.getSelected():
				if isinstance(optionSelected['subMenu'], self.__class__):
					optionSelected['subMenu'].printMenu(isSubMenu = True)
					
					if optionSelected['subMenu'].getPreviousMenu():
						optionSelected['subMenu'].setPreviousMenu(False)
						exitChoice = False
					
					if optionSelected['subMenu'].getQuit():
						self.unselectAllOptions()
						self.setQuit(True)
	
	def printMenu(self, isSubMenu = False):
		self.printHeader()
		self.printChooices(isSubMenu)
		self.printFooter()
	
	def getNoConfirmation(self):
		return self.noConfirmation
	
	def setNoConfirmation(self, noConfirmation):
		self.noConfirmation = noConfirmation
		
		return self
	
	def getPreviousMenu(self):
		return self.previousMenu
	
	def setPreviousMenu(self, previousMenu):
		self.previousMenu = previousMenu
		
		return self
	
	def getTitle(self):
		return self.title
	
	def setTitle(self, title):
		self.title = title
		
		return self
	
	def getUniqueChoice(self):
		return self.uniqueChoice
	
	def setUniqueChoice(self, uniqueChoice):
		self.uniqueChoice = uniqueChoice
		
		return self
	
	def getWidth(self):
		return self.width
	
	def setWidth(self, width):
		self.width = width
		
		return self
	
	#
	## Options methods
	def getQuit(self):
		return self.quit
	
	def setQuit(self, quit):
		self.quit = quit
		
		return self
	
	def getOption(self, index):
		return self.options[index]
	
	def getOptions(self):
		return self.options
	
	def getOptionExtraInformation(self, index):
		return self.options[index]['extraInformation']
	
	def setOptionExtraInformation(self, index, extraInformation):
		self.options[index]['extraInformation'] = extraInformation
		
		return self
	
	def getOptionsExtraInformation(self):
		extraInformations = []
		
		for option in self.options:
			extraInformations.append(option['extraInformation'])
		
		return extraInformations
	
	def getOptionLabel(self, index):
		return self.options[index]['label']
	
	def setOptionLabel(self, index, label):
		self.options[index]['label'] = label
		
		return self
	
	def getOptionsLabel(self):
		labels = []
		
		for option in self.options:
			labels.append(option['label'])
		
		return labels
	
	def getOptionSubMenu(self, index):
		return self.options[index]['subMenu']
	
	def setOptionSubMenu(self, index, subMenu):
		self.options[index]['subMenu'] = subMenu
		
		return self
	
	def getOptionsSubMenu(self):
		subMenus = []
		
		for option in self.options:
			subMenus.append(option['subMenu'])
		
		return subMenus
	
	def addOption(self, label, selected = False, extraInformation = None, subMenu = None):
		self.options.append({ "label": label, "selected": selected, "extraInformation": extraInformation, "subMenu": subMenu })
		
		return self
	
	def clearOptions(self):
		self.options = []
		
		return self
	
	def removeOption(self, index):
		del self.options[index]
		
		return self
	
	def getSelected(self):
		selected = []
		
		for option in self.options:
			if option['selected']:
				selected.append(option)
		
		return selected
	
	def getSelectedIndex(self):
		selected = []
		
		for optionKey, option in enumerate(self.options):
			if option['selected']:
				selected.append(optionKey)
		
		return selected
	
	def getSelectedIndexes(self):
		selected = []
		subSelected = []
		
		for optionKey, option in enumerate(self.options):
			if option['selected']:
				if isinstance(option['subMenu'], self.__class__):
					subSelected = [ optionKey, option['subMenu'].getSelectedIndex() ]
				else:
					subSelected = [ optionKey ]
				
				selected.append(subSelected)
		
		return selected
	
	def getSelectedLabel(self):
		selected = []
		
		for option in self.options:
			if option['selected']:
				selected.append(option['label'])
		
		return selected
	
	def getSelectedLabels(self):
		selected = []
		subSelected = []
		
		for option in self.options:
			if option['selected']:
				if isinstance(option['subMenu'], self.__class__):
					subSelected = [ option['label'], option['subMenu'].getSelectedLabel() ]
				else:
					subSelected = [ option['label'] ]
				
				selected.append(subSelected)
		
		return selected
	
	def selectAllOptions(self):
		for option in self.options:
			option['selected'] = True
	
	def selectOption(self, index):
		self.options[index]['selected'] = True
	
	def unselectAllOptions(self):
		for option in self.options:
			option['selected'] = False
	
	def unselectOption(self, index):
		self.options[index]['selected'] = False
	
	def switchSelectOption(self, index):
		self.options[index]['selected'] = not self.options[index]['selected']
