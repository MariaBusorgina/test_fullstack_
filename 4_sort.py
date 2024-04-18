def sort_by_length(some_list):
    sort_by_length_asc = sorted(some_list, key=len)
    sort_by_length_desc = sorted(some_list, key=len, reverse=True)

    return sort_by_length_asc, sort_by_length_desc


strings = ["Python", "Java", "PHP", "JavaScript", "C++"]

asc, desc = sort_by_length(strings)

print("Сортировка по возрастанию длины:", asc)
print("Сортировка по убыванию длины:", desc)