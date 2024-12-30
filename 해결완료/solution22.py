from urllib.request import urlretrieve
url = 'https://projecteuler.net/project/resources/p022_names.txt'
urlretrieve(url, "names.txt")

names_list = []
with open('names.txt') as names:
    names_list = names.read().split(',')  # ['"MARY"', '"PATRICIA"',...]
names_list.sort()

alphabet = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
count = 0  # 곱한 값
for i in range(0, len(names_list)):  # 리스트 순회
    name_sum = 0  # 이름 순회 전 초기화
    for j in range(0, len(names_list[i])):
        if names_list[i][j] != "'" and names_list[i][j] != "\"":
            name_sum += alphabet[names_list[i][j]]  # 이름값 구함
    count += (i+1) * name_sum  # 위치값*이름값
print(count)

# others
names = list(map(lambda x: x.strip('"'), open('names.txt').read().strip().split(',')))
names.sort()
print(sum(sum(map(lambda x: ord(x)-64, names[index])) * (index+1) for index in range(len(names))))

# First load the file and sort it.
# 1 x = eval( '[' + open( '.../names.txt' ).readlines()[ 0 ] + ']' )
# 2 x.sort()
# Then calculate what is needed.
# 3 reduce( lambda x, y: x + y, [ reduce( lambda x, y: x + y, [ ( j + 1 ) * ( ord( i ) - 64 ) for i in x[ j ] ] ) for j in xrange( len( x ) ) ] )
