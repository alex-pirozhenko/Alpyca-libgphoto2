
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------
# safetymonitor.py - Alpaca API responders for Safetymonitor
#
# Author:   Your R. Name <your@email.org> (abc)
#
# -----------------------------------------------------------------------------
# Edit History:
#   Generated by Python Interface Generator for AlpycaDevice
#
# ??-???-????   abc Initial edit

from falcon import Request, Response, HTTPBadRequest, before
from logging import Logger
from shr import PropertyResponse, MethodResponse, PreProcessRequest, \
                get_request_field, to_bool, to_int, to_float
from exceptions import *        # Nothing but exception classes

logger: Logger = None

# ----------------------
# MULTI-INSTANCE SUPPORT
# ----------------------
# If this is > 0 then it means that multiple devices of this type are supported.
# Each responder on_get() and on_put() is called with a devnum parameter to indicate
# which instance of the device (0-based) is being called by the client. Leave this
# set to 0 for the simple case of controlling only one instance of this device type.
#
maxdev = 0                      # Single instance

# -----------
# DEVICE INFO
# -----------
# Static metadata not subject to configuration changes
## EDIT FOR YOUR DEVICE ##
class SafetymonitorMetadata:
    """ Metadata describing the Safetymonitor Device. Edit for your device"""
    Name = 'Sample Safetymonitor'
    Version = '##DRIVER VERSION AS STRING##'
    Description = 'My ASCOM Safetymonitor'
    DeviceType = 'Safetymonitor'
    DeviceID = '##GENERATE A NEW GUID AND PASTE HERE##' # https://guidgenerator.com/online-guid-generator.aspx
    Info = 'Alpaca Sample Device\nImplements ISafetymonitor\nASCOM Initiative'
    MaxDeviceNumber = maxdev
    InterfaceVersion = ##YOUR DEVICE INTERFACE VERSION##        # ISafetymonitorVxxx

# --------------------
# RESOURCE CONTROLLERS
# --------------------

@before(PreProcessRequest(maxdev))
class Action:
    def on_put(self, req: Request, resp: Response, devnum: int):
        resp.text = MethodResponse(req, NotImplementedException()).json

@before(PreProcessRequest(maxdev))
class CommandBlind:
    def on_put(self, req: Request, resp: Response, devnum: int):
        resp.text = MethodResponse(req, NotImplementedException()).json

@before(PreProcessRequest(maxdev))
class CommandBool:
    def on_put(self, req: Request, resp: Response, devnum: int):
        resp.text = MethodResponse(req, NotImplementedException()).json

@before(PreProcessRequest(maxdev))
class CommandString():
    def on_put(self, req: Request, resp: Response, devnum: int):
        resp.text = MethodResponse(req, NotImplementedException()).json

@before(PreProcessRequest(maxdev))
class Description():
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse(SafetymonitorMetadata.Description, req).json

@before(PreProcessRequest(maxdev))
class DriverInfo():
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse(SafetymonitorMetadata.Info, req).json

@before(PreProcessRequest(maxdev))
class InterfaceVersion():
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse(SafetymonitorMetadata.InterfaceVersion, req).json

@before(PreProcessRequest(maxdev))
class DriverVersion():
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse(SafetymonitorMetadata.Version, req).json

@before(PreProcessRequest(maxdev))
class Name():
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse(SafetymonitorMetadata.Name, req).json

@before(PreProcessRequest(maxdev))
class SupportedActions():
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse([], req).json  # Not PropertyNotImplemented

@before(PreProcessRequest(maxdev))
class issafe:

    def on_get(self, req: Request, resp: Response, devnum: int):
        if not ##IS DEV CONNECTED##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, 'Safetymonitor.Issafe failed', ex)).json

