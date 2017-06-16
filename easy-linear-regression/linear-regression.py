import numpy as  np
import pandas as pd
import scipy.stats as stats
from IPython.display import display
import matplotlib.pyplot as plt








class dataset(object):
    def __init__(self, x, y=[]):
        if type(x[0]) == tuple:
            x, y = zip(*x)

            self.x = np.array(x)
            self.y = np.array(y)

        elif type(x[0]) == list:
            temp = np.array(x)
            self.x = temp[:, 0]
            self.y = temp[:, 1]

        else:
            self.x = np.array(x)
            self.y = np.array(y)

        self.xlabel = 'x'
        self.xunits = ''
        self.ylabel = 'y'
        self.yunits = ''
        self.n = len(x)

        self.measurement_label = 'Measurement'

        self.__slope = slope(self.x, self.y)
        self.__slope00 = slope(self.x, self.y, through_origin=True)

        self.__slope_error = slope_error(self.x, self.y)
        self.__slope_error00 = slope_error(self.x, self.y, through_origin=True)

        self.__intercept = intercept(self.x, self.y)
        self.__intercept00 = intercept(self.x, self.y, through_origin=True)

        self.__intercept_error = intercept_error(self.x, self.y)
        self.__intercept_error00 = intercept_error(self.x, self.y, through_origin=True)

        self.__r_squared = r_squared(self.x, self.y)
        self.__r_squared00 = r_squared(self.x, self.y, through_origin=True)

        self.__sigfigs = None

    def measurement_labels(self):
        ind = []
        for i in np.arange(len(self.x)):
            ind.append(self.measurement_label + ' ' + str((i + 1)))
        return ind

    def set_xlabel(self, xlabel):
        self.xlabel = xlabel

    def set_xunits(self, xunits):
        self.xunits = xunits

    def set_ylabel(self, ylabel):
        self.ylabel = ylabel

    def set_yunits(self, yunits):
        self.yunits = yunits

    def get_variable_labels(self):
        if self.xunits == '':
            return (self.xlabel, self.ylabel)
        else:
            xlabel_with_units = self.xlabel + ' (' + self.xunits + ')'
            ylabel_with_units = self.ylabel + ' (' + self.yunits + ')'
            return xlabel_with_units, ylabel_with_units

    def data_frame(self):
        xlabel = self.get_variable_labels()[0]
        ylabel = self.get_variable_labels()[1]
        return pd.DataFrame({xlabel: self.x, ylabel: self.y},
                            columns=[xlabel,ylabel],index=self.measurement_labels())

    @property
    def slope(self):
        return self.__slope

    @property
    def slope00(self):
        return self.__slope00

    @property
    def slope_error(self):
        return self.__slope_error

    @property
    def slope_error00(self):
        return self.__slope_error00

    @property
    def intercept(self):
        return self.__intercept

    @property
    def intercept00(self):
        return self.intercept00

    @property
    def intercept_error(self):
        return self.__intercept_error

    @property
    def intercept_error00(self):
        return self.__intercept_error00

    @property
    def sigfigs(self):
        return self.__sigfigs

    @sigfigs.setter
    def sigfigs(self, sigfigs):
        self.__sigfigs = sigfigs

    @property
    def r_squared(self):
        return self.__r_squared

    @property
    def r_squared00(self):
        return self.__r_squared00

    def __str__(self):
        bfl_string = 'LINEAR LEAST-SQUARES REGRESSION ANALYSIS\n\nBEST FIT LINE:\n'
        slope_string = 'slope = ' + str(self.slope) + '\n'
        intercept_string = 'intercept = ' + str(self.intercept) + '\n'
        slope_error_string = 'std. error, slope = ' + str(self.slope_error) + '\n'
        intercept_error_string = 'std. error, intercept = ' + str(self.intercept_error) + '\n'
        r_squared_string = 'r-squared = ' + str(self.r_squared) + '\n'
        number_of_data_points = 'number of data points = ' + str(self.n)

        bfl_data = (bfl_string + slope_string + intercept_string +
                    slope_error_string + intercept_error_string +
                    r_squared_string + number_of_data_points) + '\n\n'

        bfl_string00 = 'BEST FIT LINE THROUGH THE ORIGIN, (0,0):\n'
        slope_string00 = 'slope = ' + str(self.slope00) + '\n'
        intercept_string00 = 'intercept = ' + str(0.0) + '\n'
        slope_error_string00 = 'std. error, slope = ' + str(self.slope_error00) + '\n'
        intercept_error_string00 = 'std. error, intercept = N//A \n'
        r_squared_string00 = 'r-squared = ' + str(self.r_squared00) + '\n'

        bfl_data00 = (bfl_string00 + slope_string00 + intercept_string00
                     + slope_error_string00 + intercept_error_string00
                      + r_squared_string00 + number_of_data_points)

        return bfl_data + bfl_data00

    def results(self, with_through_origin=False, through_origin=False):
        display(results_dataframe(self.x, self.y, with_through_origin, through_origin))

    def display_results(self, with_through_origin=False, through_origin=False):
        display(self.results(with_through_origin, through_origin))

    def graph(self, title='', through_origin=False, text_color='darkred'):

        if self.x.min() < 0:
            x_min = self.x.min() * .98
        else:
            x_min = 0.0
        x_max = self.x.max() * 1.02
        x = np.linspace(x_min, x_max, 100)

        if through_origin == False:
            m = self.slope
            c = self.intercept
            name = 'Best Fit Line'
            equation = self.ylabel + " = " + str(round(m, 3)) + self.xlabel + ' + ' + str(
                round(c, 3))
        else:
            m = self.slope00
            c = 0.0
            name = 'Best Fit Line Through Origin'
            equation = self.ylabel + " = " + str(round(m, 3))  + self.xlabel

        xlabel, ylabel = self.get_variable_labels()

        plt.grid()

        axisfont = axis_font(text_color)
        titlefont = title_font(text_color)
        plt.xlim(x_min, 1.05 * x_max)
        plt.xlabel(xlabel, fontdict=axisfont)
        plt.ylabel(ylabel, fontdict=axisfont)

        plt.scatter(self.x, self.y, label='Measurement', color='darkred')
        plt.plot(x, x * m + c, label=name, )
        plt.title(title, fontdict=titlefont)
        ax = plt.gca()
        plt.text(0.5, 0.75, equation, color='darkred', ha='center', va='center', transform=ax.transAxes)
        plt.legend();





