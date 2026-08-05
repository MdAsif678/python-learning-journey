def num_to_text(a):
    ones = ["","one ","Two ","Three ","Four ","Five ","Six ","Seven ","Eight ","Nine "]
    teens = ["Ten ","Eleven ","Twelve ","Thirteen ","Fourteen ","Fifteen ","Sixteen ","Seventeen ","Eighteen ","Nineteen "]
    tens = [" "," ","Twenty ","Thirty ","Forty ","Fifty ","Sixty ","Seventy ","Eighty ","Ninety "]

    if a == 0:
        return "zero"
    elif a < 10:
        x = a%10
        return ones[x]
    elif a < 20:
        x =  a%10
        return teens[x]
    elif a < 100:
        x = a%10
        y = a//10
        return tens[y] + ones[x] 
    elif a < 1000:
        x = a//100
        return ones[x] +"Hundred " + num_to_text(a%100)
    elif a < 10000:
        x = a//1000
        return ones[x] +"Thousand " + num_to_text(a%1000)
    elif a < 100000:
        x = a//10000
        return tens[x] + num_to_text(a%10000)
    elif a < 1000000:
        x = a//100000
        return ones[x] + "Hundred " + num_to_text(a%100000)
    elif a < 10000000:
        x = a//1000000
        return ones[x] + "Million " + num_to_text(a%1000000)
    elif a < 100000000:
        x = a//10000000
        return tens[x] + num_to_text(a%10000000)
    elif a < 1000000000:
        x = a//100000000
        return ones[x]+ "Hundred " + num_to_text(a%100000000)
    elif a < 10000000000:
        x = a//1000000000
        return ones[x]+ "Billion " + num_to_text(a%1000000000)
    elif a >= 10000000000:
        print("Number out of range")
        return 0
    else:
        print("Invalid Number")


print(num_to_text(8))
print(num_to_text(68))
print(num_to_text(99))
print(num_to_text(199))
print(num_to_text(1999))
print(num_to_text(3125))
print(num_to_text(9876))
print(num_to_text(0))
print(num_to_text(98764))
print(num_to_text(987642))
print(num_to_text(9876428))
print(num_to_text(98764287))
print(num_to_text(987642876))
print(num_to_text(9876428762))
