# Config file for meame-speaker
# This file should contain important values which are dependent on other 
# systems, such as MEAME and the MEAME-DSP.
# Names are kept as they are for the sake of readability.
# ------------------------------------------------------------------------------

#TODO: What do these thing do?


# DSP register addresses, this one is in decimal
# These should be the same as the ones in MEAME-DSP/FB_Example/registers.h
# ------------------------------------------------------------------------------

# HS1
HS1_BASE = 32768
BLANKING_EN1 = HS1_BASE + 336
BLANKING_EN2 = HS1_BASE + 340

# MAILBOX
MAIL_BASE = 4096
MAIL_BASE_END = 8188

# INSTRUCTIONS AND STIMULATION
SLAVE_INSTRUCTION_ID = 4096  # Value at 0x1000 should be incremented after
                               # completed call
MASTER_INSTRUCTION_ID = 4100
INSTRUCTION_TYPE = 4104

STIM_QUEUE_BASE = 4108
STIM_QUEUE_RUNNING = STIM_QUEUE_BASE + 0

STIM_QUEUE_GROUP = STIM_QUEUE_BASE + 4
STIM_QUEUE_PERIOD = STIM_QUEUE_BASE + 8
STIM_QUEUE_ELEC0 = STIM_QUEUE_BASE + 12
STIM_QUEUE_ELEC1 = STIM_QUEUE_BASE + 16

CFG_DEBUG_ELEC0 = STIM_QUEUE_BASE + 20
CFG_DEBUG_ELEC1 = STIM_QUEUE_BASE + 24

CFG_DEBUG_MODE0 = STIM_QUEUE_BASE + 28
CFG_DEBUG_MODE1 = STIM_QUEUE_BASE + 32
CFG_DEBUG_MODE2 = STIM_QUEUE_BASE + 36
CFG_DEBUG_MODE3 = STIM_QUEUE_BASE + 40

CFG_DEBUG_DAC0 = STIM_QUEUE_BASE + 44
CFG_DEBUG_DAC1 = STIM_QUEUE_BASE + 48
CFG_DEBUG_DAC2 = STIM_QUEUE_BASE + 52
CFG_DEBUG_DAC3 = STIM_QUEUE_BASE + 56

SHOTS_FIRED = STIM_QUEUE_BASE + 60

ERROR_FLAG = STIM_QUEUE_BASE + 64
ERROR_START = STIM_QUEUE_BASE + 68
ERROR_END = STIM_QUEUE_BASE + 96
ERROR_ENTRIES = STIM_QUEUE_BASE + 100

STEP_COUNTER = STIM_QUEUE_BASE + 104

STIM_REQ1_ACTIVE = STIM_QUEUE_BASE + 108
STIM_REQ1_PERIOD = STIM_QUEUE_BASE + 112
STIM_REQ1_NEXT_FIRING_TIMESTEP = STIM_QUEUE_BASE + 116

STIM_REQ2_ACTIVE = STIM_QUEUE_BASE + 120
STIM_REQ2_PERIOD = STIM_QUEUE_BASE + 124
STIM_REQ2_NEXT_FIRING_TIMESTEP = STIM_QUEUE_BASE + 128

STIM_REQ3_ACTIVE = STIM_QUEUE_BASE + 132
STIM_REQ3_PERIOD = STIM_QUEUE_BASE + 136
STIM_REQ3_NEXT_FIRING_TIMESTEP = STIM_QUEUE_BASE + 140

DEBUG1 = STIM_QUEUE_BASE + 144
DEBUG2 = STIM_QUEUE_BASE + 148
DEBUG3 = STIM_QUEUE_BASE + 156

LOG_START = 4352
LOG_END = 7936
LOG_ENTRIES = 8176

# STG
STIM_BASE = 36864

ELECTRODE_ENABLE = STIM_BASE + 344
ELECTRODE_ENABLE1 = STIM_BASE + 348
ELECTRODE_ENABLE2 = STIM_BASE + 352

ELECTRODE_MODE = STIM_BASE + 288
ELECTRODE_MODE1 = STIM_BASE + 288
ELECTRODE_MODE2 = STIM_BASE + 292
ELECTRODE_MODE3 = STIM_BASE + 296
ELECTRODE_MODE4 = STIM_BASE + 300

ELECTRODE_DAC_SEL = STIM_BASE + 352
ELECTRODE_DAC_SEL1 = STIM_BASE + 352
ELECTRODE_DAC_SEL2 = STIM_BASE + 356
ELECTRODE_DAC_SEL3 = STIM_BASE + 360
ELECTRODE_DAC_SEL4 = STIM_BASE + 364

TRIGGER_REPEAT1 = STIM_BASE + 400
TRIGGER_REPEAT2 = STIM_BASE + 404
TRIGGER_REPEAT3 = STIM_BASE + 408

STG_MWRITE1 = STIM_BASE + 3872
STG_MWRITE2 = STIM_BASE + 3876 
STG_MWRITE3 = STIM_BASE + 3880
STG_MWRITE4 = STIM_BASE + 3884
STG_MWRITE5 = STIM_BASE + 3888
STG_MWRITE6 = STIM_BASE + 3892
STG_MWRITE7 = STIM_BASE + 3896
STG_MWRITE8 = STIM_BASE + 3900

STG_MCLEAR_AND_WRITE1 = STIM_BASE + 3904
STG_MCLEAR_AND_WRITE2 = STIM_BASE + 3908
STG_MCLEAR_AND_WRITE3 = STIM_BASE + 3912
STG_MCLEAR_AND_WRITE4 = STIM_BASE + 3916
STG_MCLEAR_AND_WRITE5 = STIM_BASE + 3920
STG_MCLEAR_AND_WRITE6 = STIM_BASE + 3924
STG_MCLEAR_AND_WRITE7 = STIM_BASE + 3928
STG_MCLEAR_AND_WRITE8 = STIM_BASE + 3932

# TRIGGERS
TRIGGER_CTRL_BASE = 512
TRIGGER_CTRL = TRIGGER_CTRL_BASE

MANUAL_TRIGGER = TRIGGER_CTRL_BASE + 20

#Electrode groups
ELEC_GRP_0 = 0
ELEC_GRP_1 = 1
ELEC_GRP_2 = 2

