class Solution:
    def combine(self, x: list,y: list):
        return [str(i)+str(j) for i in x for j in y]
    
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {
            '2' : ['a','b','c'],
            '3' : ['d','e','f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r','s'],
            '8' : ['t','u','v'],
            '9' : ['w','x','y','z']
        }
        
        combos = []
        for d in digits:
            if combos == []:
                combos = keypad[d]
            else:
                combos = self.combine(combos,keypad[d])
        return combos