import xlrd
import xlwt
def write_excel():
    data = xlrd.open_workbook(r"/usr/local/python_on/Watch_list_liunx/1.xlsx")
    data = xlrd.open_workbook(r" /usr/local/python_on/Watch_list_liunx/1.xlsx")
    table = data.sheet_by_index(0)
    nrows = table.nrows
    list_big = []

   # 获取表格到列表
    for i in range(nrows):
        xx = table.row_values(i)
        list_big.append(xx)
    #切割本周的值班名单
    try:
        for i in range(0,7):
            list_big.pop(0)
    except Exception as p:
        print("BUG一堆直接OK",p)
    #写入表格
    work_book = xlwt.Workbook()
    # dateFormat = xlwt.XFStyle()
    # dateFormat.num_format_str = 'yyyy/mm/dd'
    sheet1 = work_book.add_sheet('Sheet1')
    for j, a_day in enumerate(list_big):
        aa = a_day
        for i, element in enumerate(aa):  # 往Sheet1中写入“删除一个元素”后的一列
            sheet1.write(j, i, element)  # 第index行，第0列，写入lists元素
            # sheet1.write(j, 0, element,dateFormat)

    work_book.save("/usr/local/python_on/Watch_list_liunx/1.xlsx")  # 覆盖原来的excel文件，即完成删除操作
if __name__ == '__main__':
    write_excel()

