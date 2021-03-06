# nodac/functions.py

#
# Copyright (c) 2012 Roberto D'Auria <evfirerob@gmail.com>
#
# This file is part of NODAC.
#
# NODAC is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# NODAC is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NODAC. If not, see <http://www.gnu.org/licenses/>.
#

"""Activation functions and their derivatives."""

from math import tanh

def tanh_der(x):

    return 1.0 - x ** 2

def linear(x):

    return x

def linear_der(x):
    return 1

FUNCTIONS = {'tanh': (tanh, tanh_der), 'linear': (linear, 1)}
