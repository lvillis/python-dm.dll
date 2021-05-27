import ctypes
import os

from win32com.client import Dispatch


class Dm:
    _path = os.getcwd()
    _DmReg = ctypes.WinDLL(f"{_path}\DmReg.dll")
    _DmReg.SetDllPathW(f"{_path}\dm.dll", 0)
    _dm = Dispatch('dm.dmsoft')

    """
    algorithm
    """

    @staticmethod
    def ExcludePos(all_pos, type, x1, y1, x2, y2):
        return Dm._dm.ExcludePos(all_pos, type, x1, y1, x2, y2)

    @staticmethod
    def FindNearestPos(all_pos, type, x, y):
        return Dm._dm.FindNearestPos(all_pos, type, x, y)

    @staticmethod
    def SortPosDistance(all_pos, type, x, y):
        return Dm._dm.SortPosDistance(all_pos, type, x, y)

    """
    backstage
    """

    @staticmethod
    def BindWindow(hwnd, display, mouse, keypad, mode):
        return Dm._dm.BindWindow(hwnd, display, mouse, keypad, mode)

    @staticmethod
    def BindWindowEx(hwnd, display, mouse, keypad, public, mode):
        return Dm._dm.BindWindowEx(hwnd, display, mouse, keypad, public, mode)

    @staticmethod
    def DownCpu(rate):
        return Dm._dm.DownCpu(rate)

    @staticmethod
    def EnableBind(enable):
        return Dm._dm.EnableBind(enable)

    @staticmethod
    def EnableFakeActive(enable):
        return Dm._dm.EnableFakeActive(enable)

    @staticmethod
    def EnableIme(enable):
        return Dm._dm.EnableIme(enable)

    @staticmethod
    def EnableKeypadMsg(enable):
        return Dm._dm.EnableKeypadMsg(enable)

    @staticmethod
    def EnableKeypadPatch(enable):
        return Dm._dm.EnableKeypadPatch(enable)

    @staticmethod
    def EnableKeypadSync(enable, time_out):
        return Dm._dm.EnableKeypadSync(enable, time_out)

    @staticmethod
    def EnableMouseMsg(enable):
        return Dm._dm.EnableMouseMsg(enable)

    @staticmethod
    def EnableMouseSync(enable, time_out):
        return Dm._dm.EnableMouseSync(enable, time_out)

    @staticmethod
    def EnableRealKeypad(enable):
        return Dm._dm.EnableRealKeypad(enable)

    @staticmethod
    def EnableRealMouse(enable, mousedelay, mousestep):
        return Dm._dm.EnableRealMouse(enable, mousedelay, mousestep)

    @staticmethod
    def EnableSpeedDx(enable):
        return Dm._dm.EnableSpeedDx(enable)

    @staticmethod
    def ForceUnBindWindow(hwnd):
        return Dm._dm.ForceUnBindWindow(hwnd)

    @staticmethod
    def GetBindWindow():
        return Dm._dm.GetBindWindow()

    @staticmethod
    def GetFps():
        return Dm._dm.GetFps()

    @staticmethod
    def HackSpeed(rate):
        return Dm._dm.HackSpeed(rate)

    @staticmethod
    def IsBind(hwnd):
        return Dm._dm.IsBind(hwnd)

    @staticmethod
    def LockDisplay(lock):
        return Dm._dm.LockDisplay(lock)

    @staticmethod
    def LockInput(lock):
        return Dm._dm.LockInput(lock)

    @staticmethod
    def LockMouseRect(x1, y1, x2, y2):
        return Dm._dm.LockMouseRect(x1, y1, x2, y2)

    @staticmethod
    def SetAero(enable):
        return Dm._dm.SetAero(enable)

    @staticmethod
    def SetDisplayDelay(time):
        return Dm._dm.SetDisplayDelay(time)

    @staticmethod
    def SetDisplayRefreshDelay(time):
        return Dm._dm.SetDisplayRefreshDelay(time)

    @staticmethod
    def SwitchBindWindow(hwnd):
        return Dm._dm.SwitchBindWindow(hwnd)

    @staticmethod
    def UnBindWindow():
        return Dm._dm.UnBindWindow()

    """
    base
    """

    @staticmethod
    def EnablePicCache(enable):
        return Dm._dm.EnablePicCache(enable)

    @staticmethod
    def GetBasePath():
        return Dm._dm.GetBasePath()

    @staticmethod
    def GetDmCount():
        return Dm._dm.GetDmCount()

    @staticmethod
    def GetID():
        return Dm._dm.GetID()

    @staticmethod
    def GetLastError():
        return Dm._dm.GetLastError()

    @staticmethod
    def GetPath():
        return Dm._dm.GetPath()

    reg_return = {
        "-1": "无法连接网络, (可能防火墙拦截, 如果可以正常访问大漠插件网站，那就可以肯定是被防火墙拦截)",
        "-2": "进程没有以管理员方式运行.(出现在win7 win8 vista 2008.建议关闭uac)",
        "0": "失败(未知错误)",
        "1": "成功",
        "2": "余额不足",
        "3": "绑定了本机器，但是账户余额不足50元",
        "4": "注册码错误",
        "5": "你的机器或者IP在黑名单列表中或者不在白名单列表中",
        "6": "非法使用插件",
        "7": "你的帐号因为非法使用被封禁. （如果是在虚拟机中使用插件，必须使用Reg或者RegEx，不能使用RegNoMac或者RegExNoMac, 否则可能会造成封号，或者封禁机器）",
        "8": "ver_info不在你设置的附加白名单中",
        "77": "机器码或者IP因为非法使用，而被封禁. （如果是在虚拟机中使用插件，必须使用Reg或者RegEx，不能使用RegNoMac或者RegExNoMac, "
              "否则可能会造成封号，或者封禁机器）封禁是全局的，如果使用了别人的软件导致77，也一样会导致所有注册码均无法注册。解决办法是更换IP，更换MAC.",
        "777": "同一个机器码注册次数超过了服务器限制, 被暂时封禁.请登录后台，插件今日详细消费记录里，相应的机器码是否有次数异常，并立刻优化解决.如果还有问题，可以联系我来解决.",
        "-8": "版本附加信息长度超过了20",
        "-9": "版本附加信息里包含了非法字母.",
        "-10": "非法的参数ip"
    }

    @staticmethod
    def Reg(reg_code, ver_info):
        ret = Dm._dm.Reg(reg_code, ver_info)
        return {
            "code": ret,
            "msg": Dm.reg_return[str(ret)]
        }

    @staticmethod
    def RegEx(reg_code, ver_info, ip):
        ret = Dm._dm.RegEx(reg_code, ver_info, ip)
        return {
            "code": ret,
            "msg": Dm.reg_return[str(ret)]
        }

    @staticmethod
    def RegExNoMac(reg_code, ver_info, ip):
        ret = Dm._dm.RegExNoMac(reg_code, ver_info, ip)
        return {
            "code": ret,
            "msg": Dm.reg_return[str(ret)]
        }

    @staticmethod
    def RegNoMac(reg_code, ver_info):
        ret = Dm._dm.RegNoMac(reg_code, ver_info)
        return {
            "code": ret,
            "msg": Dm.reg_return[str(ret)]
        }

    @staticmethod
    def SetDisplayInput(mode):
        return Dm._dm.SetDisplayInput(mode)

    @staticmethod
    def SetEnumWindowDelay(delay):
        return Dm._dm.SetEnumWindowDelay(delay)

    @staticmethod
    def SetPath(path):
        return Dm._dm.SetPath(path)

    @staticmethod
    def SetShowErrorMsg(show):
        return Dm._dm.SetShowErrorMsg(show)

    @staticmethod
    def SpeedNormalGraphic(enable):
        return Dm._dm.SpeedNormalGraphic(enable)

    @staticmethod
    def Ver():
        return Dm._dm.Ver()

    """
    compilation
    """

    @staticmethod
    def AsmAdd(asm_ins):
        return Dm._dm.AsmAdd(asm_ins)

    @staticmethod
    def AsmCall(hwnd, mode):
        return Dm._dm.AsmCall(hwnd, mode)

    @staticmethod
    def AsmCallEx(hwnd, mode, base_addr):
        return Dm._dm.AsmCallEx(hwnd, mode, base_addr)

    @staticmethod
    def AsmClear():
        return Dm._dm.AsmClear()

    @staticmethod
    def AsmSetTimeout(time_out, param):
        return Dm._dm.AsmSetTimeout(time_out, param)

    @staticmethod
    def Assemble(base_addr, is_64bit):
        return Dm._dm.Assemble(base_addr, is_64bit)

    @staticmethod
    def DisAssemble(asm_code, base_addr, is_64bit):
        return Dm._dm.DisAssemble(asm_code, base_addr, is_64bit)

    """
    file
    """

    @staticmethod
    def CopyFile(src_file, dst_file, over):
        return Dm._dm.CopyFile(src_file, dst_file, over)

    @staticmethod
    def CreateFolder(folder):
        return Dm._dm.CreateFolder(folder)

    @staticmethod
    def DecodeFile(file, pwd):
        return Dm._dm.DecodeFile(file, pwd)

    @staticmethod
    def DeleteFile(file):
        return Dm._dm.DeleteFile(file)

    @staticmethod
    def DeleteFolder(folder):
        return Dm._dm.DeleteFolder(folder)

    @staticmethod
    def DeleteIni(section, key, file):
        return Dm._dm.DeleteIni(section, key, file)

    @staticmethod
    def DeleteIniPwd(section, key, file, pwd):
        return Dm._dm.DeleteIniPwd(section, key, file, pwd)

    @staticmethod
    def DownloadFile(url, save_file, timeout):
        return Dm._dm.DownloadFile(url, save_file, timeout)

    @staticmethod
    def Encodefile(file, pwd):
        return Dm._dm.Encodefile(file, pwd)

    @staticmethod
    def EnumIniKey(section, file):
        return Dm._dm.EnumIniKey(section, file)

    @staticmethod
    def EnumIniKeyPwd(section, file, pwd):
        return Dm._dm.EnumIniKeyPwd(section, file, pwd)

    @staticmethod
    def EnumIniSection(file):
        return Dm._dm.EnumIniSection(file)

    @staticmethod
    def EnumIniSectionPwd(file, pwd):
        return Dm._dm.EnumIniSectionPwd(file, pwd)

    @staticmethod
    def GetFileLength(file):
        return Dm._dm.GetFileLength(file)

    @staticmethod
    def GetRealPath(path):
        return Dm._dm.GetRealPath(path)

    @staticmethod
    def IsFileExist(file):
        return Dm._dm.IsFileExist(file)

    @staticmethod
    def IsFolderExist(folder):
        return Dm._dm.IsFolderExist(folder)

    @staticmethod
    def MoveFile(src_file, dst_file):
        return Dm._dm.MoveFile(src_file, dst_file)

    @staticmethod
    def ReadFile(file):
        return Dm._dm.ReadFile(file)

    @staticmethod
    def ReadIni(section, key, file):
        return Dm._dm.ReadIni(section, key, file)

    @staticmethod
    def ReadIniPwd(section, key, file, pwd):
        return Dm._dm.ReadIniPwd(section, key, file, pwd)

    @staticmethod
    def SelectDirectory():
        return Dm._dm.SelectDirectory()

    @staticmethod
    def SelectFile():
        return Dm._dm.SelectFile()

    @staticmethod
    def WriteFile(file, content):
        return Dm._dm.WriteFile(file, content)

    @staticmethod
    def WriteIni(section, key, value, file):
        return Dm._dm.WriteIni(section, key, value, file)

    @staticmethod
    def WriteIniPwd(section, key, value, file, pwd):
        return Dm._dm.WriteIniPwd(section, key, value, file, pwd)

    """
    foobar
    """

    @staticmethod
    def CreateFoobarCustom(hwnd, x, y, pic_name, trans_color, sim):
        return Dm._dm.CreateFoobarCustom(hwnd, x, y, pic_name, trans_color, sim)

    @staticmethod
    def CreateFoobarEllipse(hwnd, x, y, w, h):
        return Dm._dm.CreateFoobarEllipse(hwnd, x, y, w, h)

    @staticmethod
    def CreateFoobarRect(hwnd, x, y, w, h):
        return Dm._dm.CreateFoobarRect(hwnd, x, y, w, h)

    @staticmethod
    def CreateFoobarRoundRect(hwnd, x, y, w, h, rw, rh):
        return Dm._dm.CreateFoobarRoundRect(hwnd, x, y, w, h, rw, rh)

    @staticmethod
    def FoobarClearText(hwnd):
        return Dm._dm.FoobarClearText(hwnd)

    @staticmethod
    def FoobarClose(hwnd):
        return Dm._dm.FoobarClose(hwnd)

    @staticmethod
    def FoobarDrawLine(hwnd, x1, y1, x2, y2, color, style, width):
        return Dm._dm.FoobarDrawLine(hwnd, x1, y1, x2, y2, color, style, width)

    @staticmethod
    def FoobarDrawPic(hwnd, x, y, pic_name, trans_color):
        return Dm._dm.FoobarDrawPic(hwnd, x, y, pic_name, trans_color)

    @staticmethod
    def FoobarDrawText(hwnd, x, y, w, h, text, color, align):
        return Dm._dm.FoobarDrawText(hwnd, x, y, w, h, text, color, align)

    @staticmethod
    def FoobarFillRect(hwnd, x1, y1, x2, y2, color):
        return Dm._dm.FoobarFillRect(hwnd, x1, y1, x2, y2, color)

    @staticmethod
    def FoobarLock(hwnd):
        return Dm._dm.FoobarLock(hwnd)

    @staticmethod
    def FoobarPrintText(hwnd, text, color):
        return Dm._dm.FoobarPrintText(hwnd, text, color)

    @staticmethod
    def FoobarSetFont(hwnd, font_name, size, flag):
        return Dm._dm.FoobarSetFont(hwnd, font_name, size, flag)

    @staticmethod
    def FoobarSetSave(hwnd, file, enable, header):
        return Dm._dm.FoobarSetSave(hwnd, file, enable, header)

    @staticmethod
    def FoobarSetTrans(hwnd, is_trans, color, sim):
        return Dm._dm.FoobarSetTrans(hwnd, is_trans, color, sim)

    @staticmethod
    def FoobarStartGif(hwnd, x, y, pic_name, repeat_limit, delay):
        return Dm._dm.FoobarStartGif(hwnd, x, y, pic_name, repeat_limit, delay)

    @staticmethod
    def FoobarStopGif(hwnd, x, y, pic_name):
        return Dm._dm.FoobarStopGif(hwnd, x, y, pic_name)

    @staticmethod
    def FoobarTextLineGap(hwnd, line_gap):
        return Dm._dm.FoobarTextLineGap(hwnd, line_gap)

    @staticmethod
    def FoobarTextPrintDir(hwnd, dir):
        return Dm._dm.FoobarTextPrintDir(hwnd, dir)

    @staticmethod
    def FoobarTextRect(hwnd, x, y, w, h):
        return Dm._dm.FoobarTextRect(hwnd, x, y, w, h)

    @staticmethod
    def FoobarUnlock(hwnd):
        return Dm._dm.FoobarUnlock(hwnd)

    @staticmethod
    def FoobarUpdate(hwnd):
        return Dm._dm.FoobarUpdate(hwnd)

    """
    guard
    """

    @staticmethod
    def DmGuard(enable, type):
        return Dm._dm.DmGuard(enable, type)

    @staticmethod
    def DmGuardParams(cmd, subcmd, param):
        return Dm._dm.DmGuardParams(cmd, subcmd, param)

    @staticmethod
    def UnLoadDriver():
        return Dm._dm.UnLoadDriver()

    """
    memory
    """

    @staticmethod
    def DoubleToData(value):
        return Dm._dm.DoubleToData(value)

    @staticmethod
    def FindData(hwnd, addr_range, data):
        return Dm._dm.FindData(hwnd, addr_range, data)

    @staticmethod
    def FindDataEx(hwnd, addr_range, data, step, multi_thread, mode):
        return Dm._dm.FindDataEx(hwnd, addr_range, data, step, multi_thread, mode)

    @staticmethod
    def FindDouble(hwnd, addr_range, double_value_min, double_value_max):
        return Dm._dm.FindDouble(hwnd, addr_range, double_value_min, double_value_max)

    @staticmethod
    def FindDoubleEx(hwnd, addr_range, double_value_min, double_value_max, step, multi_thread, mode):
        return Dm._dm.FindDoubleEx(hwnd, addr_range, double_value_min, double_value_max, step, multi_thread, mode)

    @staticmethod
    def FindFloat(hwnd, addr_range, float_value_min, float_value_max):
        return Dm._dm.FindFloat(hwnd, addr_range, float_value_min, float_value_max)

    @staticmethod
    def FindFloatEx(hwnd, addr_range, float_value_min, float_value_max, step, multi_thread, mode):
        return Dm._dm.FindFloatEx(hwnd, addr_range, float_value_min, float_value_max, step, multi_thread, mode)

    @staticmethod
    def FindInt(hwnd, addr_range, int_value_min, int_value_max, type):
        return Dm._dm.FindInt(hwnd, addr_range, int_value_min, int_value_max, type)

    @staticmethod
    def FindIntEx(hwnd, addr_range, int_value_min, int_value_max, type, step, multi_thread, mode):
        return Dm._dm.FindIntEx(hwnd, addr_range, int_value_min, int_value_max, type, step, multi_thread, mode)

    @staticmethod
    def FindString(hwnd, addr_range, string_value, type):
        return Dm._dm.FindString(hwnd, addr_range, string_value, type)

    @staticmethod
    def FindStringEx(hwnd, addr_range, string_value, type, step, multi_thread, mode):
        return Dm._dm.FindStringEx(hwnd, addr_range, string_value, type, step, multi_thread, mode)

    @staticmethod
    def FloatToData(value):
        return Dm._dm.FloatToData(value)

    @staticmethod
    def FreeProcessMemory(hwnd):
        return Dm._dm.FreeProcessMemory(hwnd)

    @staticmethod
    def GetCommandLine(hwnd):
        return Dm._dm.GetCommandLine(hwnd)

    @staticmethod
    def GetModuleBaseAddr(hwnd, module):
        return Dm._dm.GetModuleBaseAddr(hwnd, module)

    @staticmethod
    def GetModuleSize(hwnd, module):
        return Dm._dm.GetModuleSize(hwnd, module)

    @staticmethod
    def GetRemoteApiAddress(hwnd, base_addr, fun_name):
        return Dm._dm.GetRemoteApiAddress(hwnd, base_addr, fun_name)

    @staticmethod
    def Int64ToInt32(value):
        return Dm._dm.Int64ToInt32(value)

    @staticmethod
    def IntToData(value, type):
        return Dm._dm.IntToData(value, type)

    @staticmethod
    def OpenProcess(pid):
        return Dm._dm.OpenProcess(pid)

    @staticmethod
    def ReadData(hwnd, addr, len):
        return Dm._dm.ReadData(hwnd, addr, len)

    @staticmethod
    def ReadDataAddr(hwnd, addr, len):
        return Dm._dm.ReadDataAddr(hwnd, addr, len)

    @staticmethod
    def ReadDataAddrToBin(hwnd, addr, len):
        return Dm._dm.ReadDataAddrToBin(hwnd, addr, len)

    @staticmethod
    def ReadDataToBin(hwnd, addr, len):
        return Dm._dm.ReadDataToBin(hwnd, addr, len)

    @staticmethod
    def ReadDouble(hwnd, addr):
        return Dm._dm.ReadDouble(hwnd, addr)

    @staticmethod
    def ReadDoubleAddr(hwnd, addr):
        return Dm._dm.ReadDoubleAddr(hwnd, addr)

    @staticmethod
    def ReadFloat(hwnd, addr):
        return Dm._dm.ReadFloat(hwnd, addr)

    @staticmethod
    def ReadFloatAddr(hwnd, addr):
        return Dm._dm.ReadFloatAddr(hwnd, addr)

    @staticmethod
    def ReadInt(hwnd, addr, type):
        return Dm._dm.ReadInt(hwnd, addr, type)

    @staticmethod
    def ReadIntAddr(hwnd, addr, type):
        return Dm._dm.ReadIntAddr(hwnd, addr, type)

    @staticmethod
    def ReadString(hwnd, addr, type, len):
        return Dm._dm.ReadString(hwnd, addr, type, len)

    @staticmethod
    def ReadStringAddr(hwnd, addr, type, len):
        return Dm._dm.ReadStringAddr(hwnd, addr, type, len)

    @staticmethod
    def SetMemoryFindResultToFile(file):
        return Dm._dm.SetMemoryFindResultToFile(file)

    @staticmethod
    def SetMemoryHwndAsProcessId(en):
        return Dm._dm.SetMemoryHwndAsProcessId(en)

    @staticmethod
    def SetParam64ToPointer():
        return Dm._dm.SetParam64ToPointer()

    @staticmethod
    def StringToData(value, type):
        return Dm._dm.StringToData(value, type)

    @staticmethod
    def TerminateProcess(pid):
        return Dm._dm.TerminateProcess(pid)

    @staticmethod
    def VirtualAllocEx(hwnd, addr, size, type):
        return Dm._dm.VirtualAllocEx(hwnd, addr, size, type)

    @staticmethod
    def VirtualFreeEx(hwnd, addr):
        return Dm._dm.VirtualFreeEx(hwnd, addr)

    @staticmethod
    def VirtualProtectEx(hwnd, addr, size, type, old_protect):
        return Dm._dm.VirtualProtectEx(hwnd, addr, size, type, old_protect)

    @staticmethod
    def VirtualQueryEx(hwnd, addr, pmbi):
        return Dm._dm.VirtualQueryEx(hwnd, addr, pmbi)

    @staticmethod
    def WriteData(hwnd, addr, data):
        return Dm._dm.WriteData(hwnd, addr, data)

    @staticmethod
    def WriteDataAddr(hwnd, addr, data):
        return Dm._dm.WriteDataAddr(hwnd, addr, data)

    @staticmethod
    def WriteDataAddrFromBin(hwnd, addr, data, len):
        return Dm._dm.WriteDataAddrFromBin(hwnd, addr, data, len)

    @staticmethod
    def WriteDataFromBin(hwnd, addr, data, len):
        return Dm._dm.WriteDataFromBin(hwnd, addr, data, len)

    @staticmethod
    def WriteDouble(hwnd, addr, v):
        return Dm._dm.WriteDouble(hwnd, addr, v)

    @staticmethod
    def WriteDoubleAddr(hwnd, addr, v):
        return Dm._dm.WriteDoubleAddr(hwnd, addr, v)

    @staticmethod
    def WriteFloat(hwnd, addr, v):
        return Dm._dm.WriteFloat(hwnd, addr, v)

    @staticmethod
    def WriteFloatAddr(hwnd, addr, v):
        return Dm._dm.WriteFloatAddr(hwnd, addr, v)

    @staticmethod
    def WriteInt(hwnd, addr, type, v):
        return Dm._dm.WriteInt(hwnd, addr, type, v)

    @staticmethod
    def WriteIntAddr(hwnd, addr, type, v):
        return Dm._dm.WriteIntAddr(hwnd, addr, type, v)

    @staticmethod
    def WriteString(hwnd, addr, type, v):
        return Dm._dm.WriteString(hwnd, addr, type, v)

    @staticmethod
    def WriteStringAddr(hwnd, addr, type, v):
        return Dm._dm.WriteStringAddr(hwnd, addr, type, v)

    """
    mouse_keyboard
    """

    keys = {
        "1": 49,
        "2": 50,
        "3": 51,
        "4": 52,
        "5": 53,
        "6": 54,
        "7": 55,
        "8": 56,
        "9": 57,
        "0": 48,
        "-": 189,
        "=": 187,
        "back": 8,
        "a": 65,
        "b": 66,
        "c": 67,
        "d": 68,
        "e": 69,
        "f": 70,
        "g": 71,
        "h": 72,
        "i": 73,
        "j": 74,
        "k": 75,
        "l": 76,
        "m": 77,
        "n": 78,
        "o": 79,
        "p": 80,
        "q": 81,
        "r": 82,
        "s": 83,
        "t": 84,
        "u": 85,
        "v": 86,
        "w": 87,
        "x": 88,
        "y": 89,
        "z": 90,
        "ctrl": 17,
        "alt": 18,
        "shift": 16,
        "win": 91,
        "space": 32,
        "cap": 20,
        "tab": 9,
        "~": 192,
        "esc": 27,
        "enter": 13,
        "up": 38,
        "down": 40,
        "left": 37,
        "right": 39,
        "option": 93,
        "print": 44,
        "delete": 46,
        "home": 36,
        "end": 35,
        "pgup": 33,
        "pgdn": 34,
        "f1": 112,
        "f2": 113,
        "f3": 114,
        "f4": 115,
        "f5": 116,
        "f6": 117,
        "f7": 118,
        "f8": 119,
        "f9": 120,
        "f10": 121,
        "f11": 122,
        "f12": 123,
        "[": 219,
        "]": 221,
        "\\": 220,
        ";": 186,
        "'": 222,
        ":": 188,
        ".": 190,
        "/": 191
    }

    @staticmethod
    def EnableMouseAccuracy(enable):
        return Dm._dm.EnableMouseAccuracy(enable)

    @staticmethod
    def GetCursorPos(x, y):
        return Dm._dm.GetCursorPos(x, y)

    @staticmethod
    def GetCursorShape():
        return Dm._dm.GetCursorShape()

    @staticmethod
    def GetCursorShapeEx(value: int):
        return Dm._dm.GetCursorShapeEx(value)

    @staticmethod
    def GetCursorSpot():
        return Dm._dm.GetCursorSpot()

    @staticmethod
    def GetKeyState(vk_code):
        return Dm._dm.GetKeyState(vk_code)

    @staticmethod
    def GetMouseSpeed():
        return Dm._dm.GetMouseSpeed()

    @staticmethod
    def KeyDown(vk_code):
        return Dm._dm.KeyDown(vk_code)

    @staticmethod
    def KeyDownChar(key_str):
        return Dm._dm.KeyDownChar(key_str)

    @staticmethod
    def KeyPress(vk_code):
        return Dm._dm.KeyPress(vk_code)

    @staticmethod
    def KeyPressChar(key_str):
        return Dm._dm.KeyPressChar(key_str)

    @staticmethod
    def KeyPressStr(key_str, delay):
        return Dm._dm.KeyPressStr(key_str, delay)

    @staticmethod
    def KeyUp(vk_code):
        return Dm._dm.KeyUp(vk_code)

    @staticmethod
    def KeyUpChar(key_str):
        return Dm._dm.KeyUpChar(key_str)

    @staticmethod
    def LeftClick():
        return Dm._dm.LeftClick()

    @staticmethod
    def LeftDoubleClick():
        return Dm._dm.LeftDoubleClick()

    @staticmethod
    def LeftDown():
        return Dm._dm.LeftDown()

    @staticmethod
    def LeftUp():
        return Dm._dm.LeftUp()

    @staticmethod
    def MiddleClick():
        return Dm._dm.MiddleClick()

    @staticmethod
    def MiddleDown():
        return Dm._dm.MiddleDown()

    @staticmethod
    def MiddleUp():
        return Dm._dm.MiddleUp()

    @staticmethod
    def MoveR(rx, ry):
        return Dm._dm.MoveR(rx, ry)

    @staticmethod
    def MoveTo(x, y):
        return Dm._dm.MoveTo(x, y)

    @staticmethod
    def MoveToEx(x, y, w, h):
        return Dm._dm.MoveToEx(x, y, w, h)

    @staticmethod
    def RightClick():
        return Dm._dm.RightClick()

    @staticmethod
    def RightDown():
        return Dm._dm.RightDown()

    @staticmethod
    def RightUp():
        return Dm._dm.RightUp()

    @staticmethod
    def SetKeypadDelay(type, delay):
        return Dm._dm.SetKeypadDelay(type, delay)

    @staticmethod
    def SetMouseDelay(type, delay):
        return Dm._dm.SetMouseDelay(type, delay)

    @staticmethod
    def SetMouseSpeed(speed):
        return Dm._dm.SetMouseSpeed(speed)

    @staticmethod
    def SetSimMode(mode):
        return Dm._dm.SetSimMode(mode)

    @staticmethod
    def WaitKey(vk_code, time_out):
        return Dm._dm.WaitKey(vk_code, time_out)

    @staticmethod
    def WheelDown():
        return Dm._dm.WheelDown()

    @staticmethod
    def WheelUp():
        return Dm._dm.WheelUp()

    """
    other
    """

    @staticmethod
    def ActiveInputMethod(hwnd, input_method):
        return Dm._dm.ActiveInputMethod(hwnd, input_method)

    @staticmethod
    def CheckInputMethod(hwnd, input_method):
        return Dm._dm.CheckInputMethod(hwnd, input_method)

    @staticmethod
    def EnterCri():
        return Dm._dm.EnterCri()

    @staticmethod
    def ExecuteCmd(cmd, current_dir, time_out):
        return Dm._dm.ExecuteCmd(cmd, current_dir, time_out)

    @staticmethod
    def FindInputMethod(input_method):
        return Dm._dm.FindInputMethod(input_method)

    @staticmethod
    def InitCri():
        return Dm._dm.InitCri()

    @staticmethod
    def LeaveCri():
        return Dm._dm.LeaveCri()

    @staticmethod
    def ReleaseRef():
        return Dm._dm.ReleaseRef()

    @staticmethod
    def SetExitThread(enable):
        return Dm._dm.SetExitThread(enable)

    """
    picture_color
    """

    @staticmethod
    def AppendPicAddr(pic_info, addr, size):
        return Dm._dm.AppendPicAddr(pic_info, addr, size)

    @staticmethod
    def BGR2RGB(bgr_color):
        return Dm._dm.BGR2RGB(bgr_color)

    @staticmethod
    def Capture(x1, y1, x2, y2, file):
        return Dm._dm.Capture(x1, y1, x2, y2, file)

    @staticmethod
    def CaptureGif(x1, y1, x2, y2, file, delay, time):
        return Dm._dm.CaptureGif(x1, y1, x2, y2, file, delay, time)

    @staticmethod
    def CaptureJpg(x1, y1, x2, y2, file, quality):
        return Dm._dm.CaptureJpg(x1, y1, x2, y2, file, quality)

    @staticmethod
    def CapturePng(x1, y1, x2, y2, file):
        return Dm._dm.CapturePng(x1, y1, x2, y2, file)

    @staticmethod
    def CapturePre(file):
        return Dm._dm.CapturePre(file)

    @staticmethod
    def CmpColor(x, y, color, sim):
        return Dm._dm.CmpColor(x, y, color, sim)

    @staticmethod
    def EnableDisplayDebug(enable_debug):
        return Dm._dm.EnableDisplayDebug(enable_debug)

    @staticmethod
    def EnableFindPicMultithread(enable):
        return Dm._dm.EnableFindPicMultithread(enable)

    @staticmethod
    def EnableGetColorByCapture(enable):
        return Dm._dm.EnableGetColorByCapture(enable)

    @staticmethod
    def FindColor(x1, y1, x2, y2, color, sim, dir, intX, intY):
        return Dm._dm.FindColor(x1, y1, x2, y2, color, sim, dir, intX, intY)

    @staticmethod
    def FindColorBlock(x1, y1, x2, y2, color, sim, count, width, height, intX, intY):
        return Dm._dm.FindColorBlock(x1, y1, x2, y2, color, sim, count, width, height, intX, intY)

    @staticmethod
    def FindColorBlockEx(x1, y1, x2, y2, color, sim, count, width, height):
        return Dm._dm.FindColorBlockEx(x1, y1, x2, y2, color, sim, count, width, height)

    @staticmethod
    def FindColorE(x1, y1, x2, y2, color, sim, dir):
        return Dm._dm.FindColorE(x1, y1, x2, y2, color, sim, dir)

    @staticmethod
    def FindColorEx(x1, y1, x2, y2, color, sim, dir):
        return Dm._dm.FindColorEx(x1, y1, x2, y2, color, sim, dir)

    @staticmethod
    def FindMulColor(x1, y1, x2, y2, color, sim):
        return Dm._dm.FindMulColor(x1, y1, x2, y2, color, sim)

    @staticmethod
    def FindMultiColor(x1, y1, x2, y2, first_color, offset_color, sim, dir, intX, intY):
        return Dm._dm.FindMultiColor(x1, y1, x2, y2, first_color, offset_color, sim, dir, intX, intY)

    @staticmethod
    def FindMultiColorE(x1, y1, x2, y2, first_color, offset_color, sim, dir):
        return Dm._dm.FindMultiColorE(x1, y1, x2, y2, first_color, offset_color, sim, dir)

    @staticmethod
    def FindMultiColorEx(x1, y1, x2, y2, first_color, offset_color, sim, dir):
        return Dm._dm.indMultiColorEx(x1, y1, x2, y2, first_color, offset_color, sim, dir)

    @staticmethod
    def FindPic(x1, y1, x2, y2, pic_name, delta_color, sim, dir, intX, intY):
        return Dm._dm.FindPic(x1, y1, x2, y2, pic_name, delta_color, sim, dir, intX, intY)

    @staticmethod
    def FindPicE(x1, y1, x2, y2, pic_name, delta_color, sim, dir):
        return Dm._dm.FindPicE(x1, y1, x2, y2, pic_name, delta_color, sim, dir)

    @staticmethod
    def FindPicEx(x1, y1, x2, y2, pic_name, delta_color, sim, dir):
        return Dm._dm.FindPicEx(x1, y1, x2, y2, pic_name, delta_color, sim, dir)

    @staticmethod
    def FindPicExS(x1, y1, x2, y2, pic_name, delta_color, sim, dir):
        return Dm._dm.FindPicExS(x1, y1, x2, y2, pic_name, delta_color, sim, dir)

    @staticmethod
    def FindPicMem(x1, y1, x2, y2, pic_info, delta_color, sim, dir, intX, intY):
        return Dm._dm.FindPicMem(x1, y1, x2, y2, pic_info, delta_color, sim, dir, intX, intY)

    @staticmethod
    def FindPicMemE(x1, y1, x2, y2, pic_info, delta_color, sim, dir):
        return Dm._dm.FindPicMemE(x1, y1, x2, y2, pic_info, delta_color, sim, dir)

    @staticmethod
    def FindPicMemEx(x1, y1, x2, y2, pic_info, delta_color, sim, dir):
        return Dm._dm.FindPicMemEx(x1, y1, x2, y2, pic_info, delta_color, sim, dir)

    @staticmethod
    def FindPicS(x1, y1, x2, y2, pic_name, delta_color, sim, dir, intX, intY):
        return Dm._dm.FindPicS(x1, y1, x2, y2, pic_name, delta_color, sim, dir, intX, intY)

    @staticmethod
    def FindShape(x1, y1, x2, y2, offset_color, sim, dir, intX, intY):
        return Dm._dm.FindShape(x1, y1, x2, y2, offset_color, sim, dir, intX, intY)

    @staticmethod
    def FindShapeE(x1, y1, x2, y2, offset_color, sim, dir):
        return Dm._dm.FindShapeE(x1, y1, x2, y2, offset_color, sim, dir)

    @staticmethod
    def FindShapeEx(x1, y1, x2, y2, offset_color, sim, dir):
        return Dm._dm.FindShapeEx(x1, y1, x2, y2, offset_color, sim, dir)

    @staticmethod
    def FreePic(pic_name):
        return Dm._dm.FreePic(pic_name)

    @staticmethod
    def GetAveHSV(x1, y1, x2, y2):
        return Dm._dm.GetAveHSV(x1, y1, x2, y2)

    @staticmethod
    def GetAveRGB(x1, y1, x2, y2):
        return Dm._dm.GetAveRGB(x1, y1, x2, y2)

    @staticmethod
    def GetColor(x, y):
        return Dm._dm.GetColor(x, y)

    @staticmethod
    def GetColorBGR(x, y):
        return Dm._dm.GetColorBGR(x, y)

    @staticmethod
    def GetColorHSV(x, y):
        return Dm._dm.GetColorHSV(x, y)

    @staticmethod
    def GetColorNum(x1, y1, x2, y2, color, sim):
        return Dm._dm.GetColorNum(x1, y1, x2, y2, color, sim)

    @staticmethod
    def GetPicSize(pic_name):
        return Dm._dm.GetPicSize(pic_name)

    @staticmethod
    def GetScreenData(x1, y1, x2, y2):
        return Dm._dm.GetScreenData(x1, y1, x2, y2)

    @staticmethod
    def GetScreenDataBmp(x1, y1, x2, y2, data, size):
        return Dm._dm.GetScreenDataBmp(x1, y1, x2, y2, data, size)

    @staticmethod
    def ImageToBmp(pic_name, bmp_name):
        return Dm._dm.ImageToBmp(pic_name, bmp_name)

    @staticmethod
    def IsDisplayDead(x1, y1, x2, y2, t):
        return Dm._dm.IsDisplayDead(x1, y1, x2, y2, t)

    @staticmethod
    def LoadPic(pic_name):
        return Dm._dm.LoadPic(pic_name)

    @staticmethod
    def LoadPicByte(addr, size, pic_name):
        return Dm._dm.LoadPicByte(addr, size, pic_name)

    @staticmethod
    def MatchPicName(pic_name):
        return Dm._dm.MatchPicName(pic_name)

    @staticmethod
    def RGB2BGR(rgb_color):
        return Dm._dm.RGB2BGR(rgb_color)

    @staticmethod
    def SetExcludeRegion(mode, info):
        return Dm._dm.SetExcludeRegion(mode, info)

    @staticmethod
    def SetPicPwd(pwd):
        return Dm._dm.SetPicPwd(pwd)

    """
    system
    """

    @staticmethod
    def Beep(f, duration):
        return Dm._dm.Beep(f, duration)

    @staticmethod
    def CheckFontSmooth():
        return Dm._dm.CheckFontSmooth()

    @staticmethod
    def CheckUAC():
        return Dm._dm.CheckUAC()

    @staticmethod
    def Delay(mis):
        return Dm._dm.Delay(mis)

    @staticmethod
    def Delays(mis_min, mis_max):
        return Dm._dm.Delays(mis_min, mis_max)

    @staticmethod
    def DisableCloseDisplayAndSleep():
        return Dm._dm.DisableCloseDisplayAndSleep()

    @staticmethod
    def DisableFontSmooth():
        return Dm._dm.DisableFontSmooth()

    @staticmethod
    def DisablePowerSave():
        return Dm._dm.DisablePowerSave()

    @staticmethod
    def DisableScreenSave():
        return Dm._dm.DisableScreenSave()

    @staticmethod
    def EnableFontSmooth():
        return Dm._dm.EnableFontSmooth()

    @staticmethod
    def ExitOs(type):
        return Dm._dm.ExitOs(type)

    @staticmethod
    def GetClipboard():
        return Dm._dm.GetClipboard()

    @staticmethod
    def GetCpuType():
        return Dm._dm.GetCpuType()

    @staticmethod
    def GetCpuUsage():
        return Dm._dm.GetCpuUsage()

    @staticmethod
    def GetDir(type):
        return Dm._dm.GetDir(type)

    @staticmethod
    def GetDiskModel(index):
        return Dm._dm.GetDiskModel(index)

    @staticmethod
    def GetDiskReversion(index):
        return Dm._dm.GetDiskReversion(index)

    @staticmethod
    def GetDiskSerial(index):
        return Dm._dm.GetDiskSerial(index)

    @staticmethod
    def GetDisplayInfo():
        return Dm._dm.GetDisplayInfo()

    @staticmethod
    def GetDPI():
        return Dm._dm.GetDPI()

    @staticmethod
    def GetLocale():
        return Dm._dm.GetLocale()

    @staticmethod
    def GetMachineCode():
        return Dm._dm.GetMachineCode()

    @staticmethod
    def GetMachineCodeNoMac():
        return Dm._dm.GetMachineCodeNoMac()

    @staticmethod
    def GetMemoryUsage():
        return Dm._dm.GetMemoryUsage()

    @staticmethod
    def GetNetTime():
        return Dm._dm.GetNetTime()

    @staticmethod
    def GetNetTimeByIp(ip):
        return Dm._dm.GetNetTimeByIp(ip)

    @staticmethod
    def GetNetTimeSafe():
        return Dm._dm.GetNetTimeSafe()

    @staticmethod
    def GetOsBuildNumber():
        return Dm._dm.GetOsBuildNumber()

    @staticmethod
    def GetOsType():
        return Dm._dm.GetOsType()

    @staticmethod
    def GetScreenDepth():
        return Dm._dm.GetScreenDepth()

    @staticmethod
    def GetScreenHeight():
        return Dm._dm.GetScreenHeight()

    @staticmethod
    def GetScreenWidth():
        return Dm._dm.GetScreenWidth()

    @staticmethod
    def GetTime():
        return Dm._dm.GetTime()

    @staticmethod
    def Is64Bit():
        return Dm._dm.Is64Bit()

    @staticmethod
    def IsSurrpotVt():
        return Dm._dm.IsSurrpotVt()

    @staticmethod
    def Play(media_file):
        return Dm._dm.Play(media_file)

    @staticmethod
    def RunApp(app_path, mode):
        return Dm._dm.RunApp(app_path, mode)

    @staticmethod
    def SetClipboard(value):
        return Dm._dm.SetClipboard(value)

    @staticmethod
    def SetDisplayAcceler(level):
        return Dm._dm.SetDisplayAcceler(level)

    @staticmethod
    def SetLocale():
        return Dm._dm.SetLocale()

    @staticmethod
    def SetScreen(width, height, depth):
        return Dm._dm.SetScreen(width, height, depth)

    @staticmethod
    def SetUAC(enable):
        return Dm._dm.SetUAC(enable)

    @staticmethod
    def ShowTaskBarIcon(hwnd, is_show):
        return Dm._dm.ShowTaskBarIcon(hwnd, is_show)

    @staticmethod
    def Stop(id):
        return Dm._dm.Stop(id)

    """
    windows
    """

    @staticmethod
    def ClientToScreen(hwnd, x, y):
        return Dm._dm.ClientToScreen(hwnd, x, y)

    @staticmethod
    def EnumProcess(name):
        return Dm._dm.EnumProcess(name)

    @staticmethod
    def EnumWindow(parent, title, class_name, filter):
        return Dm._dm.EnumWindow(parent, title, class_name, filter)

    @staticmethod
    def EnumWindowByProcess(process_name, title, class_name, filter):
        return Dm._dm.EnumWindowByProcess(process_name, title, class_name, filter)

    @staticmethod
    def EnumWindowByProcessId(pid, title, class_name, filter):
        return Dm._dm.EnumWindowByProcessId(pid, title, class_name, filter)

    @staticmethod
    def EnumWindowSuper(spec1, flag1, type1, spec2, flag2, type2, sort):
        return Dm._dm.EnumWindowSuper(spec1, flag1, type1, spec2, flag2, type2, sort)

    @staticmethod
    def FindWindow(_class, title):
        return Dm._dm.FindWindow(_class, title)

    @staticmethod
    def FindWindowByProcess(process_name, _class, title):
        return Dm._dm.FindWindowByProcess(process_name, _class, title)

    @staticmethod
    def FindWindowByProcessId(process_id, _class, title):
        return Dm._dm.FindWindowByProcessId(process_id, _class, title)

    @staticmethod
    def FindWindowEx(parent, _class, title):
        return Dm._dm.FindWindowEx(parent, _class, title)

    @staticmethod
    def FindWindowSuper(spec1, flag1, type1, spec2, flag2, type2):
        return Dm._dm.FindWindowSuper(spec1, flag1, type1, spec2, flag2, type2)

    @staticmethod
    def GetClientRect(hwnd, x1, y1, x2, y2):
        return Dm._dm.GetClientRect(hwnd, x1, y1, x2, y2)

    @staticmethod
    def GetClientSize(hwnd, width, height):
        return Dm._dm.GetClientSize(hwnd, width, height)

    @staticmethod
    def GetForegroundFocus():
        return Dm._dm.GetForegroundFocus()

    @staticmethod
    def GetForegroundWindow():
        return Dm._dm.GetForegroundWindow()

    @staticmethod
    def GetMousePointWindow():
        return Dm._dm.GetMousePointWindow()

    @staticmethod
    def GetPointWindow(x, y):
        return Dm._dm.GetPointWindow(x, y)

    @staticmethod
    def GetProcessInfo(pid):
        return Dm._dm.GetProcessInfo(pid)

    @staticmethod
    def GetSpecialWindow(flag):
        return Dm._dm.GetSpecialWindow(flag)

    @staticmethod
    def GetWindow(hwnd, flag):
        return Dm._dm.GetWindow(hwnd, flag)

    @staticmethod
    def GetWindowClass(hwnd):
        return Dm._dm.GetWindowClass(hwnd)

    @staticmethod
    def GetWindowProcessId(hwnd):
        return Dm._dm.GetWindowProcessId(hwnd)

    @staticmethod
    def GetWindowProcessPath(hwnd):
        return Dm._dm.GetWindowProcessPath(hwnd)

    @staticmethod
    def GetWindowRect(hwnd, x1, y1, x2, y2):
        return Dm._dm.GetWindowRect(hwnd, x1, y1, x2, y2)

    @staticmethod
    def GetWindowState(hwnd, flag):
        return Dm._dm.GetWindowState(hwnd, flag)

    @staticmethod
    def GetWindowTitle(hwnd):
        return Dm._dm.GetWindowTitle(hwnd)

    @staticmethod
    def MoveWindow(hwnd, x, y):
        return Dm._dm.MoveWindow(hwnd, x, y)

    @staticmethod
    def ScreenToClient(hwnd, x, y):
        return Dm._dm.ScreenToClient(hwnd, x, y)

    @staticmethod
    def SendPaste(hwnd):
        return Dm._dm.SendPaste(hwnd)

    @staticmethod
    def SendString(hwnd, str):
        return Dm._dm.SendString(hwnd, str)

    @staticmethod
    def SendString2(hwnd, str):
        return Dm._dm.SendString2(hwnd, str)

    @staticmethod
    def SendStringIme(str):
        return Dm._dm.SendStringIme(str)

    @staticmethod
    def SendStringIme2(hwnd, str, mode):
        return Dm._dm.SendStringIme2(hwnd, str, mode)

    @staticmethod
    def SetClientSize(hwnd, width, height):
        return Dm._dm.SetClientSize(hwnd, width, height)

    @staticmethod
    def SetWindowSize(hwnd, width, height):
        return Dm._dm.SetWindowSize(hwnd, width, height)

    @staticmethod
    def SetWindowState(hwnd, flag):
        return Dm._dm.SetWindowState(hwnd, flag)

    @staticmethod
    def SetWindowText(hwnd, title):
        return Dm._dm.SetWindowText(hwnd, title)

    @staticmethod
    def SetWindowTransparent(hwnd, trans):
        return Dm._dm.SetWindowTransparent(hwnd, trans)
