# -*- encoding: utf-8 -*-

import unittest

import sys
import sympy as sy


import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication

from euler import Euler, MainWindow

class TestEuler(unittest.TestCase):

    def setUp(self):
        self.euler = Euler("y'=y*cos(x),\ny(0)=1\n\n")

    def test_getCoord(self):
        self.assertEqual((self.euler.getCoord()), ([0.0, 1.0, 1.0, 2.4]), "Invalid initial or final conditions.")

    def test_getExactfunc(self):
        self.assertEqual((self.euler.getExactfunc()), (sy.sympify("exp(sin(x))")), "Invalid equation")

    def test_getExactfunc(self):
        self.assertEqual((self.euler.getEquation()), (sy.sympify("y*cos(x)")), "Invalid exact function")

    def test_getLstX(self):
        self.assertEqual(self.euler.getLstX(),([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]), "Invalid argument x")

    def test_getLstY(self):
        self.assertEqual(self.euler.getSolution(), ([1.1, 1.209, 1.328, 1.455, 1.589, 1.728, 1.871, 2.014, 2.154, 2.288, 2.412]), "Invalid Euler's method solution")

    def test_getLstDiff(self):
        self.assertEqual(self.euler.getLstDiff(), ([-0.1, -0.104, -0.108, -0.111, -0.113, -0.113, -0.112, -0.11, -0.105, -0.1, -0.092]), "Invalid difference")

    def test_getLstExac(self):
        self.assertEqual(self.euler.getLstExac(), ([1.0, 1.105, 1.22, 1.344, 1.476, 1.615, 1.759, 1.904, 2.049, 2.189, 2.32]), "Invalid exact solution")


class TestMainWindow(unittest.TestCase):

    def setUp(self):
        self.app = QApplication(sys.argv)
        self.mainwindow = MainWindow()

    @unittest.expectedFailure
    def test_plot_single_empty_graph(self):

        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10, 7), dpi=85, facecolor='white', frameon=True, edgecolor='black', linewidth=1)
        fig.subplots_adjust(wspace=0.4, hspace=0.6, left=0.15, right=0.85, top=0.9, bottom=0.1)
        self.assertEqual(self.mainwindow.plot_single_empty_graph(), (fig, axes), "Different axis code.")

    def test_newEquation(self):
        self.assertEqual(self.mainwindow.newEquation(), "y'=y*cos(x),\ny(0)=1\n\n", "Incorrect equation")

    def test_addEquation(self):
        list_equation = ["y'=y*cos(x),\ny(0)=1\n\n", "y'=x*(y**2),\ny(0)=1\n\n", "y'=2*exp(x**2)-y/x,\ny(1)=e"]
        self.assertEqual(self.mainwindow.list_equation.addItems(list_equation), None, "Error add equation")

    def test_graph(self):
        method_el = [1.1, 1.209, 1.328, 1.455, 1.589, 1.728, 1.871, 2.014, 2.154, 2.288, 2.412]
        exact = [1.0, 1.105, 1.22, 1.344, 1.476, 1.615, 1.759, 1.904, 2.049, 2.189, 2.32]
        diff = [-0.1, -0.104, -0.108, -0.111, -0.113, -0.113, -0.112, -0.11, -0.105, -0.1, -0.092]

        self.assertEqual(self.mainwindow.txt_solution.setText(" Exact solution: " + str(exact)
                                  + "\n\n Euler's method: " + str(method_el)
                                  + "\n\n Difference: " + str(diff)), None, "Error add list")


if __name__ == '__main__':
    unittest.main()