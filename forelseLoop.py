success = True
for i in range(3):
    print("Attempt")
    if success:
        print("successful")
        break
else:
    print("attempted 3 times and failed")
