
qlist =[]#dic
print("Quiz application")
print(''' Select Your Choice:
1. Attempt Quiz
2. Add Question
3. Exit''')
ch=0
while(ch != 3):
	ch=int(input("Enter Your Choice"))
	if ch == 1:
		rans=0
		wans=0
		print("Attempt Quiz Now")
		for q in qlist:
			print(q['qt'])
			print(q['A'])
			print(q['B'])
			print(q['C'])
			print(q['D'])
			ans= input("answer")

			if q['CAns']==ans:
				rans=rans+1
			else:
				wans=wans+1
			print("Total right ans",rans)
			print("Total wrong ans",wans)
	if ch == 2:
		q={}
		q['qt']=input("Enter Question")
		q['A']=input("option A")
		q['B']=input("option B")
		q['C']=input("option C")
		q['D']=input("option D")
		q['CAns']=input("Correct Option")
		qlist.append(q)
		print("Add new question here")
