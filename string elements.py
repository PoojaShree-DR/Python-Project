class strings:
    def __init__(self):
        self.uppercase=0
        self.lowercase=0
        self.vowels=0
        self.consonants=0
        self.spaces=0
        self.string=" "
    def getstr(self):
        self.string=input("Enter a string:")
    def count_upper(self):
        for ch in self.string:
            if (ch.isupper()):
                self.uppercase+=1
    def count_lower(self):
        for ch in self.string:
            if (ch.islower()):
                self.lowercase+=1
    def count_vowels(self):
        for ch in self.string:
            if(ch in('A','a','E','e','I','i','O','o','U','u')):
                self.vowels+=1
    def count_consonants(self):
        for ch in self.string:
            if(ch not in('A','a','E','e','I','i','O','o','U','u')):
                self.consonants+=1
    def count_spaces(self):
        for ch in self.string:
            if(ch==" "):
                self.spaces+=1
    def execute(self):
        self.count_upper()
        self.count_lower()
        self.count_vowels()
        self.count_consonants()
        self.count_spaces()
    def display(self):
        print("The given string contains...")
        print("%d Uppercase letters"%self.uppercase)
        print("%d Lowecase letters"%self.lowercase)
        print("%d Vowels"%self.vowels)
        print("%d Consonants"%self.consonants)
        print("%d Spaces"%self.spaces)
s=strings()
s.getstr()
s.execute()
s.display()
                
            
                
                