###INDIVIDUAL FUNCTIONS

def slope(x, y, through_origin=False):
    '''

    :param x: array_like
    :param y: array_like
    :param through_origin: defaults to False.
    :return: Slope of best fit line. If through_origin is set to True, the
             slope will be of the best fit line crossing the point (0,0).
    '''
    x = np.array(x)
    y = np.array(y)
    if through_origin == False:
        x = np.array(x)
        y = np.array(y)
        return ((x - x.mean()) * y).sum() / ((x - x.mean()) ** 2).sum()
    else:
        return ((x * y).sum()) / (x ** 2).sum()


def intercept(x, y, through_origin=False):
    '''

    :param x: array_like
    :param y: array_like
    :param through_origin: defaults to False
    :return: y-intercept of best fit line.

            If through_origin is set to True, returns 0.0 (intercept of best-fit line through (0,0)).
    '''
    if through_origin == False:
        x = np.array(x)
        y = np.array(y)
        return y.mean() - slope(x, y) * x.mean()
    else:
        return 0.0


def slope_error(x, y, through_origin=False):
    '''

    :param x: array_list
    :param y: array_list
    :param through_origin: defaults to False
    :return: std. error of the slope of the best fit line.

             If through_origin is set to True, returns the std. error of
             the slope of slope of the best fit line crossing the origin.

    '''
    x = np.array(x)
    y = np.array(y)
    n = len(x)

    if through_origin == False:
        residuals_squared = (y - slope(x, y) * x - intercept(x, y)) ** 2
        residuals_squared_sum = residuals_squared.sum()
        D = ((x - x.mean()) ** 2).sum()
        return np.sqrt((1 / (n - 2)) * residuals_squared_sum / D)
    else:
        residuals_squared = (y - slope(x, y, True) * x) ** 2
        return np.sqrt(residuals_squared.sum() / ((n - 1) * (x ** 2).sum()))


def intercept_error(x, y, through_origin=False):
    '''

    :param x: array_like
    :param y: array_like
    :param through_origin: defaults to False
    :return: The std. error of the y intercept.

             If through_origin is set to True, returns 'NaN', since the
             best fit line through the origin has no std. error for its intercept (0).

    '''
    if through_origin == False:
        x = np.array(x)
        y = np.array(y)
        n = len(x)
        D = ((x - x.mean()) ** 2).sum()
        residuals_squared = (y - slope(x, y) * x - intercept(x, y)) ** 2
        return np.sqrt(((1 / n) + (x.mean() ** 2) / D) * residuals_squared.sum() / (n - 2))
    else:
        return 'NaN'

def results(x,y,through_origin = False):
    return (slope(x,y,through_origin),intercept(x,y,through_origin),
            slope_error(x,y,through_origin),intercept_error(x,y,through_origin),
            r_squared(x,y,through_origin))

