# txt = 'привет'
# print(type(txt))
# txt[0] = 'П'
# print(txt)

txt = 'привет'
txt = list(txt)  # O(n)
print(type(txt))
txt[0] = 'П'
txt = ''.join(txt)  # O(n)
print(txt)
