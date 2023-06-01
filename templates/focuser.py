
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------
# focuser.py - Alpaca API responders for Focuser
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
class FocuserMetadata:
    """ Metadata describing the Focuser Device. Edit for your device"""
    Name = 'Sample Focuser'
    Version = '##DRIVER VERSION AS STRING##'
    Description = 'My ASCOM Focuser'
    DeviceType = 'Focuser'
    DeviceID = '##GENERATE A NEW GUID AND PASTE HERE##' # https://guidgenerator.com/online-guid-generator.aspx
    Info = 'Alpaca Sample Device\nImplements IFocuser\nASCOM Initiative'
    MaxDeviceNumber = maxdev
    InterfaceVersion = ##YOUR DEVICE INTERFACE VERSION##        # IFocuserVxxx

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
        resp.text = PropertyResponse(FocuserMetadata.Description, req).json

@before(PreProcessRequest(maxdev))
class DriverInfo():
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse(FocuserMetadata.Info, req).json

@before(PreProcessRequest(maxdev))
class InterfaceVersion():
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse(FocuserMetadata.InterfaceVersion, req).json

@before(PreProcessRequest(maxdev))
class DriverVersion():
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse(FocuserMetadata.Version, req).json

@before(PreProcessRequest(maxdev))
class Name():
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse(FocuserMetadata.Name, req).json

@before(PreProcessRequest(maxdev))
class SupportedActions():
    def on_get(self, req: Request, resp: Response, devnum: int):
        resp.text = PropertyResponse([], req).json  # Not PropertyNotImplemented

@before(PreProcessRequest(maxdev))
class absolute:

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
                            DriverException(0x500, 'Focuser.Absolute failed', ex)).json

@before(PreProcessRequest(maxdev))
class ismoving:

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
                            DriverException(0x500, 'Focuser.Ismoving failed', ex)).json

@before(PreProcessRequest(maxdev))
class maxincrement:

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
                            DriverException(0x500, 'Focuser.Maxincrement failed', ex)).json

@before(PreProcessRequest(maxdev))
class maxstep:

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
                            DriverException(0x500, 'Focuser.Maxstep failed', ex)).json

@before(PreProcessRequest(maxdev))
class position:

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
                            DriverException(0x500, 'Focuser.Position failed', ex)).json

@before(PreProcessRequest(maxdev))
class stepsize:

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
                            DriverException(0x500, 'Focuser.Stepsize failed', ex)).json

@before(PreProcessRequest(maxdev))
class tempcomp:

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
                            DriverException(0x500, 'Focuser.Tempcomp failed', ex)).json

    def on_put(self, req: Request, resp: Response, devnum: int):
        if not ## IS DEV CONNECTED ##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        tempcompstr = get_request_field('TempComp', req)      # Raises 400 bad request if missing
        tempcomp = to_bool(tempcompstr)                       # Same here

        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, 'Focuser.Tempcomp failed', ex)).json

    def on_put(self, req: Request, resp: Response, devnum: int):
        if not ## IS DEV CONNECTED ##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, 'Focuser.Tempcomp failed', ex)).json

@before(PreProcessRequest(maxdev))
class tempcompavailable:

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
                            DriverException(0x500, 'Focuser.Tempcompavailable failed', ex)).json

@before(PreProcessRequest(maxdev))
class temperature:

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
                            DriverException(0x500, 'Focuser.Temperature failed', ex)).json

@before(PreProcessRequest(maxdev))
class halt:

    def on_put(self, req: Request, resp: Response, devnum: int):
        if not ## IS DEV CONNECTED ##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, 'Focuser.Halt failed', ex)).json

@before(PreProcessRequest(maxdev))
class move:

    def on_put(self, req: Request, resp: Response, devnum: int):
        if not ## IS DEV CONNECTED ##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        positionstr = get_request_field('Position', req)      # Raises 400 bad request if missing
        try:
            position = int(positionstr)
        except:
            resp.text = MethodResponse(req,
                            InvalidValueException(f'Position " + positionstr + " not a valid number.')).json
            return
        ### RANGE CHECK AS NEEDED ###       # Raise Alpaca InvalidValueException with details!
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, 'Focuser.Move failed', ex)).json

    def on_put(self, req: Request, resp: Response, devnum: int):
        if not ## IS DEV CONNECTED ##:
            resp.text = PropertyResponse(None, req,
                            NotConnectedException()).json
            return
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, 'Focuser.Move failed', ex)).json

