def slope(x, y, through_origin = False):
    """

    :param x: list, array, or tuple of x-coordinates
    :param y: list, array, or tuple of y-coordinates
    :param through_origin: default is False. If True, returns slope of best fit line through the origin (0,0)
    :return: slope of the best fit line
    """
    x = np.array(x)
    y = np.array(y)
    if through_origin == False:
        x = np.array(x)
        y = np.array(y)
        return ((x - x.mean()) * y).sum() / ((x - x.mean()) ** 2).sum()
    else:
        return ((x * y).sum()) / (x ** 2).sum()


def intercept(x, y, through_origin=False):
    """

    :param x: list, array, or tuple of x-coordinates
    :param y: list, array, or tuple of y-coordinates
    :param through_origin:  default: False. If True, returns 0.0
    :return: Intercept of the best fit line.
    """
    if through_origin == False:
        x = np.array(x)
        y = np.array(y)
        return y.mean() - slope(x, y) * x.mean()
    else:
        return 0.0


def slope_error(x, y, through_origin=False):
    """

    :param x: list, array, or tuple of x-coordinates
    :param y: list, array, or tuple of y-coordinates
    :param through_origin: default: False. If True, functions returns standard error of the slope
                                           of the best fit line through the origin
    :return: std. error of the slope of the best fit line
    """

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

    :param x: list, array, or tuple of x-coordinates
    :param y: list, array, or tuple of y-coordinates
    :param through_origin: default is False; if True, returns 'NaN'
    :return: std. error of the intercept of the best fit line
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


def results(x, y, through_origin=False):
    '''

    :param x: list, array, or tuple of x-coordinates
    :param y: list, array, or tuple of y-coordinates
    :param through_origin: default False; If True, results are for best fit line through the origin (0,0)
    :return: variables for the slope, intercept, slope_error, intercept error, and correlation coefficient of the best fit line.
    '''
    return (slope(x, y, through_origin), intercept(x, y, through_origin),
            slope_error(x, y, through_origin), intercept_error(x, y, through_origin),
            correlation_coefficient(x, y,through_origin))


def print_results(x, y, through_origin=False):
    '''

    :param x: list, array, or tuple of x-coordinates
    :param y: list, array, or tuple of y-coordinates
    :param through_origin: default False; If True, results are for best fit line through the origin (0,0)
    :return: None
    :prints: the slope, intercept, slope_error, intercept error, and correlation coefficient of the best fit line.
    '''
    if through_origin == False:
        print(pd.DataFrame([[slope(x, y), intercept(x, y), slope_error(x, y)]],
                           columns=['Slope', 'Intercept', 'Std. Error, Slope'],
                           index=['']))
        print("")
        print(pd.DataFrame([[intercept_error(x, y), correlation_coefficient(x, y)]],
                           columns=['Std. Error, Intercept', 'r'],
                           index=['']))
    if through_origin == True:
        print(pd.DataFrame([[slope(x, y, through_origin=True), intercept(x, y, through_origin=True),
                             slope_error(x, y, through_origin=True)]],
                           columns=['Slope', 'Intercept', 'Std. Error, Slope'],
                           index=['']))
        print("")

        print(pd.DataFrame([[correlation_coefficient(x, y, through_origin)]], columns=['r'], index=['']))


def correlation_coefficient(x, y, through_origin = False):
    '''
    :param x: list, array, or tuple of x-coordinates
    :param y: list, array, or tuple of y-coordinates
    :return: correlation coefficient, r
    '''
    x = np.array(x)
    y = np.array(y)
    if through_origin == False:

        n = len(x)
        xy = x * y

        return (n * (xy.sum()) - (x.sum()) * (y.sum())) / (
        (((n * (x ** 2).sum()) - (x.sum()) ** 2) ** .5) * ((n * ((y ** 2).sum()) - (y.sum()) ** 2) ** .5))
    else:
        return np.sqrt(1.0-((((y-slope(x,y,through_origin)*x)**2).sum())/((y**2).sum())))



def r(x, y, through_origin = False):
    '''
      :param x: list, array, or tuple of x-coordinates
      :param y: list, array, or tuple of y-coordinates
      :param through_origin: Default fault. If true, regression line forced to go through (0,0)
      :return: correlation coefficient, r
      '''
    return correlation_coefficient(x, y,through_origin)


def r_squared(x, y, through_origin = False):
    '''
      :param x: list, array, or tuple of x-coordinates
      :param y: list, array, or tuple of y-coordinates
      :param through_origin: default is False. If True, best fit line forced through origin (0,0)
      :return: correlation of determination, r^2
      '''
    return (correlation_coefficient(x, y,through_origin)) ** 2


import scipy.stats as stats


def p_value(x, y, through_origin=False):
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
