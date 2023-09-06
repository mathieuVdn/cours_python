import random

# # Le tri par selection
# liste = [8, 1, 5, 4, 3]
#
#
# def sort_list(l):
#     for unsorted_index in range(0, len(l) - 1):
#         min_nb = l[unsorted_index]
#         min_index = unsorted_index
#         for i in range(unsorted_index + 1, len(l)):
#             if l[i] < min_nb:
#                 min_nb = l[i]
#                 min_index = i
#         l[min_index] = l[unsorted_index]
#         l[unsorted_index] = min_nb
#     return l
#
#
# def generate_random_list(n, min, max):
#     l = []
#     for i in range(n - 1):
#         l.append(random.randint(min, max))
#     return l
#
#
# #
# # print(sort_list(generate_random_list(10000, 0, 10)))
#
# print(len(liste))
