import random
import math

#this is test variant
def generator(percentage : dict):
    rangesWithValues = []#[start,end,value]
    i=0
    for j in percentage.keys():
        rangesWithValues.append([i,i+percentage[j],j])
        i+=percentage[j]
    val = random.randint(1,100)
    for l in rangesWithValues:
        if val>l[0] and val<l[1]:
            return l[2]


class generatorRange:
    """
    generate a rand int with a dict.Keys is a value to return, value is a drop percentage
    example:
        {
            '12':25,
            '1':25,
            '2':50,
        }
        return a random key with drop percentage
    
    """
    def __init__(self, percentage) -> None:
        self.percentage = percentage
        self.rangesWithValues = []
        i=0
        for j in percentage.keys():
            self.rangesWithValues.append([i,i+percentage[j],j])
            i+=percentage[j]
        if self.rangesWithValues[-1][1]!=100:
            raise ValueError("the sum of procent not equals to 100")
    def generate(self):
        val = random.randint(1,100)
        for l in self.rangesWithValues:
            if val>l[0] and val<=l[1]:
                return l[2]
    
