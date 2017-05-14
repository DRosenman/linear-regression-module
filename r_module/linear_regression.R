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

r <- function(x,y,through_origin = FALSE) {
    if (through_origin == FALSE){
        n <- length(x)
        return_r<- (n*sum(x*y)-sum(x)*sum(y))/(sqrt(n*sum(x^2) - sum(x)^2) * sqrt(n*sum(y^2) - sum(y)^2))
        return_r      
    }
    else{
        return_r <- sqrt(1 - sum((y-slope(x,y,through_origin)*x)^2)/sum(y^2))
        return_r
    }
  
}

r_squared <- function(x,y,through_origin= FALSE) {
  return_r_squared <- (r(x,y,through_origin))^2
  return_r_squared
}

summary_stats <- function(x,y,through_origin = FALSE) {
  return_values <- list(slope = slope(x,y,through_origin),intercept = intercept(x,y,through_origin),
                        slope_error = slope_error(x,y,through_origin),
                              intercept_error = intercept_error(x,y,through_origin),r = r(x,y,through_origin))
  return_values
}

summary_stats_df <- function(x,y,both = FALSE,through_origin = FALSE) {
  if(both == TRUE) {
    row_names = c('Summary Stats: Regular Linear Regression', 'Summary Stats: Regression Line Through (0,0)')
    df <- data.frame(slope = c(slope(x,y,through_origin=FALSE),slope(x,y,through_origin = TRUE)),
                     intercept = c(intercept(x,y,through_origin = FALSE), 0.0),
                     slope_error = c(slope_error(x,y,through_origin= FALSE), slope_error(x,y,through_origin = TRUE)),
                     intercept_error = c(intercept_error(x,y,through_origin = FALSE),intercept_error(x,y,through_origin = TRUE)),
                     r = c(r(x,y),r(x,y,through_origin = TRUE)), row.names = row_names)
  }
  
  else {
    if(through_origin == FALSE) {
      row_names = c('Summary Stats: Linear Regression')
    }
    else {
      row_names = c('Summary Stats: Regression Line Through (0,0)')
    }
      
      df <- data.frame(slope = c(slope(x,y,through_origin)),
                       intercept = c(intercept(x,y,through_origin)),
                       slope_error = c(slope_error(x,y,through_origin)),
                       intercept_error = c(intercept_error(x,y,through_origin)),
                       r = c(r(x,y)), row.names = row_names)
      
  }
  df
  }
    
