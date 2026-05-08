def calculate_discounted_prices(cart_items, customer_tier):
    """
    Calculates the final price of items based on customer tier and item type.
    WARNING: This code intentionally has high cyclomatic complexity (Spaghetti Code) 
    for evaluation purposes.
    """
    final_prices = []
    
    if cart_items is not None:
        if len(cart_items) > 0:
            for item in cart_items:
                if customer_tier == "GOLD":
                    if item["type"] == "electronics":
                        final_prices.append(item["price"] * 0.80)
                    elif item["type"] == "clothing":
                        final_prices.append(item["price"] * 0.85)
                    else:
                        final_prices.append(item["price"] * 0.90)
                elif customer_tier == "SILVER":
                    if item["type"] == "electronics":
                        final_prices.append(item["price"] * 0.90)
                    elif item["type"] == "clothing":
                        final_prices.append(item["price"] * 0.95)
                    else:
                        final_prices.append(item["price"] * 0.98)
                else:
                    # Standard or unrecognized tier
                    if item["type"] == "electronics":
                        final_prices.append(item["price"])
                    elif item["type"] == "clothing":
                        final_prices.append(item["price"])
                    else:
                        final_prices.append(item["price"])
        else:
            return []
    else:
        return []
        
    return final_prices