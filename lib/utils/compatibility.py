class Compatibility:

    def read(self):
        text = ''
        try:
            text = raw_input()
        except:
            text = input()

        return text
