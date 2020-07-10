class StringConverter:

    def add(self, input):
        output = 0

        if not input:
            return output

        if ',' in input:
            numbers = input.split(',')
            for number in numbers:
                output += int(number)
            return output

        return int(input)
