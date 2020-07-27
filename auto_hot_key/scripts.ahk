; Program for show hide toggle files/dir in folder
!h::
	RegRead, HiddenFiles_Status, HKEY_CURRENT_USER, Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced, Hidden 
	If HiddenFiles_Status = 2
	RegWrite, REG_DWORD, HKEY_CURRENT_USER, Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced, Hidden, 1
	Else
	RegWrite, REG_DWORD, HKEY_CURRENT_USER, Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced, Hidden, 2
	send {F5}
	return


; Script for open git bash
!g::
	Run "C:\Program Files\Git\git-bash.exe"
	return

!c::
	Run "C:\Windows\system32\cmd.exe"
	return


;Remap Keys
	;Capslock::Shift
	;return


;Open webpages
	!l::Run "http://127.0.0.1:8000"
	return


;Window always on Top
	^SPACE:: Winset, Alwaysontop, , A
	return


;Turn off monitor after locking system
	#l::
	{
		Sleep, 200
		DllCall("LockWorkStation")
		Sleep, 200
		SendMessage,0x112,0xF170,2,,Program Manager
	}
	return


;Open Documents folder
	!d::Run "C:\Users\Abhay\Documents\emorize"
	return


;Custom volume buttons
	!Up:: Send {Volume_Up}
	!Down:: Send {Volume_Down}
	break::Send {Volume_Mute}
	return


;Suspend AutoHotKey
	!Del::Suspend
	return
	

;Open Visual Studio code With project
	!e:: Run, code, C:\Users\Abhay\Documents\emorize
	return