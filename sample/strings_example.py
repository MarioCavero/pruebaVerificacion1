import urllib3

class StringsExamples(object):
    """A class to play with the strings"""

    @staticmethod
    def concat_strings(string1, string2):
        if type(string1) is not str or type(string2) is not str:
            raise TypeError
        return string1+string2

    @staticmethod
    def concat_3strings(string1, string2, string3):
        if type(string1) is not str or type(string2) is not str or type(string3) is not str:
            raise TypeError
        return string1 + string2+string3

    @staticmethod
    def concat_4strings(string1, string2, string3, string4):
        if type(string1) is not str or type(string2) is not str or type(string3) is not str or type(string4) is not str:
            raise TypeError
        return string1 + string2 + string3 +string4

    @staticmethod
    def concat_5strings(string1, string2, string3, string4, string5):
        if type(string1) is not str or type(string2) is not str or type(string3) is not str or type(string4) is not str or type(string5) is not str:
            raise TypeError
        return string1 + string2+string3+string4+string5

    @staticmethod
    def concat_6strings(string1, string2, string3, string4, string5, string6):
        if type(string1) is not str or type(string2) is not str or type(string3) is not str or type(
                string4) is not str or type(string5) is not str or type (string6) is not str:
            raise TypeError
        return string1 + string2 + string3 + string4 + string5+string6

    @staticmethod
    def concat_7strings(string1, string2, string3, string4, string5, string6, string7):
        if type(string1) is not str or type(string2) is not str or type(string3) is not str or type(
                string4) is not str or type(string5) is not str or type(string6) is not str or type(string7) is not str:
            raise TypeError
        return string1 + string2 + string3 + string4 + string5 + string6 +string7

    @staticmethod
    def concat_8strings(string1, string2, string3, string4, string5, string6,string7, string8 ):
        if type(string1) is not str or type(string2) is not str or type(string3) is not str or type(
                string4) is not str or type(string5) is not str or type(string6) is not str or type(string7) is not str or type(string8) is not str:
            raise TypeError
        return string1 + string2 + string3 + string4 + string5 + string6+string7+string8

    @staticmethod
    def concat_9strings(string1, string2, string3, string4, string5, string6, string7, string8, string9):
        if type(string1) is not str or type(string2) is not str or type(string3) is not str or type(
                string4) is not str or type(string5) is not str or type(string6) is not str or type(
            string7) is not str or type(string8) is not str or type(string9) is not str:
            raise TypeError
        return string1 + string2 + string3 + string4 + string5 + string6 + string7 + string8+string9

    @staticmethod
    def concat_10strings(string1, string2, string3, string4, string5, string6, string7, string8, string9, string10):
        if type(string1) is not str or type(string2) is not str or type(string3) is not str or type(
                string4) is not str or type(string5) is not str or type(string6) is not str or type(
            string7) is not str or type(string8) is not str or type(string9) is not str or type(string10) is not str:
            raise TypeError
        return string1 + string2 + string3 + string4 + string5 + string6 + string7 + string8 +string9 +string10

    @staticmethod
    def concat_11strings(string1, string2, string3, string4, string5, string6, string7, string8, string9, string10, string11):
        if type(string1) is not str or type(string2) is not str or type(string3) is not str or type(
                string4) is not str or type(string5) is not str or type(string6) is not str or type(
            string7) is not str or type(string8) is not str or type(string9) is not str or type(string10) is not str or type(string11) is not str:
            raise TypeError
        return string1 + string2 + string3 + string4 + string5 + string6 + string7 + string8+string9 +string10+string11

    @staticmethod
    def get_first_string():
        response = urllib3.urlopen('https://gist.githubusercontent.com/jsdario/6d6c69398cb0c73111e49f1218960f79/raw/8d4fc4548d437e2a7203a5aeeace5477f598827d/el_quijote.txt')
        full_text = response.read()
        text_tokenized = full_text.split(' ')
        return text_tokenized[0]
