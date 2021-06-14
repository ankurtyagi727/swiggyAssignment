import pandas as pd
import os
import csv
import operator
import functools
import random
import math


while True:
	df = pd.read_csv(os.getcwd()+"\\single\\combined_csv.csv")


	df["id"] = df["id"].astype(str)
	print("*************************Welcome*****************************")
	print("Enter the restaurant id ( 1 to 1000000)")
	userid=input()
	print("The restaurant id entered is " +userid)
	x=df.loc[df['id'].str.contains(userid)]
	

	#print(x.to_string())
	non1=None
	print("********************The details of restaurant are******************")
	print("S.no" )
	print(x.transpose())

	print(" *******************ORDER THE FOOD*********************** ")
	print("PLEASE ENTER NAME EXACTLY SAME AS SHOWN ABOVE IN MENU OTHERWISE STRINGS WILL NOT MATCH")
	print("\nEnter name of bread you want ")
	bread1=input()
	print("\nEnter the name of beverage you want ")
	beverage1=input()
	print("\nEnter the name of dessert you want ")
	dessert1=input()
	print("\nEnter the name of veg_item you want")
	veg1=input()
	if x['price_non_veg'].isnull().values.any()==False:
		print("\nEnter the name of non veg item you want")
		non1=input()

	p_bread=random.randint(20,60)
	p_beverage=random.randint(20,80)
	p_desserts=random.randint(60,200)
	p_veg=random.randint(200,400)
	p_non=random.randint(300,500)


	print("YOUR ORDER IS ")
	print("item------------------------------price")
	print(bread1+"-------------------------------"+str(p_bread))
	print(beverage1+"-------------------------------"+str(p_beverage))
	print(dessert1+"-------------------------------"+str(p_desserts))
	print(veg1+"---------------------------------"+str(p_veg))
	if bool(non1)==True:
	   print(non1+"-------------------------------"+str(p_non))

	sum=p_bread+p_beverage+p_desserts+p_veg+p_non
	tax= (sum*6)/100
	bill=sum+tax
	print("***************BILL DETAILS***************** ")
	print("price"+"-----------------------------"+str(sum))
	print("GST"+"--------------------------------"+str(tax))
	print("Grand_total"+"--------------------------"+str(bill))
	print(" THANK YOU VISIT AGAIN")
	if input("DO YOU WANT TO CONTINUE(Enter y or n ") !='y' :
		break