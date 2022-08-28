import os


os.chdir(r'C:\Users\user\Desktop\python\server\project\templates\work')

for f in os.listdir():
	li = []
	r = range(1,7)
	f_name , f_ext = os.path.splitext(f)
	a,b = f_name.split('.')
	print (f'{a}{r}{b}')


# os.chdir(r'C:\Users\user\Desktop\python\server\project\templates\work')
# li = []
# for f in os.listdir():
# 	f_name , f_ext = os.path.splitext(f)
# 	li.append (f_name)

# print (li)	

# for n,i in enumerate(li):
# 	i.pop
# 	print (n,i)



