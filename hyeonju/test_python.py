p1_v = [-1, 3]
p1_u = [0, 4]
p1_v_plus_u = [p1_v[i]+p1_u[i] for i in range(len(p1_v))]
p1_v_minus_u = [p1_v[i]-p1_u[i] for i in range(len(p1_v))]
p1_three_v_minus_two_u = [3*(p1_v[i])-2*(p1_u[i]) for i in range(len(p1_v))]
print(p1_v_plus_u)
print(p1_v_minus_u)
print(p1_three_v_minus_two_u)
