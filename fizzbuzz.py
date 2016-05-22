class FizzBuzz():

    default_rules = { 3: 'Fizz', 5: 'Buzz' }

    def __init__(self, rules = default_rules):
        self.rules = rules

    def value_for(self, number, ):
        value = ''

        for divisor, outcome in self.rules.iteritems():
            if number % divisor == 0: value += outcome

        return value or str(number)
