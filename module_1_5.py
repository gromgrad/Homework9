
#1
immutable_var=1,2,3,True,'String'
print(immutable_var)

#2
immutable_var=1,2,3,True,'String'
immutable_var[0][0]=100
print(immutable_var)

#3
mutable_list=([1,2],True,"urban")
print( mutable_list)
mutable_list[0][1]='false'
print(mutable_list)