f=open('fobinacci.py','r')
text=f.read()
print(text)
f.close()

''' agar file humne write mode me kholi hoti to hum opened file ka
data extract nhi kr skte'''
f=open('myfile.txt','w')
f.write('ritesh verma')
f.close()
# agar mode append hota to jitni baar run krege utni baar ritesh verma add hoga

''' agar file pehle se exist kr rhi hoti or hum write mode krdete
to file ka poora code delete hojata '''
# f.close() lagana jruri hai vrna print nhi krege existing file hai agar

with open('myfile.txt','w') as f:
    f.write('i am a student')
