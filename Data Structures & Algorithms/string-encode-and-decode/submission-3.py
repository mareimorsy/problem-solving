class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for word in strs:
            output += word + '#@#'
        return output

    def decode(self, s: str) -> List[str]:

        result = s.split('#@#')

        result.pop()

        return result

        
