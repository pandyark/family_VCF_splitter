import subprocess
import sys

bcftools="/Users/bowcock_lab/Desktop/Analysis_Softwares/bcftools-1.10.2/bcftools"


def trio_vcf_splitter(input_file):
    try:

        cmd = bcftools , "query" , "-l" , input_file
        process1 = subprocess.Popen(cmd,stdout=subprocess.PIPE)
        samples =[]

        for line in process1.stdout.readlines():
            samples.append(line.decode("utf-8").strip('\n'))


        unique_sample_identifier = set([])

        for item in samples:
            identifier = item.split("-")[0]
            if identifier not in unique_sample_identifier:
                unique_sample_identifier.add(identifier)

        patient_trios = []

        for item in unique_sample_identifier:
            sample_arr = []
            for val in samples:
                if item in val:
                    sample_arr.append(val)
            patient_trios.append(sample_arr)

        #print(patient_trios)

        for item in patient_trios:
            input = ','.join(item)
            dir = input_file.rsplit('/', 1)
            out_path = dir[0]
            output_file = out_path + "/" + item[0].split("-")[0] + ".vcf.gz"
            cmd = bcftools,"view", "-c1", "-Oz", "-s", input, "-o",output_file, input_file
            process = subprocess.Popen(cmd)
            process.communicate()

    except Exception as e:
        print("An error has occurred while running the method trio vcf splitter. The error message is :  {}".format(e))