import subprocess
import sys
import csv

#input_file = sys.argv[1]
#output_file = sys.argv[2]

bcftools = "/hpc/packages/minerva-centos7/bcftools/1.9/bin/bcftools"
sample_names = []

try:
    def __biome_vcf_splitter__(input_file, output_file):
        with open(input_file) as csvfile:
            for line in csvfile:
                sample_names.append(line.strip('\n'))

            # This line will remove the square brackets from the list
            input = str(sample_names)[1:-1]

            cmd = bcftools, "view", "-c1", "-Oz", "-s", input, "-o", output_file, input_file
            process = subprocess.Popen(cmd)
            process.communicate()










except Exception as e:
    print("The error has occured while running the biome vcf splitter. The error is :  {}".format(e))