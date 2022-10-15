product_list = ["풀", "가위", "크래파스"]
price_list = [800, 2500, 5000]
product_dict =  { productlist : pricelist for productlist,pricelist in zip(product_list,price_list)}


print(product_dict)