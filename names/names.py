import time

start_time = time.time()

# # from Orig
# f = open('names_1.txt', 'r')
# names_1 = f.read().split("\n")  # List containing 10000 names
# f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

# # first try - 0.009s
with open('names_1.txt') as f:
    names_1 = set(line.strip() for line in f)

for name_2 in names_2:
    if name_2 in names_1:
        duplicates.append(name_2)

# # Orig - 8.643s
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
