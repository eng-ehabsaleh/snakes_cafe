""""""
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
print("Welcome to the Snakes Cafe!")
print("Please see our menu below.")
print("**")
print('** To quit at any time, type "quit" **')
for i in menu:
	print(i["name"])
	print("----------")
	for y in i["available_types"]:
	 print(y)
	 print()
print()
# print("***********************************")	 
# print("** What would you like to order? **")	 
# print("***********************************")	 

def handle_order(num):
    # print(f"** {number} order of {order} have been added to your meal **")
    print("hi")

if __name__ == "__main__":
	index=0
	res = ""
	while res != "quit":
	 index+=1
	 if index>1:
		    break	
	 print("***********************************")	 
	 res=input("** What would you like to order? **")
	 if res=="quit":exit()
	 else:
	  handle_order(res)
	
     	 

	 


