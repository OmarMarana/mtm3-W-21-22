

def name_already_exist(dict,name):
    for k in dict.keys():
        if k==name:
            return True
    return False

def readFile(file_name):
    file=open(file_name,'r')
    ship_list = []
    current_product = []
    ship_dict ={}
    help_list=[]
    dict_price={}
    amount_in_warehouse={}
    dict_sold_amount={}  
    for line in file:
        if(line[-1] == '\n'):
            line = line[:-1]
        help_list = line.split( )
        if help_list[0]=="add":
            if (float)(help_list[3])>=0 and (float)(help_list[4])>=0 and name_already_exist(amount_in_warehouse,help_list[2]) ==  False: 
                dict_price[help_list[2]]=(float)(help_list[3])
                amount_in_warehouse[help_list[2]]=(float)(help_list[4])
                dict_sold_amount[help_list[2]]=0
            
        if help_list[0]=="change":
            if name_already_exist(amount_in_warehouse,help_list[2]) ==  False:
                continue
            amount_in_warehouse[help_list[2]] += (float)(help_list[3])
        
        if help_list[0]=="ship":     
            product_line = line[11:] 
            ship_list=(product_line).split(' -- ')
            for i in ship_list:
                current_product= i.split(', ')

                if (name_already_exist(amount_in_warehouse,current_product[0]) == False):
                    continue
                if(  (float)(current_product[1]) > amount_in_warehouse[current_product[0]]):
                    continue
                if (float)(current_product[1]) <= 0:
                    continue

                amount_in_warehouse[current_product[0]] -= (float)(current_product[1])
                dict_sold_amount[current_product[0]] += (float)(current_product[1])


            ship_dict = {}
            ship_list = {}
                	
    file.close()
    return [dict_price, amount_in_warehouse, dict_sold_amount]


def bubbleSort(list):
    
    n = len(list)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if list[j][1] > list[j + 1][1] :
                list[j], list[j + 1] = list[j + 1], list[j]



def find_k_most_expensive_products(file_name, k):
    
    if k <=0: 
        return []

    dict_list = readFile(file_name)

    if len(dict_list[0]) == 0:
        return []

    # price_dict_val_sorted = { k1 : v for k1, v in sorted(dict_list[0].items(), key = lambda v: v[1], reverse=True)}


    final_list = []
    tuple_list = list(dict_list[0].items())
    bubbleSort(tuple_list)
    tuple_list.reverse()

    i =0 
    while i < len(tuple_list):
        first_val = tuple_list[i] 
        tmp_dict = {}
        while i < len(tuple_list) and tuple_list[i][1] ==  first_val[1] :
            tmp_dict[tuple_list[i][0]] = tuple_list[i][1]
            i += 1
        sorted_dict = { k1 : v for k1, v in sorted(tmp_dict.items())}
        for k1, v in sorted_dict.items():
            final_list.append((k1,v))

    k_most_expensive_products_list = []

    num_of_products = len(dict_list[0])
    for j in range(min((int)(k),num_of_products)):
        k_most_expensive_products_list.append(final_list[j][0])

    return k_most_expensive_products_list

def find_best_selling_product(file_name):
    list_best_selling = []
    dict_list = readFile(file_name)
    max_sold_price=0

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


    
