import time

# Make Polynomial class
class Polynomial(object):
    def __init__(self, coefficient, degree):
        self.Coefficient = coefficient
        self.Degree = degree

        for i in range(len(coefficient)):
            co_str = str(coefficient[i])
            de_str = str(degree[i])

            if i == 0:
                if degree[i] == 0:
                    self.formula = co_str
                elif degree[i] == 1:
                    self.formula = co_str + 'x'
                else:
                    self.formula = co_str + 'x**' + de_str
            else:
                if degree[i] == 0:
                    self.formula += ' + ' + co_str
                elif degree[i] == 1:
                    self.formula += ' + ' + co_str + 'x'
                else:
                    self.formula += ' + ' + co_str + 'x**' + de_str
        print(self.formula)


# Function that create a Polynomial object
def create_polynomial():
    enter = input("What polynomial? \n (in form of axb + cxd + ...)")

    split_list = enter.split(' + ')
    list_of_coefficient = []
    list_of_degree = []

    for el in split_list:
        list_small = el.split('x')
        list_of_coefficient.append(int(list_small[0]))
        list_of_degree.append(int(list_small[1]))

    return Polynomial(list_of_coefficient, list_of_degree)

start_time = time.time()
p = create_polynomial()

end_time = time.time()
elapsed_time = end_time - start_time
print("The time elapsed to execute this code is", elapsed_time, 'seconds.')
