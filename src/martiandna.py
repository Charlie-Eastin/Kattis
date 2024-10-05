import sys

file = open("input.txt", "r")

total_length, alphabet_size, base_count = list(map(int, file.readline().strip().split()))

dna = list(map(int, file.readline().strip().split()))
nucleobases = []
nucleobases_count = []


for i in range(base_count):
    x, y = file.readline().strip().split()
    nucleobases.append(int(x))
    nucleobases_count.append(int(y))

#print(dna)
#print(nucleobases)
#print(nucleobases_count)

low = 0
high = total_length
found_at_any_point = False

if high == 1:
    print(high)
else: 
    while(low < high):
        mid = (low + high) // 2
        found = False
        current_count = {}

        for i in range(mid):
                if dna[i] in current_count:
                    current_count[dna[i]] += 1  
                else:
                    current_count[dna[i]] = 1
        valid = True
        for j in range(base_count):
            if nucleobases[j] not in current_count or current_count[nucleobases[j]] < nucleobases_count[j]:
                valid = False
                break
        if (valid == True):
            found_at_any_point = True
            high = mid
            continue

        
        for i in range(mid, total_length):
            current_count[dna[i - mid]] -= 1
            if dna[i] not in current_count:
                current_count[dna[i]] = 1
            else:
                current_count[dna[i]] += 1

            valid = True    
            for j in range(base_count):
                if nucleobases[j] not in current_count or current_count[nucleobases[j]] < nucleobases_count[j]:
                    valid = False
                    break
            if (valid == True):
                found_at_any_point = True
                break

        if valid == True:
            found_at_any_point= True
            high = mid
        else:
            low = mid + 1
                    

    if (found_at_any_point == False):
        print("impossible")
    else:
        print(low)


