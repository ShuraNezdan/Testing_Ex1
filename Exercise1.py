
# geo_logs = [
#     {'visit1': ['Москва', 'Россия']},
#     {'visit2': ['Дели', 'Индия']},
#     {'visit3': ['Владимир', 'Россия']},
#     {'visit4': ['Лиссабон', 'Португалия']},
#     {'visit5': ['Париж', 'Франция']},
#     {'visit6': ['Лиссабон', 'Португалия']},
#     {'visit7': ['Тула', 'Россия']},
#     {'visit8': ['Тула', 'Россия']},
#     {'visit9': ['Курск', 'Россия']},
#     {'visit10': ['Архангельск', 'Россия']}
# ]


def rus(param):
  visit_key = []
  for geo_log in param:
    val_geo_log = list(geo_log.values())
    if 'Россия' != val_geo_log[0][1]:
      visit_key.append(geo_log.keys())

  for number_key in visit_key:
    for id_geo_logs, geo_log_filter in enumerate(param):
      key = geo_log_filter.keys()
      if number_key == key:
        del param[id_geo_logs]
  
  return param


# if __name__ == '__main__':
# 	qw = rus(geo_logs)

# 	for p in qw:
# 		print(p)

# 	print(len(qw))