# -*- coding: utf-8 -*-

# module imported to exit Python
import sys

# the module is imported to turn a string into a mathematical expression
# and solve a given mathematical expression
import sympy as sy

# the module is imported to set the number e as the initial conditions
import math

# the module is imported to parse the string with the equation.
# module imported for build
import re

# the module is imported to create curves
import matplotlib.pyplot as plt

# the module imported output curves in GUI
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# the module imported toolbar output for curves in GUI
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar

# the module is imported to interact with GUI widgets
from PyQt5 import QtWidgets

# modules are imported to display GUI and change the size of GUI elements
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy

# module imported to create GUI
from gui import Ui_MainWindow

# class that implements the Euler method for ordinary differential equations
class Euler():

    # list of argument x values  for the equation
    __xlist = []

    # list of solutions by the Euler method
    __lstsolution = []

    # list of exact solutions
    __exactlist = []

    # list of differences between the exact solution and the solution by the Euler method
    __lstdifference = []

    # list of boundary values
    __coord = []

    # initial differential equation
    __equation = ""

    # exact solution to the original equation
    __exact_func = ""

    # dictionary with initial conditions of the form y (0) = 1 and the final value of the argument
    __condition = {'y*cos(x)': [0.0, 1.0, 1.0], '2*exp(x**2)-y/x': [1.0, 2.0, math.e], 'x*(y**2)': [0.0, 1.0, 1.0]}

    # dictionary of exact solutions of the original equations
    __exact = {'y*cos(x)': 'exp(sin(x))', '2*exp(x**2)-y/x': '(exp(x**2))/x', 'x*(y**2)': '2/(2-x**2)'}


    def __init__(self, eq):

        # initialize the equation
        equation = re.split(r'[=,]', eq)
        eq = equation[1]
        self.__equation = sy.sympify(eq)

        # initialize initial
        self.__coord.append(self.__condition[eq][0])
        self.__coord.append(self.__condition[eq][1])

        # initialize the end of the segment
        self.__coord.append(self.__condition[eq][2])

        # initialize the exact solution
        self.__exact_func = sy.sympify(self.__exact[eq])

        # obtain a numerical solution of the equation by the Euler method, the exact solution and compare them
        self.__decide()

    def __del__(self):

        # clear all lists
        self.__lstdifference.clear()
        self.__exactlist.clear()
        self.__xlist.clear()
        self.__lstsolution.clear()
        self.__coord.clear()

        # remove the equation and the exact solution
        self.__exact_func = ""
        self.__equation = ""

    # the function of solving the equation by a numerical method,
    # which calculates the exact solution and compares the obtained solutions
    def __decide(self):

        # step to solve numerically
        step = 0.1

        # initial conditions
        next_y = self.__coord[2]
        start_x = self.__coord[0]

        x, y = sy.symbols('x y')
        try:
            while start_x < self.__coord[1]:

                # calculate the value of the function at the point (x,y)
                func_val = self.__equation.evalf(subs={x: start_x, y: next_y})

                # calculate the solution by the Euler method
                next_y = next_y + step * func_val

                # calculate the exact solution
                exact = self.__exact_func.evalf(subs={x: start_x})

                # add solutions to the lists
                self.__xlist.append(round(start_x, 3))
                self.__lstsolution.append(round(next_y, 3))
                self.__exactlist.append(round(exact, 3))

                # add the difference between the exact solution and the numerical solution to the list
                self.__lstdifference.append(round(exact - next_y, 3))

                # calculate the following value argument
                start_x += step
                self.__end_y = next_y

            # add the final value of the function
            self.__coord.append(round(next_y, 1))

        except ZeroDivisionError:
            print("\nYou cannot divide by zero!")
            sys.exit(1)

    # the function returns the original equation
    def getEquation(self):
        return self.__equation

    # the function returns an exact solution function
    def getExactfunc(self):
        return self.__exact_func

    # the function returns a list values argument x
    def getLstX(self):
        return self.__xlist

    # the function returns a list of solutions by the Euler method.
    def getSolution(self):
        return self.__lstsolution

    # the function returns a list of differences between the exact solution and the Euler solution
    def getLstDiff(self):
        return self.__lstdifference

    # the function returns a list of solutions exact solution
    def getLstExac(self):
        return self.__exactlist

    # the function returns a list initial and final conditions
    def getCoord(self):
        return self.__coord


