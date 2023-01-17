
# queries = [
#     'смотреть сериалы онлайн',
#     'новости спорта',
#     'афиша кино',
#     'курс доллара',
#     'сериалы этим летом',
#     'курс по питону',
#     'сериалы про спорт'
#     ]

def percent(param):
  procent = {}
  all = []
  t = []
  num = []

  # Колличество запросов
  all_queries = len(param)

  # подсчет колличества слов
  queries_split = [i.split() for i in param]
  number_words = [len(i) for i in queries_split]

  # Уникальные значения
  set_number_words = set(number_words)

  for set_number in set_number_words:
    number_words_count = number_words.count(set_number)
    procent[set_number] = (100 * number_words_count)/all_queries

  return procent



# if __name__ == '__main__':

#   print(percent(queries))
  