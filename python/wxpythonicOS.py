import wx
import os
import subprocess
class CustomWidget(wx.Panel):
    def __init__(self, parent, label):
        super(CustomWidget, self).__init__(parent)
        self.label = wx.StaticText(self, label=label)

        # Set the background color of the CustomWidget
        self.SetBackgroundColour(wx.Colour(255, 255, 0))  # Yellow background

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.label, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        self.SetSizer(sizer)

class MyFrame(wx.Frame): 
    def on_widget_click(self):
        file = self.label.GetLabel()
        subprocess.Popen(["python","/system/addons/panno.py",file])
        
    def __init__(self, *args, **kwargs):
        super(MyFrame, self).__init__(*args, **kwargs)
        self.SetTitle('Custom Widget Grid')
        self.SetSize((400, 300))
        self.Center()

        # Set the icon for the frame
        icon = wx.ArtProvider.GetIcon(wx.ART_QUESTION, wx.ART_OTHER, wx.Size(16, 16))
        self.SetIcon(icon)

        panel = wx.Panel(self)
        grid_sizer = wx.FlexGridSizer(rows=0, cols=3, vgap=10, hgap=10)

        # Directory containing the files
        directory_path = './'

        # List the files in the directory
        file_names = os.listdir(directory_path)

        for name in file_names:
            # Create the custom widget and use the file name as the label
            widget = CustomWidget(panel, label=name)
            grid_sizer.Add(widget, 1, wx.GROW | wx.ALL, 5)

        panel.SetSizer(grid_sizer)
        self.Layout()
        
        self.Bind(wx.EVT_LEFT_DOWN, self.on_widget_click)





if __name__ == '__main__':
    
    app = wx.App(False)
    frame = MyFrame(None)
    frame.Show()
    app.MainLoop()
