def GetRatings(data):
    qone = data.pop('quality_one')
    qtwo = data.pop('quality_two')
    cs = data.pop('customer_service')
    csa = data.pop('customer_service_answer')
    oone = data.pop('order_one')
    otwo = data.pop('order_two')
    istp = data.pop('install_setup')
    oagain = data.pop('order_again')
    repr = data.pop('receive_product')
    atime = data.pop('arrival_time')
    drating = data.pop('damage_rating')
    mtnc = data.pop('maintenance')

    product_quality_one = (qone * 1.25)
    product_quality_two = (qtwo * 1.25)

    if(cs == "no"):
        customer_service = 14.3
    else:
        customer_service = (csa * 0.71)

    ordering_one = (oone * 0.72)
    ordering_two = (otwo * 0.71)

    install_setup = (istp * 1.43)
    
    if(oagain == "no"):
        order_again = 0
    else:
        order_again = 12.1

    if(repr == "no"):
        receive_product = 0
    else:
        receive_product = 4
    
    arrive_ontime = (atime* 0.3)
    damaged_rating = (drating * 0.3)
    maintenance = ( (5 - mtnc) * 2)

    rating_out_of_hundred = (product_quality_one + product_quality_two + customer_service + ordering_one + ordering_two + install_setup + order_again + receive_product + arrive_ontime + damaged_rating + maintenance)
    print(rating_out_of_hundred)
    if (rating_out_of_hundred >0 and rating_out_of_hundred<10):
        rating = "ONE"
    elif (rating_out_of_hundred >= 10 and rating_out_of_hundred<20):
        rating = "TWO"
    elif (rating_out_of_hundred >= 20 and rating_out_of_hundred<50):
        rating = "THREE"
    elif (rating_out_of_hundred >= 50 and rating_out_of_hundred<80):
        rating = "FOUR"
    elif (rating_out_of_hundred >= 80 and rating_out_of_hundred <= 100):
        rating = "FIVE"
    else:
        rating = "ZERO"

    return rating
