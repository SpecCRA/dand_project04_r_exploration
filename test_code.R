# Things to run first
install.packages("ggplot2", dependencies = T) 
install.packages("knitr", dependencies = T)
install.packages("dplyr", dependencies = T)
setwd("~/dand_files/project04_files/")

# Libraries to load
library(ggplot2)
library(dplyr)
library(knitr)
library(gridExtra)

#csv file to load
sc <- read.csv("starcraft.csv")

