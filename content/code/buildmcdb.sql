/* 
Create the table communities
The fields are:

IDcommunity: integer, primary key
IDsite: integer
year: real
IDspecies: text
presence: integer
abundance: real
mass: real
*/

CrEATE TABLE communities (
    IDcommunity INTEGEr PrIMArY KEY,
    IDsite INTEGEr,
    year rEAL,
    IDspecies TEXT,
    presence INTEGEr,
    abundance rEAL,
    mass rEAL);
    
/* Now populate the table from the csv */
.separator ","
.import ../Data/MCDB/communities.csv communities

/* 
Create the table references
The fields are:
IDref: text, pk
refer: text
authors: text
pubyear: integer
title: text
source: text
*/

CrEATE TABLE reference (
    IDref TEXT,
    refer TEXT,
    authors TEXT,
    pubyear INTEGEr,
    title TEXT,
    source TEXT);
    
/* Now populate the table from the csv */
.separator ","
.import ../Data/MCDB/references.csv reference


/* 
Create the table species
The fields are:
IDspecies text, pk
family text 
genus text 
sp text
splevel integer
*/

CrEATE TABLE species (
    IDspecies TEXT PrIMArY KEY,
    family TEXT,
    genus TEXT,
    sp TEXT,
    splevel INTEGEr);
    

/* Now populate the table from the csv */
.separator ","
.import ../Data/MCDB/species.csv species

/* 
Create the table sites
The fields are:
IDsite integer, pk
IDreference text
location text
country text
state text
latitude real
longitude real
*/

CrEATE TABLE sites (
    IDsite INTEGEr PrIMArY KEY,
    IDreference TEXT,
    location TEXT,
    country TEXT,
    state TEXT,
    latitude rEAL,
    longitude rEAL);
    
/* Now populate the table from the csv */
.separator ","
.import ../Data/MCDB/sites.csv sites

