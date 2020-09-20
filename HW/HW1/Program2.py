import time

# Make Polynomial class
class Polynomial(object):
    Coefficient = []
    Degree = []
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

    # Addition Operation
    def addition(self, poly):
        new_coefficient = []
        new_degree = []
        max_degree = max(max(self.Degree), max(poly.Degree))
        for i in range(max_degree, -1, -1):
            if i in self.Degree and i in poly.Degree:
                new_degree.append(i)
                new_coefficient.append(self.Coefficient[self.Degree.index(i)] + poly.Coefficient[poly.Degree.index(i)])
            elif i in self.Degree:
                new_degree.append(i)
                new_coefficient.append(self.Coefficient[self.Degree.index(i)])
            elif i in poly.Degree:
                new_degree.append(i)
                new_coefficient.append(poly.Coefficient[poly.Degree.index(i)])
            else:
                pass
        return Polynomial(new_coefficient, new_degree)

    # Multiplication Operation
    def multiplication(self, poly):
        new_coefficient = []
        new_degree = []
        for i in self.Degree:
            for j in poly.Degree:
                co = self.Coefficient[self.Degree.index(i)] * poly.Coefficient[poly.Degree.index(j)]
                if i+j in new_degree:
                    new_coefficient[new_degree.index(i+j)] += co
                else:
                    new_degree.append(i+j)
                    new_coefficient.append(co)
        return Polynomial(new_coefficient, new_degree)

    # Differentiation Operation
    def differentiation(self):
        new_cofficient = []
        new_degree = []
        for i in range(max(self.Degree), 0, -1):
            new_degree.append(i-1)
            new_cofficient.append(i*self.Coefficient[self.Degree.index(i)])
        return Polynomial(new_cofficient, new_degree)


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
p1 = create_polynomial()
p2 = create_polynomial()

print("\n")
print("The result of addition of p1 and p2 is")
p1.addition(p2)
print("\n")
print("The result of multiplication of p1 and p2 is")
p1.multiplication(p2)
print("\n")
print("The result of differentiation of p1 is")
p1.differentiation()
print("The result of differentiation of p2 is")
p2.differentiation()
print("\n")

end_time = time.time()
elapsed_time = end_time - start_time
print("The time elapsed to execute this code is", elapsed_time, 'seconds.')
