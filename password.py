import secrets
import string 

class Password:

    _character_pool = {
         "low":string.ascii_letters,
         "mid":string.ascii_letters + string.digits,
         "high":string.ascii_letters + string.digits + string.punctuation

      }  

    _default_character_count = {
         "low": 8,
         "mid": 12,
         "high": 16
      }


    def __init__(self,strength= "mid",length=None):
        self.length = length
        self.strength = strength
        self.password = self.generate_password()

    def generate_password(self):

      final_length = self.length if self.length is not None else Password._default_character_count[self.strength]

      final_character_pool = Password._character_pool[self.strength]

      password = "".join(secrets.choice(final_character_pool) for _ in range(final_length))

      return password
    
    @staticmethod
    def show_input_universe():
       universe_of_chars = {
          "letters":list(string.ascii_letters),
          "numbers":list(string.digits),
          "punctuation": list(string.punctuation)

       }
       return universe_of_chars


    



            


