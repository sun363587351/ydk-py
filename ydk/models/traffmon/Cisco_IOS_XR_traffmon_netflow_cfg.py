""" Cisco_IOS_XR_traffmon_netflow_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR traffmon\-netflow package configuration.

This module contains definitions
for the following management objects\:
  net\-flow\: NetFlow Configuration

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class NfCacheAgingModeEnum(Enum):
    """
    NfCacheAgingModeEnum

    Nf cache aging mode

    .. data:: NORMAL = 0

    	Normal, caches age

    .. data:: PERMANENT = 1

    	Permanent, caches never age

    """

    NORMAL = 0

    PERMANENT = 1


    @staticmethod
    def _meta_info():
        from ydk.models.traffmon._meta import _Cisco_IOS_XR_traffmon_netflow_cfg as meta
        return meta._meta_table['NfCacheAgingModeEnum']


class NfSamplingModeEnum(Enum):
    """
    NfSamplingModeEnum

    Nf sampling mode

    .. data:: RANDOM = 2

    	Random sampling

    """

    RANDOM = 2


    @staticmethod
    def _meta_info():
        from ydk.models.traffmon._meta import _Cisco_IOS_XR_traffmon_netflow_cfg as meta
        return meta._meta_table['NfSamplingModeEnum']



class NetFlow(object):
    """
    NetFlow Configuration
    
    .. attribute:: flow_exporter_maps
    
    	Configure a flow exporter map
    	**type**\: :py:class:`FlowExporterMaps <ydk.models.traffmon.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowExporterMaps>`
    
    .. attribute:: flow_monitor_map_performance_table
    
    	Configure a performance traffic flow monitor map
    	**type**\: :py:class:`FlowMonitorMapPerformanceTable <ydk.models.traffmon.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapPerformanceTable>`
    
    .. attribute:: flow_monitor_map_table
    
    	Flow monitor map configuration
    	**type**\: :py:class:`FlowMonitorMapTable <ydk.models.traffmon.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapTable>`
    
    .. attribute:: flow_sampler_maps
    
    	Flow sampler map configuration
    	**type**\: :py:class:`FlowSamplerMaps <ydk.models.traffmon.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowSamplerMaps>`
    
    

    """

    _prefix = 'traffmon-netflow-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.flow_exporter_maps = NetFlow.FlowExporterMaps()
        self.flow_exporter_maps.parent = self
        self.flow_monitor_map_performance_table = NetFlow.FlowMonitorMapPerformanceTable()
        self.flow_monitor_map_performance_table.parent = self
        self.flow_monitor_map_table = NetFlow.FlowMonitorMapTable()
        self.flow_monitor_map_table.parent = self
        self.flow_sampler_maps = NetFlow.FlowSamplerMaps()
        self.flow_sampler_maps.parent = self


    class FlowExporterMaps(object):
        """
        Configure a flow exporter map
        
        .. attribute:: flow_exporter_map
        
        	Exporter map name
        	**type**\: list of :py:class:`FlowExporterMap <ydk.models.traffmon.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowExporterMaps.FlowExporterMap>`
        
        

        """

        _prefix = 'traffmon-netflow-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.flow_exporter_map = YList()
            self.flow_exporter_map.parent = self
            self.flow_exporter_map.name = 'flow_exporter_map'


        class FlowExporterMap(object):
            """
            Exporter map name
            
            .. attribute:: exporter_map_name
            
            	Exporter map name
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: destination
            
            	Configure export destination (collector)
            	**type**\: :py:class:`Destination <ydk.models.traffmon.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowExporterMaps.FlowExporterMap.Destination>`
            
            .. attribute:: dscp
            
            	Specify DSCP value for export packets
            	**type**\: int
            
            	**range:** 0..63
            
            .. attribute:: source_interface
            
            	Configure source interface for collector
            	**type**\: str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: udp
            
            	Use UDP as transport protocol
            	**type**\: :py:class:`Udp <ydk.models.traffmon.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowExporterMaps.FlowExporterMap.Udp>`
            
            .. attribute:: versions
            
            	Specify export version parameters
            	**type**\: :py:class:`Versions <ydk.models.traffmon.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowExporterMaps.FlowExporterMap.Versions>`
            
            

            """

            _prefix = 'traffmon-netflow-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.exporter_map_name = None
                self.destination = NetFlow.FlowExporterMaps.FlowExporterMap.Destination()
                self.destination.parent = self
                self.dscp = None
                self.source_interface = None
                self.udp = NetFlow.FlowExporterMaps.FlowExporterMap.Udp()
                self.udp.parent = self
                self.versions = NetFlow.FlowExporterMaps.FlowExporterMap.Versions()
                self.versions.parent = self


            class Destination(object):
                """
                Configure export destination (collector)
                
                .. attribute:: ip_address
                
                	Destination IPv4 address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6_address
                
                	IPV6 address of the tunnel destination
                	**type**\: str
                
                .. attribute:: vrf_name
                
                	VRF name
                	**type**\: str
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ip_address = None
                    self.ipv6_address = None
                    self.vrf_name = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-traffmon-netflow-cfg:destination'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.ip_address is not None:
                        return True

                    if self.ipv6_address is not None:
                        return True

                    if self.vrf_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.traffmon._meta import _Cisco_IOS_XR_traffmon_netflow_cfg as meta
                    return meta._meta_table['NetFlow.FlowExporterMaps.FlowExporterMap.Destination']['meta_info']


            class Udp(object):
                """
                Use UDP as transport protocol
                
                .. attribute:: destination_port
                
                	Configure Destination UDP port
                	**type**\: int
                
                	**range:** 1024..65535
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.destination_port = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-traffmon-netflow-cfg:udp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.destination_port is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.traffmon._meta import _Cisco_IOS_XR_traffmon_netflow_cfg as meta
                    return meta._meta_table['NetFlow.FlowExporterMaps.FlowExporterMap.Udp']['meta_info']


            class Versions(object):
                """
                Specify export version parameters
                
                .. attribute:: version
                
                	Configure export version options
                	**type**\: list of :py:class:`Version <ydk.models.traffmon.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version>`
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.version = YList()
                    self.version.parent = self
                    self.version.name = 'version'


                class Version(object):
                    """
                    Configure export version options
                    
                    .. attribute:: version_number
                    
                    	Export version number
                    	**type**\: int
                    
                    	**range:** 9..10
                    
                    .. attribute:: common_template_timeout
                    
                    	Specify custom timeout for the template
                    	**type**\: int
                    
                    	**range:** 1..604800
                    
                    .. attribute:: data_template_timeout
                    
                    	Data template configuration options
                    	**type**\: int
                    
                    	**range:** 1..604800
                    
                    .. attribute:: options
                    
                    	Specify options for exporting templates
                    	**type**\: :py:class:`Options <ydk.models.traffmon.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version.Options>`
                    
                    .. attribute:: options_template_timeout
                    
                    	Option template configuration options
                    	**type**\: int
                    
                    	**range:** 1..604800
                    
                    

                    """

                    _prefix = 'traffmon-netflow-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.version_number = None
                        self.common_template_timeout = None
                        self.data_template_timeout = None
                        self.options = NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version.Options()
                        self.options.parent = self
                        self.options_template_timeout = None


                    class Options(object):
                        """
                        Specify options for exporting templates
                        
                        .. attribute:: interface_table_export_timeout
                        
                        	Specify timeout for exporting interface table
                        	**type**\: int
                        
                        	**range:** 0..604800
                        
                        .. attribute:: sampler_table_export_timeout
                        
                        	Specify timeout for exporting sampler table
                        	**type**\: int
                        
                        	**range:** 0..604800
                        
                        .. attribute:: vrf_table_export_timeout
                        
                        	Specify timeout for exporting vrf table
                        	**type**\: int
                        
                        	**range:** 0..604800
                        
                        

                        """

                        _prefix = 'traffmon-netflow-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.interface_table_export_timeout = None
                            self.sampler_table_export_timeout = None
                            self.vrf_table_export_timeout = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-traffmon-netflow-cfg:options'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.interface_table_export_timeout is not None:
                                return True

                            if self.sampler_table_export_timeout is not None:
                                return True

                            if self.vrf_table_export_timeout is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.traffmon._meta import _Cisco_IOS_XR_traffmon_netflow_cfg as meta
                            return meta._meta_table['NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version.Options']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.version_number is None:
                            raise YPYDataValidationError('Key property version_number is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-traffmon-netflow-cfg:version[Cisco-IOS-XR-traffmon-netflow-cfg:version-number = ' + str(self.version_number) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.version_number is not None:
                            return True

                        if self.common_template_timeout is not None:
                            return True

                        if self.data_template_timeout is not None:
                            return True

                        if self.options is not None and self.options._has_data():
                            return True

                        if self.options_template_timeout is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.traffmon._meta import _Cisco_IOS_XR_traffmon_netflow_cfg as meta
                        return meta._meta_table['NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-traffmon-netflow-cfg:versions'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.version is not None:
                        for child_ref in self.version:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.traffmon._meta import _Cisco_IOS_XR_traffmon_netflow_cfg as meta
                    return meta._meta_table['NetFlow.FlowExporterMaps.FlowExporterMap.Versions']['meta_info']

            @property
            def _common_path(self):
                if self.exporter_map_name is None:
                    raise YPYDataValidationError('Key property exporter_map_name is None')

                return '/Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/Cisco-IOS-XR-traffmon-netflow-cfg:flow-exporter-maps/Cisco-IOS-XR-traffmon-netflow-cfg:flow-exporter-map[Cisco-IOS-XR-traffmon-netflow-cfg:exporter-map-name = ' + str(self.exporter_map_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.exporter_map_name is not None:
                    return True

                if self.destination is not None and self.destination._has_data():
                    return True

                if self.dscp is not None:
                    return True

                if self.source_interface is not None:
                    return True

                if self.udp is not None and self.udp._has_data():
                    return True

                if self.versions is not None and self.versions._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.traffmon._meta import _Cisco_IOS_XR_traffmon_netflow_cfg as meta
                return meta._meta_table['NetFlow.FlowExporterMaps.FlowExporterMap']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/Cisco-IOS-XR-traffmon-netflow-cfg:flow-exporter-maps'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.flow_exporter_map is not None:
                for child_ref in self.flow_exporter_map:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.traffmon._meta import _Cisco_IOS_XR_traffmon_netflow_cfg as meta
            return meta._meta_table['NetFlow.FlowExporterMaps']['meta_info']


    class FlowMonitorMapPerformanceTable(object):
        """
        Configure a performance traffic flow monitor map
        
        .. attribute:: flow_monitor_map
        
        	Monitor map name
        	**type**\: list of :py:class:`FlowMonitorMap <ydk.models.traffmon.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap>`
        
        

        """

        _prefix = 'traffmon-netflow-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.flow_monitor_map = YList()
            self.flow_monitor_map.parent = self
            self.flow_monitor_map.name = 'flow_monitor_map'


        class FlowMonitorMap(object):
            """
            Monitor map name
            
            .. attribute:: monitor_map_name
            
            	Monitor map name
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: cache_active_aging_timeout
            
            	Specify the active flow cache aging timeout
            	**type**\: int
            
            	**range:** 1..604800
            
            .. attribute:: cache_aging_mode
            
            	Specify the flow cache aging mode
            	**type**\: :py:class:`NfCacheAgingModeEnum <ydk.models.traffmon.Cisco_IOS_XR_traffmon_netflow_cfg.NfCacheAgingModeEnum>`
            
            .. attribute:: cache_entries
            
            	Specify the number of entries in the flow cache
            	**type**\: int
            
            	**range:** 4096..1000000
            
            .. attribute:: cache_inactive_aging_timeout
            
            	Specify the inactive flow cache aging timeout
            	**type**\: int
            
            	**range:** 0..604800
            
            .. attribute:: cache_timeout_rate_limit
            
            	Specify the maximum number of entries to age each second
            	**type**\: int
            
            	**range:** 1..1000000
            
            .. attribute:: cache_update_aging_timeout
            
            	Specify the update flow cache aging timeout
            	**type**\: int
            
            	**range:** 1..604800
            
            .. attribute:: exporters
            
            	Configure exporters to be used by the monitor\-map
            	**type**\: :py:class:`Exporters <ydk.models.traffmon.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters>`
            
            .. attribute:: option
            
            	Specify an option for the flow cache
            	**type**\: :py:class:`Option <ydk.models.traffmon.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Option>`
            
            .. attribute:: record
            
            	Specify a flow record format
            	**type**\: :py:class:`Record <ydk.models.traffmon.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Record>`
            
            

            """

            _prefix = 'traffmon-netflow-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.monitor_map_name = None
                self.cache_active_aging_timeout = None
                self.cache_aging_mode = None
                self.cache_entries = None
                self.cache_inactive_aging_timeout = None
                self.cache_timeout_rate_limit = None
                self.cache_update_aging_timeout = None
                self.exporters = NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters()
                self.exporters.parent = self
                self.option = NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Option()
                self.option.parent = self
                self.record = None


            class Exporters(object):
                """
                Configure exporters to be used by the
                monitor\-map
                
                .. attribute:: exporter
                
                	Configure exporter to be used by the monitor\-map
                	**type**\: list of :py:class:`Exporter <ydk.models.traffmon.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters.Exporter>`
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.exporter = YList()
                    self.exporter.parent = self
                    self.exporter.name = 'exporter'


                class Exporter(object):
                    """
                    Configure exporter to be used by the
                    monitor\-map
                    
                    .. attribute:: exporter_name
                    
                    	Exporter name
                    	**type**\: str
                    
                    	**range:** 0..32
                    
                    

                    """

                    _prefix = 'traffmon-netflow-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.exporter_name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.exporter_name is None:
                            raise YPYDataValidationError('Key property exporter_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-traffmon-netflow-cfg:exporter[Cisco-IOS-XR-traffmon-netflow-cfg:exporter-name = ' + str(self.exporter_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.exporter_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.traffmon._meta import _Cisco_IOS_XR_traffmon_netflow_cfg as meta
                        return meta._meta_table['NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters.Exporter']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-traffmon-netflow-cfg:exporters'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.exporter is not None:
                        for child_ref in self.exporter:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.traffmon._meta import _Cisco_IOS_XR_traffmon_netflow_cfg as meta
                    return meta._meta_table['NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters']['meta_info']


            class Option(object):
                """
                Specify an option for the flow cache
                
                .. attribute:: filtered
                
                	Specify whether data should be filtered
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: out_phys_int
                
                	Specify whether it exports the physical output interface
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.filtered = None
                    self.out_phys_int = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-traffmon-netflow-cfg:option'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.filtered is not None:
                        return True

                    if self.out_phys_int is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.traffmon._meta import _Cisco_IOS_XR_traffmon_netflow_cfg as meta
                    return meta._meta_table['NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Option']['meta_info']


            class Record(object):
                """
                Specify a flow record format
                
                .. attribute:: label
                
                	Enter label value for MPLS record type
                	**type**\: int
                
                	**range:** 1..6
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                .. attribute:: record_name
                
                	Flow record format (Either 'ipv4\-raw' ,'ipv4\-peer\-as', 'ipv6', 'mpls', 'mpls\-ipv4', 'mpls\-ipv6', 'mpls\-ipv4\-ipv6', 'ipv6\-peer\-as')
                	**type**\: str
                
                	**range:** 0..32
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.label = None
                    self.record_name = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-traffmon-netflow-cfg:record'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.label is not None:
                        return True

                    if self.record_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.traffmon._meta import _Cisco_IOS_XR_traffmon_netflow_cfg as meta
                    return meta._meta_table['NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Record']['meta_info']

            @property
            def _common_path(self):
                if self.monitor_map_name is None:
                    raise YPYDataValidationError('Key property monitor_map_name is None')

                return '/Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/Cisco-IOS-XR-traffmon-netflow-cfg:flow-monitor-map-performance-table/Cisco-IOS-XR-traffmon-netflow-cfg:flow-monitor-map[Cisco-IOS-XR-traffmon-netflow-cfg:monitor-map-name = ' + str(self.monitor_map_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.monitor_map_name is not None:
                    return True

                if self.cache_active_aging_timeout is not None:
                    return True

                if self.cache_aging_mode is not None:
                    return True

                if self.cache_entries is not None:
                    return True

                if self.cache_inactive_aging_timeout is not None:
                    return True

                if self.cache_timeout_rate_limit is not None:
                    return True

                if self.cache_update_aging_timeout is not None:
                    return True

                if self.exporters is not None and self.exporters._has_data():
                    return True

                if self.option is not None and self.option._has_data():
                    return True

                if self.record is not None and self.record._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.traffmon._meta import _Cisco_IOS_XR_traffmon_netflow_cfg as meta
                return meta._meta_table['NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/Cisco-IOS-XR-traffmon-netflow-cfg:flow-monitor-map-performance-table'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.flow_monitor_map is not None:
                for child_ref in self.flow_monitor_map:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.traffmon._meta import _Cisco_IOS_XR_traffmon_netflow_cfg as meta
            return meta._meta_table['NetFlow.FlowMonitorMapPerformanceTable']['meta_info']


    class FlowMonitorMapTable(object):
        """
        Flow monitor map configuration
        
        .. attribute:: flow_monitor_map
        
        	Monitor map name
        	**type**\: list of :py:class:`FlowMonitorMap <ydk.models.traffmon.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapTable.FlowMonitorMap>`
        
        

        """

        _prefix = 'traffmon-netflow-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.flow_monitor_map = YList()
            self.flow_monitor_map.parent = self
            self.flow_monitor_map.name = 'flow_monitor_map'


        class FlowMonitorMap(object):
            """
            Monitor map name
            
            .. attribute:: monitor_map_name
            
            	Monitor map name
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: cache_active_aging_timeout
            
            	Specify the active flow cache aging timeout
            	**type**\: int
            
            	**range:** 1..604800
            
            .. attribute:: cache_aging_mode
            
            	Specify the flow cache aging mode
            	**type**\: :py:class:`NfCacheAgingModeEnum <ydk.models.traffmon.Cisco_IOS_XR_traffmon_netflow_cfg.NfCacheAgingModeEnum>`
            
            .. attribute:: cache_entries
            
            	Specify the number of entries in the flow cache
            	**type**\: int
            
            	**range:** 4096..1000000
            
            .. attribute:: cache_inactive_aging_timeout
            
            	Specify the inactive flow cache aging timeout
            	**type**\: int
            
            	**range:** 0..604800
            
            .. attribute:: cache_timeout_rate_limit
            
            	Specify the maximum number of entries to age each second
            	**type**\: int
            
            	**range:** 1..1000000
            
            .. attribute:: cache_update_aging_timeout
            
            	Specify the update flow cache aging timeout
            	**type**\: int
            
            	**range:** 1..604800
            
            .. attribute:: exporters
            
            	Configure exporters to be used by the monitor\-map
            	**type**\: :py:class:`Exporters <ydk.models.traffmon.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters>`
            
            .. attribute:: option
            
            	Specify an option for the flow cache
            	**type**\: :py:class:`Option <ydk.models.traffmon.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapTable.FlowMonitorMap.Option>`
            
            .. attribute:: record
            
            	Specify a flow record format
            	**type**\: :py:class:`Record <ydk.models.traffmon.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapTable.FlowMonitorMap.Record>`
            
            

            """

            _prefix = 'traffmon-netflow-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.monitor_map_name = None
                self.cache_active_aging_timeout = None
                self.cache_aging_mode = None
                self.cache_entries = None
                self.cache_inactive_aging_timeout = None
                self.cache_timeout_rate_limit = None
                self.cache_update_aging_timeout = None
                self.exporters = NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters()
                self.exporters.parent = self
                self.option = NetFlow.FlowMonitorMapTable.FlowMonitorMap.Option()
                self.option.parent = self
                self.record = None


            class Exporters(object):
                """
                Configure exporters to be used by the
                monitor\-map
                
                .. attribute:: exporter
                
                	Configure exporter to be used by the monitor\-map
                	**type**\: list of :py:class:`Exporter <ydk.models.traffmon.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters.Exporter>`
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.exporter = YList()
                    self.exporter.parent = self
                    self.exporter.name = 'exporter'


                class Exporter(object):
                    """
                    Configure exporter to be used by the
                    monitor\-map
                    
                    .. attribute:: exporter_name
                    
                    	Exporter name
                    	**type**\: str
                    
                    	**range:** 0..32
                    
                    

                    """

                    _prefix = 'traffmon-netflow-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.exporter_name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.exporter_name is None:
                            raise YPYDataValidationError('Key property exporter_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-traffmon-netflow-cfg:exporter[Cisco-IOS-XR-traffmon-netflow-cfg:exporter-name = ' + str(self.exporter_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.exporter_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.traffmon._meta import _Cisco_IOS_XR_traffmon_netflow_cfg as meta
                        return meta._meta_table['NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters.Exporter']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-traffmon-netflow-cfg:exporters'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.exporter is not None:
                        for child_ref in self.exporter:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.traffmon._meta import _Cisco_IOS_XR_traffmon_netflow_cfg as meta
                    return meta._meta_table['NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters']['meta_info']


            class Option(object):
                """
                Specify an option for the flow cache
                
                .. attribute:: filtered
                
                	Specify whether data should be filtered
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: out_phys_int
                
                	Specify whether it exports the physical output interface
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.filtered = None
                    self.out_phys_int = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-traffmon-netflow-cfg:option'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.filtered is not None:
                        return True

                    if self.out_phys_int is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.traffmon._meta import _Cisco_IOS_XR_traffmon_netflow_cfg as meta
                    return meta._meta_table['NetFlow.FlowMonitorMapTable.FlowMonitorMap.Option']['meta_info']


            class Record(object):
                """
                Specify a flow record format
                
                .. attribute:: label
                
                	Enter label value for MPLS record type
                	**type**\: int
                
                	**range:** 1..6
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                .. attribute:: record_name
                
                	Flow record format (Either 'ipv4\-raw' ,'ipv4\-peer\-as', 'ipv6', 'mpls', 'mpls\-ipv4', 'mpls\-ipv6', 'mpls\-ipv4\-ipv6', 'ipv6\-peer\-as')
                	**type**\: str
                
                	**range:** 0..32
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.label = None
                    self.record_name = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-traffmon-netflow-cfg:record'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.label is not None:
                        return True

                    if self.record_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.traffmon._meta import _Cisco_IOS_XR_traffmon_netflow_cfg as meta
                    return meta._meta_table['NetFlow.FlowMonitorMapTable.FlowMonitorMap.Record']['meta_info']

            @property
            def _common_path(self):
                if self.monitor_map_name is None:
                    raise YPYDataValidationError('Key property monitor_map_name is None')

                return '/Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/Cisco-IOS-XR-traffmon-netflow-cfg:flow-monitor-map-table/Cisco-IOS-XR-traffmon-netflow-cfg:flow-monitor-map[Cisco-IOS-XR-traffmon-netflow-cfg:monitor-map-name = ' + str(self.monitor_map_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.monitor_map_name is not None:
                    return True

                if self.cache_active_aging_timeout is not None:
                    return True

                if self.cache_aging_mode is not None:
                    return True

                if self.cache_entries is not None:
                    return True

                if self.cache_inactive_aging_timeout is not None:
                    return True

                if self.cache_timeout_rate_limit is not None:
                    return True

                if self.cache_update_aging_timeout is not None:
                    return True

                if self.exporters is not None and self.exporters._has_data():
                    return True

                if self.option is not None and self.option._has_data():
                    return True

                if self.record is not None and self.record._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.traffmon._meta import _Cisco_IOS_XR_traffmon_netflow_cfg as meta
                return meta._meta_table['NetFlow.FlowMonitorMapTable.FlowMonitorMap']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/Cisco-IOS-XR-traffmon-netflow-cfg:flow-monitor-map-table'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.flow_monitor_map is not None:
                for child_ref in self.flow_monitor_map:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.traffmon._meta import _Cisco_IOS_XR_traffmon_netflow_cfg as meta
            return meta._meta_table['NetFlow.FlowMonitorMapTable']['meta_info']


    class FlowSamplerMaps(object):
        """
        Flow sampler map configuration
        
        .. attribute:: flow_sampler_map
        
        	Sampler map name
        	**type**\: list of :py:class:`FlowSamplerMap <ydk.models.traffmon.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowSamplerMaps.FlowSamplerMap>`
        
        

        """

        _prefix = 'traffmon-netflow-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.flow_sampler_map = YList()
            self.flow_sampler_map.parent = self
            self.flow_sampler_map.name = 'flow_sampler_map'


        class FlowSamplerMap(object):
            """
            Sampler map name
            
            .. attribute:: sampler_map_name
            
            	Sampler map name
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: sampling_modes
            
            	Configure packet sampling mode
            	**type**\: :py:class:`SamplingModes <ydk.models.traffmon.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes>`
            
            

            """

            _prefix = 'traffmon-netflow-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.sampler_map_name = None
                self.sampling_modes = NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes()
                self.sampling_modes.parent = self


            class SamplingModes(object):
                """
                Configure packet sampling mode
                
                .. attribute:: sampling_mode
                
                	Configure sampling mode
                	**type**\: list of :py:class:`SamplingMode <ydk.models.traffmon.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes.SamplingMode>`
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.sampling_mode = YList()
                    self.sampling_mode.parent = self
                    self.sampling_mode.name = 'sampling_mode'


                class SamplingMode(object):
                    """
                    Configure sampling mode
                    
                    .. attribute:: mode
                    
                    	Sampling mode
                    	**type**\: :py:class:`NfSamplingModeEnum <ydk.models.traffmon.Cisco_IOS_XR_traffmon_netflow_cfg.NfSamplingModeEnum>`
                    
                    .. attribute:: interval
                    
                    	Sampling interval in units of packets
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: sample_number
                    
                    	Number of packets to be sampled in the sampling interval
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'traffmon-netflow-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.mode = None
                        self.interval = None
                        self.sample_number = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.mode is None:
                            raise YPYDataValidationError('Key property mode is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-traffmon-netflow-cfg:sampling-mode[Cisco-IOS-XR-traffmon-netflow-cfg:mode = ' + str(self.mode) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.mode is not None:
                            return True

                        if self.interval is not None:
                            return True

                        if self.sample_number is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.traffmon._meta import _Cisco_IOS_XR_traffmon_netflow_cfg as meta
                        return meta._meta_table['NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes.SamplingMode']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-traffmon-netflow-cfg:sampling-modes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.sampling_mode is not None:
                        for child_ref in self.sampling_mode:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.traffmon._meta import _Cisco_IOS_XR_traffmon_netflow_cfg as meta
                    return meta._meta_table['NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes']['meta_info']

            @property
            def _common_path(self):
                if self.sampler_map_name is None:
                    raise YPYDataValidationError('Key property sampler_map_name is None')

                return '/Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/Cisco-IOS-XR-traffmon-netflow-cfg:flow-sampler-maps/Cisco-IOS-XR-traffmon-netflow-cfg:flow-sampler-map[Cisco-IOS-XR-traffmon-netflow-cfg:sampler-map-name = ' + str(self.sampler_map_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.sampler_map_name is not None:
                    return True

                if self.sampling_modes is not None and self.sampling_modes._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.traffmon._meta import _Cisco_IOS_XR_traffmon_netflow_cfg as meta
                return meta._meta_table['NetFlow.FlowSamplerMaps.FlowSamplerMap']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/Cisco-IOS-XR-traffmon-netflow-cfg:flow-sampler-maps'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.flow_sampler_map is not None:
                for child_ref in self.flow_sampler_map:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.traffmon._meta import _Cisco_IOS_XR_traffmon_netflow_cfg as meta
            return meta._meta_table['NetFlow.FlowSamplerMaps']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-traffmon-netflow-cfg:net-flow'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.flow_exporter_maps is not None and self.flow_exporter_maps._has_data():
            return True

        if self.flow_monitor_map_performance_table is not None and self.flow_monitor_map_performance_table._has_data():
            return True

        if self.flow_monitor_map_table is not None and self.flow_monitor_map_table._has_data():
            return True

        if self.flow_sampler_maps is not None and self.flow_sampler_maps._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.traffmon._meta import _Cisco_IOS_XR_traffmon_netflow_cfg as meta
        return meta._meta_table['NetFlow']['meta_info']


