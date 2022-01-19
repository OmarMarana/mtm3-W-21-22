


# d1 = {'banana' : 10, 'apple' : 10, 'apples' : 10,  'ffff' : 11 ,'c' : 10 , 'd' : 9, 'a' : 9}

# sort_d1_key = { k : v for k, v in sorted(d1.items())}

# print(list(sort_d1_val.items()))
# print(final_list)






def name_already_exist(dict,name):
    for k in dict.keys():
        if k==name:
            return True
    return False

def readFile(file_name):
    file=open(file_name,'r')
    ship_list = []
    tmp = []
    ship_dict ={}
    help_list=[]
    dict_price={}
    amount_in_warehouse={}
    dict_sold_amount={} # reset to zero 
    for line in file:
        help_list = line.split( )
        if help_list[0]=="add":
            if help_list[3]>=0 and help_list[4]>=0 and name_already_exist(amount_in_warehouse,help_list[3]) ==  False: 
                dict_price[help_list[2]]=(int)(help_list[3])
                amount_in_warehouse[help_list[2]]=(int)(help_list[4])
                dict_sold_amount[help_list[2]]=0
            
        if help_list[0]=="change":
            amount_in_warehouse[help_list[2]] += (int)(help_list[3])
        
        if help_list[0]=="ship":     #check format of ship
            ship_list=(help_list[2]).split('--')
            for i in ship_list:
                tmp= i.split(',')
                ship_dict[tmp[0]]+=tmp[1]
            
    # for k,v in ship_dict.items():
    
    # return [dict_price, amount_in_warehouse, dict_sold_amount]

def find_k_most_expensive_products(file_name, k):
    
    dict_list = readFile(file_name)
    price_dict_val_sorted = { k : v for k, v in sorted(dict_list[0].items(), key = lambda v: v[1], reverse=True)}
    final_list = []
    tuple_list = list(price_dict_val_sorted.items())
    i =0 
    while i < len(tuple_list):
        first_val = tuple_list[i] 
        tmp_dict = {}
        while i < len(tuple_list) and tuple_list[i][1] ==  first_val[1] :
            tmp_dict[tuple_list[i][0]] = tuple_list[i][1]
            i += 1
        sorted_dict = { k : v for k, v in sorted(tmp_dict.items())}
        for k, v in sorted_dict.items():
            final_list.append((k,v))

    k_most_expensive_products_list = []
    for j in range(k):
        k_most_expensive_products_list.append(final_list(j)[0])

    return k_most_expensive_products_list

def find_best_selling_product(file_name):
    list_best_selling = []
    dict_list = readFile(file_name)
    max_sold_price=0
    # return [dict_price, amount_in_warehouse, dict_sold_amount]

    for k in (dict_list[0]).keys():
        if dict_list[0][k]*dict_list[2][k] > max_sold_price:
            max_sold_price = dict_list[0][k]*dict_list[2][k]

    for k in (dict_list[0]).keys():
        if dict_list[0][k]*dict_list[2][k] == max_sold_price:
            list_best_selling.append(k)

    if len(list_best_selling) != 0:        
        sorted_list_best_selling = sorted(list_best_selling)
        return (sorted_list_best_selling[0], max_sold_price)
    
    return ('',0)


    
