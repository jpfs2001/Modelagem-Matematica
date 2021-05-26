import xlrd

def lerPlanilha(diretorio, comeca, tamanho):
    # abrir planilha
    wb = xlrd.open_workbook(diretorio)
    # primeira página
    sheet = wb.sheet_by_index(0)
    
    arr = []

    for i in range(comeca[1], comeca[1]+tamanho):
        arj = []
        for j in range(comeca[0], comeca[0]+tamanho):
            arj.append(sheet.cell_value(i-1, j-1))
        arr.append(arj)
    return arr