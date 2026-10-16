class Publication:
    title:str
    author:str
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def set_title(self,title):
        self.title = title
    def set_author(self,author):
        self.author = author
    def display_info(self):
        print(f"Title: {self.title}\nAuthor: {self.author}")
        
class Book(Publication):
    number_of_pages:int
    def __init__(self,title,author,number_pages):
        self.title = title
        self.author = author
        self.number_pages = number_pages
        self.set_number_of_pages(number_pages)
    def get_number_of_pages(self):
        if self.number_pages>0:
            return f"Number of pages: {self.number_pages}"
        else:
            return "Number of pages must be positive."
    def set_number_of_pages(self,number_pages):
        if number_pages>0:
            self.number_pages = number_pages
        else:
            print("Number of pages must be positive.")
    
class Magazine(Publication):
    issue_number:int
    def __init__(self,title,author,issue_number):
        self.title = title
        self.author = author
        self.issue_number = issue_number
        self.set_issue_number
    def get_issue_number(self):
        if self.issue_number>0:
            return f"Issue number: {self.issue_number}"
        else:    
            return "Issue number must be positive."
    def set_issue_number(self,issue_number):
        self.issue_number = issue_number
        

    
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

print("Publication Information:")
pub1.display_info()
    
print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()
print(book1.get_number_of_pages())

print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())









