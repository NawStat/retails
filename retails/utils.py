
def ratios_per_invoice(collection):
    """
    grouping ratios for each invoice
    """
    dict_ratio = {}
    for row in collection:
        if row.InvoiceNo not in dict_ratio:
            dict_ratio[row.InvoiceNo] = [row.ratio]
        else:
            dict_ratio[row.InvoiceNo].append(row.ratio)
    ratio_list = [(i, dict_ratio[i])for i in dict_ratio]
    return ratio_list

def data_per_invoice(collection):
    """
    Group all transactions by invoice
    """
    data = {}
    for row in collection:
        if row.InvoiceNo not in data:
            data[row.InvoiceNo] = [{'Country': row.Country,
                                    'CustomerID': row.CustomerID,
                                    'Description': row.Description,
                                    'InvoiceDate': row.InvoiceDate,
                                    'InvoiceNo': row.InvoiceNo,
                                    'Quantity': row.Quantity,
                                    'StockCode': row.StockCode,
                                    'StockCode': row.StockCode,
                                    'UnitPrice': row.UnitPrice,
                                    }]
            # data[row.InvoiceNo] = [(row.Country, row.CustomerID,row.Description, row.InvoiceDate,
            #                         row.InvoiceNo,row.Quantity, row.StockCode,row.UnitPrice )]
        else:
            data[row.InvoiceNo].append((row.Country, row.CustomerID,row.Description, row.InvoiceDate,
                                    row.InvoiceNo,row.Quantity, row.StockCode,row.UnitPrice ))
    ratio_list = [(i, data[i])for i in data]
    return ratio_list
