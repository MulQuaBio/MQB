plant_control_data <- read.csv("~/Documents/FIU/research/JapBeetle_Temp_Herbivory/Data/No_Choice_Assays/plant_control_data.csv")

box.elder <- subset(plant_control_data, Plant=='Box Elder')
be.mod <- lm(Change~PreMass, box.elder)

red.maple <- subset(plant_control_data, Plant=='red Maple')
rm.mod <- lm(Change~PreMass, red.maple[-15,]) # remove observation where petiole was not in water

sweetgum <- subset(plant_control_data, Plant=='Sweetgum')
sg.mod <- lm(Change~PreMass, sweetgum[-8,]) # remove observation where petiole was not in water

syc <- subset(plant_control_data, Plant=='Sycamore')
syc.mod <- lm(Change~PreMass, syc)

rosa <- subset(plant_control_data, Plant=='Multiflora rose')
rosa.mod <- lm(Change~PreMass, rosa)

b.berry <- subset(plant_control_data, Plant=='Blackberry')
bberry.mod <- lm(Change~PreMass, b.berry)

w.berry <- subset(plant_control_data, Plant=='Wineberry')
wberry.mod <- lm(Change~PreMass, w.berry)

vib <- subset(plant_control_data, Plant=='V. prunifolium')
vib.mod <- lm(Change~PreMass, vib)

vit <- subset(plant_control_data, Plant=='Frost Grape')
vit.mod <- lm(Change~PreMass, vit)

plot(Change~PreMass, vit)