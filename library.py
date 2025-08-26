library = ["python for beginners","data structures in C", "AI basics"]
borrowed_books= {}
student_id = 1

def start():
	while True:

		print('''
	1. display books
	2. add books
	3. borrow books
	4. return books
	5. list of students that borrow books
	6. exit

		''')

		user_choice = int(input("enter command:\n"))
		call_function(user_choice)
		if user_choice ==6:
			break

def call_function(user_choice):
	if user_choice ==1:
		display_books()
	elif user_choice ==2:
		book_name= input("enter book to add:\n")
		add_book(book_name)
	elif user_choice ==3:
		book_name = input("enter name of book:\n")
		borrow_book(book_name)
	elif user_choice == 4:
		book_name = input("enter book name to return:\n")
		return_book(book_name)
	elif user_choice == 5:
		students_that_borrow()		
	
	

def display_books():
	if len(library)	!= 0:
		for book in library:
			print(book)
	else:
		print("no books in the library")		
def add_book(book_name):
	if book_name in library:
		print("book already exist")
	else:
		library.append(book_name)
		print(f"{book_name} succesfully added")
		
def borrow_book(book_name):
	global student_id
	if book_name in library:
		library.remove(book_name)
		borrowed_books[student_id] = book_name
		student_id += 1
	else:
		print("book not found")
		

def return_book(book_name):
	book_found = False
	student_to_remove = None
	global student_id
	if not borrowed_books:
		print("no book has been borrowed")
	for student_id_key, borrowed_book in borrowed_books.items():
		if borrowed_book == book_name:
			book_found = True
			student_to_remove = student_id_key
			break				
	if book_found:
		del borrowed_books[student_to_remove]
		library.append(book_name)
		print(f"{book_name} has been returned successfully")
def students_that_borrow():
	if borrowed_books:
		print(borrowed_books)
	else:
		print("no book has been borrowed")	
				

	



















				
			

















start()	
