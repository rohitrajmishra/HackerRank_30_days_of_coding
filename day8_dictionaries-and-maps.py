# Empty dictionary
phone_dict = {}

n = int(input())

def myPrint(query_key):
    if query_key in phone_dict.keys():
        print("%s=%d" % (query_key, phone_dict[query_key]))
    else:
        print("Not found")
    return 0

for i in range(n):
    name, phone_number = input().split(' ')
    phone_number = int(phone_number)

    # Update dict
    phone_dict[name] = phone_number

# Taking unknown no. of inputs with while loop
while True:
    try:
        query_key = input()
        # print("debug: %s" % query_key)
        myPrint(query_key)
    except EOFError:
        break