rm(list = ls())

Students <- read.csv("../data/students_all.csv") 

Students$Name <- paste(Students$X1st.Name, Students$Surname, sep=" ")

MSc_rep <- sample(Students$Name[which(Students$Program.Name == "Computational Methods in Ecology and Evolution (MSc 1YFT)")],1) 

Mres_rep <- sample(Students$Name[which(Students$Program.Name == "Computational Methods in Ecology and Evolution (Mres 1YFT)")],1)

print(paste("MSc rep is ", MSc_rep, ", WOO-HOO!", sep = ""))
print(paste("Mres rep is ", Mres_rep, ", WOO-HOO!", sep = ""))
