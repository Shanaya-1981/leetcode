
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for char in strs:
            current_word_no = len(char)
            encoded_string += str(current_word_no) + "#" + char
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        length_finder = 0

        while length_finder < len(s):
            hash_finder = length_finder

            while s[hash_finder] != "#":
                hash_finder += 1

            length = int(s[length_finder:hash_finder])
            word = s[hash_finder + 1 : hash_finder + 1 + length]
            decoded_list.append(word)
            length_finder = hash_finder + 1 + length

        return decoded_list