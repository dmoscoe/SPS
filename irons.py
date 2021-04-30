# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 09:48:54 2021

@author: dmosc
"""

import random
import matplotlib.pyplot as plt

class irons(object):
    def __init__(self, qty, ship_cost, yearly_hold_cost):
        """qty: quantity per shipment. ship_cost: shipping cost per shipment regardless of qty. hold_cost: holding cost per item per year."""

        self.qty = qty
        self.ship_cost = ship_cost
        self.yearly_hold_cost = yearly_hold_cost
        
        self.on_hand = qty
        self.restock_tally = 1
        self.sell_times = []
    
    def sell(self, time):
        self.sell_times.append(time)
        self.sell_times.sort()
        self.on_hand -= 1
        if self.on_hand == 0:
            self.restock()
    
    def restock(self):
        self.on_hand = self.qty
        self.restock_tally += 1
    
    def item_hold_cost(self, sale_no):
        """Computes the hold_cost incurred by a particular iron. The iron is indicated by its ordinal place in the sequence of all irons sold. For example, the fifth iron sold has sale_no 5."""

        time_of_sale = self.sell_times[sale_no - 1]
        #print("time_of_sale = " + str(time_of_sale))

        time_of_stocking = self.sell_times[self.qty * ((sale_no - 1) // self.qty) - 1]
        if time_of_stocking >= time_of_sale:
            time_of_stocking = 0
        #print("time_of_stocking = " + str(time_of_stocking))

        item_hold_cost = self.yearly_hold_cost * (time_of_sale - time_of_stocking)
        return round(item_hold_cost, 2)

    def tell_all(self):
        print("qty = " + str(self.qty))
        print("ship_cost = " + str(self.ship_cost))
        print("yearly_hold_cost = " + str(self.yearly_hold_cost))
        print("on_hand = " + str(self.on_hand))
        print("restock_tally = " + str(self.restock_tally))
        print("sell_times = " + str(self.sell_times))
        print("total hold_costs = " + str(round(sum(a.calc_hold_costs()), 2)))
        print("total ship_costs = " + str(a.calc_ship_costs()))
        print("total costs = " + str(a.calc_total_costs()))
    
    def calc_hold_costs(self):
        hold_costs = []
        for i in range(len(self.sell_times)):
            hold_costs.append(self.item_hold_cost(i + 1))
        return hold_costs
    
    def calc_ship_costs(self):
        return self.restock_tally * self.ship_cost
    
    def calc_total_costs(self):
        return(round(sum(self.calc_hold_costs()) + self.calc_ship_costs(), 2))
    
    def sim(self, sells):
        """sells is the number of times a sale is made in 1 year."""
        
        sell_times = []
        for i in range(sells):
            sell_times.append(round(random.random(), 4))
        sell_times.sort()
        for j in range(len(sell_times)):
            self.sell(sell_times[j])

total_costs = []
for i in range(5,100): #varying lot size
    a = irons(i, 8.50, 3.75)
    a.sim(110)
    total_costs.append(a.calc_total_costs())

print(total_costs)

fig, axs = plt.subplots()
axs.scatter(range(5,100), total_costs, marker = ".") #x is lotsize
axs.set(title = "Total Cost Depending on Lot Size", ylabel = "Total cost ($)", xlabel = "Lot size (irons)")