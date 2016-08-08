from sympy.solvers.solveset import solveset_complex
from sympy import *
t, y, z = symbols('t y z')
init_printing(use_unicode=True)

def my_func(y, t):
    eqn = -(4*z**3 - 9*t*z + 27)*(z**2 - 3*t) - y**2
    return solveset_complex(eqn, z)

def plot_func(y, t):
    import matplotlib as mpl
    mpl.use('Agg')
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim((-10,10))
    ax.set_ylim((-10,10))
    ax.set_xlabel('Real')
    ax.set_ylabel('Imaginary')
    for item in y:
        print item
        output = my_func(item/10000, t)
        # print output
        sols = [N(solution) for solution in output]
        # print sols
        # for item in sols:
        #     print complex(item).real
        #     print complex(item).imag
        for x in range(len(sols)):
            ax.plot(complex(sols[x]).real, complex(sols[x]).imag, 'ro-',label='python')
    fig.savefig('temp1.png')

# plot_func(range(0,100,10), 0)



def plot_func_bokeh(y, t):
    from bokeh.plotting import figure, output_file, show
    # mpl.use('Agg')
    # import matplotlib.pyplot as plt
    # fig = plt.figure()
    output_file("bokeh_plot.html")
    p = figure(title="simple example", x_axis_label='Real', y_axis_label='Imaginary', x_range = [-10,10], y_range = [-10,10])

    # ax = fig.add_subplot(111)
    # ax.set_xlim((-10,10))
    # ax.set_ylim((-10,10))
    # ax.set_xlabel('Real')
    # ax.set_ylabel('Imaginary')
    for item in y:
        print item
        output = my_func(item, t)
        # print output
        sols = [N(solution) for solution in output]
        # print sols
        # for item in sols:
        #     print complex(item).real
        #     print complex(item).imag
        for x in range(len(sols)):
            p.circle(complex(sols[x]).real, complex(sols[x]).imag, fill_color = "red", size=6)
    # fig.savefig('temp1.png')
    show(p)

plot_func_bokeh(range(0,100,1), 0)


#
# def my_func2(y, t):
#     eqn = -(4 * z ** 3 - 9 * t * z + 27) * (z ** 2 - 3 * t) - y ** 2
#     return solveset_complex(eqn, z)