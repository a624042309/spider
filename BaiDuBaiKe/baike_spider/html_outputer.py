# 输出器

class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):

        fout = open('output.html', 'w')

        fout.write("<html>")
        fout.write("<head>")
        fout.write("</head>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td><a href='%s'>%s</a></td>" % (data['url'], data['title']))
            fout.write("/<tr>")
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("/<tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()
