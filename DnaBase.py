"""

#Understanding the requirements

When we recieve for nucleotide it wants to validated and standaridez

expose the nucleotide in attribute called based:
does that mean it want to create an attribute called base and save 
nucleotide

only valid input are adenine, cytosine, guanine, and thymine


user write like dnabase (a) or (adenine) are accepted as long as 
they match to valid input list but also should be case insesitively
so have all input be lowercase so capitlazation doesn't have an effect

accessing the value it should return full name no matter
how it was spelt orginally


object should full string represtion of how to build it in ground up


Invalid input should be rejected always and produce typeerror 
dont matter if it at instance creation or later altered through 
attribute setters


"""
class DNABase:

    valid_bases={
        "a":"adenine",
        "c":"cytosine",
        "g":"guanine",
        "t":"thymine"
    }

    def __init__(self,nucleotide):
        self.base = nucleotide

    def __repr__(self):
        return f"DNABase(nucleotide='{self.base}')"

    @property
    def base(self):
        return self._base


    @base.setter
    def base(self,nucleotide):
        base = nucleotide.lower()

        if base in self.valid_bases:
            self._base = self.valid_bases[base]
        elif base in self.valid_bases.values():
            self._base = base
        else:
            raise ValueError(f"{nucleotide} is not a recognized DNA nucleotide")




def main():

    b1 = DNABase("A")

    b2 = DNABase("CYTOSINE")

    b3 = DNABase("g")

    b4 = DNABase("ThYmInE")

    b5 = DNABase("Aoli")

    #adenine
    print(b1.base)

    #cytosine
    print(b2.base)

    #guanine
    print(b3.base)

    #thymine
    print(b4.base)

    #Aoli is not a recognized DNA nucleotide
    print(b5.base)



if __name__ == "__main__":
    main()


