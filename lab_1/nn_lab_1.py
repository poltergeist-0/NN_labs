# training and testing data
u =  [[1, 3, 6], [1, 3, -4], [1, 2, 6], [1, -6, -1], [1, 7, -4], [1, 7, -2], [1, 1, 3], [1, -1, 3], [1, 4, 1], [1, 5, -8], [1, -3, 8], [1, 7, 8], [1, 1, 8], [1, 8, 4], [1, -1, -2], [1, -8, 4], [1, 0, -1], [1, -5, -8], [1, -6, 1], [1, 4, -2], [1, -6, 8], [1, -3, -3], [1, -1, 5], [1, -5, 3]]
y = [[1, 0], [1, 0], [1, 0], [0, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 1], [1, 0], [1, 1], [1, 0], [0, 0], [0, 1], [1, 0], [0, 0], [0, 1], [1, 0], [0, 1], [0, 0], [1, 1], [0, 1]]
n1 = len(u)

u_testing = [[1, -3, 7], [1, -5, 3], [1, -4, 3], [1, -3, -6], [1, 3, -5], [1, -3, 5]] 
y_testing =  [[1, 1], [0, 1], [0, 1], [0, 0], [1, 0], [1, 1]]
n2 = len(u_testing)


# activation function
def sgn(n):
    if n > 0: return 1
    else: return 0


## model initialization
w = [[0,0,0],[0,0,0]]

## cycle through training data (stops when all training examples are correctly classificated)
counter = n1*2

while counter != 0:
    counter = n1*2
    
    for i in range(n1):
        for k in range(len(w)):
            wk_u_matrix_product = 0
            for j in range(len(w[k])):
                wk_u_matrix_product += w[k][j] * u[i][j]
            y_o = sgn(wk_u_matrix_product)
            if y_o != y[i][k]:
                for j in range(len(w[0])):
                    w[k][j] += (y[i][k] - y_o) * u[i][j]
            else: counter -= 1
            
for i in range(len(w)):
    print("\nw",i+1,"1 =",w[i][1],"\nw",i+1,"2 =",w[i][2],"\nb",i+1,"=",w[i][0])

# cycle through testing data
y_output = []
for i in range(len(u_testing)):
    y_o = []
    for k in range(len(w)):
        w_u_matrix_product = 0
        for j in range(len(w[k])):
            w_u_matrix_product += w[k][j] * u_testing[i][j]
        y_o.append(sgn(w_u_matrix_product))
    y_output.append(y_o)

print("\nthe result of test data processing and the correct values\n",*y_output,"\n",*y_testing)

# counting errors
counter = 0
for i in range(len(u_testing)):
    if y_output[i] != y_testing[i]:
        counter += 1
print("number of mistakes made - ",counter," (that is",int(counter/(len(u_testing)/100)),"%)")


# for visualisation
##u1_wrong_testing = []
##u2_wrong_testing = []
##
##u1_right_testing = []
##u2_right_testing = []

##for i in range(len(y_output)):
##    if y_output[i] == y_testing[i]:
##        u1_wrong_testing.append(u_testing[i][1])
##        u2_wrong_testing.append(u_testing[i][2])
##    else:
##        u1_right_testing.append(u_testing[i][1])
##        u2_right_testing.append(u_testing[i][2])
##
##print(u1_right_testing)
##print(u2_right_testing)
##
##print(u1_wrong_testing)
##print(u2_wrong_testing)