# the class for creating a canvas on which the
# curves of the exact solution and the Euler method will be placed
# at the input it takes the parameters of the shape
# based on the input gets the size of the window to display the curves
class MyMplCanvas(FigureCanvas):
    def __init__(self, fig, parent = None):
        self.fig = fig
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


# class interacting with GUI
class MainWindow(QMainWindow, Ui_MainWindow):

    # list of legends of exact solutions and solutions by the Euler method
    graph_legend = []

    def __init__(self, parent=None, *args, **kwargs):

        QMainWindow.__init__(self)
        self.setupUi(self)

        # add equations and initial conditions in the text field
        self.addEqaution()

        # get the parameters of the shape and axes
        self.fig, self.axes = self.plot_single_empty_graph()

        # by pressing the button solve the equation,
        # derive the values of the exact solution,
        # the solutions by the Euler method and draw curves
        self.btn_decide.clicked.connect(self.showSchedule)

        # create a widget for displaying curves and a toolbar
        self.campanovka = QtWidgets.QGridLayout(self.widget)
        self.canavas = MyMplCanvas(self.fig)
        self.campanovka.addWidget(self.canavas, 1, 3, 1, 1)
        self.toolbar = NavigationToolbar(self.canavas, self)
        self.campanovka.addWidget(self.toolbar, 2, 3, 1, 1)

    # the function adds equations and initial conditions to the widget list
    def addEqaution(self):

        # list equation and initial conditions
        list_equation = ["y'=y*cos(x),\ny(0)=1\n\n", "y'=x*(y**2),\ny(0)=1\n\n", "y'=2*exp(x**2)-y/x,\ny(1)=e"]
        self.list_equation.addItems(list_equation)
        self.list_equation.setCurrentRow(0)

    # the function receives  lists with solutions, initial and final conditions and transfers
    # them to the function of the image of curves and output the resulting solutions
    def showSchedule(self):

        # solve the selected equation
        method_Euler = Euler(self.newEquation())

        # obtain a list of initial and final conditions
        coord = method_Euler.getCoord()

        # initialize the initial conditions
        start_x = coord[0]
        start_y = coord[2]

        # initialize the final conditions
        end_x = coord[1]
        end_y = coord[3]

        # receive lists of decisions and differences of these decisions
        xlist = method_Euler.getLstX()
        ylist = method_Euler.getSolution()
        exlst = method_Euler.getLstExac()
        difflst = method_Euler.getLstDiff()

        # display the lists of solutions in the text field and draw the curves
        self.graph(self.axes, self.graph_legend,
                    start_y, end_y,
                    start_x, end_x, xlist,
                   ylist, exlst, difflst)

        self.fig.canvas.draw()

    # the function displays the obtained solutions
    # and the difference between the solutions in the text field and displays the curves
    # At the input, it accepts the lists of solutions and differences of these decisions,
    # the parameters of the shape and axes, the initial and final conditions
    def graph(self, axes=None, legend=None,
               start_y=None, end_y=None,
               start_x=None, end_x=None, xlist=None,
               ylist=None, exactlist=None, lstdifference=None):

        # clear the text field to display the solutions and the difference of these solutions
        self.txt_solution.clear()
        # display lists of solutions and differences of these solutions
        self.txt_solution.setText(" Exact solution: " + str(exactlist)
                                  + "\n\n Euler's method: " + str(ylist)
                                  + "\n\n Difference: " + str(lstdifference))

        # add the legends of the curves
        legend.append("Euler's method")
        legend.append("Exact solution")

        # draw curves
        plt.cla()
        axes.plot(xlist, ylist, '-', lw=2)
        axes.plot(xlist, exactlist, '.', lw=2)
        axes.set_xlim(float(start_x), float(end_x))
        axes.set_ylim(float(start_y), float(end_y))
        axes.legend(legend, loc='best', fontsize=8)
        axes.grid(True, c='lightgrey', alpha=0.5)
        axes.set_xlabel('X', fontsize=8)
        axes.set_ylabel('Y', fontsize=8)

    # the function returns the parameters of the shape and axes
    def plot_single_empty_graph(self):

        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10, 7), dpi=85,
                                 facecolor='white', frameon=True, edgecolor='black', linewidth=1)
        fig.subplots_adjust(wspace=0.4, hspace=0.6, left=0.15, right=0.85, top=0.9, bottom=0.1)

        return fig, axes

    # the function returns the selected equation
    def newEquation(self):
        return self.list_equation.currentItem().text()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

