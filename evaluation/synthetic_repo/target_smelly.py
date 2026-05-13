def get_discount(customer_type, years_active):
    """
    Calculates discount percentage based on customer type and loyalty.
    WARNING: High Cyclomatic Complexity!
    """
    discount = 0
    
    if customer_type == "regular":
        if years_active < 1:
            discount = 0
        else:
            if years_active <= 3:
                discount = 5
            else:
                discount = 10
    elif customer_type == "premium":
        if years_active < 1:
            discount = 10
        else:
            if years_active <= 3:
                discount = 15
            else:
                discount = 20
    elif customer_type == "vip":
        if years_active < 1:
            discount = 20
        else:
            if years_active <= 3:
                discount = 25
            else:
                discount = 30
    else:
        discount = 0
        
    return discount