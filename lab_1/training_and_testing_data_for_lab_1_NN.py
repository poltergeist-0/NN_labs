import random

s = -8
e = 8
n_training = 24
n_testing = 6

def f(n):
    flag = 0
    while flag == 0:
        counter = 0
        # for training and testing
        u = []
        y = []
        # for visualisation
        uu1 = []
        uu2 = []
        for i in range(n):
            x1,x2 = random.randint(s,e),random.randint(s,e)
            y_o = []
            if x2 > (-2) * x1 - 3:
                y1 = 1
            else:
                y1 = 0
            if x2 > x1 + 5:
                y2 = 1
            else:
                y2 = 0
            y.append([y1,y2])
            u.append([1,x1,x2])
            
            uu1.append(x1)
            uu2.append(x2)

        for i in range(n):
            if u[i][1] == (-2) * u[i][2] - 3 or u[i][1] == u[i][2] + 5:
                counter += 1
        if counter == 0: flag = 1

    print(uu1,"\n",uu2,"\n")
    return u,y;

u_training,y_training = f(n_training)
u_testing,y_testing = f(n_testing)

print()

print("training data is 80% that is",n_training,"elements\nu:\n",u_training,"\ny:\n",y_training)
print("\ntesting data is 20% that is",n_testing,"elements\nu:\n",u_testing,"\ny:\n",y_testing)
