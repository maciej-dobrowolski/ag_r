library(tidyverse)

dane <- read_csv("sets_export.csv")
ceny    <- read_csv("ceny_promoklocki.csv")

dane <- dane %>%
  mutate(price_promoklocki = ceny$price_promoklocki[match(set_number, ceny$set_number)],
         .after = price_pln)
