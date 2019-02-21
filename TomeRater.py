class User:
	
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.books = {}
		

	def get_email(self):
		return self.email

	def change_email(self, new_email):
		self.users[new_email] = name
		print("Email address for {name} has been changed to {email}.".format(name = self.name, email = self.email))
			
	
	def __repr__(self):
		print('User: ' + self.name + ', email: ' + self.email + ', books read: ' + 'Hold')

	def __eq__(self, other_user):
		if self.name == other_user.name and self.email == other_user.email:
			other_user = self
	
	def read_book(self, book, rating = None):
		self.books[book] = rating
						
	
class Book:
	def __init__(self, title, isbn):
		self.title = title
		self.isbn = isbn
		self.ratings = []
		
	def get_title(self):
		return self.title
		
	def get_isbn(self):
		return self.isbn
		
	def set_isbn(self, new_isbn):
		if self.isbn != new_isbn:
			self.isbn = new_isbn
			print ("ISBN has been updated")
			
	def add_rating(self, rating):
		if self.rating >= 0 and self.rating <= 4:
			self.ratings.append(rating)
		else:
			print("Invalid Rating")
		
	def __eq__(self, new_book):
		if self.title == new_book.title and self.isbn == new_book.isbn:
			self = new_book
		
	def get_average_rating(self, rating):
		count = 0
		for i in self.books:
			count += rating
		
	def __hash__(self):
		return hash((self.title, self.isbn))	

class Fiction(Book):
	def __init__(self, title, author, isbn):
		super().__init__(title, isbn)
		self.author = author
	
	def get_author(self):
		return self.author
		
	def __repr__(self, title, author):
		return self.title + " by " + self.author
		
class NonFiction(Book):
	def __init__(self, title, subject, level, isbn):
		super().__init__(title, isbn)
		self.subject = subject
		self.level = level
		
	def get_subject(self):
		return self.subject
	
	def get_level(self):
		return self.level
		
	def __repr__(self, title, level, subject):
		return self.title + " , a " + self.level + " manual on " + self.subject

class TomeRater:
	
	def __init__(self):
		self.users = {}
		self.books = {}
			
	def create_book(self, title, isbn):
		new_book = Book(title, isbn)
		return new_book
			
	def create_novel(self, title, author, isbn):
		new_fiction = Fiction(title, author, isbn)
		return new_fiction
		
	def create_non_fiction(self, title, subject, level, isbn):
		new_non_fiction = NonFiction(title, subject, level, isbn)
		return new_non_fiction
		
	def add_book_to_user(self, book, email, rating = None):
		if email in self.users:
			self.users[email].read_book(email, rating)
			book.add_rating(rating)
		else:
			print ("No user with this email")
			
			
	def add_user(self, name, email, user_books = None):
		self.users[email] = User(name, email)
		if user_books:
			for book in user_books:
				self.add_book_to_user(book, email)
	
	def __repr__(self):
		return self.title + self.isbn

	def print_catalog(self):
		for i in self.books:
			print (i)
	
	def print_users(self):
		for i in self.users:
			print (i)

Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)

#Uncomment these to test your functions:
Tome_Rater.print_catalog()
Tome_Rater.print_users()

#print("Most positive user:")
#print(Tome_Rater.most_positive_user())
#print("Highest rated book:")
#print(Tome_Rater.highest_rated_book())
#print("Most read book:")
#print(Tome_Rater.most_read_book())







