# import pandas as pd

# df = pd.DataFrame({
# 	"user":['Maria', 'Pesho', 'Ivan'],
# 	"age":[10, 20, 50]
# })
# print(df)
# print('*'*10)


# # re-arange columns - best way
# # df = df[['age','user']]
# # print(df)

# # do not use that
# # df[['user', 'age']] = df[['age','user']]
# # print(df)


# # Find user name which is 20 years old

# # df[colname] - get column
# print( df['user'] )
# print( df.user )

# # df[slice] - get rows
# print(df[1:])

# # df.loc[labels,columns]
# print( df.loc[:,'user'] )

# l = [1,2,3]

# # del l[1]
# el = l.pop(1)
# print(l)
# print(el)


l = [1,2,3]
# add 9 to the end of l:
l.append(9)
print(l)