


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'LogErrorEnum' : _MetaInfoEnum('LogErrorEnum', 'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper',
        {
            'unknown':'UNKNOWN',
            'log-message-error':'LOG_MESSAGE_ERROR',
            'get-issuer-name-failed':'GET_ISSUER_NAME_FAILED',
        }, 'Cisco-IOS-XR-crypto-sam-oper', _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper']),
    'LogCodeEnum' : _MetaInfoEnum('LogCodeEnum', 'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper',
        {
            'unknown':'UNKNOWN',
            'sam-server-restared-router-reboot':'SAM_SERVER_RESTARED_ROUTER_REBOOT',
            'sam-server-restared':'SAM_SERVER_RESTARED',
            'added-certificate-in-table':'ADDED_CERTIFICATE_IN_TABLE',
            'copied-certificate-in-table':'COPIED_CERTIFICATE_IN_TABLE',
            'certificate-flag-changed':'CERTIFICATE_FLAG_CHANGED',
            'validated-certificate':'VALIDATED_CERTIFICATE',
            'certificate-expired-detected':'CERTIFICATE_EXPIRED_DETECTED',
            'certificate-revoked-detected':'CERTIFICATE_REVOKED_DETECTED',
            'ca-certificate-expired-detected':'CA_CERTIFICATE_EXPIRED_DETECTED',
            'ca-certificate-revoked-detected':'CA_CERTIFICATE_REVOKED_DETECTED',
            'deleted-certificate-from-table':'DELETED_CERTIFICATE_FROM_TABLE',
            'crl-added-updated-in-table':'CRL_ADDED_UPDATED_IN_TABLE',
            'checked-memory-digest':'CHECKED_MEMORY_DIGEST',
            'nvram-digest-mismatch-detected':'NVRAM_DIGEST_MISMATCH_DETECTED',
            'insecure-backup-file-detected':'INSECURE_BACKUP_FILE_DETECTED',
            'error-restore-operation':'ERROR_RESTORE_OPERATION',
            'backup-file-on-nvram-deleted':'BACKUP_FILE_ON_NVRAM_DELETED',
            'sam-log-file-recovered-from-system-database':'SAM_LOG_FILE_RECOVERED_FROM_SYSTEM_DATABASE',
            'validated-elf':'VALIDATED_ELF',
            'namespace-deleted-recovered-by-sam':'NAMESPACE_DELETED_RECOVERED_BY_SAM',
        }, 'Cisco-IOS-XR-crypto-sam-oper', _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper']),
    'CertificateIssuerEnum' : _MetaInfoEnum('CertificateIssuerEnum', 'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper',
        {
            'unknown':'UNKNOWN',
            'code-signing-server-certificate-authority':'CODE_SIGNING_SERVER_CERTIFICATE_AUTHORITY',
        }, 'Cisco-IOS-XR-crypto-sam-oper', _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper']),
    'LogTablesEnum' : _MetaInfoEnum('LogTablesEnum', 'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper',
        {
            'unkown':'UNKOWN',
            'memory-digest-table':'MEMORY_DIGEST_TABLE',
            'system-database-digest':'SYSTEM_DATABASE_DIGEST',
            'sam-tables':'SAM_TABLES',
        }, 'Cisco-IOS-XR-crypto-sam-oper', _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper']),
    'Sam.CertificateRevocationListSummary.Issuer' : {
        'meta_info' : _MetaInfoClass('Sam.CertificateRevocationListSummary.Issuer',
            False, 
            [
            _MetaInfoClassMember('common-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Common name
                ''',
                'common_name',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('country', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Country
                ''',
                'country',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('organization', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Organization
                ''',
                'organization',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'issuer',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.CertificateRevocationListSummary' : {
        'meta_info' : _MetaInfoClass('Sam.CertificateRevocationListSummary',
            False, 
            [
            _MetaInfoClassMember('crl-index', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                 CRL index
                ''',
                'crl_index',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('issuer', REFERENCE_CLASS, 'Issuer' , 'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper', 'Sam.CertificateRevocationListSummary.Issuer', 
                [], [], 
                '''                Issuer name
                ''',
                'issuer',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('updates', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Updated time of CRL is displayed
                ''',
                'updates',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'certificate-revocation-list-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail.Issuer' : {
        'meta_info' : _MetaInfoClass('Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail.Issuer',
            False, 
            [
            _MetaInfoClassMember('common-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Common name
                ''',
                'common_name',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('country', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Country
                ''',
                'country',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('organization', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Organization
                ''',
                'organization',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'issuer',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail' : {
        'meta_info' : _MetaInfoClass('Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail',
            False, 
            [
            _MetaInfoClassMember('crl-index', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                 CRL index
                ''',
                'crl_index',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('issuer', REFERENCE_CLASS, 'Issuer' , 'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper', 'Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail.Issuer', 
                [], [], 
                '''                Issuer name
                ''',
                'issuer',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('updates', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Updated time of CRL is displayed
                ''',
                'updates',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'certificate-revocation-list-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.CertificateRevocations.CertificateRevocation' : {
        'meta_info' : _MetaInfoClass('Sam.CertificateRevocations.CertificateRevocation',
            False, 
            [
            _MetaInfoClassMember('crl-index', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                CRL index
                ''',
                'crl_index',
                'Cisco-IOS-XR-crypto-sam-oper', True),
            _MetaInfoClassMember('certificate-revocation-list-detail', REFERENCE_CLASS, 'CertificateRevocationListDetail' , 'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper', 'Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail', 
                [], [], 
                '''                Certificate revocation list detail information
                ''',
                'certificate_revocation_list_detail',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'certificate-revocation',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.CertificateRevocations' : {
        'meta_info' : _MetaInfoClass('Sam.CertificateRevocations',
            False, 
            [
            _MetaInfoClassMember('certificate-revocation', REFERENCE_LIST, 'CertificateRevocation' , 'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper', 'Sam.CertificateRevocations.CertificateRevocation', 
                [], [], 
                '''                Certificate revocation list index information
                ''',
                'certificate_revocation',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'certificate-revocations',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.Devices.Device.Certificate.Brief.CertificateFlags' : {
        'meta_info' : _MetaInfoClass('Sam.Devices.Device.Certificate.Brief.CertificateFlags',
            False, 
            [
            _MetaInfoClassMember('is-expired', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Expired flag
                ''',
                'is_expired',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('is-revoked', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Revoked flag
                ''',
                'is_revoked',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('is-trusted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Trusted flag
                ''',
                'is_trusted',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('is-validated', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Validated flag
                ''',
                'is_validated',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'certificate-flags',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.Devices.Device.Certificate.Brief' : {
        'meta_info' : _MetaInfoClass('Sam.Devices.Device.Certificate.Brief',
            False, 
            [
            _MetaInfoClassMember('certificate-flags', REFERENCE_CLASS, 'CertificateFlags' , 'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper', 'Sam.Devices.Device.Certificate.Brief.CertificateFlags', 
                [], [], 
                '''                Certificate flags
                ''',
                'certificate_flags',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('certificate-index', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Certificate index
                ''',
                'certificate_index',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Certificate location
                ''',
                'location',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'brief',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail.CertificateFlags' : {
        'meta_info' : _MetaInfoClass('Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail.CertificateFlags',
            False, 
            [
            _MetaInfoClassMember('is-expired', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Expired flag
                ''',
                'is_expired',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('is-revoked', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Revoked flag
                ''',
                'is_revoked',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('is-trusted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Trusted flag
                ''',
                'is_trusted',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('is-validated', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Validated flag
                ''',
                'is_validated',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'certificate-flags',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail' : {
        'meta_info' : _MetaInfoClass('Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail',
            False, 
            [
            _MetaInfoClassMember('certificate-flags', REFERENCE_CLASS, 'CertificateFlags' , 'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper', 'Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail.CertificateFlags', 
                [], [], 
                '''                Certificate flags
                ''',
                'certificate_flags',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('certificate-index', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Certificate index
                ''',
                'certificate_index',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Certificate location
                ''',
                'location',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'detail',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex' : {
        'meta_info' : _MetaInfoClass('Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Specify certificate index
                ''',
                'index',
                'Cisco-IOS-XR-crypto-sam-oper', True),
            _MetaInfoClassMember('detail', REFERENCE_CLASS, 'Detail' , 'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper', 'Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail', 
                [], [], 
                '''                Certificate table detail information
                ''',
                'detail',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'certificate-index',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.Devices.Device.Certificate.CertificateIndexes' : {
        'meta_info' : _MetaInfoClass('Sam.Devices.Device.Certificate.CertificateIndexes',
            False, 
            [
            _MetaInfoClassMember('certificate-index', REFERENCE_LIST, 'CertificateIndex' , 'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper', 'Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex', 
                [], [], 
                '''                Certificate detail index information
                ''',
                'certificate_index',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'certificate-indexes',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.Devices.Device.Certificate' : {
        'meta_info' : _MetaInfoClass('Sam.Devices.Device.Certificate',
            False, 
            [
            _MetaInfoClassMember('brief', REFERENCE_CLASS, 'Brief' , 'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper', 'Sam.Devices.Device.Certificate.Brief', 
                [], [], 
                '''                Certificate table brief information
                ''',
                'brief',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('certificate-indexes', REFERENCE_CLASS, 'CertificateIndexes' , 'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper', 'Sam.Devices.Device.Certificate.CertificateIndexes', 
                [], [], 
                '''                Certificate detail index table information
                ''',
                'certificate_indexes',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'certificate',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.Devices.Device' : {
        'meta_info' : _MetaInfoClass('Sam.Devices.Device',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Specify device name
                ''',
                'device_name',
                'Cisco-IOS-XR-crypto-sam-oper', True),
            _MetaInfoClassMember('certificate', REFERENCE_CLASS, 'Certificate' , 'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper', 'Sam.Devices.Device.Certificate', 
                [], [], 
                '''                Certificate table information
                ''',
                'certificate',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'device',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.Devices' : {
        'meta_info' : _MetaInfoClass('Sam.Devices',
            False, 
            [
            _MetaInfoClassMember('device', REFERENCE_LIST, 'Device' , 'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper', 'Sam.Devices.Device', 
                [], [], 
                '''                Certificate table device information
                ''',
                'device',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'devices',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.LogContents.LogContent.Logs' : {
        'meta_info' : _MetaInfoClass('Sam.LogContents.LogContent.Logs',
            False, 
            [
            _MetaInfoClassMember('code', REFERENCE_ENUM_CLASS, 'LogCodeEnum' , 'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper', 'LogCodeEnum', 
                [], [], 
                '''                Log code
                ''',
                'code',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'LogErrorEnum' , 'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper', 'LogErrorEnum', 
                [], [], 
                '''                Log error message
                ''',
                'error',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Device index
                ''',
                'index',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('issuer', REFERENCE_ENUM_CLASS, 'CertificateIssuerEnum' , 'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper', 'CertificateIssuerEnum', 
                [], [], 
                '''                Issuer of the certificate
                ''',
                'issuer',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('sam-table-index', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                SAM table index
                ''',
                'sam_table_index',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('serial-no', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Serial number
                ''',
                'serial_no',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('source-device', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                source device name
                ''',
                'source_device',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('table', REFERENCE_ENUM_CLASS, 'LogTablesEnum' , 'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper', 'LogTablesEnum', 
                [], [], 
                '''                Log table information
                ''',
                'table',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('target-device', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Target device
                ''',
                'target_device',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Log time
                ''',
                'time',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('update-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last update time of the certificate
                ''',
                'update_time',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'logs',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.LogContents.LogContent' : {
        'meta_info' : _MetaInfoClass('Sam.LogContents.LogContent',
            False, 
            [
            _MetaInfoClassMember('number-of-lines', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Number of lines
                ''',
                'number_of_lines',
                'Cisco-IOS-XR-crypto-sam-oper', True),
            _MetaInfoClassMember('entries-shown', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total entries shown
                ''',
                'entries_shown',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('logs', REFERENCE_LIST, 'Logs' , 'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper', 'Sam.LogContents.LogContent.Logs', 
                [], [], 
                '''                SAM logs
                ''',
                'logs',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('total-entries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total log entries available
                ''',
                'total_entries',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'log-content',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.LogContents' : {
        'meta_info' : _MetaInfoClass('Sam.LogContents',
            False, 
            [
            _MetaInfoClassMember('log-content', REFERENCE_LIST, 'LogContent' , 'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper', 'Sam.LogContents.LogContent', 
                [], [], 
                '''                Number of lines for SAM log message
                ''',
                'log_content',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'log-contents',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.Packages.Package.CertificateFlags' : {
        'meta_info' : _MetaInfoClass('Sam.Packages.Package.CertificateFlags',
            False, 
            [
            _MetaInfoClassMember('is-expired', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Expired flag
                ''',
                'is_expired',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('is-revoked', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Revoked flag
                ''',
                'is_revoked',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('is-trusted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Trusted flag
                ''',
                'is_trusted',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('is-validated', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Validated flag
                ''',
                'is_validated',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'certificate-flags',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.Packages.Package' : {
        'meta_info' : _MetaInfoClass('Sam.Packages.Package',
            False, 
            [
            _MetaInfoClassMember('package-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Specify package name
                ''',
                'package_name',
                'Cisco-IOS-XR-crypto-sam-oper', True),
            _MetaInfoClassMember('certificate-flags', REFERENCE_CLASS, 'CertificateFlags' , 'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper', 'Sam.Packages.Package.CertificateFlags', 
                [], [], 
                '''                Certificate flags
                ''',
                'certificate_flags',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('certificate-index', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Certificate index
                ''',
                'certificate_index',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Certificate location
                ''',
                'location',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.Packages' : {
        'meta_info' : _MetaInfoClass('Sam.Packages',
            False, 
            [
            _MetaInfoClassMember('package', REFERENCE_LIST, 'Package' , 'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper', 'Sam.Packages.Package', 
                [], [], 
                '''                SAM certificate information for a specific
                package
                ''',
                'package',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'packages',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.SystemInformation' : {
        'meta_info' : _MetaInfoClass('Sam.SystemInformation',
            False, 
            [
            _MetaInfoClassMember('is-default-response', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if promptdefault response is true
                ''',
                'is_default_response',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('is-running', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if SAM status information runs
                ''',
                'is_running',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('prompt-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Prompt interval atreboot time in seconds
                ''',
                'prompt_interval',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'system-information',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam' : {
        'meta_info' : _MetaInfoClass('Sam',
            False, 
            [
            _MetaInfoClassMember('certificate-revocation-list-summary', REFERENCE_CLASS, 'CertificateRevocationListSummary' , 'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper', 'Sam.CertificateRevocationListSummary', 
                [], [], 
                '''                Certificate revocation list summary information 
                ''',
                'certificate_revocation_list_summary',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('certificate-revocations', REFERENCE_CLASS, 'CertificateRevocations' , 'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper', 'Sam.CertificateRevocations', 
                [], [], 
                '''                Certificate revocation list index table
                information
                ''',
                'certificate_revocations',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('devices', REFERENCE_CLASS, 'Devices' , 'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper', 'Sam.Devices', 
                [], [], 
                '''                Certificate device table information
                ''',
                'devices',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('log-contents', REFERENCE_CLASS, 'LogContents' , 'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper', 'Sam.LogContents', 
                [], [], 
                '''                SAM log content table information
                ''',
                'log_contents',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('packages', REFERENCE_CLASS, 'Packages' , 'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper', 'Sam.Packages', 
                [], [], 
                '''                SAM certificate information  package
                ''',
                'packages',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('system-information', REFERENCE_CLASS, 'SystemInformation' , 'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper', 'Sam.SystemInformation', 
                [], [], 
                '''                SAM system information
                ''',
                'system_information',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'sam',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.crypto.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
}
_meta_table['Sam.CertificateRevocationListSummary.Issuer']['meta_info'].parent =_meta_table['Sam.CertificateRevocationListSummary']['meta_info']
_meta_table['Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail.Issuer']['meta_info'].parent =_meta_table['Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail']['meta_info']
_meta_table['Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail']['meta_info'].parent =_meta_table['Sam.CertificateRevocations.CertificateRevocation']['meta_info']
_meta_table['Sam.CertificateRevocations.CertificateRevocation']['meta_info'].parent =_meta_table['Sam.CertificateRevocations']['meta_info']
_meta_table['Sam.Devices.Device.Certificate.Brief.CertificateFlags']['meta_info'].parent =_meta_table['Sam.Devices.Device.Certificate.Brief']['meta_info']
_meta_table['Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail.CertificateFlags']['meta_info'].parent =_meta_table['Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail']['meta_info']
_meta_table['Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail']['meta_info'].parent =_meta_table['Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex']['meta_info']
_meta_table['Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex']['meta_info'].parent =_meta_table['Sam.Devices.Device.Certificate.CertificateIndexes']['meta_info']
_meta_table['Sam.Devices.Device.Certificate.Brief']['meta_info'].parent =_meta_table['Sam.Devices.Device.Certificate']['meta_info']
_meta_table['Sam.Devices.Device.Certificate.CertificateIndexes']['meta_info'].parent =_meta_table['Sam.Devices.Device.Certificate']['meta_info']
_meta_table['Sam.Devices.Device.Certificate']['meta_info'].parent =_meta_table['Sam.Devices.Device']['meta_info']
_meta_table['Sam.Devices.Device']['meta_info'].parent =_meta_table['Sam.Devices']['meta_info']
_meta_table['Sam.LogContents.LogContent.Logs']['meta_info'].parent =_meta_table['Sam.LogContents.LogContent']['meta_info']
_meta_table['Sam.LogContents.LogContent']['meta_info'].parent =_meta_table['Sam.LogContents']['meta_info']
_meta_table['Sam.Packages.Package.CertificateFlags']['meta_info'].parent =_meta_table['Sam.Packages.Package']['meta_info']
_meta_table['Sam.Packages.Package']['meta_info'].parent =_meta_table['Sam.Packages']['meta_info']
_meta_table['Sam.CertificateRevocationListSummary']['meta_info'].parent =_meta_table['Sam']['meta_info']
_meta_table['Sam.CertificateRevocations']['meta_info'].parent =_meta_table['Sam']['meta_info']
_meta_table['Sam.Devices']['meta_info'].parent =_meta_table['Sam']['meta_info']
_meta_table['Sam.LogContents']['meta_info'].parent =_meta_table['Sam']['meta_info']
_meta_table['Sam.Packages']['meta_info'].parent =_meta_table['Sam']['meta_info']
_meta_table['Sam.SystemInformation']['meta_info'].parent =_meta_table['Sam']['meta_info']
