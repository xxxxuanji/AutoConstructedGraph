import argparse


parser = argparse.ArgumentParser(description='modify_test')
parser.add_argument('--paper_file',type=str,required=True)
parser.add_argument('--output_file', type=str, required=True)
args=parser.parse_args()


fd = open(args.paper_file,"r",encoding="utf-8")
ft = open(args.output_file,"w",encoding="utf-8")
for line in fd.readlines():
        ft.write(line.replace('"',''))