import subprocess

subprocess.Popen("rscript --verbose test_r.r > \
../results/test_r.rout 2> ../results/test_r_errFile.rout",\
 shell=True).wait()
