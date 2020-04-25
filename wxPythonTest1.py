#!/usr/bin/env python
import wx
class ExampleFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
        panel = wx.Panel(self)
        self.quote = wx.StaticText(panel, label="Your quote: ", pos=(20, 30))
        clearButton = wx.Button(self, wx.ID_CLEAR, "Clear")
        self.Bind(wx.EVT_BUTTON, self.OnClear, clearButton)

        textField = wx.TextCtrl(self)
        self.Bind(wx.EVT_TEXT, self.OnChange, textField)
        self.Bind(wx.EVT_CHAR, self.OnKeyPress, textField)
     # A multiline TextCtrl - This is here to show how the events work in this program, don't pay too much attention to it
        self.logger = wx.TextCtrl(self, pos=(300,20), size=(200,300), style=wx.TE_MULTILINE | wx.TE_READONLY)


        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(panel)
        self.sizer.Add(textField)
        self.sizer.Add(clearButton)
        self.sizer.Add(self.logger)

        #Layout sizers
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)

        self.Show()

    def OnClear(self, event):
        self.logger.AppendText('On clear pressed')
    def OnChange(self, event):
        self.logger.AppendText('On change pressed')
    def OnKeyPress(self, event):
        self.logger.AppendText('On KeyPress pressed')


    def EvtRadioBox(self, event):
        self.logger.AppendText('EvtRadioBox: %d\n' % event.GetInt())
    def EvtComboBox(self, event):
        self.logger.AppendText('EvtComboBox: %s\n' % event.GetString())
    def OnClick(self,event):
        self.logger.AppendText(" Click on object with Id %d\n" %event.GetId())
    def EvtText(self, event):
        self.logger.AppendText('EvtText: %s\n' % event.GetString())
    def EvtChar(self, event):
        self.logger.AppendText('EvtChar: %d\n' % event.GetKeyCode())
        event.Skip()
    def EvtCheckBox(self, event):
        self.logger.AppendText('EvtCheckBox: %d\n' % event.Checked())
if __name__ == '__main__':
    app = wx.App(False)
    exampleFrame = ExampleFrame(None)
    app.MainLoop()
