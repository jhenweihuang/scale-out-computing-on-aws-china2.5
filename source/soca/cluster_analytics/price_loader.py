from __future__ import division

import xlrd

# There is no pricing api in ZHY region, need to load ec2 price from an xlsx file
def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)
    price_dict = {}

    if table.nrows >0:
        for rowNum in range(table.nrows):
            rowValueStr = table.row_values(rowNum)
            for colNum in range(table.ncols):
                # if rowNum > 0 and colNum == 0:
                if colNum == 0:
                    # use col0 as key of the dict
                    price_dict[rowValueStr[0]] = []
                    # print(rowValueStr[0])
                else:
                    # load col1,col2 into a list as value of the dict
                    price_dict[rowValueStr[0]].append(rowValueStr[colNum])
                    # print(rowValueStr[colNum])
        # print(price_dict)
    else:
        print("Error: empty price file...")
    return price_dict



if __name__ == '__main__':
    excelFile = 'price.xlsx'
    read_xlrd(excelFile)
