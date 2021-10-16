

menu=[
	{
		"name":"Appetizers",
		"available_types":["Wings","Cookies","Spring Rolls"]
	},{
		"name":"Entrees",
		"available_types":["Salmon","Steak","Meat Tornado","A Literal Garden"]
	},{
		"name":"Desserts",
		"available_types":["Ice Cream","Cake","Pie"]
	},{
		"name":"Drinks",
		"available_types":["Coffee","Tea","Unicorn Tears"]
	}
]

available_menu=['wings', 'cookies',
     'spring rolls', 'salmon',
      'steak', 'meat tornado',
      'a literal garden', 'ice Cream',
       'cake', 'pie', 'coffee',
        'tea', 'unicorn tears']

 

def handle_print():
	"""this function will prent the welcoming msg to the user 
	takes no argument
	return nothing"""
	print ("""**************************************
**    Welcome to the Snakes Cafe!🐍 **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************""")
	for i in menu:
	  print(i["name"])
	  print("----------")
	  for y in i["available_types"]:
	   print(y)
	print()
	print("""***********************************
** What would you like to order? **
***********************************""")	 
	

		
order_list=[]	    
def handle_order():
	"""this function will take the user order and will add it to a list and will keep asking the user for the next item until the user type quit also will count how many time the user asked for the same order also if the user type an order not in the list the function will till him to type from the menu and will provide the user of how many time asked for the same order """
	order=input("> ")
	if order != "quit":
		if order in available_menu:
			
			order_list.append(order)
			if order in order_list:
				count=0
				for i in order_list:
					if i==order:
						count+=1
				print(f"** {count} order of {order} have been added to your meal **")
				handle_order()
			else:
				order_list.append(order)
				print(f"** 1 order of {order} have been added to your meal **")
				handle_order()	

		else:
			print(f"please choose item form the menu or type quit to quit")
			handle_order()	
	else:
		return		


			

	
				
					
		

if __name__=="__main__":
	handle_print()
	handle_order()
  
	
   
     

	
	 
	
	
     	 

	 


