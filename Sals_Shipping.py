#Codeacademy lesson Python Control Flow Sal's Shipping. 
#Enter package weight here:
weight = 4.8

#Function calculates cost of Normal Ground for weight
def cost_normal_ground(weight):
  cost_normal_ground = 0
  if weight <= 2: 
    cost_normal_ground = 20 + (weight * 1.50)
  elif weight > 2 and weight <=6:
    cost_normal_ground = 20 + (weight * 3.00)
  elif weight > 6 and weight <=10:
    cost_normal_ground = 20 + (weight * 4.00)
  else:
    weight > 10
    cost_normal_ground = 20 + (weight * 4.75)
  return cost_normal_ground
#print("NG " + str(cost_normal_ground(weight)))

#Function calculates cost of Premium Ground for weight
def cost_premium_ground(weight):
  cost_premium_ground = 0
  if weight > 0: 
    cost_premium_ground = 125.00
  return cost_premium_ground
#print("PG " + str(cost_premium_ground(weight)))

#Function calculates cost of Drone shipping for weight
def cost_drone(weight):
  cost_drone = 0
  if weight <= 2: 
    cost_drone = 4.50
  elif weight > 2 and weight <=6:
    cost_drone = 9.00
  elif weight > 6 and weight <=10:
    cost_drone = 12.00
  else:
    weight > 10
    cost_drone = 14.25
  return cost_drone
#print("D " + str(cost_drone(weight)))

#Function to determine cheapest shipping method
def method_lowest_cost(weight):
  shipping_cost = 0

  #Test normal ground cost
  if cost_normal_ground(weight) < cost_premium_ground(weight) and cost_normal_ground(weight) < cost_drone(weight):
    print("The cheapest way to ship a " + str(weight) + " lb package is by Normal Ground and it will cost $" + str(cost_normal_ground(weight) + shipping_cost))

    #Test premium ground cost
  elif cost_premium_ground(weight) < cost_normal_ground(weight) and cost_premium_ground(weight) < cost_drone(weight):
    print("The cheapest way to ship a " + str(weight) + " lb package is by Premium Ground and it will cost $" + str(cost_premium_ground(weight) + shipping_cost))

    #Test drone shipping cost
  else:
    print("The cheapest way to ship a " + str(weight) + " lb package is by Drone and it will cost $" + str(cost_drone(weight) + shipping_cost))

#Finally, call the cheapest shipping method function