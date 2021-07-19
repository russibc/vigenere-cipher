from utils import Utils


class Vigenere:

    def vigenere(text, key, alphabet, cipher):
        result = ""

        text = text.lower()

        split_text = Utils.split_text(text, len(key))

        dic_num = dict(zip(alphabet, range(len(alphabet))))
        dic_letter = dict(zip(range(len(alphabet)), alphabet+' '))

        for split in split_text:
            i = 0
            for letter in split:
                if(cipher):
                    num = (dic_num[letter] + dic_num[key[i]]) % len(alphabet)
                else:
                    num = (dic_num[letter] - dic_num[key[i]]) % len(alphabet)
                result += dic_letter[num]
                i += 1

        return result
