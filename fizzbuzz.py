class FizzBuzz():

    default_rules = { 3: 'Fizz', 5: 'Buzz' }

    def __init__(self, rules = default_rules):
        self.rules = rules

    def iterator(self, start = 1, stop = 100):
        while stop == -1 or start <= stop:
            yield self.value_for(start)
            start += 1

    def value_for(self, number, ):
        value = ''

        for divisor, outcome in self.rules.iteritems():
            if number % divisor == 0: value += outcome

        return value or str(number)
