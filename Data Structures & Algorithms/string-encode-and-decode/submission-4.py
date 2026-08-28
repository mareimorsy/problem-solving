class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word

        return result

    def decode(self, s: str) -> List[str]:
        result = []

        i = 0

        while i < len(s):
            # Find the # separating length from word
            j = i

            while s[j] != "#":
                j += 1

            # Get the length
            length = int(s[i:j])

            # Start of the word
            start = j + 1

            # Extract exactly `length` characters
            word = s[start:start + length]

            result.append(word)

            # Move to the next encoded word
            i = start + length

        return result