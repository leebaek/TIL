# Read Files

# 1. open()
# f = open('mulcam.txt', 'r')
# all_text = f.read() # String
# print(all_text)
# f.close()

# 2. with open()
with open('mulcam.txt', 'r') as f:
    lines = f.readlines() # list로 반환
    for line in lines:
        print(line)