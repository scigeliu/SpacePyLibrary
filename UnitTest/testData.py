#******************************************************************************
# (C) 2014, Stefan Korner, Austria                                            *
#                                                                             *
# The Space Python Library is free software; you can redistribute it and/or   *
# modify it under the terms of the GNU Lesser General Public License as       *
# published by the Free Software Foundation; either version 2.1 of the        *
# License, or (at your option) any later version.                             *
#                                                                             *
# The Space Python Library is distributed in the hope that it will be useful, *
# but WITHOUT ANY WARRANTY; without even the implied warranty of              *
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser     *
# General Public License for more details.                                    *
#******************************************************************************
# Test Data for Unit Tests                                                    *
#******************************************************************************
import array

#############
# constants #
#############
ZERO_CUC_TIME_FIELD = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
CUC_TIME1_FIELD = [0x00, 0x00, 0x00, 0x00, 0x00, 0x01]
CUC_TIME2_FIELD = [0x00, 0x00, 0x00, 0x00, 0x00, 0x02]
CUC_TIME3_FIELD = [0x00, 0x00, 0x00, 0x00, 0x01, 0x00]
CUC_TIME4_FIELD = [0x00, 0x00, 0x00, 0x00, 0xFF, 0xFE]
CUC_TIME5_FIELD = [0x00, 0x00, 0x00, 0x00, 0xFF, 0xFF]
CUC_TIME6_FIELD = [0x3A, 0xD7, 0x27, 0x48, 0x00, 0x00]
CUC_TIME_MISSION_EPOCH_STR = "1980.006.00.00.00.000"
CUC_TIME1_STR = "1980.005.23.59.45.000015"
CUC_TIME2_STR = "1980.005.23.59.45.000031"
CUC_TIME3_STR = "1980.005.23.59.45.003906"
CUC_TIME4_STR = "1980.005.23.59.45.999970"
CUC_TIME5_STR = "1980.005.23.59.45.999985"
CUC_TIME6_STR = "2011.108.16.20.09.000000"
TM_PACKET_01 = [
  0x08, 0x44, 0xC0, 0x00, 0x00, 0x0F, 0x10, 0x01,
  0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
TM_PACKET_01_versionNumber = 0
TM_PACKET_01_packetType = 0
TM_PACKET_01_dataFieldHeaderFlag = 1
TM_PACKET_01_applicationProcessId = 68
TM_PACKET_01_segmentationFlags = 3
TM_PACKET_01_sequenceControlCount = 0
TM_PACKET_01_packetLength = 15
TM_PACKET_01_pusVersionNumber = 1
TM_PACKET_01_serviceType = 1
TM_PACKET_01_serviceSubType = 1
TM_PACKET_02 = [
  0x08, 0xA0, 0xC0, 0x00, 0x01, 0xC9, 0x10, 0x03,
  0x19, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0x80]
TM_PACKET_02_versionNumber = 0
TM_PACKET_02_packetType = 0
TM_PACKET_02_dataFieldHeaderFlag = 1
TM_PACKET_02_applicationProcessId = 160
TM_PACKET_02_segmentationFlags = 3
TM_PACKET_02_sequenceControlCount = 0
TM_PACKET_02_packetLength = 457
TM_PACKET_02_pusVersionNumber = 1
TM_PACKET_02_serviceType = 3
TM_PACKET_02_serviceSubType = 25
EN_TM_PACKET_01 = [
  0x00, 0x01, 0xC0, 0x00, 0x00, 0x25, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x01, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00]
TM_FRAME_01 = [
  0x00, 0x00, 0x04, 0x6F, 0x02, 0xF6, 0x00, 0x00,
  0x00, 0x00, 0x4B, 0x2D, 0x03, 0xC4, 0xC7, 0x3F,
  0x03, 0x7A, 0x00, 0x00, 0x2F, 0x61, 0x00, 0x00,
  0x18, 0x00, 0x08, 0x44, 0xC0, 0x00, 0x00, 0x0F,
  0x00, 0x01, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x07, 0xFF, 0xC0, 0x00, 0x04, 0x32, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xC5,
  0x08, 0x01, 0x00, 0x00, 0x00, 0xB2, 0xFC]
NCTRS_TM_FRAME_01 = [
  0x00, 0x00, 0x04, 0x63, 0x02, 0xF6, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x6F,
  0x02, 0xF6, 0x00, 0x00, 0x00, 0x00, 0x4B, 0x2D,
  0x03, 0xC4, 0xC7, 0x3F, 0x03, 0x7A, 0x00, 0x00,
  0x2F, 0x61, 0x00, 0x00, 0x18, 0x00, 0x08, 0x44,
  0xC0, 0x00, 0x00, 0x0F, 0x00, 0x01, 0x01, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x07, 0xFF, 0xC0, 0x00,
  0x04, 0x32, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0xC5, 0x08, 0x01, 0x00, 0x00,
  0x00, 0xB2, 0xFC]
NCTRS_TM_FRAME_01_packetSize = 1123
NCTRS_TM_FRAME_01_spacecraftId = 758
NCTRS_TM_FRAME_01_dataStreamType = 0
NCTRS_TM_FRAME_01_virtualChannelId = 0
NCTRS_TM_FRAME_01_routeId = 0
NCTRS_TM_FRAME_01_earthReceptionTime = array.array('B', [0, 0, 0, 0, 0, 0, 0, 0])
NCTRS_TM_FRAME_01_sequenceFlag = 0
NCTRS_TM_FRAME_01_qualityFlag = 0
TC_PACKET_01 = [
  0x1A, 0x8C, 0xC0, 0x0E, 0x01, 0x0D, 0x19, 0x06,
  0x02, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00,
  0x01, 0x00, 0x00, 0x00, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x01, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x02, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x03, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x04, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x05, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x06, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x07, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x08, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x09, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x0A, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x0B, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x0C, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x0D, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x0E, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x0F, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x10, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x11, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x12, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x13, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x14, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x15, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x16, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x17, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x18, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x19, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x1A, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x1B, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x1C, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x1D, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x1E, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0x00, 0x1F, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x0F, 0xAC, 0x8F]
TC_PACKET_01_versionNumber = 0
TC_PACKET_01_packetType = 1
TC_PACKET_01_dataFieldHeaderFlag = 1
TC_PACKET_01_applicationProcessId = 652
TC_PACKET_01_segmentationFlags = 3
TC_PACKET_01_sequenceControlCount = 14
TC_PACKET_01_packetLength = 269
TC_PACKET_01_pusVersionNumber = 1
TC_PACKET_01_ack = 9
TC_PACKET_01_serviceType = 6
TC_PACKET_01_serviceSubType = 2
TC_SEGMENT_01 = [
  0x42, 0x1A, 0x8C, 0xC0, 0x0E, 0x01, 0x0D, 0x19,
  0x06, 0x02, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00,
  0x00, 0x01, 0x00, 0x00, 0x00, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0x00, 0x01, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0x00, 0x02, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0x00, 0x03, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0x00, 0x04, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0x00, 0x05, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0x00, 0x06, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0x00, 0x07, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0x00, 0x08, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0x00, 0x09, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0x00, 0x0A, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0x00, 0x0B, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0x00, 0x0C, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0x00, 0x0D, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0x00, 0x0E, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0x00, 0x0F, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0x00, 0x10, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0x00, 0x11, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0x00, 0x12, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0x00, 0x13, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0x00, 0x14, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0x00, 0x15, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0x00, 0x16, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0x00, 0x17, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0x00, 0x18, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0x00, 0x19, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0x00, 0x1A, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0x00, 0x1B, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0x00, 0x1C, 0xFF, 0x00, 0x00,
  0x00]
TC_SEGMENT_01_sequenceFlags = 1
TC_SEGMENT_01_mapId = 2
TC_SEGMENT_02 = [
  0x82, 0x00, 0x0F, 0x00, 0x1D, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0x00, 0x1E, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0x00, 0x1F, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x0F, 0xAC, 0x8F]
TC_SEGMENT_02_sequenceFlags = 2
TC_SEGMENT_02_mapId = 2
TC_FRAME_01 = [
  0x22, 0xF6, 0x00, 0xFF, 0x00, 0x42, 0x1A, 0x8C,
  0xC0, 0x0E, 0x01, 0x0D, 0x19, 0x06, 0x02, 0x00,
  0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00,
  0x00, 0x00, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x01, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x02, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x03, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x04, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x05, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x06, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x07, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x08, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x09, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x0A, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x0B, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x0C, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x0D, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x0E, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x0F, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x10, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x11, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x12, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x13, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x14, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x15, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x16, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x17, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x18, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x19, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x1A, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x1B, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x1C, 0xFF, 0x00, 0x00, 0x00, 0xAD, 0x1A]
TC_FRAME_01_versionNumber = 0
TC_FRAME_01_reservedFieldB = 0
TC_FRAME_01_virtualChannelId = 0
TC_FRAME_01_controlCommandFlag = 0
TC_FRAME_01_reservedFieldA = 0
TC_FRAME_01_frameLength = 255
TC_FRAME_01_sequenceNumber = 0
TC_FRAME_01_spacecraftId = 758
TC_FRAME_01_bypassFlag = 1
TC_FRAME_02 = [
  0x22, 0xF6, 0x00, 0x23, 0x00, 0x82, 0x00, 0x0F,
  0x00, 0x1D, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x1E, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x1F, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0xAC, 0x8F, 0x00, 0x68]
TC_FRAME_02_versionNumber = 0
TC_FRAME_02_reservedFieldB = 0
TC_FRAME_02_virtualChannelId = 0
TC_FRAME_02_controlCommandFlag = 0
TC_FRAME_02_reservedFieldA = 0
TC_FRAME_02_frameLength = 35
TC_FRAME_02_sequenceNumber = 0
TC_FRAME_02_spacecraftId = 758
TC_FRAME_02_bypassFlag = 1
CLTU_01 = [
  0xEB, 0x90, 0x22, 0xF6, 0x00, 0xFF, 0x00, 0x42,
  0x1A, 0x12, 0x8C, 0xC0, 0x0E, 0x01, 0x0D, 0x19,
  0x06, 0x5A, 0x02, 0x00, 0x00, 0x01, 0x00, 0x00,
  0x00, 0x8A, 0x00, 0x01, 0x00, 0x00, 0x00, 0xFF,
  0x00, 0xCC, 0x00, 0x00, 0x00, 0x0F, 0x00, 0x01,
  0xFF, 0x28, 0x00, 0x00, 0x00, 0x00, 0x0F, 0x00,
  0x02, 0x5A, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x92, 0x03, 0xFF, 0x00, 0x00, 0x00, 0x00,
  0x0F, 0xD6, 0x00, 0x04, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0xD4, 0x0F, 0x00, 0x05, 0xFF, 0x00, 0x00,
  0x00, 0xA8, 0x00, 0x0F, 0x00, 0x06, 0xFF, 0x00,
  0x00, 0xC8, 0x00, 0x00, 0x0F, 0x00, 0x07, 0xFF,
  0x00, 0xCA, 0x00, 0x00, 0x00, 0x0F, 0x00, 0x08,
  0xFF, 0x66, 0x00, 0x00, 0x00, 0x00, 0x0F, 0x00,
  0x09, 0xA8, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x92, 0x0A, 0xFF, 0x00, 0x00, 0x00, 0x00,
  0x0F, 0xF4, 0x00, 0x0B, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x5A, 0x0F, 0x00, 0x0C, 0xFF, 0x00, 0x00,
  0x00, 0xB0, 0x00, 0x0F, 0x00, 0x0D, 0xFF, 0x00,
  0x00, 0xD8, 0x00, 0x00, 0x0F, 0x00, 0x0E, 0xFF,
  0x00, 0x96, 0x00, 0x00, 0x00, 0x0F, 0x00, 0x0F,
  0xFF, 0xDA, 0x00, 0x00, 0x00, 0x00, 0x0F, 0x00,
  0x10, 0x82, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x92, 0x11, 0xFF, 0x00, 0x00, 0x00, 0x00,
  0x0F, 0x92, 0x00, 0x12, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x2A, 0x0F, 0x00, 0x13, 0xFF, 0x00, 0x00,
  0x00, 0x24, 0x00, 0x0F, 0x00, 0x14, 0xFF, 0x00,
  0x00, 0x4A, 0x00, 0x00, 0x0F, 0x00, 0x15, 0xFF,
  0x00, 0x72, 0x00, 0x00, 0x00, 0x0F, 0x00, 0x16,
  0xFF, 0x2E, 0x00, 0x00, 0x00, 0x00, 0x0F, 0x00,
  0x17, 0x20, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x00, 0x92, 0x18, 0xFF, 0x00, 0x00, 0x00, 0x00,
  0x0F, 0xB0, 0x00, 0x19, 0xFF, 0x00, 0x00, 0x00,
  0x00, 0x90, 0x0F, 0x00, 0x1A, 0xFF, 0x00, 0x00,
  0x00, 0x3C, 0x00, 0x0F, 0x00, 0x1B, 0xFF, 0x00,
  0x00, 0xF8, 0x00, 0x00, 0x0F, 0x00, 0x1C, 0xFF,
  0x00, 0x2E, 0x00, 0x00, 0xAD, 0x1A, 0x55, 0x55,
  0x55, 0xEC, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55,
  0x55, 0x55]
CLTU_02 = [
  0xEB, 0x90, 0x22, 0xF6, 0x00, 0x23, 0x00, 0x82,
  0x00, 0x24, 0x0F, 0x00, 0x1D, 0xFF, 0x00, 0x00,
  0x00, 0x34, 0x00, 0x0F, 0x00, 0x1E, 0xFF, 0x00,
  0x00, 0x10, 0x00, 0x00, 0x0F, 0x00, 0x1F, 0xFF,
  0x00, 0xD8, 0x00, 0x00, 0x00, 0x0F, 0xAC, 0x8F,
  0x00, 0x90, 0x68, 0x55, 0x55, 0x55, 0x55, 0x55,
  0x55, 0x06, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55,
  0x55, 0x55]
NCTRS_CLTU_01 = [
  0x00, 0x00, 0x01, 0x61, 0x00, 0x07, 0x02, 0xf6,
  0x00, 0x00, 0x00, 0x00, 0x10, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xEB,
  0x90, 0x22, 0xF6, 0x00, 0xFF, 0x00, 0x42, 0x1A,
  0x12, 0x8C, 0xC0, 0x0E, 0x01, 0x0D, 0x19, 0x06,
  0x5A, 0x02, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00,
  0x8A, 0x00, 0x01, 0x00, 0x00, 0x00, 0xFF, 0x00,
  0xCC, 0x00, 0x00, 0x00, 0x0F, 0x00, 0x01, 0xFF,
  0x28, 0x00, 0x00, 0x00, 0x00, 0x0F, 0x00, 0x02,
  0x5A, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F, 0x00,
  0x92, 0x03, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0xD6, 0x00, 0x04, 0xFF, 0x00, 0x00, 0x00, 0x00,
  0xD4, 0x0F, 0x00, 0x05, 0xFF, 0x00, 0x00, 0x00,
  0xA8, 0x00, 0x0F, 0x00, 0x06, 0xFF, 0x00, 0x00,
  0xC8, 0x00, 0x00, 0x0F, 0x00, 0x07, 0xFF, 0x00,
  0xCA, 0x00, 0x00, 0x00, 0x0F, 0x00, 0x08, 0xFF,
  0x66, 0x00, 0x00, 0x00, 0x00, 0x0F, 0x00, 0x09,
  0xA8, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F, 0x00,
  0x92, 0x0A, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0xF4, 0x00, 0x0B, 0xFF, 0x00, 0x00, 0x00, 0x00,
  0x5A, 0x0F, 0x00, 0x0C, 0xFF, 0x00, 0x00, 0x00,
  0xB0, 0x00, 0x0F, 0x00, 0x0D, 0xFF, 0x00, 0x00,
  0xD8, 0x00, 0x00, 0x0F, 0x00, 0x0E, 0xFF, 0x00,
  0x96, 0x00, 0x00, 0x00, 0x0F, 0x00, 0x0F, 0xFF,
  0xDA, 0x00, 0x00, 0x00, 0x00, 0x0F, 0x00, 0x10,
  0x82, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F, 0x00,
  0x92, 0x11, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0x92, 0x00, 0x12, 0xFF, 0x00, 0x00, 0x00, 0x00,
  0x2A, 0x0F, 0x00, 0x13, 0xFF, 0x00, 0x00, 0x00,
  0x24, 0x00, 0x0F, 0x00, 0x14, 0xFF, 0x00, 0x00,
  0x4A, 0x00, 0x00, 0x0F, 0x00, 0x15, 0xFF, 0x00,
  0x72, 0x00, 0x00, 0x00, 0x0F, 0x00, 0x16, 0xFF,
  0x2E, 0x00, 0x00, 0x00, 0x00, 0x0F, 0x00, 0x17,
  0x20, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F, 0x00,
  0x92, 0x18, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x0F,
  0xB0, 0x00, 0x19, 0xFF, 0x00, 0x00, 0x00, 0x00,
  0x90, 0x0F, 0x00, 0x1A, 0xFF, 0x00, 0x00, 0x00,
  0x3C, 0x00, 0x0F, 0x00, 0x1B, 0xFF, 0x00, 0x00,
  0xF8, 0x00, 0x00, 0x0F, 0x00, 0x1C, 0xFF, 0x00,
  0x2E, 0x00, 0x00, 0xAD, 0x1A, 0x55, 0x55, 0x55,
  0xEC, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55,
  0x55]
NCTRS_CLTU_01_packetSize = 353
NCTRS_CLTU_01_spacecraftId = 758
NCTRS_CLTU_01_dataUnitType = 7
NCTRS_CLTU_01_delay = 0
NCTRS_CLTU_01_latestProdTime = array.array('B', [0, 0, 0, 0, 0, 0, 0, 0])
NCTRS_CLTU_01_serviceType = 0
NCTRS_CLTU_01_earliestProdTime = array.array('B', [0, 0, 0, 0, 0, 0, 0, 0])
NCTRS_CLTU_01_virtualChannelId = 0
NCTRS_CLTU_01_mapId = 0
NCTRS_CLTU_01_aggregationFlag = 0
NCTRS_CLTU_01_tcId = 16
NCTRS_CLTU_01_earliestProdTimeFlag = 0
NCTRS_CLTU_01_latestProdTimeFlag = 0
NCTRS_CLTU_02 = [
  0x00, 0x00, 0x00, 0x69, 0x00, 0x07, 0x02, 0xF6,
  0x00, 0x00, 0x00, 0x00, 0x11, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xEB,
  0x90, 0x22, 0xF6, 0x00, 0x23, 0x00, 0x82, 0x00,
  0x24, 0x0F, 0x00, 0x1D, 0xFF, 0x00, 0x00, 0x00,
  0x34, 0x00, 0x0F, 0x00, 0x1E, 0xFF, 0x00, 0x00,
  0x10, 0x00, 0x00, 0x0F, 0x00, 0x1F, 0xFF, 0x00,
  0xD8, 0x00, 0x00, 0x00, 0x0F, 0xAC, 0x8F, 0x00,
  0x90, 0x68, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55,
  0x06, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55,
  0x55]
NCTRS_CLTU_02_packetSize = 105
NCTRS_CLTU_02_spacecraftId = 758
NCTRS_CLTU_02_dataUnitType = 7
NCTRS_CLTU_02_delay = 0
NCTRS_CLTU_02_latestProdTime = array.array('B', [0, 0, 0, 0, 0, 0, 0, 0])
NCTRS_CLTU_02_serviceType = 0
NCTRS_CLTU_02_earliestProdTime = array.array('B', [0, 0, 0, 0, 0, 0, 0, 0])
NCTRS_CLTU_02_virtualChannelId = 0
NCTRS_CLTU_02_mapId = 0
NCTRS_CLTU_02_aggregationFlag = 0
NCTRS_CLTU_02_tcId = 17
NCTRS_CLTU_02_earliestProdTimeFlag = 0
NCTRS_CLTU_02_latestProdTimeFlag = 0
BCH_BLOCK_01 = [
  0x22, 0xF6, 0x00, 0xFF, 0x00, 0x42, 0x1A, 0x12]
BCH_BLOCK_02 = [
  0x8C, 0xC0, 0x0E, 0x01, 0x0D, 0x19, 0x06, 0x5A]
