from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfparser import PDFDocument, PDFParser
# 访问显示对象
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator


pf = open("D:/project/python/6-25/bbf_learn_python.pdf",'rb')

#创建与文档关联的解释器
parser = PDFParser(pf)

#pdf文档对象
doc = PDFDocument()

#链接解释器和文档对象
parser.set_document(doc)
doc.set_parser(parser)

# 文档初始化
doc.initialize("")

# pdf 资源管理器
resource = PDFResourceManager()

# 参数分析器
laparams = LAParams()


#pdf聚合器
device = PDFPageAggregator(resource, laparams=laparams)
#pdf解释器
interpreter = PDFPageInterpreter(resource, device)


# 使用文档对象得到页面的集合
for page in doc.get_pages():
    # 使用解析器来读取页面
    interpreter.process_page(page)
    # 聚合器获得布局内容
    layout = device.get_result()

    for out in layout:
        if hasattr(out,"get_text"):
            print(out.get_text())