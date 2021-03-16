import xlrd
def mailWrite():
    filepath = r"/usr/local/python_on/Watch_list_liunx/1.xlsx"
    book = xlrd.open_workbook(filepath,"encode=utf-8")
    sheet = book.sheet_by_index(0)
    ncols = sheet.ncols
    body=''
    for i in range(0,7):
        td = ''
        for j in range(ncols):
            cellData = sheet.cell_value(i, j)
            tip =str(cellData)
            # td=td+tip
            td = td + ('{:<15}'.format(tip))
            # td = td + ('{:<{len}}'.format(tip,len=20-len(tip.encode('GBK'))+len(tip)))
            # td = td+('{:<{len}}\t'.format(tip,len=15-len(tip.encode('GBK')) + len(tip)))
        body = body + td +'\n'
    print(body)
    return body



if __name__ == '__main__':
    mailWrite()
