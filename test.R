library(DT)

df <- readRDS("C:/Users/lijia/Downloads/byState2a.RDS")

df1 <- readRDS("C:/Users/lijia/Downloads/byState2.RDS")


write.csv(df, "C:/Users/lijia/Downloads/df.csv")


datatable(df1)

