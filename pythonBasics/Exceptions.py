items_in_cart = 0
if items_in_cart != 2:
   pass
   # raise Exception('ERR: counts not matching')

assert(items_in_cart == 0)

try:
    with open('filelog.txt', 'r') as reader:
        content = reader.readlines()
except Exception as e:
    print('!!!!!!!!~~~~Failed~~~~!!!!!!!!')
    print(e)
    print('!!!!!!!!~~~~Failed~~~~!!!!!!!!')
# incorrect file name, try/except = pythons try/catch
finally:
    print("TEST COMPLETE")
# finally blocks will always execute after the try/except
