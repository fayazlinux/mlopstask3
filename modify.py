import os
for file in os.listdir('/fayaz'):
    if file.endswith('.py'):
        myfile = file
print('Modifying file : ',myfile )

f= open('Churn-Model/'+myfile,"r")
filedata = f.read()
f.close()

newdata = filedata.replace('epochs=','epochs=2*')
newdata = newdata.split("\n")
newdata.insert(25,"model.add(Dense(units=16,activation='relu'))")
newdata = "\n".join(newdata)

f= open('Churn-Model/'+myfile,"w")
f.write(newdata)
f.close()