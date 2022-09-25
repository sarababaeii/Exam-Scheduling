* Maximizing minimum distance between any two following exams
* Works well

option MIP = CPLEX;
option optcr = 0;

set
    i
    j
    k /1 * 7/
    t /1 * 28/;
    
parameter
    a(i, j)
    b(i, k)
    d(t, k)
    max_t
    M
    c1 /10/
    c2 /-1/;
    
d(t, k) $ (floor(t.val / 7) * 7 + k.val = t.val) = 1;
max_t = smax(t, t.val);
M = 2 * max_t;


$onecho > task.txt
set=i cdim=0 rdim=1  rng=Data!A2:A58
set=j cdim=0 rdim=1  rng=Data!C2:C581
par=b cdim=0 rdim=2  rng=Data!E1:G108
par=a cdim=0 rdim=2  rng=Data!I1:K2310

$offecho

$call GDXXRW D:\Uni\00-1\CO\Project\final_data.xlsx  @task.txt
$GDXIN final_data.gdx
$LOAD i, j, b, a
$GDXIN

display i, j, k, t, a, b, d, M;


alias(i, i1);

variable z, z1, z2;
binary variable delta(i, t), gamma(j, t), theta(i, i1);
nonnegative variable x(i), y(j), u(j, t);

equation obj, obj1, obj2,
        completness, ignore, course_day, conflict,
        exam_date, distance1, distance2, free_y,
        student_exam_date, consecutive_exams;

obj..
    z =e= c1 * z1 + c2 * z2;
    
obj1..
    z1 =e= sum(j, y(j));
    
obj2..
    z2 =e= sum((j, t), u(j, t));
    
completness(i) $ (sum(j, a(i, j)) > 0)..
    sum(t, delta(i, t)) =e= 1;
    
ignore(i) $ (sum(j, a(i, j)) = 0)..
    sum(t, delta(i, t)) =e= 0;
    
course_day(i, t)..
    delta(i, t) =l= sum(k, b(i, k) * d(t, k));
    
student_exam_date(j, t)..
    gamma(j, t) =e= sum(i, a(i, j) * delta(i, t));
    
conflict(j, t)..
    gamma(j, t) =l= 1;
   
exam_date(i)..
    x(i) =e= sum(t, t.val * delta(i, t));

distance1(i, i1, j) $ (i.val <> i1.val and a(i, j) and a(i1, j))..
    y(j) =l= x(i) - x(i1) + M * theta(i, i1);
    
distance2(i, i1, j) $ (i.val <> i1.val and a(i, j) and a(i1, j))..
    y(j) =l= x(i1) - x(i) + M * (1 - theta(i, i1));

free_y(j) $ (sum(i, a(i, j)) < 2)..
    y(j) =e= 0;
    
consecutive_exams(j, t) $ (t.val <= max_t - 2)..
    gamma(j, t) + gamma(j, t + 1) + gamma(j, t + 2) - u(j, t) =l= 2;


model examScheduling /obj, obj1, obj2, completness, ignore, course_day, conflict, exam_date, distance1, distance2, free_y, student_exam_date, consecutive_exams/;
solve examScheduling using MIP maximizing z;
display z.l, z1.l, z2.l;
display delta.l, x.l;
display gamma.l, y.l, theta.l, u.l;


parameter et;
et = examScheduling.etsolve;

Execute_unload "D:\Uni\00-1\CO\Project\output.gdx" z.l, z1.l, z2.l, et, delta, x, gamma, y, u, theta;

$onecho > task1.txt
var=z.l cdim=0 rdim=0 rng=Summary!A2
var=z1.l cdim=0 rdim=0 rng=Summary!B2
var=z2.l cdim=0 rdim=0 rng=Summary!C2
par=et cdim=0 rdim=0 rng=Summary!D2
var=delta cdim=1 rdim=1 rng=delta!A1
var=x cdim=0 rdim=1 rng=x!A1
var=gamma cdim=1 rdim=1 rng=gamma!A1
var=y cdim=0 rdim=1 rng=y!A1
var=u cdim=1 rdim=1 rng=u!A1
var=theta cdim=1 rdim=1 rng=theta!A1
$offecho

execute 'gdxxrw.exe D:\Uni\00-1\CO\Project\output.gdx o=D:\Uni\00-1\CO\Project\output.xlsx @task1.txt'