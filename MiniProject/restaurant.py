class Table:
    def __init__(self, capacity):
        self.items = []
        self.capacity = capacity
        self.bill = []

# method 1 - creating the order first 
    def order(self, item, price, quantity=1):
        for existing_item in self.bill:
            if existing_item["item"] == item and existing_item["price"] == price:
                existing_item["quantity"] += quantity
                break
        else:
            new_item = {"item": item, "price": price, "quantity": quantity}
            self.bill.append(new_item)
# method 2 - that is similiar to total 
    def remove(self, item, price, quantity=1):
        items_to_remove = []
        item_found = False
        for existing_item in self.bill:
            if existing_item["item"] == item and existing_item["price"] == price:
                if existing_item["quantity"] >= quantity:
                    existing_item["quantity"] -= quantity
                    if existing_item["quantity"] == 0:
                        items_to_remove.append(existing_item)
                    item_found = True 
                    break  
        for item in items_to_remove:
            self.items.remove(item)
        return item_found
    
# method 3 - getting the subtotal 
    def get_subtotal(self):
        subtotal = 0.0
        for item in self.bill:
           subtotal += float(item["price"]) * item["quantity"] # caculating the subtotal
        return subtotal
# method 4 - getting the total after the service charge
    def get_total(self,service_charge_percentage = 0.10):
        #getting the subtotal first 
        subtotal = self.get_subtotal()
        # caculating the the subtotal after the service charge
        service_amount_charge = subtotal * service_charge_percentage
        total = subtotal + service_amount_charge

        #converting subtoals, total, service charge into string 
        subtotal_str = "£{:.2f}".format(subtotal)
        service_charge_str = "£{:.2f}".format(service_amount_charge)
        total_str = "£{:.2f}".format(total)
           
        return {
            "Sub Total": subtotal_str,
            "Service Charge": service_charge_str,
            "Total": total_str
        }
    
# method 5 - splitting the bill 
    def split_bill(self, num_diners=5):
        subtotals = float(self.get_subtotal())
        split_cost = subtotals / num_diners
        # rounding it to the nearest penny 
        rounded_cost = "{:.2f}".format(split_cost)
        return float(rounded_cost)
    
# method 6 getting the bill 
    def get_bill(self):
        return self.items
    

# #------ test 
# # Create a table instance
# my_table = Table()

# # Order items
# my_table.order("Pizza", 12.99, 2)  # Item: Pizza, Price: 12.99, Quantity: 2
# my_table.order("Burger", 8.99, 3)  # Item: Burger, Price: 8.99, Quantity: 3

# # Get the split cost for 4 diners
# split_cost = my_table.split_bill(4)
# print("Split Cost:", split_cost)  # Output: Split Cost: 7.00 (rounded up from 6.99)



