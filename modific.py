#!/usr/bin/python
import sys
import copy
from sys import exit
import time
class Module1:
	def line_partition(self,f):
		akshara_list=[]
		num_lines=sum([1 for line in f])
		f.seek(0, 0)
		for i in range(0,num_lines):
			line=f.readline().strip()
			split=list(line)
			akshara_list.append(split)
		f.close()
		letter1=['್']
		letter2=['ಾ','ಿ','ೀ','ು','ೂ','ೃ','ೄ','ೆ','ೇ','ೈ','ೊ','ೋ','ೌ','ಂ','ಃ']
		uniLRange=3202
		uniHRange=3299
		len1=len(akshara_list)
		i=0
		while i<len1 :
			len2=len(akshara_list[i])
			j=0
			while j<len2 :
				if (ord(akshara_list[i][j]) < uniLRange or ord(akshara_list[i][j]) > uniHRange) and akshara_list[i][j] != " " :
					akshara_list[i].pop(j)
					len2=len2-1
				elif akshara_list[i][j] == " " and j+1<len2 :
					while akshara_list[i][j+1] == " " :
						akshara_list[i].pop(j+1)
						len2=len2-1
					if j-1>=0 and akshara_list[i][j-1] == " " :
						akshara_list[i].pop(j-1)
						len2=len2-1
						continue
					j=j+1
				elif akshara_list[i][j] in letter1:
					if j+1 == len2 or akshara_list[i][j+1] == " " :
						akshara_list[i][j-1:j+1]=[''.join(akshara_list[i][j-1:j+1])]
						len2=len2-1
					else :
						akshara_list[i][j-1:j+2]=[''.join(akshara_list[i][j-1:j+2])]
						len2=len2-2
				elif akshara_list[i][j] in letter2:
					akshara_list[i][j-1:j+1]=[''.join(akshara_list[i][j-1:j+1])]
					len2=len2-1
				else :
					j=j+1
			if len(akshara_list[i]) != 0 :
				if akshara_list[i][0] == " " :
					akshara_list[i].pop(0)
				if akshara_list[i][-1] == " " :
					akshara_list[i].pop(-1)
			i=i+1
		with open("Akshara.txt","w") as f:
			f.write(str(akshara_list))
		t=[]
		f=open("Normalized.txt","w")
		for i in range(0,len(akshara_list)):
			t.append(akshara_list[i])
		for k in range(0,len(t)):
			z=t[k]
			for g in range(0,len(z)):
				f.write(str(z[g]))
			f.write('\n')
		return akshara_list

class Module2:
	def laghu_guru(self,akshara_list):
		lg_list=[]
		lg_line=[]
		h_letter=['ಕ್', 'ಖ್', 'ಗ್', 'ಘ್', 'ಙ್', 'ಚ್', 'ಛ್', 'ಜ್', 'ಝ್', 'ಞ್', 'ಟ್', 'ಠ್', 'ಡ್', 'ಢ್', 'ಣ್', 'ತ್', 'ಥ್', 'ದ್', 'ಧ್', 'ನ್','ಪ್', 'ಫ್', 'ಬ್', 'ಭ್', 'ಮ್', 'ಯ್', 'ರ್', 'ಲ್', 'ವ್', 'ಶ್', 'ಷ್', 'ಸ್', 'ಹ್', 'ಳ್']
		g_letter=['ಆ', 'ಈ', 'ಊ', 'ೠ', 'ಏ', 'ಐ', 'ಓ', 'ಔ','ಾ', 'ೀ', 'ೂ', 'ೄ', 'ೇ', 'ೈ', 'ೋ', 'ೌ', 'ಂ', 'ಃ']
		halant_letter=['್']
		len1=len(akshara_list)
		i=0
		while i<len1 :
			lf=[]
			len2=len(akshara_list[i])
			j=0
			while j<len2 :
				if akshara_list[i][j] == " " :
					lg_line.append(0)
					j=j+1
					continue
				if akshara_list[i][j] in h_letter :
					if len(lg_line)>0 :
						lg_line[-1]=2
						lg_line.append(0)						
				elif any([l in akshara_list[i][j] for l in g_letter]):
					lg_line.append(2)					
				elif j+1 < len2 :
					if any([l in akshara_list[i][j+1] for l in halant_letter]) and akshara_list[i][j+1] not in h_letter :
						lg_line.append(2)						
					elif akshara_list[i][j+1] == " " and any([l in akshara_list[i][j+2] for l in halant_letter]) and akshara_list[i][j+2] not in h_letter :
						lg_line.append(2)						
					else :
						lg_line.append(1)
				elif i+1<len1 and len(akshara_list[i+1])!=0:
					if any([l in akshara_list[i+1][0] for l in halant_letter]) or akshara_list[i+1][0] in h_letter :
						lg_line.append(2)
					else :
						lg_line.append(1)
				else :
					lg_line.append(1)
				j=j+1
			lg_list.append(lg_line)
			lg_line=[]
			i=i+1
		lm=copy.deepcopy(lg_list)#Line numbers=86-91
		for k in range(0,3):
			for i in range(0,len(lg_list)):
				for j in lg_list[i]:
					if j==0:
						lg_list[i].remove(j)
		return lm,lg_list
