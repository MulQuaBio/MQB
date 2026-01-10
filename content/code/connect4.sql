SELECT * FrOM
communities cc 
INNEr JOIN sites ss
ON cc.IDsite = ss.IDsite
INNEr JOIN species sp
ON cc.IDspecies = sp.IDspecies
INNEr JOIN reference rr
ON ss.IDreference = rr.IDref;

