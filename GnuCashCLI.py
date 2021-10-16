import argparse
import GnuCashConverter

# Parse input arguments
parser = argparse.ArgumentParser(description='Convert CSV files for GnuCash import.')
parser.add_argument('type', choices=['rabobank', 'rabobankold', 'ing', 'triodos'])
parser.add_argument('inputFile', type=str, nargs='+',
                    help='the csv file to convert')

args = parser.parse_args()

inputFile = vars(args)['inputFile'][0]
print(vars(args)['inputFile'])
typeOfFile = vars(args)['type']
# Append -conv to filename
inputFileSplit = inputFile.split(".")
inputFileSplit[len(inputFileSplit)-2] = inputFileSplit[len(inputFileSplit)-2] + '-conv'
outputFile = ".".join(inputFileSplit)
#print(outputFile)

converter = GnuCashConverter.GnuCashConverter()
converter.convert(
            inputFile,
            outputFile,
            typeOfFile)
