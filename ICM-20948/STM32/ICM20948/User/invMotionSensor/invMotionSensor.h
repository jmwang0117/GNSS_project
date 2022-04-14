
#ifndef __INV_MOTION_SENSOR_H
#define __INV_MOTION_SENSOR_H
#include "DEV_Config.h"
#include "Public_StdTypes.h"

#define ARR_SIZE(a)  (sizeof((a))/sizeof(((a)[0])))

typedef enum {
	INVMS_EN_SENSOR_TYPY_MPU9255 = 0,
	INVMS_EN_SENSOR_TYPY_MPU9250,
	INVMS_EN_SENSOR_TYPY_ICM20948,
    INVMS_EN_SENSOR_TYPY_MAX
}INVMS_EN_SENSOR_TYPY;

typedef bool (*INVMS_SENSOR_CHECK_FUNCTION)(void);
typedef void (*INVMS_SENSOR_INIT_FUNCTION)(void);
typedef void (*INVMS_SENSOR_READ_FUNCTION)(int16_t* ps16X, int16_t* ps16Y, int16_t* ps16Z);
typedef struct invms_st_sen_info_tag
{
    INVMS_EN_SENSOR_TYPY enSensorType;
    INVMS_SENSOR_CHECK_FUNCTION pFunCheck;
    INVMS_SENSOR_INIT_FUNCTION  pFunInit;
    INVMS_SENSOR_READ_FUNCTION  pFunGyroRead;
    INVMS_SENSOR_READ_FUNCTION  pFunAccelRead;
    INVMS_SENSOR_READ_FUNCTION  pFunMagRead;
    
}INVMS_ST_SEN_FUN_INFO;    

extern void invMSInit(void);
extern void invMSAccelRead(int16_t* ps16AccelX, int16_t* ps16AccelY, int16_t* ps16AccelZ);
extern void invMSGyroRead(int16_t* ps16GyroX, int16_t* ps16GyroY, int16_t* ps16GyroZ);
extern void invMSMagRead(int16_t* ps16MagnX, int16_t* ps16MagnY, int16_t* ps16MagnZ);

#endif //__INV_MOTION_SENSOR_H
