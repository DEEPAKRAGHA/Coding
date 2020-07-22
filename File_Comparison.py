import difflib
import PySimpleGUI as pii

layout=[[pii.Text("        TEXT FILE COMPARE          ")],
        [pii.Text('*'*100)],
        [pii.Text('Enter Original File')],
        [pii.InputText(),pii.FileBrowse()],
        [pii.Text("Enter Modified file ")],
        [pii.InputText(),pii.FileBrowse()],
        [pii.Text("Enter Destination Folder")],
        [pii.InputText(),pii.FolderBrowse()],
        [pii.Button("ENTER")]]

window=pii.Window('Let be successful').Layout(layout)

button,values=window.Read()



if button == "ENTER" :
    window.Close()
    first_file=values[0]
    second_file=values[1]

    first_file_line=open(first_file).readlines()
    second_file_line=open(second_file).readlines()

    difference=difflib.HtmlDiff().make_file(first_file_line,second_file_line,first_file,second_file)

    filename_output= values[2] + "/Compare.html"
    print(filename_output)
    difference_report=open(filename_output,'w')
    difference_report.write(difference)
    difference_report.close()