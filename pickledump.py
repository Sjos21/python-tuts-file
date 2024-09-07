import pickle,studentf

f=open("student.dat","wb")
s=studentf.Student(123,"john",90)
pickle.dump(s,f)
f.close()