
def convert(num):
    map1 = {1: 'I', 2: 'II', 3: 'III', 4 : 'IV',  5: 'V', 6: 'VI', 7 : 'VII', 8 : 'VIII', 9 : 'IX', 10: 'X',40 : 'XL', 50: 'L',90 :'XC', 100: 'C',400: 'CD', 500 : 'D',900 : 'CM', 1000: 'M'}
    result=""
    while num != 0:
        if num >= 1000:
            if num in map1.keys():
                result = result + map1[num]
                break
            else:
                result = result + map1[1000] * int(num / 1000)
                num = int(num % 1000)
            print(num)
            print(result)
            # break
        elif num >= 500:
            if num in map1.keys():
                result = result + map1[num]
                break
            else:
                result = result + map1[500] * int(num / 500)
                num = int(num % 500)
            print(num)
            print(result)
        elif num >= 100:
            if num in map1.keys():
                result = result + map1[num]
                break
            else:
                result = result + map1[100] * int(num / 100)
                num = int(num % 100)
            print(num)
            print(result)
        elif num >= 50:
            if num in map1.keys():
                result = result + map1[num]
                break
            else:
                result = result + map1[50] * int(num / 50)
                num = int(num % 50)
            print(num)
            print(result)
        elif num >= 10:
            if num in map1.keys():
                result = result + map1[num]
                break
            else:
                result = result +map1[10] * int(num / 10)
                num = int(num % 10)
            print(num)
            print(result)

        else:
            if num in map1.keys():
                result = result + map1[num]
            num = int(num % 10)
            print(num)
            print(result)
            break

    return result


print(convert(3549))
print(convert(1904))
print(convert(3655))
print(convert(3656))
print(convert(656))




