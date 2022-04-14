#ifndef __ICM_20948_H
#define __ICM_20948_H
#include "DEV_Config.h"
#include "Public_StdTypes.h"
/* define ICM-20948 Device I2C address*/
#define I2C_ADD_ICM20948            0xD0
#define I2C_ADD_ICM20948_AK09916    0x0C
#define I2C_ADD_ICM20948_AK09916_READ  0x80
#define I2C_ADD_ICM20948_AK09916_WRITE 0x00
/* define ICM-20948 Register */
/* user bank 0 register */
#define REG_ADD_WIA             0x00
    #define REG_VAL_WIA             0xEA
#define REG_ADD_USER_CTRL       0x03
    #define REG_VAL_BIT_DMP_EN          0x80
    #define REG_VAL_BIT_FIFO_EN         0x40
    #define REG_VAL_BIT_I2C_MST_EN      0x20
    #define REG_VAL_BIT_I2C_IF_DIS      0x10
    #define REG_VAL_BIT_DMP_RST         0x08
    #define REG_VAL_BIT_DIAMOND_DMP_RST 0x04
#define REG_ADD_PWR_MIGMT_1     0x06
    #define REG_VAL_ALL_RGE_RESET   0x01
    #define REG_VAL_RUN_MODE        0x01    //Non low-power mode
#define REG_ADD_LP_CONFIG       0x05
#define REG_ADD_PWR_MGMT_1      0x06
#define REG_ADD_PWR_MGMT_2      0x07
#define REG_ADD_ACCEL_XOUT_H    0x2D
#define REG_ADD_ACCEL_XOUT_L    0x2E
#define REG_ADD_ACCEL_YOUT_H    0x2F
#define REG_ADD_ACCEL_YOUT_L    0x30
#define REG_ADD_ACCEL_ZOUT_H    0x31
#define REG_ADD_ACCEL_ZOUT_L    0x32
#define REG_ADD_GYRO_XOUT_H     0x33
#define REG_ADD_GYRO_XOUT_L     0x34
#define REG_ADD_GYRO_YOUT_H     0x35
#define REG_ADD_GYRO_YOUT_L     0x36
#define REG_ADD_GYRO_ZOUT_H     0x37
#define REG_ADD_GYRO_ZOUT_L     0x38
#define REG_ADD_EXT_SENS_DATA_00 0x3B
#define REG_ADD_REG_BANK_SEL    0x7F
    #define REG_VAL_REG_BANK_0  0x00
    #define REG_VAL_REG_BANK_1  0x10
    #define REG_VAL_REG_BANK_2  0x20
    #define REG_VAL_REG_BANK_3  0x30

/* user bank 1 register */
/* user bank 2 register */
#define REG_ADD_GYRO_SMPLRT_DIV 0x00
#define REG_ADD_GYRO_CONFIG_1   0x01
    #define REG_VAL_BIT_GYRO_DLPCFG_2   0x10 /* bit[5:3] */
    #define REG_VAL_BIT_GYRO_DLPCFG_4   0x20 /* bit[5:3] */
    #define REG_VAL_BIT_GYRO_DLPCFG_6   0x30 /* bit[5:3] */
    #define REG_VAL_BIT_GYRO_FS_250DPS  0x00 /* bit[2:1] */
    #define REG_VAL_BIT_GYRO_FS_500DPS  0x02 /* bit[2:1] */
    #define REG_VAL_BIT_GYRO_FS_1000DPS 0x04 /* bit[2:1] */
    #define REG_VAL_BIT_GYRO_FS_2000DPS 0x06 /* bit[2:1] */    
    #define REG_VAL_BIT_GYRO_DLPF       0x01 /* bit[0]   */
#define REG_ADD_ACCEL_SMPLRT_DIV_2  0x11
#define REG_ADD_ACCEL_CONFIG        0x14
    #define REG_VAL_BIT_ACCEL_DLPCFG_2  0x10 /* bit[5:3] */
    #define REG_VAL_BIT_ACCEL_DLPCFG_4  0x20 /* bit[5:3] */
    #define REG_VAL_BIT_ACCEL_DLPCFG_6  0x30 /* bit[5:3] */
    #define REG_VAL_BIT_ACCEL_FS_2g     0x00 /* bit[2:1] */
    #define REG_VAL_BIT_ACCEL_FS_4g     0x02 /* bit[2:1] */
    #define REG_VAL_BIT_ACCEL_FS_8g     0x04 /* bit[2:1] */
    #define REG_VAL_BIT_ACCEL_FS_16g    0x06 /* bit[2:1] */    
    #define REG_VAL_BIT_ACCEL_DLPF      0x01 /* bit[0]   */

/* user bank 3 register */
#define REG_ADD_I2C_SLV0_ADDR   0x03
#define REG_ADD_I2C_SLV0_REG    0x04
#define REG_ADD_I2C_SLV0_CTRL   0x05
    #define REG_VAL_BIT_SLV0_EN     0x80
    #define REG_VAL_BIT_MASK_LEN    0x07
#define REG_ADD_I2C_SLV0_DO     0x06
#define REG_ADD_I2C_SLV1_ADDR   0x07
#define REG_ADD_I2C_SLV1_REG    0x08
#define REG_ADD_I2C_SLV1_CTRL   0x09
#define REG_ADD_I2C_SLV1_DO     0x0A

/* define ICM-20948 Register  end */

/* define ICM-20948 MAG Register  */
#define REG_ADD_MAG_WIA1    0x00
    #define REG_VAL_MAG_WIA1    0x48
#define REG_ADD_MAG_WIA2    0x01
    #define REG_VAL_MAG_WIA2    0x09
#define REG_ADD_MAG_ST2     0x10
#define REG_ADD_MAG_DATA    0x11
#define REG_ADD_MAG_CNTL2   0x31
    #define REG_VAL_MAG_MODE_PD     0x00
    #define REG_VAL_MAG_MODE_SM     0x01
    #define REG_VAL_MAG_MODE_10HZ   0x02
    #define REG_VAL_MAG_MODE_20HZ   0x04
    #define REG_VAL_MAG_MODE_50HZ   0x05
    #define REG_VAL_MAG_MODE_100HZ  0x08
    #define REG_VAL_MAG_MODE_ST     0x10
/* define ICM-20948 MAG Register  end */

#define MAG_DATA_LEN    6


typedef struct icm20948_st_sensor_data_tag
{
	int16_t s16X;
	int16_t s16Y;
	int16_t s16Z;
}ICM20948_ST_SENSOR_DATA;

typedef struct icm20948_st_avg_data_tag
{
	uint8_t u8Index;
	int16_t s16AvgBuffer[8];
}ICM20948_ST_AVG_DATA;

extern bool invmsICM20948Check(void);
extern void invmsICM20948Init(void);
extern void invmsICM20948GyroRead(int16_t* ps16X, int16_t* ps16Y, int16_t* ps16Z);
extern void invmsICM20948AccelRead(int16_t* ps16X, int16_t* ps16Y, int16_t* ps16Z);
extern void invmsICM20948MagRead(int16_t* ps16X, int16_t* ps16Y, int16_t* ps16Z);

#endif //__ICM_20948_H
