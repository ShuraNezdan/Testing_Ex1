

# stats = {
#   'facebook': 55, 
#   'yandex': 120, 
#   'vk': 115, 
#   'google': 132, 
#   'email': 42, 
#   'ok': 98}



def max_max(param):
  return max(param, key=param.get)


# if __name__ == '__main__':
#   print(max_max(stats))