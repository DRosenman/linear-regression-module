slope <- function(x,y,through_origin = FALSE) {
  if (through_origin == FALSE) {
    return_slope <- sum(((x-mean(x))*y))/sum((x-mean(x))^2)
    return_slope
  }
  else {
    return_slope <- sum((x*y))/sum((x^2))
    return_slope
  }
}

intercept <- function(x,y,through_origin = FALSE) {
  if (through_origin == FALSE) {
    return_intercept <- mean(y) - mean(x)*slope(x,y)
    return_intercept
  }
  else {
    return_intercept <- 0.0
    return_intercept
  }
}

slope_error <- function(x,y,through_origin = FALSE) {
  n <- length(x)
  if (through_origin == FALSE) {
    return_slope_error <- sqrt((1/(n-2))*(sum((y-slope(x,y)*x-intercept(x,y))^2))/sum((x-mean(x))^2))
    return_slope_error
  }
  else {
    return_slope_error <- sqrt(sum((y-slope(x,y,through_origin = TRUE)*x)^2)/((n-1)*sum(x^2)))
    return_slope_error
  }
}

intercept_error <- function(x,y,through_origin = FALSE) {
  if (through_origin == FALSE) {
    n <- length(x)
    return_intercept_error <- sqrt(((1/n)+mean(x)^2/sum((x-mean(x))^2))*sum((y-slope(x,y)*x-intercept(x,y))^2)/(n-2))
    return_intercept_error
  }
  else {
    return_intercept_error <- as.numeric(NA)
    return_intercept_error
  }
}

r <- function(x,y) {
  n <- length(x)
  return_r<- (n*sum(x*y)-sum(x)*sum(y))/(sqrt(n*sum(x^2) - sum(x)^2) * sqrt(n*sum(y^2) - sum(y)^2))
  return_r
}

r_squared <- function(x,y) {
  return_r_squared <- (r(x,y))^2
  return_r_squared
}
