# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
Windows specific functionality

Functionality for get_file_owner() can be found here:
http://stackoverflow.com/questions/8086412/howto-determine-file-owner-on-windows-using-python-without-pywin32
"""

import ctypes
from ctypes import wintypes

PSECURITY_DESCRIPTOR = ctypes.POINTER(wintypes.BYTE)
PSID = ctypes.POINTER(wintypes.BYTE)
LPDWORD = ctypes.POINTER(wintypes.DWORD)
LPBOOL = ctypes.POINTER(wintypes.BOOL)

OWNER_SECURITY_INFORMATION = 0X00000001

"""
MSDN windows/desktop/aa446639

The GetFileSecurity function obtains specified information about the 
security of a file or directory. The information obtained is constrained 
by the caller's access rights and privileges.
"""
GetFileSecurity = ctypes.windll.advapi32.GetFileSecurityW
GetFileSecurity.restype = wintypes.BOOL
GetFileSecurity.argtypes = [
    wintypes.LPCWSTR,      # File Name (in)
    wintypes.DWORD,        # Requested Information (in)
    PSECURITY_DESCRIPTOR,  # Security Descriptor (out_opt)
    wintypes.DWORD,        # Length (in)
    LPDWORD,               # Length Needed (out)
]

"""
MSDN windows/desktop/aa446651

The GetSecurityDescriptorOwner function retrieves the owner information 
from a security descriptor.
"""
GetSecurityDescriptorOwner = ctypes.windll.advapi32.GetSecurityDescriptorOwner
GetSecurityDescriptorOwner.restype = wintypes.BOOL
GetSecurityDescriptorOwner.argtypes = [
    PSECURITY_DESCRIPTOR,  # Security Descriptor (in)
    ctypes.POINTER(PSID),  # Owner (out)
    LPBOOL,                # Owner Exists (out)
]

"""
MSDN windows/desktop/aa379166

The LookupAccountSid function accepts a security identifier (SID) as input. 
It retrieves the name of the account for this SID and the name of the first 
domain on which this SID is found.
"""
LookupAccountSid = ctypes.windll.advapi32.LookupAccountSidW
LookupAccountSid.restype = wintypes.BOOL
LookupAccountSid.argtypes = [
    wintypes.LPCWSTR, # System Name (in)
    PSID,             # SID (in)
    wintypes.LPCWSTR, # Name (out)
    LPDWORD,          # Name Size (inout)
    wintypes.LPCWSTR, # Domain(out_opt)
    LPDWORD,          # Domain Size (inout)
    LPDWORD,          # SID Type (out)
]

def get_file_security_descriptor(filename, request):
    """
    Get the file security descriptor for the 
    specified file and request
    
    :return: Security Descriptor
    """
    length = wintypes.DWORD()
    GetFileSecurity(filename, request, None, 0, ctypes.byref(length))

    if length.value:
        sd = (wintypes.BYTE * length.value)()
        if GetFileSecurity(filename, request, sd, length, 
                            ctypes.byref(length)):
            return sd

def get_security_descriptor_owner(sd):
    """
    Get the owner of the specified security 
    descriptor
    
    :return: Security Identifier
    """
    if sd is not None:
        sid = PSID()
        sid_defaulted = wintypes.BOOL()

        if GetSecurityDescriptorOwner(sd, ctypes.byref(sid), 
                                       ctypes.byref(sid_defaulted)):
            return sid

def look_up_account_sid(sid):
    """
    Lookup the account details for the
    specified Security Identifier
    
    :return: (name, domain, SID type)
    """
    if sid is not None:
        SIZE = 256
        name = ctypes.create_unicode_buffer(SIZE)
        domain = ctypes.create_unicode_buffer(SIZE) 
        cch_name = wintypes.DWORD(SIZE)
        cch_domain = wintypes.DWORD(SIZE)
        sid_type = wintypes.DWORD()

        if LookupAccountSid(None, sid, name, ctypes.byref(cch_name),
                             domain, ctypes.byref(cch_domain),
                             ctypes.byref(sid_type)):
            return name.value, domain.value, sid_type.value

    return None, None, None


def get_owner(filename):
    """
    Retrieve the current owner of the specified file
    """
    # get the file security descriptor:
    request = OWNER_SECURITY_INFORMATION
    sd = get_file_security_descriptor(filename, request)
    
    # get the security identifier for the
    # owner of the descriptor
    sid = get_security_descriptor_owner(sd)
    
    # finally, get the account name in the
    # security identifier!
    name, _, _ = look_up_account_sid(sid)
    
    return name
