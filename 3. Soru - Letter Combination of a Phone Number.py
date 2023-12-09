class TextToPhoneConversion:
    def __init__(self):
        self.phoneMap = {
            '1': 1,
            'a': 2, 'b': [2,2], 'c': [2,2,2], '2': [2,2,2,2],
            'd': 3, 'e': [3,3], 'f': [3,3,3], '3': [3,3,3,3],
            'g': 4, 'h': [4,4], 'i': [4,4,4], '4': [4,4,4,4],
            'j': 5, 'k': [5,5], 'l': [5,5,5], '5': [5,5,5,5],
            'm': 6, 'n': [6,6], 'o': [6,6,6], '6': [6,6,6,6],
            'p': 7, 'q': [7,7], 'r': [7,7,7], 's': [7,7,7,7], '7': [7,7,7,7,7],
            't': 8, 'u': [8,8], 'v': [8,8,8], '8': [8,8,8,8],
            'w': 9, 'x': [9,9], 'y': [9,9,9], 'z': [9,9,9,9], '9': [9,9,9,9,9],
            ' ': 0, '0': [0,0]
        }

    def TextToNumber(self, text):
        result = []
        for char in text:
            if char in self.phoneMap:
                result.append(self.phoneMap[char])
        return result


# Örnek
phone = TextToPhoneConversion()
text = "soru 3"
output = phone.TextToNumber(text)
print("Input:", text)
print("Output:", output)

