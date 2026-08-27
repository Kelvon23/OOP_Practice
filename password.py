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
    


def main():

    print("=== Default Password ===")
    default = Password()
    print(f"Strength: {default.strength}")
    print(f"Length: {len(default.password)}")
    print(f"Password: {default.password}")
    print()

    print("=== Low Strength Password ===")
    low = Password("low")
    print(f"Strength: {low.strength}")
    print(f"Length: {len(low.password)}")
    print(f"Password: {low.password}")
    print()

    print("=== Mid Strength Password ===")
    mid = Password("mid")
    print(f"Strength: {mid.strength}")
    print(f"Length: {len(mid.password)}")
    print(f"Password: {mid.password}")
    print()

    print("=== High Strength Password ===")
    high = Password("high")
    print(f"Strength: {high.strength}")
    print(f"Length: {len(high.password)}")
    print(f"Password: {high.password}")
    print()

    print("=== Custom Length Password ===")
    custom = Password("mid", 20)
    print(f"Strength: {custom.strength}")
    print(f"Length: {len(custom.password)}")
    print(f"Password: {custom.password}")
    print()

    print("=== Input Universe ===")
    universe = Password.show_input_universe()
    print(universe)


if __name__ == "__main__":
    main()

            


