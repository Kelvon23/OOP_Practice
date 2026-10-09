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

    valid_bases = ["adenine","cytosine","guanine","thymine"]

    def __init__(self,nucleotide):
        self.base = nucleotide

    def __repr__(self):
        return f"DNABase(nucleotide= '{self.base}')"



def main():
    pass