class Module3:
	def chandassuPattern(self,lg_list,gana1,gana2,syllable1,syllable2,longLine1,longLine2,extraGuru) :
		len1=len(lg_list)
		i=0
		while i<len1 :
			len2=len(lg_list[i])
			gana=0
			if longLine1==-1 or longLine2==-1 :
				if extraGuru == True :
					len2=len2-1 
			if i==longLine1 or i==longLine2 :
				gana=gana2
				if extraGuru == True :
					len2=len2-1
			else :
				gana=gana1
			syllable=syllable1
			t3f4=True
			j=0
			while j<len2 :
				syllable=syllable-lg_list[i][j]
				if syllable==0 :
					gana=gana-1
					if t3f4 == True :
						syllable=syllable2
						t3f4=False
					else :
						syllable=syllable1
						t3f4=True
					if gana==0 :
						if (j+1) != len2 :
							return False
						else :
							break
					elif (j+1) == len2 :
						return False
				elif syllable<0 :
					return False
				elif (j+1) == len2 :
					return False
				j=j+1
			i=i+1
		return True

	def chandassuCondition(self,lg_list,syllable1,syllable2,pattern1,pattern2,extraGuru,tsfk):
		if pattern1 != "" and pattern2 != "":
			count=0
			pattern=[]
			stringPattern=""
			len1=len(lg_list)
			i=0
			while i<len1 :
				t3f4=True
				len2=len(lg_list[i])
				if i==2 or i==5 :
					if extraGuru == True :
						len2=len2-1
				j=0
				while j<len2 :
					pattern.append(lg_list[i][j])
					stringPattern = stringPattern + str(lg_list[i][j])
					if tsfk == True :
						if t3f4 == True :
							if sum(pattern) == syllable1 :
								if syllable1 == syllable2 :
									if stringPattern == pattern1 or stringPattern == pattern2 :
										return False
								t3f4=False
								pattern=[]
								stringPattern=""
						elif sum(pattern) == syllable2 :
							if stringPattern == pattern1 or stringPattern == pattern2 :
								return False
							t3f4=True
							pattern=[]
							stringPattern=""
					elif sum(pattern) == syllable1 or sum(pattern) == syllable2 :
						count=count+1;
						if ( count == 6 or count == 14 ) and (stringPattern != "1111" and stringPattern != "121") :
							return False
						if ( count == 8 or count == 16 ) and (stringPattern != "22" and stringPattern != "112") :
							return False
						if ((count%2) != 0) and (stringPattern == pattern1) or ((count%2) != 0) and (stringPattern == pattern2) :
							return False
						pattern=[]
						stringPattern=""		
					j=j+1
				i=i+1
		return True

	def kandapadya(self,akshara_list,lg_list,lg_dup):
		if len(lg_list)==4 :
			if sum(lg_list[0])==12 and sum(lg_list[2])==12 and sum(lg_list[1])==20 and sum(lg_list[3])==20 :
				tf=self.chandassuPattern(copy.deepcopy(lg_list),3,5,4,4,1,3,False)
				if tf !=True :
					return False
				tf=self.chandassuCondition(copy.deepcopy(lg_list),4,4,"121","121",False,False)
				if tf == True :
					self.Print_Master(akshara_list,"ಕಂದ ಪದ್ಯ",4,lg_list,lg_dup)
					return True
			else :
				return False
		else :
			return False

	def shatpadiMaster(self,lg_list,gana1,gana2,syllable1,syllable2,pattern1,pattern2):
		if len(lg_list)==6 :
			lg_list[2][-1]=2
			lg_list[5][-1]=2
			for i in range(0,len(lg_list)):
				if i == 2 or i == 5 :
					if sum(lg_list[i]) != ((gana2/2)*(syllable1+syllable2)+2) :
						return False
				else :
					if sum(lg_list[i]) != ((gana1/2)*(syllable1+syllable2)) :
						return False
			tf=self.chandassuPattern(copy.deepcopy(lg_list),gana1,gana2,syllable1,syllable2,2,5,True)
			if tf !=True :
				return False
			tf=self.chandassuCondition(copy.deepcopy(lg_list),syllable1,syllable2,pattern1,pattern2,True,True)
			return tf
		else :
			return False

	def shatpadi(self,akshara_list,lg_list,lg_dup) :
		tf=self.shatpadiMaster(copy.deepcopy(lg_list),2,3,4,4,"121","121")
		if tf == True :
			self.Print_Master(akshara_list,"ಶರ ಷಟ್ಪದಿ",4,lg_list,lg_dup)
			return True
		tf=self.shatpadiMaster(copy.deepcopy(lg_list),2,3,5,5,"1211","122")
		if tf == True :
			self.Print_Master(akshara_list,"ಕುಸುಮ ಷಟ್ಪದಿ",5,lg_list,lg_dup)
			return True
		tf=self.shatpadiMaster(copy.deepcopy(lg_list),4,6,3,3,"12","12")
		if tf == True :
			self.Print_Master(akshara_list,"ಭೋಗ ಷಟ್ಪದಿ",3,lg_list,lg_dup)
			return True
		tf=self.shatpadiMaster(copy.deepcopy(lg_list),4,6,3,4,"121","121")
		if tf == True :
			self.Print_Master(akshara_list,"ಭಾಮಿನೀ ಷಟ್ಪದಿ",1,lg_list,lg_dup)
			return True
		tf=self.shatpadiMaster(copy.deepcopy(lg_list),4,6,4,4,"121","121")
		if tf == True :
			self.Print_Master(akshara_list,"ಪರಿವರ್ಧಿನೀ ಷಟ್ಪದಿ",4,lg_list,lg_dup)
			return True
		tf=self.shatpadiMaster(copy.deepcopy(lg_list),4,6,5,5,"","")
		if tf == True :
			self.Print_Master(akshara_list,"ವಾರ್ಧಕ ಷಟ್ಪದಿ",5,lg_list,lg_dup)
			return True
		return False

	def ragaleMaster(self,lg_list,u0m1l2):
		if u0m1l2 == 0 :
			tf=True
			for line in lg_list :
				if sum(line) != 12 :
					tf=False
					break
			if tf == True :
				tf=self.chandassuPattern(copy.deepcopy(lg_list),4,4,3,3,-1,-1,False)
				if tf == True :
					return True
			for line in lg_list :
				if line[-1] != 2 or sum(line) != 11 :
					return False
			tf=self.chandassuPattern(copy.deepcopy(lg_list),3,3,3,3,-1,-1,True)
			return tf
		elif u0m1l2 == 1 :
			for line in lg_list :
				if sum(line) != 16 :
					return False
			tf=self.chandassuPattern(copy.deepcopy(lg_list),4,4,4,4,-1,-1,False)
			if tf == True :
				return True
			tf=self.chandassuPattern(copy.deepcopy(lg_list),4,4,3,5,-1,-1,False)
			return tf
		else :
			for line in lg_list :
				if sum(line) != 20 :
					return False
			tf=self.chandassuPattern(copy.deepcopy(lg_list),4,4,5,5,-1,-1,False)
			return tf

	def ragale(self,akshara_list,lg_list,lg_dup):
		tf=self.ragaleMaster(copy.deepcopy(lg_list),0)
		if tf == True :
			self.Print_Master(akshara_list,"ಉತ್ಸಾಹ ರಗಳೆ",3,lg_list,lg_dup)
			return True
		tf=self.ragaleMaster(copy.deepcopy(lg_list),1)
		if tf == True :
			self.Print_Master(akshara_list,"ಮಂದಾನಿಲ ರಗಳೆ",4,lg_list,lg_dup)
			return True
		tf=self.ragaleMaster(copy.deepcopy(lg_list),2)
		if tf == True :
			self.Print_Master(akshara_list,"ಲಲಿತ ರಗಳೆ",5,lg_list,lg_dup)
			return True
		return False		

	def vruttaMaster(self,lg_list,string):
		if len(lg_list) == 4 :
			for line in lg_list :
				line_string=''.join(str(l) for l in line)
				if line_string != string :
					return False
			return True
		else :
			return False

	def vrutta(self,akshara_list,lg_list,lg_dup) :
		utpalamalaK="21121211121121121212"
		champakamalaK="111121211121121121212"
		shardulaK="2221121211122212212"
		mattebhaK="11221121211122212212"
		sragdharaK="222212211111122122122"
		mahasragdharaK="1122212211111122122122"
		tf=self.vruttaMaster(copy.deepcopy(lg_list),utpalamalaK)
		if tf == True :
			self.Print_Master(akshara_list,"ಉತ್ಪಲಮಾಲಾವೃತ್ತ",0,lg_list,lg_dup)
			return True
		tf=self.vruttaMaster(copy.deepcopy(lg_list),champakamalaK)
		if tf == True :
			self.Print_Master(akshara_list,"ಚಂಪಕಮಾಲಾವೃತ್ತ",0,lg_list,lg_dup)
			return True
		tf=self.vruttaMaster(copy.deepcopy(lg_list),shardulaK)
		if tf == True :
			self.Print_Master(akshara_list,"ಶಾರ್ದೂಲವಿಕ್ರೀಡಿತವೃತ್ತ",0,lg_list,lg_dup)
			return True
		tf=self.vruttaMaster(copy.deepcopy(lg_list),mattebhaK)
		if tf == True :
			self.Print_Master(akshara_list,"ಮತ್ತೇಭವಿಕ್ರೀಡಿತವೃತ್ತ",0,lg_list,lg_dup)
			return True
		tf=self.vruttaMaster(copy.deepcopy(lg_list),sragdharaK)
		if tf == True :
			self.Print_Master(akshara_list," ಸ್ರಗ್ಧರಾವೃತ್ತ ",0,lg_list,lg_dup)
			return True
		tf=self.vruttaMaster(copy.deepcopy(lg_list),mahasragdharaK)
		if tf == True :
			self.Print_Master(akshara_list,"ಮಹಾಸ್ರಗ್ಧರಾವೃತ್ತ",0,lg_list,lg_dup)
			return True
		return False

	def chandassu(self,akshara_list,lg_list,lm):
		akshara_para=[]
		lg_para=[]
		lg_dup=[]
		len1=len(akshara_list)
		i=0
		while i<len1 :
			while i<len1 and len(akshara_list[i]) != 0 :
				akshara_para.append(akshara_list[i])
				lg_para.append(lg_list[i])
				lg_dup.append(lm[i])
				i=i+1	
			tf=self.kandapadya(copy.deepcopy(akshara_para),copy.deepcopy(lg_para),copy.deepcopy(lg_dup))
			if tf == True :
				akshara_para=[]
				lg_para=[]
				lg_dup=[]
				i=i+1
				continue
			tf=self.shatpadi(copy.deepcopy(akshara_para),copy.deepcopy(lg_para),copy.deepcopy(lg_dup))
			if tf == True :
				akshara_para=[]
				lg_para=[]
				lg_dup=[]
				i=i+1
				continue
			tf=self.ragale(copy.deepcopy(akshara_para),copy.deepcopy(lg_para),copy.deepcopy(lg_dup))
			if tf == True :
				akshara_para=[]
				lg_para=[]
				lg_dup=[]
				i=i+1
				continue
			tf=self.vrutta(copy.deepcopy(akshara_para),copy.deepcopy(lg_para),copy.deepcopy(lg_dup))
			if tf == True :
				akshara_para=[]
				lg_para=[]
				lg_dup=[]
				i=i+1
				continue
			self.Print_Master(akshara_list,"Invalid",7,lg_list,lm)
			akshara_para=[]
			lg_para=[]
			lg_dup=[]
			i=i+1
	def Print_Master(self,akshara_list,str1,ch,lg_list,lm) :
		akshara_list1=copy.deepcopy(akshara_list)
		akshara_list2=copy.deepcopy(akshara_list)
		laghu_guru=[]
		Join=[]
		Gana=[]
		lk=[]
		lk1=[]
		b = {'211':'  ಭ  ','111':'  ನ  ','122':'  ಯ  ','121':'  ಜ   ','212':'  ರ  ','112':'  ಸ   ','221':'  ತ   ','222':'  ಮ  ','1':'ಲ','2':'ಗು','12':'ಲ ಗು','21':'ಗು ಲ','11':'ಲ ಲ','22':'ಗು ಗು '}
		for j in range(0,len(lg_list),1):
			m=[]
			k=[]
			sum1=0
			x=3
			y=4
			k1=0
			for i in range(0,len(lg_list[j]),3):
				if (i+3)<len(lg_list[j]):
					m.append((''.join([str(ele) for ele in lg_list[j][i:i+3]])))
				else:
					m.append((''.join([str(ele) for ele in lg_list[j][i:]])))
			Join.append(m)
			for i in range(0,len(m),1):
				if m[i] in b:
					k.append(b[m[i]])
			Gana.append(k)
			k=[]
			le=[]
			le1=[]
			for i in range(0,len(lm[j])):
				if lm[j][i]==1:
					le.append('U')
					le1.append('U')
				elif lm[j][i]==2:	
					le.append('_ ')
					le1.append('_ ')
				k1=k1+1
				if i!=len(lm[j])-1:
					if lm[j][i+1]==0:
						le.append(' ')
						le1.append(' ')
						k1=k1-1
				sum1=sum1+lm[j][i]
				if ch==1 and sum1==x:
					le.insert(len(le),'|')
					akshara_list[j].insert(len(le)-1,'|')	
					sum1=0
					temp=x
					x=y
					y=temp
				else:
					if sum1==ch:
						le.insert(len(le),'|')
						c=akshara_list[j]
						c.insert(len(le)-1,'|')	
						sum1=0
				if k1==3:
					le1.insert(len(le1)+1,'|')
					akshara_list2[j].insert(len(le1)-1,'|')
					k1=0
			lk1.append(le1)
			lk.append(le)
			laghu_guru.append(k)
		for i in range(0,len(lg_list)):
			laghu_guru[i].append(sum(lg_list[i]))
		if (len(akshara_list))==0:
			f=open("Chandassu.txt",'w')
			f.write("Invalid")
		elif ch==0:
			self.print_to_file(akshara_list2,lk1,2,'Chandassu.txt',Gana,str1)
		elif ch==7:
			for i in range(0,len(lk)):
				for j in lk[i]:
					if j=='|':
						lk[i].remove(j)
			self.print_to_file(akshara_list1,lk,2,'Chandassu.txt',[],str1)
		elif ch==1 or ch==3 or ch==4 or ch==5:
			self.print_to_file(akshara_list,lk,2,'Chandassu.txt',[],str1)
		for k in range(0,3):
			for i in range(0,len(lk)):
				for j in lk[i]:
					if j=='|':
						lk[i].remove(j)						
		for k in range(0,3):
			for i in range(0,len(akshara_list)):
				for j in akshara_list[i]:
					if j=='|':
						akshara_list[i].remove(j)						
		self.print_to_file(akshara_list,lk,8,'laghu_Guru.txt',[],' ')
	def print_to_file(self,akshara_list=[],laghu_guru=[],ch=None,file1='',Gana=[],str1=''):
		t=[]
		f=open(file1,"a")
		for i in range(0,len(akshara_list)):
			if (len(Gana))==(len(akshara_list)):
				t.append(Gana[i])
			t.append(laghu_guru[i])
			t.append(akshara_list[i])
		t1=[x for x in t if x!=[]]
		for k in range(0,len(t1)):
			z=t1[k]
			for g in range(0,len(z)):
				f.write(str(z[g]))
			f.write('\n')
		f.write('\n')
		if str1!=' ':
			f.write(str1)
		if ch!=8 :
			f.write("\n-----------------------------------------------------------------------------\n")
		f.close()
if __name__ == '__main__':	
	f = open(sys.argv[1],"r")
	f1=open("Chandassu.txt",'w')
	f1.close()
	f2=open("laghu_Guru.txt",'w')
	f2.close()
	Module1_instance=Module1()
	akshara_list=Module1_instance.line_partition(f)
	Module2_instance=Module2()
	lm,lg_list=Module2_instance.laghu_guru(copy.deepcopy(akshara_list))
	Module3_instance=Module3()
	Module3_instance.chandassu(copy.deepcopy(akshara_list),copy.deepcopy(lg_list),copy.deepcopy(lm))
