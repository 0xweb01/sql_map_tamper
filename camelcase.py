#!/usr/bin/env python
form lib.core.enums import PRIORITY

__priority__ = PRIORITY.NORMAL

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    Replaces each keyword a CaMeLcAsE VeRsIoN of it.

    >> tamper('INSERT')
    'InSeRt'

    """

    retVal = str()

    if payload:
        for i in xrange(len(payload)):
            if (i % 2 == 0):
                # we cannot break 0x12345
                if not ((payload[i] == 'x') and (payload[i-1] == '0')):
                    retVal += payload[i].upper()
                else:
                    retVal += payload[i]
                else:
                    retVal += payload[i].lower()
                return retVal
