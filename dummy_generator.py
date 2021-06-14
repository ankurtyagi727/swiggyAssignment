import string    
import random # define the random module  
import csv 
import os
import glob
import pandas as pd


os.chdir(os.getcwd()+"\\separate")
global id_value
id_value=0
for x in range(1000000):
    S = 10  # number of characters in the string.  
     
    res_name = ''.join(random.choices(string.ascii_lowercase, k = S))    
    print("The randomly generated string is : " + str(res_name))


    id_value=id_value+1


    rating= random.randint(1,5)
    print("The rating of restaurant is " + str(rating)) 

    if rating%2==0:
        veg_non="Green"
    else :
        veg_non="Red"



    distance=random.randint(1,30)
    Del_time=random.randint(10,60)

    food_cat=['Beverages', 'Desserts',"Breads","Veg","Non_Veg"]

    Beverages=['Sweet lassi','Shikanji','Aam panna','Ice tea','Coke','Orange juice','Shake','Cold coffee','Coke zero','Lemon tea']
    Desserts=["Phirni","Gulab jamun","Shahi tukda","Cupcake","Lemon tart","Nutella cake","Choco brownie","Honey pastry","Ras malai"]
    Veg_food=["Shahi malai kofta"," Subz bahaar","Paneer kastoori","Paneer hyderabadi","Paneer butter masala","Paneer makhani","Dal tadka","Punjabi cholle","Mix veg","Tawa chaap","Mushroom mattar","Palak kofta","Soya chaap masala","Palak mushroom","Dal makhani","Jeera aloo"]
    Non_Veg=["Murgh kadhai","Murgh Tikka","Rara ghost","Rogan","Chicken malai tikka","Chicken patanga","Mutton korma","Kebab","Hyderabadi biryani","Dum ghost","Tokhm biryani","galouti kebab","ghost mefil","showrma"]
    Bread=["Roti","Butter roti","Plain naan","Lacha parantha","Missi roti","Chilli parantha","Rumali roti","Aloo naan"]





    Bev=Beverages[random.randint(0,3):random.randint(5,9)]
    print(Bev)
    price_bev=[]
    a=len(Bev)
    for i in range(a):
        price_bev.append(random.randint(20,80))
    print(price_bev)


    Des=Desserts[random.randint(0,3):random.randint(4,8)]
    print(Des)
    price_des=[]
    b=len(Des)
    for i in range(b):
        price_des.append(random.randint(60,200))
    print(price_des)



    Bred=Bread[random.randint(0,3):random.randint(4,8)]
    print(Bred)
    price_Bread=[]
    c=len(Bred)
    for i in range(c):
        price_Bread.append(random.randint(20,60))
    print(price_Bread)






    veg=Veg_food[random.randint(0,5):random.randint(6,10)] +[Veg_food[random.randint(11,15)]] 
    print(veg)
    price_veg=[]
    d=len(veg)
    for i in range(d):
        price_veg.append(random.randint(200,400))
    print(price_veg)


    nov=Non_Veg[random.randint(0,5):random.randint(6,10)] +[Non_Veg[random.randint(11,13)]] 
    print(nov)
    price_non=[]
    e=len(Bev)
    for i in range(e):
        price_non.append(random.randint(300,500))
    print(price_non)



    empty=None
    print(os.getcwd())




    '''with open('python.csv', mode='w') as csv_file:
        fieldnames = ["restaurant_name", "id", "rating","food_cat","Beverages"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames) 
    writer.writeheader()    
    writer.writerow(res_name,res_id,rating,food_cat,Beverages)    
      '''
   
    '''dir=os.getcwd()
    print(dir)
    os.chdir(dir+"\\separate")
    print(os.getcwd())
    '''


    filename=''.join([res_name,".csv"]) 
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["id", "Name","rating","Veg_Non","Distance(Km)","Delivery time(Min)","Food_categories","Bread","price_bread","Beverages","price_Beverages","Desserts","price_desserts","Veg course","price_veg","Non veg course","price_non_veg"])   
        if veg_non=="Green" :
           writer.writerow([id_value, res_name, rating,veg_non,distance,Del_time,food_cat,Bred,price_Bread,Bev,price_bev,Des,price_des,veg,price_veg,empty])
        else :
           writer.writerow([id_value, res_name, rating,veg_non,distance,Del_time,food_cat,Bred,price_Bread,Bev,price_bev,Des,price_des,veg,price_veg,nov,price_non])
    
    


 


extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
os.chdir("../single")
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
#os.chdir("../")
print(os.getcwd())

#print(os.getcwd())





CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURRENT_DIR)
filename="combined_csv.csv"
#os.chdir(os.getcwd()+"\\bisected")
full_file_path = os.path.join(CURRENT_DIR+"\\half_separate", filename)
print(full_file_path)

file_name = os.path.splitext(full_file_path)[0]

rows_per_csv = 2 

with open(filename) as infile:
    reader = csv.DictReader(infile)
    header = reader.fieldnames
    rows = [row for row in reader]
    pages = []

    row_count = len(rows)
    start_index = 0
    # here, we slice the total rows into pages, each page having [row_per_csv] rows
    while start_index < row_count:
        pages.append(rows[start_index: start_index+rows_per_csv])
        start_index += rows_per_csv

    for i, page in enumerate(pages):
        with open('{}_{}.csv'.format(file_name, i+1), 'w+') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=header)
            writer.writeheader()
            for row in page:
                writer.writerow(row)

        print('DONE splitting {} into {} files'.format(filename, len(pages)))

