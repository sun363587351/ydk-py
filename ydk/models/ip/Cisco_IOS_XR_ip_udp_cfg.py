""" Cisco_IOS_XR_ip_udp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-udp package configuration.

This module contains definitions
for the following management objects\:
  ip\-udp\: Global IP UDP configuration

This YANG module augments the
  Cisco\-IOS\-XR\-ip\-tcp\-cfg
module with configuration data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class IpUdp(object):
    """
    Global IP UDP configuration
    
    .. attribute:: directory
    
    	UDP directory details
    	**type**\: :py:class:`Directory <ydk.models.ip.Cisco_IOS_XR_ip_udp_cfg.IpUdp.Directory>`
    
    .. attribute:: num_thread
    
    	UDP InQueue and OutQueue threads
    	**type**\: :py:class:`NumThread <ydk.models.ip.Cisco_IOS_XR_ip_udp_cfg.IpUdp.NumThread>`
    
    .. attribute:: receive_q
    
    	UDP receive Queue Size
    	**type**\: int
    
    	**range:** 40..800
    
    

    """

    _prefix = 'ip-udp-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.directory = None
        self.num_thread = None
        self.receive_q = None


    class Directory(object):
        """
        UDP directory details
        
        .. attribute:: directoryname
        
        	Directory name
        	**type**\: str
        
        .. attribute:: max_file_size_files
        
        	Set size of debug files in bytes
        	**type**\: int
        
        	**range:** 1024..4294967295
        
        .. attribute:: max_udp_debug_files
        
        	Set number of Debug files
        	**type**\: int
        
        	**range:** 1..5000
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ip-udp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.directoryname = None
            self.max_file_size_files = None
            self.max_udp_debug_files = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-udp-cfg:ip-udp/Cisco-IOS-XR-ip-udp-cfg:directory'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.directoryname is not None:
                return True

            if self.max_file_size_files is not None:
                return True

            if self.max_udp_debug_files is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return True

        @staticmethod
        def _meta_info():
            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_cfg as meta
            return meta._meta_table['IpUdp.Directory']['meta_info']


    class NumThread(object):
        """
        UDP InQueue and OutQueue threads
        
        .. attribute:: udp_in_q_threads
        
        	InQ Threads
        	**type**\: int
        
        	**range:** 1..16
        
        .. attribute:: udp_out_q_threads
        
        	OutQ Threads
        	**type**\: int
        
        	**range:** 1..16
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ip-udp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.udp_in_q_threads = None
            self.udp_out_q_threads = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-udp-cfg:ip-udp/Cisco-IOS-XR-ip-udp-cfg:num-thread'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.udp_in_q_threads is not None:
                return True

            if self.udp_out_q_threads is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return True

        @staticmethod
        def _meta_info():
            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_cfg as meta
            return meta._meta_table['IpUdp.NumThread']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-udp-cfg:ip-udp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.directory is not None and self.directory._has_data():
            return True

        if self.directory is not None and self.directory.is_presence():
            return True

        if self.num_thread is not None and self.num_thread._has_data():
            return True

        if self.num_thread is not None and self.num_thread.is_presence():
            return True

        if self.receive_q is not None:
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_udp_cfg as meta
        return meta._meta_table['IpUdp']['meta_info']

