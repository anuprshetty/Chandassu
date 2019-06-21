from flask import Flask, render_template, request
import os
import random
app = Flask(__name__)
from os import environ

@app.route('/')
def Home():
   return render_template('Home.html')

@app.route('/Laghu_Guru')
def Laghu_Guru():
   return render_template('Laghu_Guru.html')

@app.route('/kandapadya')
def Kandapadya():
   return render_template('Kandapadya.html')

@app.route('/Shatpadi')
def Shatpadi():
   return render_template('Shatpadi.html')

@app.route('/Ragale')
def Ragale():
   return render_template('Ragale.html')

@app.route('/Chandassu')
def Chandassu():
   return render_template('Chandassu.html')

@app.route('/Shara')
def Shara():
   return render_template('Shara.html')

@app.route('/Bhoga')
def Bhoga():
   return render_template('Bhoga.html')

@app.route('/Bhamini')
def Bhamini():
   return render_template('Bhamini.html')

@app.route('/Vardhaka')
def Vardhaka():
   return render_template('Vardhaka.html')

@app.route('/Parivardhini')
def Parivardhini():
   return render_template('Parivardhini.html')

@app.route('/Kusuma')
def Kusuma():
   return render_template('Kusuma.html')

@app.route('/Lalita')
def Lalita():
   return render_template('Lalita.html')

@app.route('/Mandanila')
def Mandanila():
   return render_template('Mandanila.html')

@app.route('/Utsaha')
def Utsaha():
   return render_template('Utsaha.html')

@app.route('/Vrutta')
def Vrutta():
   return render_template('Vrutta.html')

@app.route('/Testing')
def Testing():
   return render_template('Testing.html')

@app.route('/Akshara')
def Akshara():
   return render_template('Akshara.html')

@app.route('/exe1')
def exe1():
   return render_template('exe2.html')

@app.route('/files')
def files():
   return render_template('files.html')

@app.route('/Kandapadya_file')
def Kandapadya_file():
   f=open('Kandapadya.txt','r').read()
   splitfile=f.split('\n')
   akshara_list=[]
   for eachline in splitfile:
       akshara_list.append(eachline)
   return render_template('files_output.html',akshara_lists=akshara_list)

@app.route('/Shatpadi_file')
def Shatpadi_file():
   f=open('Shatpadi.txt','r').read()
   splitfile=f.split('\n')
   akshara_list=[]
   for eachline in splitfile:
       akshara_list.append(eachline)
   return render_template('files_output.html',akshara_lists=akshara_list)

@app.route('/Ragale_file')
def Ragale_file():
   f=open('Ragale.txt','r').read()
   splitfile=f.split('\n')
   akshara_list=[]
   for eachline in splitfile:
       akshara_list.append(eachline)
   return render_template('files_output.html',akshara_lists=akshara_list)

@app.route('/exe')
def exe():
   f=open("input1.txt",'r')
   akshara_list=[]
   lg=[]
   num_lines=sum([1 for line in f])
   f.seek(0, 0)
   i=0
   while i<num_lines:
     str1=f.readline()
     if str1!='\n':
          akshara_list.append(str1)
     else:
          lg.append(akshara_list)
          akshara_list=[]	
     i=i+1
   num=random.randint(0,11)
   f=open("input.txt",'w')
   k=lg[num]
   for i in range(0,len(k)):
       f.write(str(k[i]))
   f.close()
   f=open('input.txt','r').read()
   splitfile1=f.split('\n')
   akshara_list1=[]
   for eachline1 in splitfile1:
        akshara_list1.append(eachline1)
   run_python_script()
   f=open('Chandassu.txt','r').read()
   splitfile=f.split('\n')
   akshara_list=[]
   for eachline in splitfile:
        akshara_list.append(eachline)
   return render_template('exe1.html',akshara_lists=akshara_list,akshara_list1=akshara_list1)

@app.route('/About')
def About():
   return render_template('About.html')

@app.route('/Norm')
def Norm():
	f=open('Chandassu.txt','r')
	num_lines=0
	for line in f:
		num_lines+=1
	if 'Invalid' in open('Chandassu.txt').read() and num_lines==1:
		akshara_list1=[]
		akshara_list4=[]
		akshara_list3=[]
		akshara_list1.append('Invalid')
		akshara_list4.append('Invalid')
		akshara_list3.append('Invalid')
		f=open('input.txt','r').read()
		splitfile=f.split('\n')
		akshara_list2=[]
		for eachline in splitfile:
			akshara_list2.append(eachline)
		f=open('Chandassu.txt','r').read()
		splitfile=f.split('\n')
		akshara_list=[]
		for eachline in splitfile:
			akshara_list.append(eachline)
	else:
		f=open('input.txt','r').read()
		splitfile=f.split('\n')
		akshara_list2=[]
		for eachline in splitfile:
			akshara_list2.append(eachline)
		f=open('Chandassu.txt','r').read()
		splitfile=f.split('\n')
		akshara_list=[]
		for eachline in splitfile:
			akshara_list.append(eachline)
		f=open('Akshara.txt','r').read()
		splitfile=f.split('\n')
		akshara_list1=[]
		for eachline in splitfile:
			akshara_list1.append(eachline)
		f=open('Normalized.txt','r').read()
		splitfile=f.split('\n')
		akshara_list3=[]
		for eachline in splitfile:
			akshara_list3.append(eachline)
		f=open('laghu_Guru.txt','r').read()
		splitfile=f.split('\n')
		akshara_list4=[]
		for eachline in splitfile:
			akshara_list4.append(eachline)
	return render_template('Normalizer1.html',akshara_lists=akshara_list,akshara_lists1=akshara_list1,akshara_lists2=akshara_list2,akshara_lists3=akshara_list3,akshara_lists4=akshara_list4)

@app.route('/result',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		result = request.form.get("textarea")
		text2 = result.split('\n')
		text_changed = ''.join([line for line in text2])
		with open('input.txt','w') as f:
			f.write(text_changed)
		run_python_script()
		f=open('Chandassu.txt','r').read()
		splitfile=f.split('\n')
		akshara_list=[]
		for eachline in splitfile:
			akshara_list.append(eachline)
	if request.method == 'GET':
		f=open('input.txt','r').read()
		splitfile=f.split('\n')
		text_changed1=[]
		for eachline in splitfile:
			text_changed1.append(eachline)
			text_changed1.append('\n')
		text_changed = ''.join([line for line in text_changed1])		
		f=open('Chandassu.txt','r').read()
		splitfile=f.split('\n')
		akshara_list=[]
		for eachline in splitfile:
			akshara_list.append(eachline)
	#f=open('Chandassu.txt','w')
	#f.write("Invalid")	
	return render_template('Testing1.html',akshara_lists=akshara_list,text_changed=text_changed)
def run_python_script():
	os.system('python3 modific.py input.txt')
if __name__ == '__main__':
	app.run(debug=True)
