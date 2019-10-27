flat_rate = 125

def determine_ground_rate(weight):
  if weight <= 2:
    ground_cost = (1.50 * weight) + 20
    # return ground_cost
  elif (weight > 2) and (weight <= 6):
    ground_cost = (3 * weight) + 20
    # return ground_cost
  elif (weight > 6) and (weight <= 10):
    ground_cost = (4 * weight) + 20
    # return ground_cost
  else:
    ground_cost = (4.75 * weight) + 20
  return ground_cost
  

def determine_drone_rate(weight):
  if weight <= 2:
    drone_cost = (4.50 * weight)
    # return drone_cost
  elif (weight > 2) and (weight <= 6):
    drone_cost = (9 * weight)
    # return drone_cost
  elif (weight > 6) and (weight <= 10):
    drone_cost = (12 * weight)
    # return drone_cost
  else:
    drone_cost = (14.25 * weight)
  return drone_cost


def compare_rates(ground_total, drone_total, flat_rate):
  if (ground_total < drone_total) and not (ground_total > flat_rate):
    best_value = "Ground Shipping"
    print('The best value is our ' + best_value + ' option, which will cost $' + str(ground_total) + '.')
  elif (drone_total < ground_total) and not (drone_total > flat_rate):
    best_value = "Drone Shipping"
    print('The best value is our ' + best_value + ' option, which will cost $' + str(drone_total) + '.')
  else:
    best_value = "Premium Ground Shipping"
    print('The best value is our ' + best_value + ' option, which will cost $' + str(flat_rate) + '.')


def get_weight(input):
  weight = input
  ground_total = determine_ground_rate(weight)
  drone_total = determine_drone_rate(weight)
  compare_rates(ground_total, drone_total, flat_rate)

get_weight(5.24)
