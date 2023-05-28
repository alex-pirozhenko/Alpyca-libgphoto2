
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------
# switch.py - Alpaca API responders for Switch
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
                get_request_field, to_bool
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
class SwitchMetadata:
    """ Metadata describing the Switch Device. Edit for your device"""
    Name = 'Sample Switch'
    Version = '##DRIVER VERSION AS STRING##'
    Description = 'My ASCOM Switch'
    DeviceType = 'Switch'
    DeviceID = '##GENERATE A NEW GUID AND PASTE HERE##' # https://guidgenerator.com/online-guid-generator.aspx
    Info = 'Alpaca Sample Device\nImplements ISwitch\nASCOM Initiative'
    MaxDeviceNumber = maxdev
    InterfaceVersion = ##YOUR DEVICE INTERFACE VERSION##        # ISwitchVxxx

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
        resp.text = PropertyResponse(SwitchMetadata.Description, req).json

@before(PreProcessRequest(maxdev))
class DriverInfo():
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse(SwitchMetadata.Info, req).json

@before(PreProcessRequest(maxdev))
class InterfaceVersion():
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse(SwitchMetadata.InterfaceVersion, req).json

@before(PreProcessRequest(maxdev))
class DriverVersion():
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse(SwitchMetadata.Version, req).json

@before(PreProcessRequest(maxdev))
class Name():
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse(SwitchMetadata.Name, req).json

@before(PreProcessRequest(maxdev))
class SupportedActions():
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse([], req).json  # Not PropertyNotImplemented

@before(PreProcessRequest(maxdev))
class maxswitch:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest(maxdev))
class canwrite:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest(maxdev))
class getswitch:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest(maxdev))
class getswitchdescription:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest(maxdev))
class getswitchname:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest(maxdev))
class getswitchvalue:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest(maxdev))
class minswitchvalue:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest(maxdev))
class maxswitchvalue:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest(maxdev))
class setswitch:

    def on_put(self, req: Request, resp: Response, devnum: int):
        formdata = req.get_media()
        ##PARAMVAL## = ##PARAMCVT##formdata['##PARAMNAME##'])
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest(maxdev))
class setswitchname:

    def on_put(self, req: Request, resp: Response, devnum: int):
        formdata = req.get_media()
        ##PARAMVAL## = ##PARAMCVT##formdata['##PARAMNAME##'])
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest(maxdev))
class setswitchvalue:

    def on_put(self, req: Request, resp: Response, devnum: int):
        formdata = req.get_media()
        ##PARAMVAL## = ##PARAMCVT##formdata['##PARAMNAME##'])
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest(maxdev))
class switchstep:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

