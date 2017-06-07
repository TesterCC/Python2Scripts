# coding: utf-8
# wxPython: 这是一个开源的Python接口的wxWindows http://wxpython.org.

import wx

app = wx.PySimpleApp()
frame = wx.Frame(None,-1,'')

frame.SetToolTip(wx.ToolTip('This is a frame'))
frame.SetCursor(wx.StockCursor(wx.CURSOR_MAGNIFIER))
frame.SetPosition(wx.Point(0,0))
frame.SetSize(wx.Size(800,600))
frame.SetTitle('GR QA Team Tools')

frame.Show()
app.MainLoop()