def results_dataframe(x, y, with_through_origin=False, through_origin=False):
    '''

    :param x: array_like
    :param y: array_like
    :param with_through_origin: defaults to False
    :param through_origin: defaults to False
    :return: default: slope, intercept,
                      std. error of slope, std. error of intercept,
                       and r-squared value
             if through_origin is set to True: returns the same values as above,
                                               but for the best fit line through the origin.
             if with_through_origin is set to True: returns all of the regression coefficients mentions above
                                                    for both the regular best fit line and the best fit line through
                                                    the origin.

    '''
    x = np.array(x)
    y = np.array(y)

    if with_through_origin == False:
        df = pd.DataFrame([[slope(x, y, through_origin), intercept(x, y, through_origin),
                            slope_error(x, y, through_origin), intercept_error(x, y, through_origin),
                            r_squared(x, y, through_origin)]],
                          columns=['Slope', 'Intercept', 'Std. Error, Slope', 'Std Error, Intercept', 'r-squared'],
                          index=[''])


    else:
        df = pd.DataFrame(
            [[slope(x, y), intercept(x, y), slope_error(x, y), intercept_error(x, y), correlation_coefficient(x, y)],
             [slope(x, y, True), intercept(x, y, True), slope_error(x, y, True), 'NA',
              r_squared(x, y, True)]],
            columns=['Slope', 'Intercept', 'Std. Error, Slope', 'Std Error, Intercept', 'r-squared'],
            index=['Regular Linear Regression', 'Regression Line Through (0,0)'])
    return df


def display_results(x, y, with_through_origin=False, through_origin=False):
    '''
    :param x: array_like
    :param y: array_like
    :param with_through_origin: defaults to False
    :param through_origin: defaults to False
    :displays: default: slope, intercept,
                      std. error of slope, std. error of intercept,
                       and r-squared value
             if through_origin is set to True:  the same values as above,
                                               but for the best fit line through the origin.
             if with_through_origin is set to True:  all of the regression coefficients mentions above
                                                    for both the regular best fit line and the best fit line through
                                                    the origin.
    '''
    display(results_dataframe(x, y, with_through_origin, through_origin))


def r(x, y, through_origin=False):
    '''
    :param x: array_like
    :param y: array_like
    :param through_origin: defaults to False
    :return: correlation coefficient  (r)
            if through_origin is set to False returns r for best-fit line through the origin
    '''
    return correlation_coefficient(x, y, through_origin)


def r_squared(x, y, through_origin=False):
    '''
        :param x: array_like
        :param y: array_like
        :param through_origin: defaults to False
        :return: the coefficient of determination, r-squared.
                if through_origin is set to False returns r-squared for best-fit line through the origin
        '''
    return correlation_coefficient(x, y, through_origin)
    return (correlation_coefficient(x, y, through_origin)) ** 2


def p_value(x, y, through_origin=False):
    '''
    :param x: array_like
    :param y: array_like
    :param through_origin: defaults to False
    :return: two-sided p-value for hypothesis that slope = 0.

             If through_origin is set to True, two-sided p-value for hypothesis bfl through origin.
             (if only difference from default is that number of degrees of freedom is 1 instead of 2.
    '''
    x = np.array(x)
    y = np.array(y)
    if through_origin == True:
        k = 1
    else:
        k = 2
    df = len(x) - k
    m = slope(x, y, through_origin)
    error = slope_error(x, y, through_origin)
    t = m / error
    return stats.t.sf(np.abs(t), df) * 2


def correlation_coefficient(x, y, through_origin=False):
    '''
        :param x: array_like
        :param y: array_like
        :param through_origin: defaults to False
        :return: correlation coefficient  (r)
                if through_origin is set to False returns r for best-fit line through the origin
        '''
    x = np.array(x)
    y = np.array(y)
    if through_origin == False:
        n = len(x)
        xy = x * y
        return (n * (xy.sum()) - (x.sum()) * (y.sum())) / (
            (((n * (x ** 2).sum()) - (x.sum()) ** 2) ** .5) * ((n * ((y ** 2).sum()) - (y.sum()) ** 2) ** .5))
    else:
        return np.sqrt(1.0 - (((y - x * slope(x, y, through_origin)) ** 2).sum()) / ((y ** 2).sum()))


def axis_font(color='darkred'):
    '''
    :param color: defaults to darkred
    :return: serif style font with 'color' = color, ''weight' = 'bold', 'size' = 12
    '''
    return {'family': 'serif', 'color': color, 'weight': 'bold', 'size': 12,
            }


def title_font(color='darkred'):
    '''
        :param color: defaults to darkred
        :return: serif style font with 'color' = color, ''weight' = 'bold', 'size' = 16
        '''
    return {'family': 'serif', 'color': color, 'weight': 'bold', 'size': 16,
            }


